import grpc
import raft_pb2
import raft_pb2_grpc
import shlex

class Client:
    def __init__(self):
        self.stub = None

    def connect(self, ip_port):
        try:
            channel = grpc.insecure_channel(ip_port)
            self.stub = raft_pb2_grpc.ServerStub(channel)
        except Exception as e:
            print("Connection error:", e)

    def getleader(self):
        try:
            msg = raft_pb2.EmptyMessage()
            reply = self.stub.GetLeader(msg)
            print(reply.message)
        except Exception as e:
            print("Error getting leader:", e)

    def suspend(self, time):
        try:
            msg = raft_pb2.Message(message=str(time))
            reply = self.stub.Suspend(msg)
            print(reply.message)
        except Exception as e:
            print("Error suspending:", e)

    def setval(self, *args):
        try:
            # Extract task name, task description, and any additional arguments
            task_name = args[2]  # Task name is the second argument
            task_description = args[3]  # Task description is the third argument
            # Concatenate all remaining arguments into the task description
            for arg in args[4:]:
                task_description += ' ' + arg

            msg = raft_pb2.MessageKeyValue(key=str(task_name), value=str(task_description))
            reply = self.stub.SetVal(msg)
            print(reply.message)
        except Exception as e:
            print("Error setting value:", e)

    def getval(self, key):
        try:
            msg = raft_pb2.MessageKey(key=str(key))
            reply = self.stub.GetVal(msg)
            print(reply.message)
        except Exception as e:
            print("Error getting value:", e)

    def delete_task(self, task_id):
        try:
            msg = raft_pb2.DeleteTaskRequest(key=task_id)
            reply = self.stub.DeleteTask(msg)
            print(reply.message)
        except Exception as e:
            print("Error deleting task:", e)

    def complete_task(self, task_id):
        try:
            # Send a message to the server to mark the task with the given ID as complete
            msg = raft_pb2.MessageKey(key="complete_task_" + str(task_id))
            reply = self.stub.SetVal(msg)
            print(reply.message)
        except Exception as e:
            print("Error completing task:", e)

    def quit(self):
        print("Client terminated.")

if __name__ == "__main__":
    client = Client()
    while True:
        try:
            line = shlex.split(input("> "))
            print("Input line:", line)  # Add this line for debugging
            if line[0] == 'connect':
                SERVER_ADDRESS = line[1] + ":" + line[2]
                client.connect(SERVER_ADDRESS)
            elif line[0] == 'getleader':
                client.getleader()
            elif line[0] == 'suspend':
                client.suspend(line[1])
            elif line[0] == 'setval':
                task_name = line[2]  # Task name is the second argument
                task_description = line[3]  # Task description is the third argument
                # Concatenate all remaining arguments into a single string as task description
                client.setval(*line)
            elif line[0] == 'getval':
                client.getval(line[1])
            elif line[0] == 'complete_task':
                client.complete_task(line[1])  # Directly handle complete_task command
            elif line[0] == 'delete_task':
                if len(line) == 2:  # Ensure that the command has the correct number of arguments
                    client.delete_task(line[1])  # Call delete_task method with task ID
                else:
                    print("Invalid command format. Usage: delete_task <task_id>")
            elif line[0] == 'quit':
                client.quit()
                break
            else:
                print("Undefined command")
        except KeyboardInterrupt:
            print("Keyboard interrupt")
            client.quit()
            break

