# Implemented Raft Consensus Algorithm in Python by using gRPC
### To generate gRPC filese write:
```python3 -m grpc_tools.protoc raft.proto --proto_path=. --python_out=. --grpc_python_out=.```
### Design is mostly same Raft RPC described in original paper 
### Some modifications added, which can be checked in [this file](https://github.com/bovvlet/RAFT/Lab07.pdf)