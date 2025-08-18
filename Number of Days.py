

n_days = int(input("Enter number of days: "))

years = n_days // 365

remaining_days = n_days % 365

weeks = remaining_days // 7

days = remaining_days % 7


print(f"Years = {years}, Weeks = {weeks}, Days = {days}")
