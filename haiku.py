from random import randint

wordList1 = ["Enchanting", "Amazing", "Colourful", "Delightful", "Delicate"]
wordList2 = ["visions", "distance", "conscience", "process", "chaos"]
wordList3 = ["superstitious", "contrasting", "graceful", "inviting", "contradicting", "overwhelming"]
wordList4 = ["true", "dark", "cold", "warm", "great"]
wordList5 = ["scenery","season", "colours","lights","Spring","Winter","Summer","Autumn"]
wordList6 = ["undeniable", "beautiful", "irreplaceable", "unbelievable", "irrevocable"]
wordList7 = ["inspiration", "imagination", "wisdom", "thoughts"]

file = open('tweet.txt', 'w')
sourceAdj = open('adj.txt', 'r')
sourceAdj1 = open('adj1.txt', 'r')
sourceAdj2 = open('adj2.txt', 'r')
sourceAdj3 = open('adj3.txt', 'r')
sourceNoun = open('noun.txt', 'r')
sourceNoun1 = open('noun1.txt', 'r')
sourceNoun2 = open('noun2.txt', 'r')
wordList1 = sourceAdj.read().split()
wordList2 = sourceNoun.read().split()
wordList3 = sourceAdj1.read().split()
wordList4 = sourceAdj2.read().split()
wordList5 = sourceNoun1.read().split()
wordList6 = sourceAdj3.read().split()
wordList7 = sourceNoun2.read().split()
		
wordIndex1=randint(0, len(wordList1)-1)
wordIndex2=randint(0, len(wordList2)-1)
wordIndex3=randint(0, len(wordList3)-1)
wordIndex4=randint(0, len(wordList4)-1)
wordIndex5=randint(0, len(wordList5)-1)
wordIndex6=randint(0, len(wordList6)-1)
wordIndex7=randint(0, len(wordList7)-1)

haiku = wordList1[wordIndex1] + " " + wordList2[wordIndex2] + ",\n" 
haiku = haiku + wordList3[wordIndex3] + " " + wordList4[wordIndex4] + " " + wordList5[wordIndex5]  + ",\n"
haiku = haiku + wordList6[wordIndex6] + " " + wordList7[wordIndex7] + "."

print(haiku)
file.write(haiku)