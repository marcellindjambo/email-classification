# main_script.py
import pandas as pd
from steps.data_ingestion import ingest_df

if __name__ == "__main__":
    df = ingest_df()
    print(df.head())