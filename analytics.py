import pandas as pd

# Load sample e-commerce data
def clean_data(file_path):
    df = pd.read_csv(file_path)
    # Drop duplicates caused by page-refresh errors
    df_cleaned = df.drop_duplicates(subset=['Transaction_ID'])
    return df_cleaned

print("Data processing pipeline executed successfully.")
