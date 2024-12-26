import json
import os
from Helper.RNG import generate_random_number as RNG, generate_random_string as RSG

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
USER_DATA_FILE = os.path.join(CURRENT_DIR, "..", "Tests", "user_data.json")

def register_data(generate_new=False):

    os.makedirs(os.path.dirname(USER_DATA_FILE), exist_ok=True)

    if not generate_new:
        try:
            # Check if data already exists in the file
            with open(USER_DATA_FILE, "r") as file:
                data = json.load(file)
                print("Using existing user data from file.")
                return data
        except FileNotFoundError:
            print("No existing user data found. Generating new data...")

    # Generate new data
    FirstName = RSG()
    LastName = RSG()
    Address = RSG() + str(RNG())
    City = RSG()
    State = RSG()
    ZipCode = RNG()
    Phone = RNG()
    SSN = RNG()

    Username = str(RNG()) + RSG()
    Password = str(RNG()) + RSG()
    Confirm = Password

    data = {
        "FirstName": FirstName,
        "LastName": LastName,
        "Address": Address,
        "City": City,
        "State": State,
        "ZipCode": ZipCode,
        "Phone": Phone,
        "SSN": SSN,
        "Username": Username,
        "Password": Password,
        "Confirm": Confirm,
        "Login_Username": Username,
        "Login_Password": Password,
    }

    with open(USER_DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
        print(f"New user data saved to file: {USER_DATA_FILE}")

    return data
