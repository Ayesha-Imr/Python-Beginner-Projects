#manipulating phrases

def acronym(p):
    words = p.split()
    print(words)
    data = ""
    for i in words:
        data=data + i[0].upper()
    return data
    
phrase = input("Enter phrase: ")
print(acronym(phrase))


def acronym2(p):
    words = p.split()
    print(words)
    data = ""
    for i in words:
        data=data + i[-1].upper()
    return data
    
#phrase = input("Enter phrase: ")
print(acronym2(phrase))



def acronym3(p):
    words = p.split()
    print(words)
    data = ""
    for i in words:
        prt1 = i[0:-1]
        prt2 = i[-1].upper()
        data=data + prt1 + prt2 + " "
    return data
    
#phrase = input("Enter phrase: ")
print(acronym3(phrase))



def acronym4(p):
    words = p.split()
    print(words)
    data = ""
    for i in words:
        data=data + i[:-1] + i[-1].upper() + " "
    return data
    
#phrase = input("Enter phrase: ")
print(acronym4(phrase))



def acronym5(p):
    words = p.split()
    print(words)
    data = ""
    for i in words:
        index = len(i)//2
        data=data + i[:index] + i[index].upper() + i[index + 1:] + " "
    return data
    
#phrase = input("Enter phrase: ")
print(acronym5(phrase))


def acronym6(p):
    words = p.split()
    print(words)
    data = ""
    for i in words:
        for j in i:
            data = data + j + "=" + str(ord(j)) + " "
    return data
    
#phrase = input("Enter phrase: ")
print(acronym6(phrase))
