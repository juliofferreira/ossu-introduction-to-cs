current_savings = 0
r = 0.04
r_per_month = r / 12
annual_salary = float(input("Enter your annual salary: "))
monthly_salary = annual_salary / 12
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = 1000000
portion_down_payment = 0.25
value_to_be_saved = total_cost * portion_down_payment
semi_annual_raise = 0.07

months = 0
while (current_savings < value_to_be_saved):
    investment_return = current_savings * r_per_month
    monthly_savings = monthly_salary * portion_saved
    current_savings = current_savings + investment_return + monthly_savings
    if (months % 6 == 5):
        annual_salary *= 1 + semi_annual_raise
        monthly_salary = annual_salary / 12
    months += 1

print("Number of months: ", months)