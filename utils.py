import pandas as pd
import logging

def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        logging.info("CSV loaded successfully")
        return df
    except Exception as e:
        logging.error(f"Error reading CSV: {e}")
        raise

def clean_data(df):
    try:
        # Fill missing values
        df = df.fillna("N/A")

        # Convert date column if exists
        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"], errors="coerce")

        logging.info("Data cleaned successfully")
        return df
    except Exception as e:
        logging.error(f"Error cleaning data: {e}")
        raise

def rename_columns(df, mapping):
    try:
        df = df.rename(columns=mapping)
        logging.info("Columns renamed")
        return df
    except Exception as e:
        logging.error(f"Error renaming columns: {e}")
        raise

def export_to_excel(df, output_path):
    try:
        df.to_excel(output_path, index=False, engine="openpyxl")
        logging.info(f"File saved to {output_path}")
    except Exception as e:
        logging.error(f"Error exporting to Excel: {e}")
        raise