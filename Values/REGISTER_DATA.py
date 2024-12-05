import json
from Helper.RNG import generate_random_number as RNG, generate_random_string as RSG
def register_data(generate_new=False):
    """
    Generate or retrieve registration data. Optionally generate new data if required.
    """
    if not generate_new:
        try:
            # Check if data already exists in the file
            with open("user_data.json", "r") as file:
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

    # Save to file
    with open("user_data.json", "w") as file:
        json.dump(data, file, indent=4)
        print("New user data saved to file.")

    return data
