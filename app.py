import grpc
import streamlit as st
import raft_pb2
import raft_pb2_grpc
import mysql.connector

# gRPC server address
SERVER_ADDRESS = "127.0.0.1:50000"

# gRPC connection setup
channel = grpc.insecure_channel(SERVER_ADDRESS)
stub = raft_pb2_grpc.ServerStub(channel)

# Function to add a task
def add_task(task_name, task_description):
    try:
        task_info = f"{task_name}: {task_description}"  # Include task name in description
        response = stub.SetVal(raft_pb2.MessageKeyValue(key=task_name, value=task_info))
        st.success(response.message)
    except grpc.RpcError as e:
        st.error("Error adding task: " + e.details())

# Function to delete a task
def delete_task(task_id):
    try:
        response = stub.DeleteTask(raft_pb2.DeleteTaskRequest(key=task_id))
        st.success(response.message)
    except grpc.RpcError as e:
        st.error("Error deleting task: " + e.details())

# Function to mark a task as complete
def mark_task_complete(task_id):
    try:
        response = stub.SetVal(raft_pb2.MessageKeyValue(key=f"complete_task_{task_id}", value="complete"))
        st.success(response.message)
    except grpc.RpcError as e:
        st.error("Error marking task as complete: " + e.details())

# Function to fetch tasks from the database
def fetch_tasks_from_db():
    tasks = []
    try:
        # Connect to the database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="pwd",  # Update with your MySQL password
            database="ccproject"   # Update with your database name
        )
        cursor = db.cursor()

        # Fetch tasks from the database
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()

        # Close the database connection
        cursor.close()
        db.close()
    except mysql.connector.Error as e:
        st.error("Error fetching tasks from the database: " + str(e))
    return tasks

# Streamlit app
def main():
    st.title("Task Manager")

    # Add Task
    st.header("Add Task")
    task_name = st.text_input("Task Name")
    task_description = st.text_area("Task Description")
    if st.button("Add Task"):
        if task_name and task_description:
            add_task(task_name, task_description)
        else:
            st.warning("Please enter both task name and description.")

    # Fetch tasks from the database
    tasks = fetch_tasks_from_db()
    task_columns = ["Task ID", "Task Name", "Description", "Status"]
    # Display Task List
    st.header("Task List")
    if tasks:
        st.write(task_columns)  # Display column names
        st.table(tasks)  # Display table data
    else:
         st.write("No tasks found.")

    # Delete Task
    st.header("Delete Task")
    task_id_delete = st.text_input("Task ID to Delete")
    if st.button("Delete Task"):
        if task_id_delete:
            delete_task(task_id_delete)
        else:
            st.warning("Please enter the task ID to delete.")

    # Mark Task as Complete
    st.header("Mark Task as Complete")
    task_id_complete = st.text_input("Task ID to Mark Complete")
    if st.button("Mark as Complete"):
        if task_id_complete:
            mark_task_complete(task_id_complete)
        else:
            st.warning("Please enter the task ID to mark as complete.")

if __name__ == "__main__":
    main()
