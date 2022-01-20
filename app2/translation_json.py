import json
import difflib
from difflib import get_close_matches

data = json.load(open("../data.json"))

def translate(w):
  w = w.lower()
  if w in data:
    return data[w]
  elif w.title() in data:
    return data[w.title()]
  elif w.upper() in data:
    return data[w.upper()]
  elif len(get_close_matches(w, data.keys())) > 0:
     un = input("Did you mean %s instead? Enter y if YES, or n if NO! " % get_close_matches(w, data.keys())[0]).lower()
     if un == 'y':
       return data[get_close_matches(w, data.keys())[0]]
     elif un == 'n':
       return "Please check it again. "
     else:
       return "We did not understand the word!"
  else:
    return "The word does not exist!"

user_input = input("Please enter word to see definition: ")

output = translate(user_input)

if type(output) == list:
  for o in output:
    print(o)
else:
  print(output)