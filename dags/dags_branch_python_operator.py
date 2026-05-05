from airflow import DAG
import pendulum
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.python import BranchPythonOperator

with DAG(
    dag_id='dags_branch_python_operator', 
    start_date = pendulum.datetime(2026, 5, 5, tz = 'Asia/Seoul'), 
    schedule = None,
    catchup = False
) as dag: 

    def select_random():
        import random

        item_list = ['A','B','C']
        select_random = random.choice(item_list)
        if select_random == 'A' :
            return 'task_a'
        elif select_random in ['B','C'] :
            return ['task_b','task_c']
        
    python_branch_task = BranchPythonOperator(
        task_id = 'python_branch_task', 
        python_callable=select_random
    )




    def common_func(**kwargs):
        print(kwargs['selected'])

    task_a = PythonOperator(
        task_id = 'task_a', 
        python_callable=common_func,
        op_kwargs={'selected' : 'A'}
    )

    task_b = PythonOperator(
        task_id = 'task_b', 
        python_callable = common_func, 
        op_kwargs={'selected' : 'B'}
    )

    task_c = PythonOperator(
        task_id = 'task_c', 
        python_callable = common_func, 
        op_kwargs={'selected' : 'C'}
    )

    
    python_branch_task >> [task_a, task_b, task_c]
