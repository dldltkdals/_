'''
시작시간 16:09
화은이는 이번 영어 시험에서 틀린 문제를 바탕으로 영어 단어 암기를 하려고 한다. 그 과정에서 효율적으로 영어 단어를 외우기 위해 영어 단어장을 만들려 하고 있다. 화은이가 만들고자 하는 단어장의 단어 순서는 다음과 같은 우선순위를 차례로 적용하여 만들어진다.

자주 나오는 단어일수록 앞에 배치한다.
해당 단어의 길이가 길수록 앞에 배치한다.
알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
 
$M$보다 짧은 길이의 단어의 경우 읽는 것만으로도 외울 수 있기 때문에 길이가 
$M$이상인 단어들만 외운다고 한다. 화은이가 괴로운 영단어 암기를 효율적으로 할 수 있도록 단어장을 만들어 주자.
'''
import sys
input = sys.stdin.readline
N,M = list(map(int,input().split(" ")))
WordCnt = {}
for _ in range(N):
    word = input().rstrip()
    # print(word)
    if word in WordCnt:
        WordCnt[word] += 1
    else:
        WordCnt[word] = 1
voca = []

for k,item in WordCnt.items():
    AlphaCnt = len(k)#단어의 글자수
    if AlphaCnt >= M:
        voca.append([-item,-AlphaCnt,k])
        
for word in sorted(voca):
    print(word[-1])