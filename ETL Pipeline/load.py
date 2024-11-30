from sqlalchemy import create_engine
from logger import logger


def load_data(dim_tables, fact_table, db_config):
    try:
        logger.info("Starting data loading into the database...")

        # Database connection
        engine = create_engine(f"postgresql+psycopg2://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

        # Load Dimension Tables
        dim_customer, dim_product, dim_location, dim_payment_method = dim_tables
        dim_customer.to_sql('dim_customer', con=engine, index=False, if_exists='replace')
        dim_product.to_sql('dim_product', con=engine, index=False, if_exists='replace')
        dim_location.to_sql('dim_location', con=engine, index=False, if_exists='replace')
        dim_payment_method.to_sql('dim_payment_method', con=engine, index=False, if_exists='replace')

        # Load Fact Table
        fact_table.to_sql('fact_purchases', con=engine, index=False, if_exists='replace')

        logger.info("Data loading completed successfully.")
    except Exception as e:
        logger.error("Data loading failed.", exc_info=True)
        raise
