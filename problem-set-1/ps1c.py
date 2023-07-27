r = 0.04
months_per_year = 12
r_per_month = r / months_per_year
total_cost_house = 1000000
portion_down_payment = 0.25
value_to_be_saved = total_cost_house * portion_down_payment
semi_annual_raise = 0.07
goal_months = 36
epsilon_dollar = 100
portion_saved_low_range = 0
portion_saved_high_range = 10000
decimal_transform_constant = 10000
bisection_steps = 0
is_not_possible = False

annual_salary = float(input("Enter your annual salary: "))
monthly_salary = annual_salary / months_per_year
original_annual_salary = annual_salary
months_count = 0
current_savings = 0


while True:
    bisection_steps += 1
    portion_saved_half_point = portion_saved_low_range + ((portion_saved_high_range - portion_saved_low_range) / 2)
    if portion_saved_half_point == portion_saved_high_range:
        is_not_possible = True
        break
    portion_saved_half_point_decimal = portion_saved_half_point / decimal_transform_constant
    while (current_savings < (value_to_be_saved - epsilon_dollar) or current_savings < (value_to_be_saved + epsilon_dollar)) and months_count <= goal_months:
        investment_return = current_savings * r_per_month
        monthly_savings = monthly_salary * portion_saved_half_point_decimal
        current_savings = current_savings + investment_return + monthly_savings
        if (months_count % 6 == 5):
            annual_salary *= 1 + semi_annual_raise
            monthly_salary = annual_salary / months_per_year
        months_count += 1
    if months_count != goal_months:
        if months_count > goal_months:
            portion_saved_low_range = portion_saved_half_point_decimal * decimal_transform_constant
        else:
            portion_saved_high_range = portion_saved_half_point_decimal * decimal_transform_constant
        months_count = 0
        current_savings = 0
        annual_salary = original_annual_salary
        monthly_salary = annual_salary / months_per_year
        continue
    else:
        break

if is_not_possible:
    print("It is not possible to pay the down payment in three years.")
else :
    print("Best savings rate:", portion_saved_half_point_decimal)
    print("Steps in bisection search:", bisection_steps)