word = input("Enter word = ")
acnt = 0
ecnt = 0
icnt = 0
ocnt = 0
ucnt = 0

for i in range(len(word)):
    if word[i] == "a" or word[i] == "A":
        acnt += 1
    elif word[i] == "e" or word[i] == "E":
        ecnt += 1
    elif word[i] == "i" or word[i] == "I": 
        icnt += 1
    elif word[i] == "o" or word[i] == "O":
        ocnt += 1
    elif word[i] == "u" or word[i] == "U":
        ucnt += 1
    else:
        print("Character",(word[i]), "is not vowel")


print("Total counts:")
print("a:", acnt)
print("e:", ecnt)
print("i:", icnt)
print("o:", ocnt)
print("u:", ucnt)