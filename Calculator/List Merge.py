numBuffer = False 
negativecheck = False  
operationStore = ["(","-","5","5","+","-","4","3",")"]
i = 0 
while(i < len(operationStore)): 
        print("i is:", i)
        try:
            numCheck = float(operationStore[i]) 
            if(numBuffer == False): 
                x = i 
                print("x is:", x)
                numBuffer = True
                if((operationStore[0] == "-") or (operationStore[x-1] == "-" and (operationStore[x-2] == "-" or operationStore[x-2] == "+" or operationStore[x-2] == "*" or operationStore[x-2] == "/" or operationStore[x-2] == "(" or operationStore[x-2] == ")"))):
                    operationStore[x-1] += operationStore[x]
                    operationStore.pop(x) 
                    numBuffer = False
                    i = 0 
                     
                else:
                    i +=1

            else:  
                operationStore[x] += operationStore[i] 
                operationStore.pop(i)
                i = x
                print("x:",x, "i:",i)
                i+=1  
            print(operationStore)
        except ValueError:  
            
            if(operationStore[i] == "."):
                operationStore[x] += operationStore[i]
                operationStore.pop(i)  
            
            else: 
                print("Yes")
                numBuffer = False
                i += 1 

print(operationStore)