inputfile = open("wireshark.txt", "r", encoding="utf-8")

for line in inputfile:
    #x = ("Frame ?, Src: **:**:**:**:**:**, Dst: **:**:**:**:**:**, Type: IPv4 0x0800 ")
    x = ("Frame")
    y = ("Type")
    z = ("Src:")
    a = ("Dst:")
    #e = ("Internet")

    s = line.find(x)
    t = line.find(y)
    b = line.find(z)
    c = line.find(a)
    #f = line.find(e)

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
        cols = line.split(")") and line.split(")")
        print(cols[0])       
        #print(cols[0][2])
        
    
    
    #if (c!= -1):

        #print (line)
        #cols = line.split("(")
        #print(cols[0])
        #print(cols[0][2])

    if line.find("Src:") != -1 and line.find("(") != -1 and line.find(")") != -1 :

        
        #print(line)
        cols = line.split("(") and line.split(")")
        print(cols[0])       
        #print(cols[0][2])

    #if line.find("Ethernet II") != -1 and line.find("Internet Protocol Version 4") != -1:

        #cols = line.split("")
        #print (cols[0][1])
    #if (f!= -1):
        #cols = line.split("4")
        #print(cols[1])  
        

