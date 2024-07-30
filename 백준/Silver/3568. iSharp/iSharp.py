declare = list(input().split(' '))
var_num = len(declare) - 1
common = declare[0]

var_dict = {}

for i in range(1,len(declare)):
    alpha = ''
    format = ''
    for x in declare[i]:
        if x.isalpha():
            alpha+=x
          
        else:
            if x !="," and x!=";":
                format+=x
    if '[]' in format:
        format = format.replace('[]','][')
    var_dict[i] = (alpha,format)


result = [common] * (len(declare)-1)


for i in range(len(result)):

    alpha,format=var_dict[i+1]
    added = format[::-1] + ' ' + alpha 
    result[i] +=added

for i in range(len(result)):
    result[i] +=";"

for x in result:
    print(x)
    