def is_valid_name(name):
    return name.isalpha() and len(name) <= 50

def is_valid_empid(empid):
    return empid.isalnum() and 5 <= len(empid) <= 10

def get_float(prompt, min_val=0, max_val=10000000):
    while True:
        try:
            val = float(input(prompt))
            if min_val <= val <= max_val:
                return val
        except:
            pass
        print("Invalid input. Try again.")

while True:
    name = input("Enter name: ")
    if is_valid_name(name):
        break
    print("Invalid name")

while True:
    empid = input("Enter EmpID: ")
    if is_valid_empid(empid):
        break
    print("Invalid EmpID")

basic = get_float("Enter Basic Monthly Salary: ", 0.01, 10000000)
allowance = get_float("Enter Special Allowance: ", 0, 10000000)
bonus_percent = get_float("Enter Bonus Percentage: ", 0, 100)

gross_monthly = basic + allowance
if gross_monthly <= 0:
    print("Gross salary must be greater than 0")
    exit()

annual_gross = gross_monthly * 12
bonus = (annual_gross * bonus_percent) / 100
annual_gross += bonus

if annual_gross > 10000000 * 12 + (100 * 10000000 * 12 / 100):
    print("Annual gross salary too high")
    exit()

std_deduction = 50000
taxable_income = max(annual_gross - std_deduction, 0)

tax = 0
slabs = [(300000, 0), (300000, 0.05), (300000, 0.10), (300000, 0.15), (300000, 0.20)]
remaining = taxable_income
for amount, rate in slabs:
    if remaining > amount:
        tax += amount * rate
        remaining -= amount
    else:
        tax += remaining * rate
        remaining = 0
        break
if remaining > 0:
    tax += remaining * 0.30

if taxable_income <= 700000:
    tax = 0

cess = tax * 0.04
total_tax = tax + cess

net_salary = annual_gross - total_tax

print("\n----- Employee Tax Report -----")
print("Name:", name)
print("EmpID:", empid)
print("Gross Monthly Salary: ₹", round(gross_monthly, 2))
print("Annual Gross Salary: ₹", round(annual_gross, 2))
print("Taxable Income: ₹", round(taxable_income, 2))
print("Tax Payable (before cess): ₹", round(tax, 2))
print("Health & Education Cess (4%): ₹", round(cess, 2))
print("Total Tax Payable: ₹", round(total_tax, 2))
print("Annual Net Salary: ₹", round(net_salary, 2))
