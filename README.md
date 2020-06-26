You will be creating a Python program saved in a file named "extractFrame.py". The Python program will read text from a file named "wireShark.txt" and display the frames with essential frame data. For each frame, you need to extract and present its frame number, the source and destination addresses, as well as the frame type. The frame number always appears after "Frame" at the beginning of each frame in the document. For either source or destination address, it is composed of 12 hexadecimal digits, every two of which are separated by colon. The address examples could be like below:

00:14:ee:08:dd:b1
01:00:5e:7f:ff:fa

The frame type is a hexadecimal value that is used to indicate the type of upper-level protocol in the data fields. A common value is 0x800 that describes the IPv4 protocol.

For example, the first frame in the given "wireShark.txt" file is presented below. Note that here I highlight the data fields that you need to extract from each frame in the document.

Frame 1: 372 bytes on wire (2976 bits), 372 bytes captured (2976 bits) on interface 0
Ethernet II, Src: WesternD_08:dd:b1 (00:14:ee:08:dd:b1), Dst: IPv4mcast_7f:ff:fa (01:00:5e:7f:ff:fa)
    Destination: IPv4mcast_7f:ff:fa (01:00:5e:7f:ff:fa)
        Address: IPv4mcast_7f:ff:fa (01:00:5e:7f:ff:fa)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...1 .... .... .... .... = IG bit: Group address (multicast/broadcast)
    Source: WesternD_08:dd:b1 (00:14:ee:08:dd:b1)
        Address: WesternD_08:dd:b1 (00:14:ee:08:dd:b1)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Type: IPv4 (0x0800)
Internet Protocol Version 4, Src: 192.168.1.180, Dst: 239.255.255.250
    0100 .... = Version: 4
    .... 0101 = Header Length: 20 bytes (5)
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)
    Total Length: 358
    Identification: 0xfe2a (65066)
    Flags: 0x4000, Don't fragment
    Time to live: 4
    Protocol: UDP (17)
    Header checksum: 0xc505 [validation disabled]
    [Header checksum status: Unverified]
    Source: 192.168.1.180
    Destination: 239.255.255.250
User Datagram Protocol, Src Port: 35064, Dst Port: 1900
Simple Service Discovery Protocol

No.     Time           Source                Destination           Protocol Length Info
      2 0.307821       192.168.1.180         239.255.255.250       SSDP     422    NOTIFY * HTTP/1.1 

After analyzing the frames in the text file, your program should display all frames with the essential data. Below is the result that should be displayed by running your program based on the given text file:

Frame 1, Src:00:14:ee:08:dd:b1, Des:01:00:5e:7f:ff:fa, Type:0x0800
Frame 2, Src:00:14:ee:08:dd:b1, Des:01:00:5e:7f:ff:fa, Type:0x0800
Frame 3, Src:cc:2f:71:3e:ca:a1, Des:14:91:82:36:7a:8d, Type:0x0800
Frame 4, Src:cc:2f:71:3e:ca:a1, Des:14:91:82:36:7a:8d, Type:0x0800
Frame 5, Src:cc:2f:71:3e:ca:a1, Des:14:91:82:36:7a:8d, Type:0x0800
Frame 6, Src:14:91:82:36:7a:8d, Des:cc:2f:71:3e:ca:a1, Type:0x0800
Frame 7, Src:14:91:82:36:7a:8d, Des:cc:2f:71:3e:ca:a1, Type:0x0800

Note that if there are more frames given in the input file "wireShark.txt", your Python program should be able to extract all the frames with the expected presentation. (That is, you cannot hard code the output based on the given file! When I test your code at my side, I might use a different input file that has more than the frames provided to you.)

Hints and Notes
To approach the problems, you may need to use certain methods and functions to analyze and manipulate the lines in the given text file. For example, you may need to find if a substring, such as "Frame" or "Type:", appears on a line. You may also need to split a line into multiple parts, or slice a string in order to get a substring of it.

Below I provide some Python code examples to provide you clues on which methods/functions you could use and how to use them.

#How to check if a substring is on a line? Hint: use the find method
seedStr = "Internet Protocol Version 4"
a_str = "Internet Protocol Version 4, Src: 192.168.1.180, Dst: 239.255.255.250"
x = a_str.find(seedStr)
print(x)
#should print 0

x_str ="(I am Li Xu)"
x = x_str.find(seedStr)
print(x)
#should print -1

#How to extract a substring from a line? Hint: slice the string!
x = x_str[1:len(x_str)-1]
print(x)
#should print "I am Li Xu"

#How to split a line into several parts? Hint: use split method!
a_str = "Internet Protocol Version 4, Src: 192.168.1.180, Dst: 239.255.255.250"
a_parts = a_str.split(", ")
print(a_parts)
#should print ['Internet Protocol Version 4', 'Src: 192.168.1.180', 'Dst: 239.255.255.250']

x = a_parts[0]
words = x.split() #default split token is white space
print(words)
#should print ['Internet', 'Protocol', 'Version', '4']
0
-1
I am Li Xu
['Internet Protocol Version 4', 'Src: 192.168.1.180', 'Dst: 239.255.255.250']
['Internet', 'Protocol', 'Version', '4']
