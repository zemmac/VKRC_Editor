data ='    ;FOLD KLIN VB=7[mm/s] Genau=0[mm] ACC=100% RobWzg=1 Base=2 SPSTrig=5[1/100s] P ;' \
       '%{P}%MKUKATPVW,%CMOVE8,%VKLIN,%P 1:4, 2: VB=, 3:7, 4:[mm/s], 5: Genau=, 6:0, 7:[mm], 8: ACC=, 9:100, ' \
       '10:%, 11: RobWzg=, 12:1, 13: Base=, 14:2, 15: SPSTrig=, 16:5, 17:[1/100s], 18: P, 19:18, 20:-1, 21:16'
dict={}

data = data.split(',')
print(data)







# data = data.split('%P ')
#
#
# for name, val in [item.split(':') for item in data[1].split(",")]:
#     dict[(name)] = val
# print(dict)
# string =' '
# for item in dict:
#     string += f'{item}:{dict[item]},'
# print(string)
#
# a = ' '+''.join([f'{item}:{dict[item]},' for item in dict])
# print(a)