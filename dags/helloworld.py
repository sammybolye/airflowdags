from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

# Define the DAG
dag = DAG(
    'hello_world',
    description='A simple tutorial DAG',
    schedule_interval=None,
    start_date=datetime(2023, 3, 22),
    catchup=False
)

# Define the BashOperator task
hello_world_task = BashOperator(
    task_id='hello_world_task',
    bash_command='python -c "print(\'Hello, world!\')"',
    dag=dag
)

# Define the task dependencies
hello_world_task
