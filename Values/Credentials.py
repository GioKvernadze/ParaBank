from Helper.RNG import generate_random_number as RNG, generate_random_string as RSG
FirstName = RSG()
LasName = RSG()
Address = RSG() + str(RNG())
City = RSG()
State = RSG()
ZipCode = RNG()
Phone = RNG()
SSN = RNG()

Username = str(RNG()) + RSG()
Password = str(RNG()) + RSG()
Confirm = Password

Login_Username = Username
Login_Password = Password
