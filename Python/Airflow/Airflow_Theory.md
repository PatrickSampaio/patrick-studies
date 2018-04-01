## DAG (Directed Acyclic Graph)

The DAG is just an python script to configure the pipeline, no data handling is done in the DAG script. Concepetually a DAG
is an task wrapper that organizes your tasks in the order that makes sense to you. It's important to mark that the DAG
doest not care about what is running, it will just run it in an order like an workflow.
Different tasks run on different workers.

#### Scope

Everything that can be seeng from the global is scope will be an DAG

`
dag_1 = DAG('this_dag_will_be_discovered')

def my_function()
    dag_2 = DAG('but_this_dag_will_not')

my_function()
`
#### Context-Manager

`
with DAG('my_dag', start_date=datetime(2016, 1, 1)) as dag:
    op = DummyOperator('op')

op.dag is dag # True
`

### Operators

Operators tells how the tasks must run, they should be atomic and stand by itself.

- BashOperator - executes a bash command
- PythonOperator - calls an arbitrary Python function
- EmailOperator - sends an email
- HTTPOperator - sends an HTTP request
- MySqlOperator, SqliteOperator, PostgresOperator, MsSqlOperator, OracleOperator, 
- JdbcOperator, etc. - executes a SQL command
- Sensor - waits for a certain time, file, database row, S3 key, etc…

#### DAG Assignment

The DAG Assignment can be done explicit, implicit and by other operator already assigned. Once an operator is assigned it cannot be un-assigned

`
dag = DAG('my_dag', start_date=datetime(2016, 1, 1))

# sets the DAG explicitly
explicit_op = DummyOperator(task_id='op1', dag=dag)

# deferred DAG assignment
deferred_op = DummyOperator(task_id='op2')
deferred_op.dag = dag

# inferred DAG assignment (linked operators must be in the same DAG)
inferred_op = DummyOperator(task_id='op3')
inferred_op.set_upstream(deferred_op)
`
#### BitShift Composion

`op1 >> op2 >> op3 << op4`

`
op1.set_downstream(op2)
op2.set_downstream(op3)
op3.set_upstream(op4)
`

#### Triggers

- all_success: (default) all parents have succeeded
- all_failed: all parents are in a failed or upstream_failed state
- all_done: all parents are done with their execution
- one_failed: fires as soon as at least one parent has failed, it does not wait for all parents to be done
- one_success: fires as soon as at least one parent succeeds, it does not wait for all parents to be done
- dummy: dependencies are just for show, trigger at will

`depends_on_past`, is an boolean that configures a tasks to not be executed if the past task wasn't executed

#### Hooks

Hooks are commom interface to external services, and act as a building block for opertors. Hooks are very useful to use Python Scripts, it will leave metadata and security out of the way.

#### Branching

![alt text](https://github.com/PatrickSampaio/patrick-studies/blob/master/images/Screenshot%20from%202018-04-01%2015-16-12.png)





























