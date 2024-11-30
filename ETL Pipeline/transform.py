from logger import logger


def transform_data(df):

    try:
        logger.info("Starting transformation stage...")
        print(df.duplicated().sum())  # No duplicate
        df['Purchase Amount (USD)'] = df['Purchase Amount (USD)'].astype('float')
        # Split into Fact and Dimension Tables

        # Create Dim_Customer
        dim_customer = df[['Customer ID', 'Age', 'Gender', 'Subscription Status', 'Frequency of Purchases',
                           'Previous Purchases']].drop_duplicates()

        # Create Dim_Product
        dim_product = df[['Item Purchased', 'Category', 'Size', 'Color', 'Season']].drop_duplicates()
        dim_product['Product ID'] = range(1, len(dim_product) + 1)

        # Create Dim_location
        dim_location = df[['Location']].drop_duplicates()
        dim_location['Location ID'] = range(1, len(dim_location) + 1)

        # Create Dim_Payment_Method
        dim_payment_method = df[['Payment Method', 'Preferred Payment Method']].drop_duplicates()
        dim_payment_method['Payment Method ID'] = range(1, len(dim_payment_method) + 1)

        # Create Fact_Purchases
        fact_purchases = df.merge(dim_product, on=['Item Purchased', 'Category', 'Size', 'Color', 'Season'], how='left')\
                           .merge(dim_location, on=['Location'], how='left')\
                           .merge(dim_payment_method,on=['Payment Method', 'Preferred Payment Method'], how='left')
        fact_purchases = fact_purchases[['Customer ID', 'Product ID', 'Location ID', 'Payment Method ID',
                                         'Purchase Amount (USD)', 'Review Rating', 'Shipping Type', 'Discount Applied',
                                         'Promo Code Used']]
        logger.info("Finished transformation stage...")
        return (dim_customer, dim_product, dim_location, dim_payment_method), fact_purchases

    except Exception as e:
        logger.error(f"Data transformation failed {e}")
        raise
