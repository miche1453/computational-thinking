inputfile = open("wireshark.txt", "r", encoding="utf-8")

for line in inputfile:
    #x = ("Frame ?, Src: **:**:**:**:**:**, Dst: **:**:**:**:**:**, Type: IPv4 0x0800 ")
    x = ("Frame")
    #y = ("IPv4")
    #z = ("Src:")
    #a = ("Dst:")

    s = line.find(x)
    #t = line.find(y)
    #b = line.find(z)
    #c = line.find(a)
    
    if (s!= -1):
        print(line)
        cols = line.split("Frame") #Think: What does this line do?
        print(cols[0])   #Think: Why 0 is used here? Probably because I only interested in this piece?        
        print(cols[0][6:])   #Think: Why 6 is used here?  This is a slicing method used to slice a substring

