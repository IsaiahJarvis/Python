import random

def MONKEYTYPE(length):
    monkword = ""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    for x in range(length):
        monkword += letters[random.randint(0, 26)]
    return monkword
        

def COMPARE(monkeyword, word):
    score = 0
    for x in range(len(word)):
        if monkeyword[x] == word[x]:
            score += 1
    if score == len(word):
        return True, score
    else:
        return False, score

def RUN():
    counter = 0
    bestscore = 0
    bestword = ""
    running = True
    realword = str(input("input: "))
    while running:
        counter += 1
        curword = MONKEYTYPE(len(realword))
        result, points = COMPARE(curword, realword)
        if result:
            running = False
            print("after " + str(counter) + " attempts the monkey typed the sentence correct")
        else:
            if points > bestscore:
                bestword = curword
                bestscore = points
            if counter % 1000 == 0:
                print(bestword, bestscore)
        
        
    
