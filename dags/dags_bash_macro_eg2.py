from airflow import DAG
import pendulum
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id = 'dags_bash_macro_eg2', 
    schedule = '10 0 L * 6#2',
    start_date = pendulum.datetime(2026, 4, 27, tz = 'Asia/Seoul')
) as dag :

    bash_task_t1 = BashOperator(
        task_id = 'bash_task_t1', 
        env = {
            'START_DATE' : '{{() data_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days = 19))|ds }}', 
            'END_DATE' : '{{ (data_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days = 14)) | ds}}'
        }, 
        bash_command = 'echo "START_DATE : $START_DATE" && echo "END_DATE " $END_DATE' 
    )