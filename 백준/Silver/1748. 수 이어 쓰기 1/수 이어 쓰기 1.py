str_num = input()
length = len(str_num)

# 한자리(9)
# 두자리(9*10*2)
# 세자리(9*100*3)


result = 0

for i in range(1,length+1):
    x = 9*pow(10,i-1)*i
    result += x

y = pow(10,length)-1
y -= int(str_num)

result -= y*length
print(result)  