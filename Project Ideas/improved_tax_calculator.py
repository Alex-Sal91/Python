def salary():
    print("How much do you earn annually? ")
    salary_new = int(input())
    tax_calculator(salary_new)


def basic_rate(salary_new):
    salary_after_tax = 'Your salary after tax is ' + str(salary_new * 0.8)
    return salary_after_tax


def higher_rate(salary_new):
    salary_after_tax = 'Your salary after tax is ' + str(salary_new * 0.6)
    return salary_after_tax


def additional_rate(salary_new):
    salary_after_tax = 'Your salary after tax is ' + str(salary_new * 0.55)
    return salary_after_tax


def tax_calculator(salary_new):
    rate = ''
    if salary_new > 11850 and salary_new <= 46350:
        rate = basic_rate(salary_new)
    elif salary_new > 46350 and salary_new <= 150000:
        rate = higher_rate(salary_new)
    elif salary_new > 150000:
        rate = additional_rate(salary_new)
    else:
        rate = "Your salary isn't taxed"
    print(rate)


salary()

