#updated code for handling bracets w/ bidmas. 
#some variable names maybe be changed
operationStore = ["5","/","(","5","+","5",")"]   
bidmas = ["(","/","*","+","-"] 
bid = 0 
i = 0 
index = 0  
bracetCheck = False 

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
    





def div(x,y,i):
    z = float(x) / float(y)
    operationStore[i-1] = z

def times(x,y,i):
    z = float(x) * float(y)
    #print(z) 
    operationStore[i-1] = z 


def add(x,y,i):
    z = float(x) + float(y)
    #print(z)
    operationStore[i-1] = z 

def minus(x,y,i): 
    z = float(x) - float(y)
    operationStore[i-1] = z 


funcMap = { 
  '(':bracets, 
  '/':div,
  '*':times, 
  '+': add,
  '-': minus,
   
  
} 

def aFunction(operationStore, funcMap, bid, i, index, bracetCheck): 
    a = len(operationStore)-1
    while (bid < len(bidmas)): 
        while (i < len(operationStore)) and (i < a): 
            print(operationStore)
            print(a)
            if(operationStore[i] == "-") and (bidmas[index] == "+") or (operationStore[i] == "*") and (bidmas[index] == "/"): 
                funcMap[operationStore[i]](operationStore[i-1], operationStore[i+1], i)   
                operationStore.pop(i)
                operationStore.pop(i)
                a = a -2
                if(bracetCheck == True):
                    i = x
                else:

                    i = 0  
                

            elif operationStore[i] == bidmas[index]:
                try:
                    funcMap[operationStore[i]](operationStore[i-1], operationStore[i+1], i)   
                    operationStore.pop(i)
                    operationStore.pop(i)
                    a = a-2
                    print(a)
                    if(bracetCheck == True):
                        i = x
                    else:
                        
                        i = 0
                except TypeError:
                    bracetCheck = True 
                    a = funcMap[operationStore[i]](operationStore, a) 
                    print(i) 
                    x = i 
                    print(a) 
                    i+=1 
            else:
                i+=1  
        if(bracetCheck == True):  
            i = x 
            if(i + 2  == a) :
                operationStore.pop(a)
                operationStore.pop(i)
                bracetCheck = False
                bid = 1
                index = 1
                i = 0 
            elif (i + 1 == a):
                operationStore.pop(i)
                bracetCheck = False
                bid = 1
                index = 1
                i = 0 

            else:
                index+=1  
                bid+=1 
        else:

            index+=1  
            bid+=1
            i = 0 
    print(operationStore)
    

aFunction(operationStore, funcMap, bid, i, index, bracetCheck)
#print(stuff)


    

