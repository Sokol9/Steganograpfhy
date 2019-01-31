from PIL import Image as img

def zakoduj(nazov,text):
    obr=img.open(nazov)
    obr=obr.resize((800,800*obr.height//obr.width))
    A=[]
    for i in text:
        x=ord(i) 
        v=""
        while x>0:
            v=str(x%2)+v        
            x=x//2
        if len(v)<9:
            v="0"*(8-len(v))+v
        A.append(v)
    
    p=0
    for i in A:
        for t in i:
            x=obr.getpixel((p%800,p//800))
            y=x[2]
            v=""
            while y>0:
                v=str(y%2)+v        
                y=y//2
            v = str(int(v)//10*10+int(t))            
            l=len(v)
            y=0
            for i in v:
                l=l-1
                y=y+int(i)*2**l                 
            x=x[0:2]+(y,)
            obr.putpixel((p%800,p//800),x)
            p=p+1
    obr.save("z"+nazov[0:len(nazov)-4]+".png")

def rozkoduj(nazov):
    obr1=img.open(nazov)
    width=obr1.width
    p=0    
    a=0
    Vys=""
    while a==0:
        V=""
        while not len(V)==8:
            x=obr1.getpixel((p%width,p//width))
            V=V+str(x[2]%2)
            p=p+1 
        l=len(V)
        x=0
        for i in V:
            l=l-1
            x=x+int(i)*2**l
        if chr(x)=="}":
            a=1  
        else:
            Vys=Vys+chr(x)
                    
       
    print(Vys)       