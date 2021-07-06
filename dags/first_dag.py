"""First DAG Module."""

from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "first_dag",
    description="Simple first DAG.",
    schedule_interval="@hourly",
    start_date=days_ago(1),
    catchup=False,
    tags=["example", "simple"],
) as dag:
    task_one = BashOperator(
        task_id="show_time",
        bash_command="date",
    )

if __name__ == "__main__":
    from airflow.utils.state import State

    dag.clear(dag_run_state=State.NONE)
    dag.run()
