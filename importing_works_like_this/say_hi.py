def say_hi(name):
  if name == 'Matt':
    print(matt_greeting)
  else:
    print(f'Hello {name}')

matt_greeting = (
  'Hello Matt.\n'
  'I really missed you around here.\n\n'
  'Love,\n'
  'Python'
)

if __name__ == '__main__':
  say_hi('Matt')
