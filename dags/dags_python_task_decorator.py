from airflow import DAG
import pendulum
import random
from airflow.providers.standard.operators.python import PythonOperator
from common.common_func import get_sftp
from airflow.decorators import task


with DAG(
    dag_id="dags_python_task_decorator",
    schedule= "0 2 * * 1",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:

    @task(task_id="python_task_1")
    def print_context(some_imput):
        print(some_imput)
    
    python_task_1 = print_context("task_decorator 실행")