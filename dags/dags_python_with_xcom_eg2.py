from airflow import DAG 
import pendulum
import datetime
from airflow.decorators import task


with DAG(
    task_id = 'dags_python_with_xcom_eg2',
    schedule="10 6 * * *",
    start_date=pendulum.datetime(2026,04,29, tz = 'Asia/Seoul'), 
    catchup = False
) as dag:
    
    @task (task_id = 'python_xcom_push_by_return')
    def xcom_push_result(**kwargs):
        return "Success"
    
    @task (task_id = 'python_xcom_pull_1')
    def xcom_pull_1(**kwargs):
        ti = kwargs('ti')
        value1 = ti.
