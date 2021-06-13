phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key,value in phone_numbers.items():
  print("{} has a phone number {}.".format(key,value))




# repace + front of phone number to 00 
for value in phone_numbers.values():
  print(value.replace("+", "00"))