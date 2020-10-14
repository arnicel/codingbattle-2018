N = int(input())
P1 = int(input())
P2 = int(input())
P3 = int(input())

price = 0

if N>100:
	N-=100
	price += 100*P1
else:
	price += N*P1
	N-=N

if N>100:
	N-=100
	price += 100*P2
else:
	price += N*P2
	N-=N
	
price += N*P3

	


print(price)