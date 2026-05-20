import pandas as pd

def clean_data(raw_data):
    df = pd.json_normalize(raw_data)
    cleaned_df = df[['name', 'email', 'address.city', 'company.name']]
    cleaned_df.columns = ['Name', 'Email', 'City', 'Company']
    return cleaned_df
