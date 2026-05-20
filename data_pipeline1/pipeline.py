import requests

def fetch_data():
    print("Fetching data from API...")
    url = "https://jsonplaceholder.typicode.com/users"
    
    response = requests.get(url)
    
    # We want to make sure the request was successful (Status code 200 means OK)
    if response.status_code == 200:
        print("Data fetched successfully!\n")
        # The API gives us JSON (which easily converts to a Python dictionary/list)
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data. Error code: {response.status_code}")
        return None

if __name__ == "__main__":
    # This block only runs if we execute this script directly from the terminal
    users_data = fetch_data()
    
    if users_data:
        # Let's print out the details of the first user in the list to see if it worked!
        first_user = users_data[0]
        print(f"First user found: {first_user['name']}")
        print(f"Their email is: {first_user['email']}")
