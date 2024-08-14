N,M = map(int,input().split())


no_hear = set()
no_see = set()
result = set()
for _ in range(N):
    name = input()
    no_hear.add(name)

for _ in range(M):
    name = input()
    if name in no_hear:
        no_see.add(name)

if len(no_see) < len(no_hear):
    for name in no_see:
        if name in no_hear:
            result.add(name)

else:
    for name in no_hear:
        if name in no_see:
            result.add(name)

print(len(result))
result=sorted(result)
for name in result:
    print(name)