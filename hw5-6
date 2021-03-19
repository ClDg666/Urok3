def for_dict(line):
    lst = []
    # print(line)
    lst = line.split(' ')
    # print(lst)
    j = 0
    s1 = 0
    s2 = 0
    s3 = 0
    while j < len(lst):
        index = lst[j]
        # print(index)
        i = index.find('(л)')
        if i != -1:
            s1 = int(index[:i])
        i = index.find('(пр)')
        if i != -1:
            s2 = int(index[:i])
        i = index.find('(лаб)')
        if i != -1:
            s3 = int(index[:i])
        j += 1
    sum = s1 + s2 + s3
    # print(sum)
    total = {}
    return lst[0], sum

def convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct


fil_obj = open("0061.txt", encoding='UTF-8')
line = fil_obj.readline()
count = sum(1 for line in fil_obj)
fil_obj.close()

fil_obj = open("006.txt", encoding='UTF-8')
nums = fil_obj.read().splitlines()
# print(nums)
count_lst = len(nums)
i = 0
dict_total = {}
while i < count_lst:
    line = nums[i]
    ret = for_dict(line)
    ret_dict = convert(ret)
    # print(ret_dict)
    # print(i)
    i += 1
    dict_total.update(ret_dict)
print(dict_total)

fil_obj.close()
