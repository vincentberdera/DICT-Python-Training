yearsOfService = int(input("Enter years in service: "))
office = str(input("Enter office: "))

if yearsOfService >= 10:
    if office.upper() == "IT":
        amount = 10000
    elif office.upper() == "ACCT":
        amount = 12000
    elif office.upper() == "HR":
        amount = 15000
else:
    if office.upper() == "IT":
        amount = 5000
    elif office.upper() == "ACCT":
        amount = 6000
    elif office.upper() == "HR":
        amount = 7500

print(f"Amount Given: {amount}")