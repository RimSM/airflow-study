from airflow import DAG
import pendulum
from airflow.decorators import task
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id = 'dags_bash_python_with_xcom', 
    schedule= "30 9 * * *", 
    start_date = pendulum.datetime(2025, 5, 2, tz = 'Asia/Seoul'),
    catchup = False
) as dag :

    @task(task_id = 'python_push')
    def python_push_xcom() :
        result_dict = {'status' : 'Good', 'data' : [1,2,3], 'option_cnt' : 100}
        return result_dict
    
    bash_pull = BashOperator(
        task_id = 'bash_pull', 
        env={
            'STATUS': '{{ti.xcom_pull(task_id = "python_pull")["status"]}}',
            'DATA' : '{{ti.xcom_pull(task_id = "python_pull")["data"]}}',
            'OPTION_CNT' : '{{ti.xcom_pull(task_id = "python_pull")["option_cnt"]}}'
        },
        bash_command='echo $STATUS && echo $DATA && echo $OPTION_CNT'
    )

    python_push_xcom() >> bash_pull 

    bash_push = BashOperator(
        task_id = 'bash_push', 
        bash_command='echo PUSH_START '
                     '{{ti.xcom_push(key="bash_pushed",value = 200)}} &&'
                     'echo PUSH_COMPLETE'
    )

    @task(task_id = 'python_pull')
    def python_pull_xcom(**kwarg):
        ti = kwarg['ti']
        start_value = ti.xcom_pull(key='bash_pusheded')
        retrun_value = ti.xcom_pull(task_ids = 'bash_push')


    bash_push >> python_pull_xcom()