from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 10, 1),
    'retries': 1
}

# Define the DAG
dag = DAG(
    'simple_dag',
    default_args=default_args,
    description='A simple DAG with three tasks',
    schedule_interval='@daily'
)

# Define the first task
def task_1():
    print("Task 1: Extracting data...")

# Define the second task
def task_2():
    print("Task 2: Transforming data...")

# Define the third task
def task_3():
    print("Task 3: Loading data...")

# Create the tasks
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=task_1,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=task_2,
    dag=dag
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=task_3,
    dag=dag
)

# Set task dependencies
extract_task >> transform_task >> load_task
