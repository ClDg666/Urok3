fil_obj = open("003.txt", encoding = 'UTF-8')
lst1 = fil_obj.read().split()
# print(lst1)

pay = []
j = 1

print('Менее 20000.00 получают:')
while j < len(lst1):
    p = float(lst1[j])
    if p < 20000:
        print(lst1[j-1])
    pay.append(p)
    j += 2
# print(pay)
aver = sum(pay) / len(pay)
print(aver)

fil_obj.close()