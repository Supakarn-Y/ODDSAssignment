
def A(number) :
    text1 = str(number)
    text = ""
    for i in text1 :
        if( int(i) % 2 == 0 ) :
            text += "Even" + i
        else :
            text += "Odd" + i
    return text


def B(text) :
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

def C(text) :
    text2 = ""
    for i in text :
        if(ord(i) >= 48 and ord(i) <= 57) :
            text2 += i
        else :
            text2 += str(ord(i))
    return text2

def D(text) :
    check = ["DDO","NEVE"]
    text2 = ""
    rslt = ""
    i = 0
    while i < len(text) : 
        if(text2 == check[0] or text2 == check[1]):        
            text2 +=  str(text[i])
            rslt += text2
            text2 = ""
            i += 1
        else :
            text2 += chr(int(text[i:i+2]))
            i += 2
    return rslt

def E(text) :
    check = ["DDO","NEVE"]
    text2 = ""
    rslt = ""
    i = 0
    while i < len(text) : 
        if(text2 == check[0] or text2 == check[1]):        
            text2 =  text2[::-1]
            text2 = text2[0].upper() + text2[1:].lower()
            text2 += text[i]
            rslt += text2
            text2 = ""
            i += 1
        else :
            text2 += text[i]
            i += 1

    return rslt

def F(text) :
    rslt =""
    for i in text :
        if(ord(i) >= 48 and ord(i) <= 57 ) :
            rslt += i
    return rslt 


target = int(input("Enter number : "))
print("Input is" ,target)
A = A(target)
print("Funtion A :" ,A)
B = B(A)
print("Funtion B :" ,B)
C = C(B)
print("Funtion C :" ,C)
D = D(C)
print("Funtion D :" ,D)
E = E(D)
print("Funtion E :" ,E)
F = F(E)
print("Funtion F :" ,F)