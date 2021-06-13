# iterate each temperature in new_temp arr divide by 10 and if temp less than 0 ignore
temperature = [123,234,235,345,-356,278, -9999]

new_temp = [temp/10 for temp in temperature if temp > 0]
print(new_temp)


# if you would like to use if else it should come before for loop

# new_temp = [temp/10 if temp != -9999 else 0 for temp in temperature]
# print(new_temp)