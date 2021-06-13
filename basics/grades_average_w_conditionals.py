import time
start = time.time()

def average(val):
  if type(val) == dict:
    ave = sum(val.values( ))/len(val)
  else:
    ave = sum(val)/ len(val)
  return ave


student_grades = {"bob": 90, "ab": 99, "joe": 89}
print(average(student_grades))


end = time.time()
print(end - start)