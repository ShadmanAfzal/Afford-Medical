def compress(string):
    res = ""
    count = 1
    res += string[0]
    for i in range(len(string)-1):
        if(string[i] == string[i+1]):
            count+=1
        else:
            if(count > 1):
                res += str(count)
            res += string[i+1]
            count = 1
    if(count > 1):
        res += str(count)
    return res
    
def decompress(string):
    res=""
    i=0
    while i<len(string)-1:
        if string[i+1].isnumeric():
            next_num = int(string[i+1])
            res+=string[i]*next_num
            i+=2
        else:
            res+=string[i]
            i+=1
    return res

if __name__=="__main__":
    while True:
        print("<< Press 1. to compress string\n<< Press 2. to decompress string\n<< Press 3. to exit\n")
        choice = int(input(">> "))
        if choice == 1:
            print("<< Enter string to compress")
            string = input(">> ")
            res = compress(string)
            print(f"Compressed string {res}\n")
        elif choice == 2:
            print("<< Enter string to decompress\n")
            string = input(">> ")
            res = decompress(string)
            print(f"Decompressed string {res}\n")
        else:
            break
