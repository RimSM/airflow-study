from airflow import DAG
import pendulum
import random
from airflow.providers.standard.operators.python import PythonOperator
from common.common_func import get_sftps


with DAG(
    dag_id="dags_python_import_func",
    schedule= "30 6 *  * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    