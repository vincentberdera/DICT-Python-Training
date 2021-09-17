employeeName = str(input("Enter Employee Name: "))
hoursRendered = float(input("Enter number of hours rendered: "))
hourRate = float(input("Enter rate per hour: "))
GSIS = float(input("GSIS Premium: "))
philHealth = float(input("PhilHealth: "))
housingLoan = float(input("Housing Loan: "))
taxRate = float(input("Tax rate: "))

grossSalary = hoursRendered * hourRate
taxRate = taxRate / 100
taxGrossSalary = grossSalary * taxRate
totalDeduct = GSIS + philHealth + housingLoan + taxGrossSalary
netSalary = grossSalary - totalDeduct

print("\n")
print(f"Gross Salary: {grossSalary}")
print(f"Total deductions: {totalDeduct}")
print(f"Net Salary: {netSalary}")