import sqlite3
import pandas as pd
from client.constants import LOCAL_JOBS_DB


def select_job():
    with sqlite3.connect(LOCAL_JOBS_DB) as conn:
        query = 'SELECT * FROM local_jobs'
        jobs_table = pd.read_sql_query(query, conn)
    id_list = jobs_table['id'].values.tolist()
    for i, ident in enumerate(id_list, start=1):
        print(str(i) + '. ' + str(ident))
    entry = input('Select a job ID (Enter a number): ')
    job_uuid = id_list[int(entry) - 1]
    return job_uuid