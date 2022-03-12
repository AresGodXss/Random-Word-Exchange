import random, math


stringText = ""
# Reading from file.txt
fileX = open('RandomText.txt','r')
for line in fileX:
     
    stringText += line
    splitText = stringText.split()
    
fileX.close()


# Theoretical number of changed words
editedWords = math.floor(len(stringText) / 40)   

# Trying to change the word at randomized index of the text
for specWord in range(editedWords):
    randomWord = random.randrange(0,len(splitText)-1)
    splitText[randomWord] = "cum"
    #print(randomWord)



fileY = open('RandomTextEdited.txt','w')
ListToString = ' '.join(map(str, splitText))
fileY.write(ListToString)
fileY.close()
#print(splitText)
#print(editedWords)