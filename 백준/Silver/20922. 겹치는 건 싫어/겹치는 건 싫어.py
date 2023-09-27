

'''
https://www.acmicpc.net/problem/20922
'''

N,K = list(map(int,input().split(" ")))

sets = list(map(int,input().split(" ")))
srt= 0
MaxLen = 0
idx = {}

for i in range(len(sets)):
        

    if sets[i] not in idx:
        idx[sets[i]] = 1

    else:

        idx[sets[i]] += 1
        # print(srt,sets[i])
        while idx[sets[i]] > K:
            idx[sets[srt]] -=1
            # print(sets[srt])a
            srt += 1
    if MaxLen < (i-srt+1):
            MaxLen = (i-srt+1)

    # print("s: {}, i: {}, srt: {}, maxLen: {}".format(s,i,srt,MaxLen))

print(MaxLen)
    

    