import csv
try:
    n = int(input("Enter no of employees: "))
    with open("payroll.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Employee ID", "Name", "Basic salary", "Allowance", "Deduction", "Net Salary"])
        for i in range(n):
            print(f"\nEnter details for employee {i+1}:")
            emp_id = input("Employee ID: ")
            name = input("Name: ")
            basic = float(input("Basic Salary: "))
            allowance = float(input("Allowance: "))
            deduction = float(input("Deduction: "))
            net_salary = basic+allowance-deduction
            writer.writerow([emp_id, name, basic, allowance, deduction, net_salary])       
    print("\nData successfully saved to payroll.csv.\n")
    print("---Employee Payroll Records---")
    with open("payroll.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except ValueError:
    print("invalid input")
except Exception as e:
    print(f"Error occurred: {e}")
