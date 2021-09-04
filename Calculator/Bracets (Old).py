#original code for bracets - not efficient/practical...
#doesn't work very well has been revised
#some variable names maybe be changed
operationStore = ["(","(","5","+","5",")","+","6"]   
bidmas = ["(","/","*","+","-"] 
bid = 0 
i = 0 
index = 0  

def bracets(thingmap, stuff, bid, i, index): 
    i+=1 
    while bid < len(bidmas):
        while (i < len(operationStore)) and (operationStore[i] != ")"):  
            if(bidmas[index] == "(") and (bidmas[index] == operationStore[i]):
                funcMap[operationStore[i]](funcMap, operationStore, bid, i, index)
                
            elif(operationStore[i] == "-") and (bidmas[index] == "+") or (operationStore[i] == "*") and (bidmas[index] == "/"): 
                funcMap[operationStore[i]](operationStore[i-1], operationStore[i+1], i)   
                operationStore.pop(i)
                operationStore.pop(i)
                i = 0  
            elif operationStore[i] == bidmas[index]:
                funcMap[operationStore[i]](operationStore[i-1], operationStore[i+1], i)   
                operationStore.pop(i)
                operationStore.pop(i)
                i = 0  
            else:
                i+=1  
        index+=1 
        bid+=1
        i = 0  
    operationStore.pop(i)
    try: 

        if(operationStore[i+1] == ")"):
            operationStore.pop(i+1)
    except IndexError:
        print(operationStore)

    print(operationStore)  
        
 
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




bracets(funcMap, operationStore, bid, i, index)