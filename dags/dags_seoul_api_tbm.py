from operators.seoul_api_to_csv_operator import SeoulApiToCsvOperator
from airflow import DAG 
import pendulum

with DAG(
    dag_id = 'dags_seoul_api_tbm', 
    start_date = pendulum.datetime(2026,5,10,tz = 'Asia/Seoul'),
    catchup = False,
    schedule=None 
) as dag : 
    
    tax_info = SeoulApiToCsvOperator(
        task_id = 'tax_info', 
        dataset_nm = 'FiosTbmRevdesc',
        path = '/opt/airflow/files/tbm/{{data_interval_end.in_timezone("Asia/Seoul") | ds_no_dash}}', 
        file_name = 'tax_info.csv'
    )

    tax_info