L, N = list(map(int, input().split()))
L+=1
list_of_numbers = [int(input())+1 for _ in range(N)]

def knapSack(W, val, n): 
    K = [0 for x in range(W + 1)] for x in range(n + 1)] 

    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif val[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-val[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 

if knapSack(L, list_of_numbers, N)==L:
	print("OUI")
else:
	print("NON")