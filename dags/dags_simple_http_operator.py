from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.http.operators.http import HttpOperator
from airflow.decorators import task
import pendulum

with DAG(
    dag_id = 'dags_simple_http_operator', 
    start_date = pendulum.datetime(2026,5,9, tz ='Asia/Seoul' ),
    catchup=False,
    schedule=None
) as dag: 
    
    '''서울시 데이터'''
    tax_info = HttpOperator(
        task_id = 'tax_info',
        http_conn_id = 'openapi.seoul.go.kr',
        endpoint = '{{var.value.apikey_openapi_seoul_go_kr}}/json/FiosTbmRevdesc/1/5/', 
        method = 'GET',
        headers ={
            'Content-Type' : 'application/json',
            'charset' : 'utf-8',
            'Accept' : '*/*' 
        }
    )

    @task(task_id = 'python_2')
    def python_2(**kwargs):
        ti = kwargs['ti']
        rslt = ti.xcom_pull(task_ids = 'tax_info')

        import json
        from pprint import pprint

        pprint(rslt)

    tax_info >> python_2()



