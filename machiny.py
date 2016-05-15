import re
#class State():
#    def __init__(self):
#        self.Steps = dict{}
#    def add(self,current,newchar,nextstage,directional)
#        if current not in Steps :
#            Steps[current] = dict()
#        Steps[current] = {}
def replaceChar(word,char,number):
    startWord = ""
    if number >= 0:
        startWord = word[:number]
    endWord = ""
    if number+1 < len(word):
        endWord = word[number+1:]
    if char == "B":
        char = " "
    word = startWord+char+endWord #2
    return word
def onMachine(funcFile,word):
    f = open(funcFile)
    Steps = dict()
    currentSteps = 0
    currentStage = "q1" 
    for line in f:
        func = re.match('(\w)(\w+)[-][>](\w)(\w+)?(\w)',line)
        if func != None:
            if func.group(1) not in Steps :
                Steps[func.group(1)] = dict()
            Steps[func.group(1)][func.group(2)] = (func.group(3),func.group(4),func.group(5))
    chars = []
    f = open(word)
    a = ""
    for line in f:
        for char in line:
            chars.append(char)
        a = line
    oldCS = ""
    while True:
        if currentSteps <0 or currentSteps >=len(chars) or chars[currentSteps] not in Steps:
            currentChar = "B"
        else:
            currentChar = chars[currentSteps]
        if currentStage == "STO" or currentStage == "STOP":
            a = replaceChar(a,Steps[currentChar][oldCS][0][0],currentSteps)
            break
        if Steps[currentChar][currentStage][2][0] == "R":
            if currentChar != "B":
                if len(a) > currentSteps:
                    a = replaceChar(a,Steps[currentChar][currentStage][0][0],currentSteps)
                else:
                    a+= Steps[currentChar][currentStage][0][0]
            currentSteps=currentSteps+1
            
        elif Steps[currentChar][currentStage][2][0] == "H":
            if currentChar != "B":
                if len(a) > currentSteps:
                    a = replaceChar(a,Steps[currentChar][currentStage][0][0],currentSteps)
                else:
                    a+= Steps[currentChar][currentStage][0][0]
            currentSteps=currentSteps
        elif Steps[currentChar][currentStage][2][0] == "L":
            if currentChar != "B" and currentSteps >= 0:
                a = replaceChar(a,Steps[currentChar][currentStage][0][0],currentSteps)
            currentSteps=currentSteps-1
        oldCS = currentStage
        currentStage = Steps[currentChar][currentStage][1]
    return a
if __name__ == '__main__':
    #number1 = onMachine('numbefunc.txt','input.txt')
    number2 = onMachine('word.txt','winput.txt')
    #number3 = onMachine('numbefunc.txt','input.txt')
    number4 = onMachine('word3.txt','winput3.txt')            
    number5 = onMachine('word4.txt','winput4.txt')            
    #print(number1)
    print(number2)
    #print(number3)
    print(number4)
    print(number5)
