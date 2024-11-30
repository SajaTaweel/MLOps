# ETL Pipeline Project for Shopping Dataset

## Project Description

This project is an ETL pipeline designed to process a shopping dataset. The pipeline includes data transformation, division into fact and dimension tables, and the loading of data into a PostgreSQL database.

### Key Steps:
- **Data Transformation**: Split the dataset into fact and dimension tables.
- **ETL Pipeline**: Implemented the ETL process with data cleaning, transformation, and loading to a PostgreSQL database.
- **PostgreSQL Integration**: Data is loaded into a PostgreSQL database for analytics.

### Fact and Dimension Tables Model

The shopping dataset is divided into **fact** and **dimension** tables, following best practices for data warehousing. Here is the conceptual model:

![Fact and Dimension Tables](https://github.com/SajaTaweel/MLOps/blob/aef46dea110cfc4e8d80e1df12fad1bb3c3a244e/ETL%20Pipeline/model.png)

- **Fact Table**: The fact table contains the transactional data and is typically designed to store numerical measures. The fact table often includes foreign keys that reference dimension tables.
  
- **Dimension Tables**: Dimension tables provide descriptive attributes related to the facts. They help in filtering, grouping, and analyzing the fact data. Common dimension tables in this project include:
  - **dim_customer**: Contains information about the customer.
  - **dim_location**: Contains details about the location.
  - **dim_payment_method**: Contains information on the payment methods used.
  - **dim_product**: Contains product details.

## Getting Started

### Prerequisites

- Python 3.x
- PostgreSQL
- Required Python libraries (listed in `requirements.txt`)

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone git clone https://github.com/SajaTaweel/MLOps.git
   
2. Navigate to the project folder:
    ```bash
   cd MLOps/ETL\ Pipeline

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Set up PostgreSQL with a database called shopping_data.

5. Run the pipeline:
    ```bash
    python src/etl/main.py
    ```
 





   



