from airflow import DAG
import pendulum
from airflow.providers.standard.operators.python import PythonOperator
from common.common_func import regist2
from airflow.decorators import task


with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule= "0 2 * * 1",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:

    regist2_t1 = PythonOperator(
        task_id = 'regist2_t1',
        python_callable=regist2, 
        op_args=['rimsm','man','kr','seoul'],
        op_kwargs={'email':'rsm9085@gmail.com','phone':'010-9725-2600'}
    )

    regist2_t1