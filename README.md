# Steganography
Projet Python
Manipulation d'images

Stéganographie :
Contrairement à la cryptographie, qui consiste à rendre illisible une information, pour qui ne connait pas
la clé, la stéganographie consiste à cacher de l'information, dans de l'information. Par exemple, on peut
cacher un texte dans un autre, ou dans une musique... Ici, l'objectif est de cacher une image dans une
autre image (de même taille). Dans la suite, on notera les deux images Im1 et Im2.


Commencez par définir une fonction prenant en paramètres deux images I1 et I2, et qui rogne
(éventuellement) ces deux images de manière à obtenir deux images Im1 et Im2, ayant la même taille,
cette taille étant la plus grande possible.


A partir de Im1 et Im2, nous allons créer une image Im12, ayant la même taille que Im1 et Im2,
permettant de stocker (une version un peu dégradée) de chaque image.
Comme vu plus haut, Chaque image est composée de pixels, et chaque pixel est défini par un triplet
de composantes (R,G,B). Chaque composante de chaque pixel est représentée par un entier codé sur 8
bits, soit un entier compris entre 0 et 255 (en base 10) ou entre 00000000 et 11111111 (en base 2).


Les 4 bits de poids faible (en rouge) d'une composante ne sont pas les plus importants : en effet, ils
influent au maximum à hauteur de 15 sur la valeur totale de la composante (0000 en base 2 vaut 0 en
base 10, et 1111 en base 2 vaut 15 en base 10).


Pour créer Im12, l'algorithme est donc le suivant : On note Pi1= ( Ri1, Gi1, Bi1) la couleur du pixel situé en position i dans Im1, 
et Pi2 = ( Ri2, Gi2, Bi2) le pixel situé à la même position i dans Im2. La couleur du pixel Pi12 = ( Ri12, Gi12, Bi12 ) de Im12 est calculée à partir de Pi1 et Pi2
de la manière suivante : les 4 bits de poids fort de Ri12 sont égaux aux 4 bits de poids fort de Ri1, et les 4 bits de poids faible de Ri12 sont égaux aux 4 bits de poids
fort de Ri2. On procède de la même manière pour la composante verte et la composante bleue.


L'image Im12 ressemblera donc très fortement à Im1. (il est même parfois presque impossible, à l'oeil nu, de faire la différence avec Im1)
Pour obtenir Im21 (i.e. une image ressemblant très fortement à Im2 dans laquelle se cache Im1), il suffira d'inverser les 4 bits de poids fort et les 4 bits de poids faible 7
de chaque composante de chaque pixel de Im12.


• Écrivez les fonctions de manipulation de base permettant de récupérer la valeur entière
correspondant aux 4 bits de poids faible aux 4 bits de poids fort d'un entier compris entre 0 et
255. NOTE : une simple opération arithmétique en base 10 suffit.
• Écrivez à présent la fonction permettant de mixer 2 images en une seule, selon la méthode
présentée
• Écrivez la fonction permettant de révéler l'image cachée en inversant ses bits de poids faible et
ses bits de poids fort.
