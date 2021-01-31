# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 12:43:57 2021

@author: Merilia
"""

from PIL import Image
Image.MAX_IMAGE_PIXELS = None

import numpy as np

class imagestg:
     
     
     def __init__(self,pathimage1):
        self.im1 =  Image.open(pathimage1)
        
        self.w,self.h = self.im1.size   
     def resizes(self,r,s):
         self.im1 = self.im1.resize((r,s))
     def showp(self):
         self.im1.show()
     def mastermanipbase(self,i,j):
# mastermanipbase renvoie l
#la valeur en base 10 des 4 bits de poids fort pour l'image im1 
#pour chaque couleur RGB d'un pixels (i,j)
         n = np.arange(8)
         RGB08 = np.zeros((3,8))
         V = np.zeros(3)
         value = self.im1.getpixel((i,j))
         #print(value)
         for i in range(8):
             n[i]= 2**i
         for i in range(3):
             bits08 = np.zeros(8)
#RGB08[0] associé à la couleur rouge, RGB08[1] à la couleure vert
#RGB08[2] à la couleur bleu
             RGB08[i] = self._manipbase(value[i],n,bits08)
             V[i] = self._valeurforte(RGB08[i])
             
         return V
    
    
    
        
     def _manipbase(self,v,n,b08):
        for i in range(8):
            if v-n[7-i]>= 0 :
                b08[i] = 1
                v = v-n[7-i]
        return b08
    
     def _valeurforte(self,b08):
         bitsfort = np.zeros(4)
         for i in range(4):
             bitsfort[i]= b08[i]
             bitsfort[i] = (bitsfort[i])*(2**(7-i))
         Fort = sum(bitsfort)
         return Fort
#Fonction qui prends en valeur v en décimal, et qui retourne 
#b08 qui est la valeur v écrit en binaire 
                

##Fonction dans la classe stéganographie 


class conversion: 

    
    def convdecbin(self,n):
        m = np.arange(8)
        bits = np.zeros(8)
        for i in range(8):
            m[i]= 2**(7-i)
        for i in range(8):
            if n-m[i]>= 0:
                bits[i] = 1
                n = n-m[i]

        return bits
    
    def convdecbinbis(self,n):
        bits =self.convdecbin(n)
        c = np.zeros(8)
        for i in range(4):
            c[i] = bits[4+i]
            c[4+i] = bits[i]
        return c
    
    @staticmethod
    def convbindec(m):
        for i in range(8):
            m[i] = m[i]*(2**(7-i))
        s = sum(m)
        return int(s)

    
    
    
    
class steganographie:
    
    def __init__(self,pathimage1, pathimage2):
        self.im1 = imagestg(pathimage1)
        self.im2 = imagestg(pathimage2)
        print(type(self.im1))
        
    
    def rogne(self):
        image1 = self.im1
        print(type((self.im1)))
        
        w,h = (self.im1).w,self.im1.h
        p,q = (self.im2).w,self.im2.h
        a = p*q
        b = w*h
        
        if a < b :
            self.im2.resizes(w,h)
            image12 = Image.new('RGB',(w,h))
        else :
            self.im1.resizes(p,q)
            image12 = Image.new('RGB',(p,q))
        return image12

    
    def stegano(self):
        im12 = self.rogne()
        
        
        w,h = im12.size
        c = conversion()

        for i in range(w):
            for j in range(h):
                RGB08 = np.zeros((3,8))
                RGB = np.zeros(3)
                a = self.im1.mastermanipbase(i,j)
                b = self.im2.mastermanipbase(i,j)
                
                
                for k in range(3):
                    print(a[k])
                    RGB08[k] = c.convdecbin(a[k])+c.convdecbinbis(b[k])
                    RGB[k] = c.convbindec(RGB08[k])
                im12.putpixel((i,j),(int(RGB[0]),int(RGB[1]),int(RGB[2])))
        return im12
    
    
    

a = steganographie(r'C:/Users/Merilia/Desktop/PythonMonet/Claude_Monet512px.jpg',r'C:/Users/Merilia/Desktop/PythonMonet/512px-Pacioli.jpg')
#im1 = imagestg(r'C:/Users/Merilia/Desktop/PythonMonet/Claude_Monet512px.jpg')
#im2 = imagestg(r'C:/Users/Merilia/Desktop/PythonMonet/512px-Pacioli.jpg')
#im1.resizes(100,100)
#im1.showp()
a.stegano().show()
#a.rogne()
