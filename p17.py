names = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
     11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sisteen',17:'seventeen',18:'eighteen',19:'nineteen',
     20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}

def num_name(n):
  """ Translate an integer into words form

  :param n: the integer to translate
  :return: the English phrasing of :math:`n`

  >>> num_name(127)
  'one hundred and twenty-seven'
  """
  if 0 <= n < 20:
    return names[n]
  elif 20 <= n <= 90 and n % 10 ==0:
    return names[n]
  elif 20 < n <100:
    return names[(n//10)*10] + "-" + names[n % 10]
  elif 100 <= n <= 900 and n % 100 == 0:
    return names[(n//100)] + " hundred "
  elif 100 < n < 1000:
    return names[n//100] + " hundred and " + num_name(n % 100)
  elif n == 1000:
    return "one thousand" 
  else:
    raise ValueError("unexpected input: ",n)

def p17(n):
  tmp = ''
  for i in range(1,n+1):
    tmp += num_name(i) + "\n" 
  print(tmp)
  return len(tmp.replace(" ","").replace("-","").replace('\n',''))
  #return tmp


print(p17(1000))
