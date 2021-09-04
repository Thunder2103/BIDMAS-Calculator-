#original bidmas code 
#some variable names maybe be changed
operationStore = ["5","-","5","*","5","+","5"]   
bidmas = ["/","*","+","-"] 
bid = 0 
i = 0 
index = 0 
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
  '/':div,
  '*':times, 
  '+': add,
  '-': minus,
   
  
} 




def aFunction(operationStore, funcMap, bid, i, index): 
    while (bid < len(bidmas)): 
        #print("Hello")
        while (i < len(operationStore)):
            if(operationStore[i] == "-") and (bidmas[index] == "+") or (operationStore[i] == "*") and (bidmas[index] == "/"): 
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
    print(operationStore)
    

aFunction(operationStore, funcMap, bid, i, index)
#print(stuff)