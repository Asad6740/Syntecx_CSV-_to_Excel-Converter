import argparse
import logging
from utils import read_csv, clean_data, rename_columns, export_to_excel
from config import DEFAULT_OUTPUT, COLUMN_MAPPING

# Logging setup
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    parser = argparse.ArgumentParser(description="CSV to Excel Converter")
    parser.add_argument("-i", "--input", required=True, help="Input CSV file path")
    parser.add_argument("-o", "--output", default=DEFAULT_OUTPUT, help="Output Excel file path")

    args = parser.parse_args()

    try:
        df = read_csv(args.input)
        df = clean_data(df)
        df = rename_columns(df, COLUMN_MAPPING)
        export_to_excel(df, args.output)

        print("✅ Conversion completed successfully!")

    except Exception as e:
        print("❌ Error occurred. Check logs.txt for details.")
        logging.error(f"Main error: {e}")

if __name__ == "__main__":
    main()