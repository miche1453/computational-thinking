inputfile = open("wireshark.txt", "r", encoding="utf-8")

import re

contents = inputfile.read()

#Check for Frame Number, Source, Destination, and Frame Type.


x = re.findall("0x0800", contents)
y = re.findall("Frame", contents)

if y:
  print (y)
if x:
  print (x)
else:
  pass

