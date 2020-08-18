def sum(a, b):
  return a + b

print('this is 3 + 12 =', sum(3, 12)) 

def oneUp(num):
  return num + 1

print('expect 7:', oneUp(6))

def howManySeconds(hours):
  return hours * 3600

print(howManySeconds(1))

def grade_percentage(user_score, pass_score):
  if int(user_score) >= int(pass_score):
    return 'You PASSED the Exam'
  if int(user_score) < int(pass_score):
    return 'You FAILED the Exam'

print(grade_percentage(87, 87))

def relationship(name):
  f = {'Darth Vader': 'father', 'Leia': 'sister', 'Han': 'brother in law', 'R2D2': 'droid'}
  return "Luke, I am your {}." .format(f[name]) 

print (relationship('Darth Vader')) 
