'''
시작시간 21:20
1234567
3125555

'''


N = int(input())
numbers = [[0]+[i for i in range(1,N+1)]]
numbers.append([0]+[int(input()) for _ in range(N)])

uniques = set(numbers[1][1:])
count = 0
dict = {}

check = set()
for i in uniques:
    set1,set2 = set(),set()
    j = i

    while 1:
        row_1,row_2 = numbers[0][j],numbers[1][j]
        if row_1 not in set1 and row_2 not in set2:
            set1.add(row_1)
            set2.add(row_2)
            j = row_2
        else:
            if len(set1):
                if set1==set2:
                    check.update(set1)
                break
check = list(check)
check.sort()
print(len(check))
for i in check:
    print(i)