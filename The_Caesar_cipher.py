print("Вы хотите расшифровать=F или зашифровать=T?")
a = input()
print("Вы хотите использовать анлгийский=en или русский язык=ru?")
b = input()
print("Введите текст")
c = input()
print("Шаг сдвига?")
n = int(input())

def language(b,a):
  if b == "ru" and a =="T":
    russT(c)
  elif b == "ru" and a =="F":
    russF(c)
  elif b == "en" and a =="T": 
    englishT(c)
  else:
    englishF(c)

def englisT(c):
  d = []
  for i in range(len(c)):
    if c[i].isalpha() and c[i] == c[i].lower():
      s = ord(c[i])+n
      if 96 < s < 123:
        f = chr(s)
        d.append(f)
      else:
        s = s - 26
        f = chr(s)
        d.append(f)
    elif c[i].isalpha() and c[i] == c[i].upper():
      s = ord(c[i])+n
      if  64 < s < 91:
        f = chr(s)
        d.append(f)
      else:
        s = s - 26
        f = chr(s)
        d.append(f)     
    else:
      d.append(c[i])
      continue
  
  return ''.join(d)
  
def russT(c):
  d = []
  for i in range(len(c)):
    if c[i].isalpha() and c[i] == c[i].lower():
      s = ord(c[i])+n
      if 1071 < s < 1104:
        f = chr(s)
        d.append(f)
      else:
        s = s - 32
        f = chr(s)
        d.append(f)
    elif c[i].isalpha() and c[i] == c[i].upper():
      s = ord(c[i])+n
      if  1039 < s < 1072:
        f = chr(s)
        d.append(f)
      else:
        s = s - 32
        f = chr(s)
        d.append(f)     
    else:
      d.append(c[i])
      continue
  
  return ''.join(d)
  
def englishF(c):
  d = []
  for i in range(len(c)):
    if c[i].isalpha() and c[i] == c[i].lower():
      s = ord(c[i])-n
      if 96 < s < 123:
        f = chr(s)
        d.append(f)
      else:
        s = s + 26
        f = chr(s)
        d.append(f)
    elif c[i].isalpha() and c[i] == c[i].upper():
      s = ord(c[i])-n
      if  64 < s < 91:
        f = chr(s)
        d.append(f)
      else:
        s = s + 26
        f = chr(s)
        d.append(f)     
    else:
      d.append(c[i])
      continue
  
  return ''.join(d)
  
def russF(c):
  d = []
  for i in range(len(c)):
    if c[i].isalpha() and c[i] == c[i].lower():
      s = ord(c[i])-n
      if 1071 < s < 1104:
        f = chr(s)
        d.append(f)
      else:
        s = s + 32
        f = chr(s)
        d.append(f)
    elif c[i].isalpha() and c[i] == c[i].upper():
      s = ord(c[i])-n
      if  1039 < s < 1072:
        f = chr(s)
        d.append(f)
      else:
        s = s + 32
        f = chr(s)
        d.append(f)     
    else:
      d.append(c[i])
      continue
  
  return ''.join(d)
      
def prints(b,a):
  if b == "ru" and a =="T":
    print(russT(c))
  elif b == "ru" and a =="F":
    print(russF(c))
  elif b == "en" and a =="T": 
    print(englishT(c))
  else:
    print(englishF(c))

print(prints(b,a))
