import logging
import pandas as pd
from src.ingest_data import IngestData
logging.basicConfig(level=logging.INFO)

def ingest_df() -> pd.DataFrame:
    try:
        file_path: str = r"C:\Users\djamb\OneDrive - Université Centrale\ML PROJECTS\email-classification\data\data.csv"
        ingest = IngestData()
        df = ingest.get_data_from_csv_file(file_path=file_path)
        logging.info("Ingested data completed successfully")
        return df
    except Exception as e:
        logging.error("Error while ingesting CSV: %s", str(e))