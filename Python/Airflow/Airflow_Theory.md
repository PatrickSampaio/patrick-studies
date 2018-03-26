## DAG (Directed Acyclic Graph)

The DAG is just an python script to configure the pipeline, no data handling is done in the DAG script. Concepetually a DAG
is an task wrapper that organizes your tasks in the order that makes sense to you. It's important to mark that the DAG
doest not care about what is running, it will just run it in an order like an workflow.
Different tasks run on different workers.
