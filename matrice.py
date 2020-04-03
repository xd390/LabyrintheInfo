# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module matrice
   ~~~~~~~~~~~~~~~

   Ce module gère une matrice.
"""

#-----------------------------------------
# contructeur et accesseurs
#-----------------------------------------

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):             #marche
    """
    crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant
    valeurParDefaut dans chacune des cases
    paramètres:
      nbLignes un entier strictement positif qui indique le nombre de lignes
      nbColonnes un entier strictement positif qui indique le nombre de colonnes
      valeurParDefaut la valeur par défaut
    résultat la matrice ayant les bonnes propriétés
    """
    M1=[]
    for e in range(nbLignes):
        M1.append([valeurParDefaut]*nbColonnes)
    return M1
    pass

matrice=Matrice(7,7)
#print(matrice)


def getNbLignes(matrice):                                       #marche
    """
    retourne le nombre de lignes de la matrice
    paramètre: matrice la matrice considérée
    """
    return len(matrice)


#print(getNbLignes(matrice))

def getNbColonnes(matrice):                                     #marche
    """
    retourne le nombre de colonnes de la matrice
    paramètre: matrice la matrice considérée
    """
    res=0
    for i in matrice[0]:
        res+=1
    return res
    pass

#print(getNbColonnes(matrice))

def getVal(matrice,ligne,colonne):                              #marche
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """
    return matrice[ligne][colonne]
    pass

#print(getVal(matrice,4,4))

def setVal(matrice,ligne,colonne,valeur):                       #marche
    """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                valeur la valeur à stocker dans la matrice
    cette fonction ne retourne rien mais modifie la matrice
    """
    matrice[ligne][colonne]=valeur
    pass

#setVal(matrice,4,4,4)
#print(matrice)

#------------------------------------------
# decalages
#------------------------------------------
def decalageLigneAGauche(matrice, numLig, nouvelleValeur=0):        #marche
    """
    permet de décaler une ligne vers la gauche en insérant une nouvelle
    valeur pour remplacer la premiere case à droite de cette ligne
    le fonction retourne la valeur qui a été éjectée
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat la valeur qui a été ejectée lors du décalage
    """
    res=matrice[numLig][0]
    matrice[numLig].pop(0)
    matrice[numLig].append(nouvelleValeur)
    return res


#print(decalageLigneAGauche(matrice,4,5))
#print(matrice)


def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):            #marche
    """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    aux=[nouvelleValeur]
    res=matrice[numLig][-1]
    matrice[numLig].pop(-1)
    aux.extend(matrice[numLig])
    matrice[numLig]=aux
    return res


#print(decalageLigneADroite(matrice,4,5))
#print(matrice)


def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):       #marche
    """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    res=matrice[0][numCol]
    aux=0
    for i in range(len(matrice)-1):
        matrice[i].pop(numCol)
        aux=matrice[i+1][numCol]
        matrice[i].insert(numCol, aux)
    matrice[-1][numCol]=nouvelleValeur
    return res

#decalageColonneEnHaut(matrice,4,6)
#print(matrice)

def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):            #marche
    """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    res=matrice[-1][numCol]
    aux=0
    for i in range(-1, -len(matrice),-1):
        matrice[i].pop(numCol)
        aux=matrice[i-1][numCol]
        matrice[i].insert(numCol, aux)
    matrice[0][numCol]=nouvelleValeur
    return res

#decalageColonneEnBas(matrice,4,7)
#print(matrice)


if __name__=="__main__":
    print(Matrice(7,7))
    print(getNbLignes(matrice))
    print(getNbColonnes(matrice))
    print(getVal(matrice,4,4))
    setVal(matrice,4,4,4)
    print(matrice)
    print(decalageLigneAGauche(matrice,4,5))
    print(matrice)
    print(decalageLigneADroite(matrice,4,5))
    print(matrice)
    decalageColonneEnHaut(matrice,4,6)
    print(matrice)
    decalageColonneEnBas(matrice,4,7)
    print(matrice)
