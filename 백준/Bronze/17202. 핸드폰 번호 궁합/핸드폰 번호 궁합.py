def cal_one (num1,num2):
    left_lst=[]
    right_lst=[]
    num1,num2= str(num1),str(num2)
    for i in range(min(len(num1),len(num2))):
        val = (int(num1[i]) + int(num2[i]))%10
        left_lst.append(str(val))
    left = ''.join(left_lst)

    for i in range(min(len(num1)-1,len(num2))):
        val = (int(num1[i+1]) + int(num2[i]))%10
        right_lst.append(str(val))
    right = ''.join(right_lst)

    return (left,right)
    



num1 = input()
num2 = input()

result = []
while(len(num1)>=1 and len(num2)>=1):
    if (len(num1)==1 and len(num2) == 1):
        break
    num1,num2=cal_one(num1,num2)

print(num1+num2)