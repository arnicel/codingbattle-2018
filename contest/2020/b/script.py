def split(word): 
    return [char for char in word]  
      
def isPalindrome(s):
    return s == s[::-1]
	  
def isvoyelle(carac):
	return carac in ["a", "e", "i", "o", "u", "y"]
# Driver code 
word = input()
bonus = "ker" in word
palyn = isPalindrome(word)

score=0
word = split(word)

for carac in word:
	if isvoyelle(carac):
		score+=2
	else: 
		score-=1
		
if bonus:
	score+=5
	
if score>0 and palyn:
	score*=2



print(score) 