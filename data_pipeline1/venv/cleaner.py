import pandas as pd 
from pipeline import fetch_data


def clean_data(raw_data) :
    
    df = pd.DataFrame(raw_data)

    print("the raw data table looks like: ")
    print(df.head(10))
    return df 

if __name__ == "__main__" :
    data =fetch_data()
    
    if data:
        cleaned_table =   clean_data(data)
    
 
      





