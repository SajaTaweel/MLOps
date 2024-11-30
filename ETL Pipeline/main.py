from logger import logger
from extract import extract
from transform import transform_data
from load import load_data
import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)



def main():
    try:
        logger.info("Starting ETL pipeline...")
        df = extract(config["dataset"])
        dim_tables, fact_tables = transform_data(df)
        load_data(dim_tables,fact_tables, config["database"])
    except Exception as e:
        logger.error(f"ETL pipeline failed {e}")


if __name__ == "__main__":
    main()



