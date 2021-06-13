def weather_cond(temp):
  if temp > 7:
    return "Warm"
  else:
    return "Cold"

user_input = float(input("Enter temp: "))
print(weather_cond(user_input))