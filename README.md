# Distributed storage systems and the CAP theorem

```
Project/
│
├── CentralizedDir/
│   ├── Master.py
│   └── Slave.py
│
├── DescentralizedDir/
│   └── DesNode.py
├── proto/
│   ├── store_impl.proto
│   ├── store.proto
│   ├── store_pb2.py
│   └── store_pb2_grpc.py
│
├── centralized_config.yaml
├── decentralized_config.yaml
├── centralized.py
├── decentralized.py
├── eval/
│   ├── centralized_config.yaml
│   ├── decentralized.py
│   ├── decentralized_config.yaml
│   ├── test_centralized_system.py
│   ├── eval.py
│   └── test_decentralized_system.py
├── centralized.py
├── requirements.txt
└── ...
```

## Directory Structure Explanation

- **proto/**: Contains Protocol Buffer files used for defining gRPC services and messages. Generated Python files (`store_pb2.py` and `store_pb2_grpc.py`) based on `store.proto` should be stored here.

- **centralized_config.yaml and decentralized_config.yaml**: YAML configuration files containing settings for the centralized and decentralized systems.

    - ***Centralized Format***: 

    ```yaml
    master:
      ip: <IP>
      port: <Port>

    slaves:
      - id: <slave_1_ID>
        ip: <slave_1_IP>
        port: <slave_1_Port>
      - id: <slave_2_ID>
        ip: <slave_2_IP>
        port: <slave_2_Port>
      ...
    ```

    - ***Decentralized Format***: 

    ```yaml
    nodes:
      - id: <node_1_ID>
        ip: <node_1_IP>
        port: <node_1_Port>
      - id: <node_2_ID>
        ip: <node_2_IP>
        port: <node_2_Port>
      ...
    ```

- **eval/**: Directory containing evaluation scripts and tests.

  - **centralized_system_tests.py**: Script containing unit tests for the centralized system.
  
  - **decentralized_system_tests.py**: Script containing unit tests for the decentralized system.

Each component of the project is organized into its respective directory, facilitating clear separation of concerns and ease of navigation. The `eval` directory specifically houses test scripts for evaluating the functionality and correctness of the implemented systems.

> **Note:** Students are required to define the necessary stubs for implementing the Two Phase Commit (2PC) protocol and for node registration in the system. These stubs must be manually added to the store.proto file by the students as part of their implementation.

## Description
> In this task, we have implemented two implementations of a distributed key-value storage system using Python and gRPC ‘protobuffers’. The first implementation approach follows a centralized model with a master node and a set of two slave nodes, using the Two-Phase Commit (2PC) protocol to ensure consistency in the data. The second implementation approach is decentralized and uses a weighted quorum-based protocol to coordinate read and write operations among all active nodes. We evaluated and compared both implementations in terms of consistency and performance using the provided eval.py, centralized_system_tests.py and decentralized_system_tests.py.

## How to Run it

Open a terminal and run the centralized.py file (make sure you're using the project's venv):

```python centralized.py```

Open a terminal and run the decentralized.py file:

```python decentralized.py```

Open a terminal and run the centralized_system_tests.py file:

```python eval/centralized_system_tests.py```

Open a terminal and run the decentralized_system_tests.py file:

```python eval/decentralized_system_tests.py```

Open a terminal and run the eval.py file:

```python eval/eval.py```