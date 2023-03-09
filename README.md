# Raft Consensus Algorithm by using of gRPC
### To generate gRPC files write:
```python3 -m grpc_tools.protoc raft.proto --proto_path=. --python_out=. --grpc_python_out=.```
### See examples of how to run the program in [this file](https://github.com/bovvlet/RAFT/Lab07.pdf)
### Design is mostly same Raft RPC described in original paper 
### Some modifications added, which can be checked in [this file](https://github.com/bovvlet/RAFT/Lab07.pdf)
