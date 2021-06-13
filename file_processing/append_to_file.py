with open('../file_processing/fruits.txt', 'a+') as m_file:
  m_file.write('\nGarlic')
  m_file.seek(0)  # send cursor at 0 point meaning beginning of the file
  content = m_file.read()

print(content)