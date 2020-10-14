def split(word): 
    return [char for char in word]  

L,C = list(map(int, input().split()))
map = list()
for _ in range(L):
	map.append(split(input()))
	
test = list(map(int, input().split()))
