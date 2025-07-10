print("Welcome to the yearly budget calculator!")

salary = float(input("Enter your yearly salary: "))


def yearly_budget_calculator():
    print("Enter your budget for different categories (monthly amounts): ")
    monthly_food_budget = float(input("Enter your food budget: "))
    monthly_transportation_budget = float(input("Enter your transportation budget: "))
    monthly_entertainment_budget = float(input("Enter your entertainment budget: "))
    monthly_utilities_budget = float(input("Enter your utilities budget: "))

    print("Enter your housing information: ")
    monthly_rent = 0
    monthly_mortgage = 0
    yearly_tax = 0

    yearly_living = input("Do you live in a house or an apartment? ").lower()
    if yearly_living == "apartment":
        monthly_rent = float(input("Enter your monthly rent: "))

    elif yearly_living == "house":
        yearly_mortgage_or_tax = input("Do you pay property tax or mortgage? ").lower()

        if yearly_mortgage_or_tax == "mortgage":
            monthly_mortgage = float(input("Enter your monthly mortgage: "))
        elif yearly_mortgage_or_tax == "property tax":
            yearly_tax_percent = float(input("How much percent property tax do you pay? "))
            yearly_tax = (yearly_tax_percent / 100) * salary
        else:
            print("Invalid input. Assuming $0 for mortgage and tax.")

    yearly_food_budget = monthly_food_budget * 12
    yearly_transportation_budget = monthly_transportation_budget * 12
    yearly_entertainment_budget = monthly_entertainment_budget * 12
    yearly_utilities_budget = monthly_utilities_budget * 12
    yearly_rent = monthly_rent * 12
    yearly_mortgage = monthly_mortgage * 12

    return (
        yearly_food_budget,
        yearly_transportation_budget,
        yearly_entertainment_budget,
        yearly_utilities_budget,
        yearly_rent,
        yearly_mortgage,
        yearly_tax,
    )


(
    yearly_food_budget,
    yearly_transportation_budget,
    yearly_entertainment_budget,
    yearly_utilities_budget,
    yearly_rent,
    yearly_mortgage,
    yearly_tax,
) = yearly_budget_calculator()

yearly_expenses = (
    yearly_food_budget
    + yearly_transportation_budget
    + yearly_entertainment_budget
    + yearly_utilities_budget
    + yearly_rent
    + yearly_mortgage
    + yearly_tax
)
yearly_savings = salary - yearly_expenses

if yearly_savings < 0:
    print("\nYou are in debt by: $", -yearly_savings)
elif yearly_savings == 0:
    print("\nYou are breaking even. Consider lowering some costs to save for emergencies.")
else:
    print("\nYour yearly savings is: $", yearly_savings)
