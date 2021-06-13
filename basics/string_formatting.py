from datetime import date

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
today = date.today()

message = "Hello %s %s!" % (first_name, last_name)
message2 = f"Hello {first_name} {last_name}! Sup  {today}!This format works python v 3.6 or higher" 
print(message)
print(message2)

