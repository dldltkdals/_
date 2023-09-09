H,W,N,M = list(map(int,input().split(" ")))
h_cnt = H//(N+1) if H%(N+1)==0 else H//(N+1) + 1 
w_cnt = W//(M+1) if W%(M+1)==0 else W//(M+1) + 1 
print(h_cnt*w_cnt)