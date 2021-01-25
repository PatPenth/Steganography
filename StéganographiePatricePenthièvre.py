# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 10:26:38 2020

@author: Merilia
"""

"""
Created on Sat Oct 31 20:23:40 2020

@author: Merilia
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 15:43:02 2020

@author: Merilia
"""
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

import numpy as np



image1 = Image.open(r'C:/Users/Merilia/Desktop/PythonMonet/Claude_Monet512px.jpg')
image2 = Image.open(r'C:/Users/Merilia/Desktop/PythonMonet/512px-Pacioli.jpg')


#EX3 STEGANOGRAPHIE


def rogne(im1,im2):
    w,h = im1.size
    p,q = im2.size
    a = p*q
    b = w*h
    if a < b :
        im2 = im2.resize((w,h))
        im12 = Image.new('RGB',(w,h))
    else :
        im1 = im1.resize((p,q))
        im12 = Image.new('RGB',(p,q))
    return im12, im1 , im2


#Manipbasebis(im,i,j) renvoie pour un pixel donné d'une image im, la valeurs
#en base 10 des 4 bits de poids fort associé aux couleurs rouges vert et bleu 

def manipbasebis(im,i,j):
    bits08r = np.zeros(8)
    bits08g = np.zeros(8)
    bits08b = np.zeros(8)
    b = im.getpixel((i,j))
    br = b[0]
    bg = b[1]
    bb = b[2]
    n = np.arange(8)
    for i in range(8):
        n[i]= 2**i
    for i in range(8):
        if br-n[7-i]>= 0 :
            bits08r[i] = 1
            br = br-n[7-i]
#br valeur en décimal du pixels (i,j) pour la couleur rouge 
#On vérifie si br est supérieur ou égale à 2 puissance 7-i
#Si oui alors bits08r[i] vaut 1 et br est vaut le reste de la division euclidienne
#par 2 puissance 7-i
#On a bits08r[0] correspond à 2 puissance 7 
       
    for i in range(8):
        if bg-n[7-i]>= 0 :
            bits08g[i] = 1
            bg = bg-n[7-i]
           
    for i in range(8):
        if bb-n[7-i]>= 0 :
            bits08b[i] = 1
            bb = bb-n[7-i]
           
    bitsfortr = np.zeros(4) 
    bitsfortg = np.zeros(4)
    bitsfortb = np.zeros(4)
    bitsfaibler = np.zeros(4)
    bitsfaibleg = np.zeros(4)
    bitsfaibleb = np.zeros(4)
    for i in range(4):
        bitsfortr[i] = bits08r[i]
#bitsfortr bits de poids fort pour la couleur rouge, ces bits correspondent
#à 2 puissance 7 jusqu'à 2 puissance 4
#bitsfortr[0] contient l'élément correspondant à 2 puissance 7
#bitsfortr[3] contient l'élément correspondant à 2 puissance 4
    for i in range(4):
        bitsfortg[i] = bits08g[i]
    for i in range(4):
        bitsfortb[i] = bits08b[i]
    
    for i in range(4):
        bitsfortr[i] = (bitsfortr[i])*(2**(7-i))

    for i in range(4):
        bitsfortg[i] = (bitsfortg[i])*(2**(7-i))
    for i in range(4):
        bitsfortb[i] = (bitsfortb[i])*(2**(7-i))
    
#Somme des puissances de deux allant de 16 à 128 multiplié chaqu'une par un poids qui vaut 0 ou 1        
    Sfortr = sum (bitsfortr) 
    
    
    Sfortg = sum (bitsfortg)
    Sfortb = sum (bitsfortb)

    return Sfortr, Sfortg, Sfortb


def convdecbin(n):
    m = np.arange(8)
    bits = np.zeros(8)
    for i in range(8):
        m[i]= 2**(7-i)
    for i in range(8):
        if n-m[i]>= 0:
            bits[i] = 1
            n = n-m[i]

    return bits

#Convdecbin convertit une écriture décimal en binaire

def convbindec(m):
    for i in range(8):
        m[i] = m[i]*(2**(7-i))
    s = sum(m)
    return int(s)

#Convbindec permet de convertir une écriture binaire en décimal

def stegano(im1,im2):
    im12 = rogne(im1,im2)[0]
    im2 = rogne(im1,im2)[2]
    im1 = rogne(im1,im2)[1]
    w,h = im12.size
    for i in range(w):
        for j in range(h):
            a = manipbasebis(im1,i,j)
            b = manipbasebis(im2,i,j)
# La valeur en base 10 des 4 bits de poids fort pour l'image im1 pour la couleur rouge 
# est convertit en binaire : fortr12 = convdecbin(a[0]) 
#De même pour les couleurs  vert et bleu. 
#On a pour 3<i<8 fortr12[i] = 0, fortg12[i] = 0, fortb12[i]=0
#Les bits de poids fort de l'image im1 deviennent les bits de poids
#fort de l'image im12
          
            fortr12 = convdecbin(a[0])
            fortg12 = convdecbin(a[1])
            fortb12 = convdecbin(a[2])
# La valeur en base 10 des 4 bits de poids fort pour l'image im2 pour la couleur rouge 
# est convertit en binaire : faibler12 = convdecbin(b[0]) 
#De même pour les couleurs  vert et bleu. 
#On a pour 0<i<4 faibler12[i] = 0, faibleg12[i] = 0, faibleb12[i]=0
#Les bits de poids fort de l'image im2 deviennent les bits de poids
#faible de l'image im12           
            
            faibler12 = convdecbinbis(b[0])
            faibleg12 = convdecbinbis(b[1])
            faibleb12 = convdecbinbis(b[2])
#On réalise la somme sans problème car le fortr12 est toujours 
#égale à 0 pour fortr12[i] avec 3 < i< 8
#Tandis que faibler12 est toujours égale à 0 pour faibler12[i]
#avec 0=< i < 4              
#De même pour les autres couleurs 
            
            r12 =  fortr12+faibler12
            g12 = fortg12+faibleg12
            b12 = fortb12+faibleb12
            R12 = convbindec(r12)
            G12 = convbindec(g12)
            B12 = convbindec(b12)
            im12.putpixel((i,j),(R12,G12,B12))
    return im12
def convdecbinbis(n):
    m = np.arange(8)
    bits = np.zeros(8)
    c = np.zeros(8)
    for i in range(8):
        m[i]= 2**(7-i)
    for i in range(8):
        if n-m[i]>=0:
            bits[i] = 1
            n = n - m[i]
#bits[0] correspond à 2 puissance 0 
#bits[7] corresponf à 2 puissance 7
    for i in range(4):
        c[i] = bits[4+i]
        c[4+i] = bits[i]
        
    #Permutation des bits, les bits plus faibles deviennent les plus forts
    #et les bits plus forts deviennent les plus faibles
    return c


def steganoreveler(im1,im2):
    im21 = rogne(im1,im2)[0]
    im1 = rogne(im1,im2)[1]
    im2 = rogne(im1,im2)[2]
    w,h = im21.size
    for i in range(w):
        for j in range(h):
#Manipbasebis(im,i,j) renvoie pour un pixel donné d'une image im, la valeurs
#en base 10 des 4 bits de poids fort 
# dans un tableau, les 3 premiers éléments sont les 4 bits de poids fort
# rouge vert puis bleu 
            a = manipbasebis(im1,i,j)
            b = manipbasebis(im2,i,j)
# a[0] contient la somme des 4 bits de poids fort en base 10 pour la 
#couleur rouge de même a[1] cette somme pour la couleur vert et a[2]
#pour la couleur bleu
#convdecbinbis(a[0]) convertit a[0] en nombre binaire, puis 
#permutte les bits de poids fort, on a :
#pour tout i, tel que i>=0 , i< 4:
# faibler12[i] = 0,  faibleg12[i]=0, faibleb12[i]=0
# On permutte les bit de poids fort de l'image 1 pour qu'il deviennent
#les bits de poids faible de l'image 21
            faibler12 = convdecbinbis(a[0]) 
            faibleg12 = convdecbinbis(a[1])
            faibleb12 = convdecbinbis(a[2])
# b[0] contient la somme des 4 bits de poids fort en base 10 pour la 
#couleur rouge de même b[1] cette somme pour la couleur vert et b[2]
#pour la couleur bleu
#convdecbin (b[0]) convertit b[0] en nombre binaire
#et pour tout i> 3 on a
#fortr12[i] = 0, fortg12[i] = 0, fortb12[i]=0
#Les bits de poids fort de l'image 2 deviennent les bits de poids 
#fort de l'image 21              
            
            fortr12 = convdecbin(b[0])
            fortg12 = convdecbin(b[1])
            fortb12 = convdecbin(b[2])
            #On utilise convdecbinbis pour permuter les 4 bits
            #de poids forts avec les 4 bits de poids faible pour chaque
            #pixels

            r12 = fortr12+faibler12 
#On réalise la somme sans problème car le fortr12 est toujours 
#égale à 0 pour fortr12[i] avec 3 < i< 8
#Tandis que faibler12 est toujours égale à 0 pour faibler12[i]
#avec 0=< i < 4
#De même pour les autres couleur 
 
          
     
            g12 = fortg12+faibleg12
            b12 = fortb12+faibleb12
            R12 = convbindec(r12)
            G12 = convbindec(g12)
            B12 = convbindec(b12)
            im21.putpixel((i,j),(R12,G12,B12))
    return im21


stegano(image1,image2).show()


steganoreveler(image1,image2).show()