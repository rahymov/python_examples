# m_file = open("fruits.txt")
# content = m_file.read()
# m_file.close()


# Instead of use open and close file use with function it'll close at the end for you!!!
with open("fruits.txt") as m_file:
  content = m_file.read()

print(content)


#example2  read bear.txt and print 90 Characters 

# with open('bear.txt') as m_file:
#     content = m_file.read()

# print(content[:90])