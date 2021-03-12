s = 0       # счетичик суммы
ex = 0      # флаг выхода из программы, если был символ выхода из программы 'q'
while 1:
   if ex == 1: # если флаг = 1 - то выходим из цикла и пограммы
      break
   else:
      raw = input('')
      a = raw.split(' ')
      for k in range(len(a)):
         if a[k] == 'q':
            ex = 1   # фиксируем флаг в 1 - нашёл символ 'q'
            break
         else:
            a[k] = int(a[k])
            s = s + a[k]
      print(s)
