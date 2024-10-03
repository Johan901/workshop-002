from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd

# Funciones de extracción
from postgres_test_dag import extract_spotify_csv, extract_grammy_db

def transform_data(**kwargs):
    spotify_data = kwargs['ti'].xcom_pull(task_ids='extract_spotify_csv')
    grammy_data = kwargs['ti'].xcom_pull(task_ids='extract_grammy_db')
    
    # Convertir a DataFrame
    spotify_df = pd.DataFrame(spotify_data)
    grammy_df = pd.DataFrame(grammy_data)

    spotify_df['artist_name'] = spotify_df['artist_name'].str.lower()
    grammy_df['artist'] = grammy_df['artist'].str.lower()

    # merge entre el dataset de Spotify y Grammy
    merged_data = pd.merge(spotify_df, grammy_df, 
                           left_on=['artist_name', 'track_name'], 
                           right_on=['artist', 'nominee'], 
                           how='inner')

    merged_data = merged_data[merged_data['winner'] == True]

    return merged_data

def load_to_db(**kwargs):
    merged_data = kwargs['ti'].xcom_pull(task_ids='transform_data')
    engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres/airflow')
    merged_data.to_sql('final_data', engine, if_exists='replace', index=False)

#  DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 10, 1),
    'retries': 1,
}

with DAG('spotify_grammy_etl', default_args=default_args, schedule_interval='@once') as dag:
    
    extract_spotify_task = PythonOperator(
        task_id='extract_spotify_csv',
        python_callable=extract_spotify_csv
    )
    
    extract_grammy_task = PythonOperator(
        task_id='extract_grammy_db',
        python_callable=extract_grammy_db
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
        provide_context=True
    )

    load_task = PythonOperator(
        task_id='load_to_db',
        python_callable=load_to_db,
        provide_context=True
    )

    
    extract_spotify_task >> extract_grammy_task >> transform_task >> load_task
