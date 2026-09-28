# my-python-codes
print("===Welcome to the Mtn Special Data Bundle===")
phone_number=(input("Enter your phone number:"))
bundle1="1. 500MB (N250)"
bundle2="2. 1.0GB (N500)"
bundle3="3. 2.0GB (N1000)"
print(bundle1,bundle2, bundle3  )
Data_plan=input("Choose your Data plan(1-3):").strip()
if len(phone_number) > 11:
    print("Invalid phone number...")
if Data_plan == "1":
       print(f"You have sucessfully purchase {bundle1} for {phone_number}")
elif Data_plan=="2":
       print(f"You have sucessfully purchase {bundle2} for {phone_number}")
elif Data_plan == "3":
    print(f"You have sucessfully purchase {bundle3} for {phone_number}")
else:
    print("Invalid Data plan, check it and try again.")
