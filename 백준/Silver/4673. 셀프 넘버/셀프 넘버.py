self_num_set = set()
def generate_dn(num):
    d_n = num + sum(int(digit)for digit in str(num))
    if d_n <= 10000:
        self_num_set.add(d_n)



for num in range(1,10001):
    generate_dn(num)


for i in range(1, 10001):
    if i not in self_num_set:
        print(i)
