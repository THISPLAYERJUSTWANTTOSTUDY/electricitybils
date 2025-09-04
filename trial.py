aircone_detail = {
    22 : 2.3, 23 : 2.1, 24 : 1.85, 25 : 1.6, 26 : 1.35, 27 : 1.1
}

def aircone(x,y): 
    counter = aircone_detail.get(x,0) #aircone_detail[x]
    return counter * 4.35 * y
    
def bulb (x): 
    return 0.056 * x 

def roughly(): 
    ac = aircone(int(input('enter aircone temperature')),int(input('enter time usage')))
    lampu = bulb(int(input('enter bulb time usage')))
    return ac + lampu 
print(roughly
      ())