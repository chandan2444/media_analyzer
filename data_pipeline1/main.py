from pipeline import fetch_data
from cleaner import clean_data

def run_pipeline():
    print("\n" + "="*40)
    print("STARTING ETL DATA PIPELINE")
    print("="*40 + "\n")
    
    print("[1/3] Extracting data from API...")
    raw_data = fetch_data()
    
    if not raw_data:
        print("❌ Pipeline aborted due to extraction failure.")
        return
        
    print("[2/3] Transforming and cleaning data...")
    cleaned_data = clean_data(raw_data)
    
    print("[3/3] Loading data to CSV file...")
    output_filename = "cleaned_users_data.csv"
    
    cleaned_data.to_csv(output_filename, index=False)
    
    print("\n" + "="*40)
    print(f"✅ PIPELINE FINISHED SUCCESSFULLY!")
    print(f"📁 Data saved to: {output_filename}")
    print("="*40 + "\n")
    
    print("--- Preview of Saved Data ---")
    print(cleaned_data.head())
    print("-" * 29)

if __name__ == "__main__":
    run_pipeline()
