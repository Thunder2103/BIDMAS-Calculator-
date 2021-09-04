#A calculator GUI made with tkinter - Bidmas included 

#negative numbers and error handling... 
import tkinter as tk 

#Calculator Button variables
opList = ["Del", "Clr", "X", "/", "+", "-"]  
miscList = ["0", ".", "(", ")", "Ans"]
index = 0 
y = 1 
posX = 105
posY = 65
numVal = 0


#Calculations/Merging list variables. 
operationStore = [] 
characterCheck = ""
i = 0  
numBuffer = False
operatorCheck = False 

#Calculations variables. 
bidmas = ["(","/","*","+","-"] 
bidCounter = 0 
bidIndex = 0 
opCounter = 0 
bracetsCheck = False 
ansStore = "0"
labelClearFlag = False 

#calculator display
window = tk.Tk()
window.geometry("255x315")
title = tk.Label(text = "Tom's Calculator")
displayText = tk.StringVar()
display = tk.Label(textvariable = displayText, anchor = "w", bg = "white", width = 75, height = 2)   


#Bidmas Functions... 
def bracets(operationStore, a):
    b = 0 
    while b < len(operationStore):
        if(operationStore[b] == ")"):
            a = b 
            return a
        else:
            b+=1 
    a = len(operationStore)-1 
    return a

def div(x,y,opCounter):
    try:
        z = float(x) / float(y)
        operationStore[opCounter-1] = z  
    except ValueError as error: 
        labelSyntaxError()
        operationStore.clear() 
        global labelClearFlag
        labelClearFlag = True 
        raise Exception('Invalid Syntax, THE PROGRAM WILL STILL RUN: {}'.format(error)) from None


def times(x,y,opCounter): 
    global labelClearFlag 
    try:
        z = float(x) * float(y)
        operationStore[opCounter-1] = z
    except ValueError as error: 
        operationStore.clear()
        print(operationStore)
        labelSyntaxError() 
        labelClearFlag = True
        raise Exception('Invalid Syntax, THE PROGRAM WILL STILL RUN: {}'.format(error)) from None 
        
def add(x,y,opCounter): 
    try:
        z = float(x) + float(y)
        operationStore[opCounter-1] = z  
    except ValueError as error:
        labelSyntaxError()
        operationStore.clear()
        global labelClearFlag
        labelClearFlag = True 
        raise Exception('Invalid Syntax, THE PROGRAM WILL STILL RUN: {}'.format(error)) from None  

def minus(x,y,opCounter): 
    try:
        z = float(x) - float(y)
        operationStore[opCounter-1] = z  
    except ValueError as error:
        labelSyntaxError()
        operationStore.clear()
        global labelClearFlag
        labelClearFlag = True   
        raise Exception('Invalid Syntax, THE PROGRAM WILL STILL RUN: {}'.format(error)) from None  

#Dict that holds key-value pairs, maps a function to a key value 
functionDict = {  
    '(': bracets, 
    '/': div,
    '*': times, 
    '+': add, 
    '-': minus, 

} 


#adding/removing text on the calculator:

#adds text
def labelTextAppend(n):
    s = displayText.get()
    s+= str(n)
    displayText.set(s)  

#displays final answer on display 
def labelTextAnswer(finalAns):
    s = displayText.get()
    s = str(finalAns)
    displayText.set(s) 

#deletes text from the display
def labelTextDelete():  
    characterNumber = len(characterCheck)
    s = displayText.get()
    s = s[:-int(characterNumber)]
    displayText.set(s)

#clears all the text from the display 
def labelTextClear():
    s = displayText.get()
    s = ''
    displayText.set(s)

#diaplyed when a syntax error occurs 
def labelSyntaxError():
    s = displayText.get()
    s = 'Syntax Error'
    displayText.set(s)






#Handles whenever a button is clicked - stores value in a list. 
def OnClickEvent(operationStore,n, i, numBuffer, operatorCheck): 
   
    global labelClearFlag
    
    if(labelClearFlag == True):
        labelTextClear() 
        labelClearFlag = False  
    
    if(n == "X"):
        operationStore.append("*")
        labelTextAppend("*")
    
    elif(n == "Del"):
        global characterCheck
        try:
            characterCheck = operationStore[-1]
            labelTextDelete()
            operationStore.pop()
        except IndexError:
            print("Can't delete something from an empty list") 
        
    elif(n == "Clr"):
        operationStore.clear() 
        labelTextClear()
    
    elif(n == "Ans"):
        global ansStore 
        labelTextAppend(n)
        operationStore.append(int(ansStore))
    
    elif(n == "("):
        try:
            
            numCheck = float(operationStore[-1])
            operationStore.append("*")
            labelTextAppend(n)
            operationStore.append(n)
            labelTextAppend(n)
        
        except ValueError:
            operationStore.append(n)
            labelTextAppend(n)  
        
        except IndexError:
            operationStore.append(n)
            labelTextAppend(n)  
    else:
        labelTextAppend(n)
        operationStore.append(str(n))  

    #merged indexes in list to form the numbers and operators the user inputs 
    while(i < len(operationStore)):
        
        if(operationStore[i] == "+" or operationStore[i] == "-" or operationStore[i] == "*" or operationStore[i] == "/" or operationStore[i] == "(" or operationStore[i] == ")" ):
            
            if(operationStore[0] == "-" or (operationStore[i] == "-" and (operationStore[i-1] == "+" or operationStore[i-1] == "-" or operationStore[i-1] == "*" or operationStore[i-1] == "/" or operationStore[i-1] == "(" or operationStore[i-1] == ")"))):
                operatorCheck = False 
            
            else:
                operatorCheck = True 
        
        else:
            operatorCheck = False 
        
        if(operatorCheck == False): 
           
            if(numBuffer == False): 
                x = i 
                numBuffer = True
                i +=1
                
            else:  
                operationStore[x] += operationStore[i] 
                operationStore.pop(i)
                print("x:",x, "i:",i)
                i=x
                i+=1 
        else: 
            if(operationStore[i] == "."):
                operationStore[x] += operationStore[i]
                operationStore.pop(i)  
            else: 
                numBuffer = False
                i += 1 
                    

    #print(operationStore)
   
        
    
   

    




    
