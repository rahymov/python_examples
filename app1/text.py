def sen_maker(word):
  questions = ("how", "why", "what")
  capitalized = word.capitalize()
  if word.startswith(questions):
    return "{}?".format(capitalized)
  else:
    return "{}.".format(capitalized)

user_input_results = []
while True:
  user_input = input("Say something: ")
  if user_input == "exit":
    break
  else: 
    user_input_results.append(sen_maker(user_input))
print(" ".join(user_input_results))