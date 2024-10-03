import pandas as pd

def extract_spotify_csv():
    spotify_file_path = '/opt/airflow/dags/files/spotify_dataset.csv'
    spotify_data = pd.read_csv(spotify_file_path)
    return spotify_data