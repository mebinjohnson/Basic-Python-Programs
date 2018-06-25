class Error:
  'Base Class for other exceptions'
  pass

class ValueTooSmallError(Error):
  'Raised when the input is too small'
  pass

class ValueTooLargeError(Error):
  'Raised when the input is too large'
  pass

while True:
  try:
    i_num=int(input("Enter a Number: "))
    number=100

    if i_num<number:
      raise ValueTooSmallError
    elif i_num>number:
      raise ValueTooLargeError
    break
  except ValueTooSmallError:
    print 'To Small'
  except ValueTooLargeError:
    print 'To Large'
