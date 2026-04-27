from airflow import DAG
import pendulum
import random
from airflow.providers.standard.operators.python import PythonOperator
from common.common_func import regist
from airflow.decorators import task


with DAG(
    dag_id="dags_python_with_op_arg",
    schedule= "0 2 * * 1",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:

    regist_t1 = PythonOperator(
        task_id = 'regist_t1',
        python_callable=regist, 
        op_args=['rimsm','man','kr','seoul']
    )

    regist_t1