#handles whenever equals is clicked - does calculations. 
def EqualsClickEvent(operationStore,functionDict, bidCounter, bidIndex, opCounter, bracetsCheck):  
    if(operationStore == []):
        return None

    global labelClearFlag
    labelClearFlag = True 
    a = len(operationStore)-1
    #print(a)
    while(bidCounter < len(bidmas)):
        #print(operationStore)
        while(opCounter < len(operationStore)) and (opCounter < a):
            if(operationStore[opCounter] == "-") and bidmas[bidIndex] == "+" or (operationStore[opCounter] == "*") and (bidmas[bidIndex] == "/"):
                functionDict[operationStore[opCounter]](operationStore[opCounter-1], operationStore[opCounter+1], opCounter)
                operationStore.pop(opCounter)
                operationStore.pop(opCounter)
                a = a - 2
                if(bracetsCheck == True):
                    opCounter = buffer
                else:
                    opCounter = 0  
            elif(operationStore[opCounter] == bidmas[bidIndex]): 
                try:
                    functionDict[operationStore[opCounter]](operationStore[opCounter-1], operationStore[opCounter+1], opCounter)
                    operationStore.pop(opCounter)
                    operationStore.pop(opCounter)
                    a = a - 2
                    if(bracetsCheck == True):
                        opCounter = buffer
                    else:
                        opCounter = 0  
                except TypeError:
                    bracetsCheck = True  
                    a = functionDict[operationStore[opCounter]](operationStore, a)
                    buffer = opCounter
                    opCounter = opCounter + 1

            else:
                opCounter = opCounter + 1  
        if(bracetsCheck == True):
            opCounter = buffer
            if(opCounter + 2 == a):

                operationStore.pop(a)
                operationStore.pop(opCounter)
                bracetsCheck = False
                bidIndex = 1
                bidCounter = 1
                opCounter = 0
            elif(opCounter + 1 == a):
                operationStore.pop(opCounter)
                bracetsCheck = False
                bidCounter = 1
                bidIndex = 1
                opCounter = 0 
            else:
                bidIndex +=1 
                bidCounter+=1
        else: 
            bidIndex+=1 
            bidCounter+=1 
            
            opCounter = 0 
    #print(operationStore) 
    if(len(operationStore) > 1):
        labelSyntaxError()
        labelClearFlag = True
        return None
    else:
        labelTextAnswer(operationStore[0])
        global ansStore
        ansStore = operationStore[-1] 
        #print("ansStore:", ansStore)  
        operationStore.clear()




    

    




   
      

# creates and places Exit and equals button.  
btnExit = tk.Button(text = "Exit", width = 5, height = 2, command = window.destroy).place(x = posX, y = posY + 200)
btnEqual = tk.Button(text = "=", width = 5, height = 2, command = lambda: EqualsClickEvent(operationStore,functionDict, bidCounter, bidIndex, opCounter, bracetsCheck)).place(x = posX + 100, y = posY + 200)

#creates and places button 1 - 9. 
def NumberButtons(y, posX, posY, numVal):
    while (y <= 3):
        for i in range(3): 
            tk.Button(text = str(9-numVal), width = 5, height = 2, command = lambda numVal = 9-numVal: OnClickEvent(operationStore,numVal, i, numBuffer, operatorCheck)).place(x= posX, y = posY) 
            numVal +=1  
            posX -= 50 
        y+=1 
        i = 0  
        posY += 50
        posX = 105 

 
 #creates and places Del, Clr, X, /, -, + buttons
def OperatorButtons(y, posX, posY, opList, index):
    while(y <= 3):
        for i in range(2):
            tk.Button(text = str(opList[index]), width = 5, height = 2, command = lambda index = index: OnClickEvent(operationStore,opList[index], i, numBuffer, operatorCheck)).place(x = posX + 50, y = posY)
            index += 1
            posX += 50 
        y += 1 
        i = 0  
        posY += 50 
        posX = 105 


#creates and places 0, ., (, ), Ans buttons 
def MiscButtons(y, posX, posY, index, miscList):
        for i in range(5):
            tk.Button(text = str(miscList[index]), width = 5, height = 2, command = lambda index = index: OnClickEvent(operationStore,miscList[index], i, numBuffer, operatorCheck)).place(x = posX - 100, y = posY + 150)
            index += 1  
            posX += 50 
        
        
 






# runs functions for buttons 
NumberButtons(y, posX, posY, numVal)
OperatorButtons(y, posX, posY, opList, index)
MiscButtons(y, posX, posY, index, miscList)
title.pack()
display.pack() 







#loads display 
tk.mainloop()


