bi = []
vi = input("fala garoto:")
vi = int(vi)

if (vi==0 or vi==1):
    bi=[0]*6
    bi.append(vi)
    
else:
    if (64<=vi):
        vi =(vi-64)
        bi.append(1)
    else:
        bi.append(0)
        
    if (32<=vi):
        vi =(vi-32)
        bi.append(1)
    else:
        bi.append(0)
    
    if (16<=vi):
        vi =(vi-16)
        bi.append(1)
    else:
        bi.append(0)
    if (8<=vi):
        vi =(vi-8)
        bi.append(1)
    else:
        bi.append(0)
    if (4<=vi):
        vi =(vi-4)
        bi.append(1)
    else:
        bi.append(0)
    if (2<=vi):
        vi =(vi-2)
        bi.append(1)
    else:
        bi.append(0)
    if (1<=vi):
        vi =(vi-1)
        bi.append(1)
    else:
        bi.append(0)
        
print (bi)