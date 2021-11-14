import datetime

def func():
  now = datetime.datetime.now()
  print("Current data and time: ", str(now))
  return now

if __name__ == '__main__':
  func()