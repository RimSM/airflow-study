from airflow import DAG
import pendulum
import datetime 
from airflow.providers.standard.operators.python import PythonOperator
from airflow.decorators import task
from airflow.decorators import task_group
from airflow.sdk import TaskGroup


with DAG(
    dag_id = 'dags_python_with_task_group', 
    schedule=None, 
    start_date=pendulum.datetime(2026,5,7,tz='Asia/Seoul'),
    catchup=False
) as dag:
    
    def inner_func(**kwargs):
        msg = kwargs.get('msg') or ''
        print(msg)

    
    @task_group(group_id = 'first_group')
    def group_1():
        '''task_group 데커레이터를 이용한 첫 번째 그룹입니다.'''

        @task(task_id = 'inner_function')
        def inner_function1(**kwargs):
            print('첫번째 TaskGroup 내 첫 번째 Task 입니다.')

        inner_function2 = PythonOperator(
            task_id = 'inner_function2',
            python_callable=inner_func,
            op_kwargs={'msg' : '첫 번째 Task Group 내 첫 번째 Task 입니다.'}
        )
        inner_function1() >> inner_function2

    with TaskGroup(group_id = 'second_group', tooltip = '두번째 그룹입니다.') as group_2:
        @task(task_id = 'inner_function')
        def inner_function1(**kwargs):
            print('두번째 TaskGroup 내 첫 번째 Task 입니다.')

        inner_function2 = PythonOperator(
            task_id = 'inner_function2',
            python_callable=inner_func,
            op_kwargs={'msg' : '두 번째 Task Group 내 첫 번째 Task 입니다.'}
        )
        inner_function1() >> inner_function2

    group_1() >> group_2
        
