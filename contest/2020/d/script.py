def split(word): 
    return [char for char in word]  

L,C = list(map(int, input().split()))
map = []
for _ in range(L):
	map.append(split(input()))
	
ligne = []
for element in input().split():
	ligne.append(element)
	
colonne = []
for element in input().split():
	colonne.append(element)
	
print(L, C, map , ligne, colonne)
