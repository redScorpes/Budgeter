start = 1000
monthly = 20

print("what month would you like to know?")
month = int(input())

print("what year would you like to know?")
year = int(input())

total_months = (year - 2023 - 1) * 12 + 1 + month

current_money = total_months * 20 + 900

print(current_money)