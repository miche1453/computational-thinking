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
        cols = line.split("Frame") 
        print(cols[0])       
        print(cols[0][6:])   

