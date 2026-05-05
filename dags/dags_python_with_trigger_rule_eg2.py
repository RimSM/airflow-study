from airflow import DAG
import pendulum
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
from airflow.decorators import task

with DAG(
    dag_id = 'dags_python_with_trigger_rule_eg2', 
    start_date = pendulum.datetime(2026, 5, 5, tz = 'Asia/Seoul'), 
    schedule=None, 
    catchup=False
) as dag: 
    
    @task.branch(task_id = 'branching')
    def select_random():
        import random 

        item_list = ['A','B','C']
        select_list = random.choice(item_list)

        if select_list == 'A':
            return 'task_a'
        elif select_list == 'B':
            return 'task_b'
        elif select_list == 'C':
            return 'task_c'
        
    
    task_a = BashOperator(
        task_id = 'task_a', 
        bash_command='echo upstream1'
    )

    @task(task_id = 'task_b')
    def task_b():
        print('정상처리')

    @task(task_id = 'task_c')
    def task_c():
        print('정상처리')

    @task(task_id = 'task_d', trigger_rule = 'none_skipped')
    def task_d():
        print('정상처리')

    
    select_random >> [task_a, task_b(),task_c()] >> task_d()