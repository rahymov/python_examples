import mysql.connector

con = mysql.connector.connect(
  user = "ardit700_student",
  password = "ardit700_student",
  host = "108.167.140.122",
  database = "ardit700_pm1database"
)

user_input = input("Please enter a word: ")

cursor = con.cursor()

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s' " % user_input)
results = cursor.fetchall()

if results:
  for i in results:
    print(i[0])
else: 
  print("No result!")