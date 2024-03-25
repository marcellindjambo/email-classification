import logging
import pandas as pd
logging.basicConfig(level=logging.INFO)

class IngestData:
    def __init__(self):
        pass
    
    def get_data_from_csv_file(self, file_path: str) -> pd.DataFrame:
        try:
            df = pd.read_csv(file_path,encoding='latin1')
            logging.info("Read file successfully")
            return df
        except Exception as e:
            logging.error("Error while reading csv file: %s", str(e))