import os
import random
f = open("places365_val.txt","r")
img = []
for line in f:
    img.append(line)
random.shuffle(img)
f2 = open("trainvalidation_static_view.flist","w")
for i in img:
    f2.write(i)
    #f2.write(i[1:])