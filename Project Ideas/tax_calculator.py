
print("How much is your annual salary? ")
salary = float(raw_input())

def tax_calculator(salary):
    if salary > 11850 and salary <= 46350:
        salary_after_tax = 'Your salary after tax is ' + str(salary * 0.8)
        return salary_after_tax
    elif salary > 46350 and salary <= 150000:
        salary_after_tax = 'Your salary after tax is ' + str(salary * 0.6)
        return salary_after_tax
    elif salary > 150000:
        salary_after_tax = 'Your salary after tax is ' + str(salary * 0.55)
        return salary_after_tax
    else:
        return "Your salary isn't taxed"


print(tax_calculator(salary))

