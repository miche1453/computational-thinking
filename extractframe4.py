inputfile = open("wireshark.txt", "r", encoding="utf-8")

for line in inputfile:
    #x = ("Frame ?, Src: **:**:**:**:**:**, Dst: **:**:**:**:**:**, Type: IPv4 0x0800 ")
    x = ("Frame")
    y = ("IPv4")
    z = ("Src:")
    a = ("Dst:")

    s = line.find(x)
    t = line.find(y)
    b = line.find(z)
    c = line.find(a)

    seedStr = "IPv4"
    a_str = "IPv4, Src: , Dst: "
    x = a_str.find(seedStr)
    print(x)
    #should print 0

    x_str ="()"
    x = x_str.find(seedStr)
    print(x)
    #should print -1

    #How to extract a substring from a line? Hint: slice the string!
    x = x_str[1:len(x_str)-1]
    print(x)
    #should print "I am Li Xu"

    a_str = "Internet Protocol Version 4, Src: 192.168.1.180, Dst: 239.255.255.250"
    a_parts = a_str.split(", ")
    print(a_parts)
    #should print ['Internet Protocol Version 4', 'Src: 192.168.1.180', 'Dst: 239.255.255.250']

    x = a_parts[0]
    words = x.split() #default split token is white space
    print(words)
    #should print ['Internet', 'Protocol', 'Version', '4']

    
    if (s!= -1):
        print(line)
        cols = line.split("Frame") #Think: What does this line do?
        print(cols[0])   #Think: Why 0 is used here? Probably because I only interested in this piece?        
        print(cols[0][6:])   #Think: Why 6 is used here?  This is a slicing method used to slice a substring
    if (t!= -1):
        
        print(line)
        cols = line.split("IPv4") 
        print(cols[0])       
        print(cols[0][1]) 

    if (b!= -1):
        
        print(line)
        cols = line.split("Src")
        print(cols[0])       
        print(cols[0][1])
    
    if (c!= -1):

        print (line)
        cols = line.split("Dst")
        print(cols[0])
        print(cols[0][1])
