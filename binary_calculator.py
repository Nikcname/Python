
def returnOp(num):
  arr = []
  for i in num:
    if i == '0':
      arr.append('-')
    elif i == '1':
      arr.append('+')
  return arr

sym_arr = []
sum_search = int(input("Sum Ex eq:"))
for i in range(512, 1024):
  str_calc = ''
  sym_arr = returnOp(bin(i)[3:])
  for j in range(1, 10):
    str_calc += str(sym_arr[j - 1]) + str(j)

  str_sum = int(0)

  for m in range(len(str_calc)):
    if str_calc[m] == '+':
      str_sum += int(str_calc[m+1])
    elif str_calc[m] == '-':
      str_sum -= int(str_calc[m+1])
  
  if str_sum == sum_search:
    print(str_calc)
#https://gist.github.com/webinmd/c5c3592db7dc043406469a0eb6056331
#https://git-scm.com/book/en/v2
