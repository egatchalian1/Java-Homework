#using [0:2], it wont print up to 2, you rhave to print up to 3
"""
word="apple"
print word[0]
print word[1]
print word[2]
print word[3]
print word[4]
print word[0:5]
print word[-1]
print word[-2]
print word[-3]
print word[-4]
print word[-5]
print word[-5:-1]
print"w" +word[0:3]
"""




#len "length" counts the letters in the string
"""
word="papaya"
x=len(word)

print x #input x and you get the length of the word 6
print word [x-1] #counts the character in the 5th position (6-1) "a"


for char in word: #for is a loop, char prints out the word papaya
    print char
"""
#example 1
"""
word="apple"
lenght=len(word)   
for i in range(len(word)):   #using a presetfunction
    print word[-(i+1)]
"""

#example 2
"""
word="apple"
length=len(word)
index=0
while index< len(word):
    letter=word[length-1]
    length=length-1
    index=index+1
    print letter
"""

#example 3
"""
word="papaya"
length=len(word)
index=0
while index>(-length):
    letter=word[index-1]
    print letter
    index=index-1
"""

#example 4
"""
word="racecar"
length=len(word)
index=1
while index<len(word)+1:
    letter=word[index*-1]
    print letter
    index= index+1
"""

#program to find out input of word is a palondrom


 
