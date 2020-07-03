inputfile = open("wireshark.txt", "r", encoding="utf-8")

for line in inputfile:
    #x = ("Frame ?, Src: **:**:**:**:**:**, Dst: **:**:**:**:**:**, Type: IPv4 0x0800 ")
    x = ("Frame")
    y = ("Type")
    z = ("Src:")
    a = ("Dst:")

    s = line.find(x)
    t = line.find(y)
    b = line.find(z)
    c = line.find(a)

    #seedStr = "Type, Src:, Dst:"
    #a_str = "Type, Src:, Dst: "
    #x = a_str.find(seedStr)
    #print(x)
    

    #x_str ="("
    #x = x_str.find(seedStr)
    #print(x)
    

    
    #x = x_str[1:len(x_str)-1]
    #print(x)
   

    #a_str = ("(")
    #a_parts = a_str.split("(")
    #print(a_parts)
    

    #x = a_parts[0]
    #words = x.split("(-)") 
    #print(words)
    

    
    if (s!= -1):
        #print(line)
        cols = line.split(":")
        print(cols[0])         
        #print(cols[0][6:])   
    if (t!= -1):
        
        #print(line)
        cols = line.split("(") 
        print(cols[0])       
        #print(cols[2][3]) 

    if  (b!= -1) and line.find("Src"):
        
        #print(line)
        cols = line.split("(")
        #print(cols[0])       
        print(cols[0][1])
    
    if (c!= -1):

        #print (line)
        cols = line.split("(")
        print(cols[0])
        #print(cols[2][3])
