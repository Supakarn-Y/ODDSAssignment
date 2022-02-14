
def funcA(number) :
    text1 = str(number)
    result = ""
    for i in text1 :
        if( int(i) % 2 == 0 ) :
            result += "Even" + i
        else :
            result += "Odd" + i
    return result

def funcB(text) :
    check = ["Odd","Even"]
    text1 = ""
    result = ""
    i = 0
    while i < len(text) :
        if(text1 == check[0] or text1 == check[1]):        
            text1 = text1[::-1].upper()
            text1 +=  text[i]
            result += text1
            text1 = ""
            i += 1
        else :
            text1 += text[i]
            i += 1
    return result

def funcC(text) :
    text1 = ""
    for i in text :
        if(ord(i) >= 48 and ord(i) <= 57) :
            text1 += i
        else :
            text1 += str(ord(i))
    return text1

def funcD(text) :
    check = ["DDO","NEVE"]
    text1 = ""
    result = ""
    i = 0
    while i < len(text) : 
        if(text1 == check[0] or text1 == check[1]):        
            text1 +=  str(text[i])
            result += text1
            text1 = ""
            i += 1
        else :
            text1 += chr(int(text[i:i+2]))
            i += 2
    return result

def funcE(text) :
    check = ["DDO","NEVE"]
    text1 = ""
    result = ""
    i = 0
    while i < len(text) : 
        if(text1 == check[0] or text1 == check[1]):        
            text1 =  text1[::-1]
            text1 = text1[0].upper() + text1[1:].lower()
            text1 += text[i]
            result += text1
            text1 = ""
            i += 1
        else :
            text1 += text[i]
            i += 1
    return result

def funcF(text) :
    result =""
    for i in text :
        if(ord(i) >= 48 and ord(i) <= 57 ) :
            result += i
    return result 


target = int(input("Enter number : "))

if(target > 0) :
    A = funcA(target)
    print("Funtion A :" ,A)
    B = funcB(A)
    print("Funtion B :" ,B)
    C = funcC(B)
    print("Funtion C :" ,C)
    D = funcD(C)
    print("Funtion D :" ,D)
    E = funcE(D)
    print("Funtion E :" ,E)
    F = funcF(E)
    print("Funtion F :" ,F)
else :
    print("Invalid Input")