from functools import reduce

salaries = [30000, 55000, 47000, 80000, 62000, 39000]

increased_salary = list(map(lambda x: x + (x * 10 / 100), salaries))

high_salary = list(filter(lambda x: x > 50000, salaries))

total_salary = reduce(lambda x, y: x + y, salaries)

print("Original Salaries:", salaries)
print("Increased Salaries:", increased_salary)
print("Employees Earning Above 50000:", high_salary)
print("Total Salary Expenditure:", total_salary)