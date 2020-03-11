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

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
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
	aux=[]
	for i in range(nbColonnes):
		aux.append(valeurParDefaut)
	for e in range(nbLignes):
		M1.append(aux)
    return M1
    pass



def getNbLignes(matrice):
    """
    retourne le nombre de lignes de la matrice
    paramètre: matrice la matrice considérée
    """
    res=0
    for i in matrice:
        res+=1
    return res
    pass

def getNbColonnes(matrice):
    """
    retourne le nombre de colonnes de la matrice
    paramètre: matrice la matrice considérée
    """
    res=0
    for i in matrice[0]:
        res+=1
    return res
    pass

def getVal(matrice,ligne,colonne):
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """
    return matrice[ligne][colonne]
    pass

def setVal(matrice,ligne,colonne,valeur):
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


#------------------------------------------
# decalages
#------------------------------------------
def decalageLigneAGauche(matrice, numLig, nouvelleValeur=0):
    """
    permet de décaler une ligne vers la gauche en insérant une nouvelle
    valeur pour remplacer la premiere case à droite de cette ligne
    le fonction retourne la valeur qui a été éjectée
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat la valeur qui a été ejectée lors du décalage
    """
    res=matrice[numLig[-1]]
    matrice.pop([numlig[-1]])
    matrice.insert([numlig[nouvelleValeur]])
    return res
    pass

def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):
    """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    res=matrice[numLig[0]]
    matrice.pop([numlig[0]])
    matrice.insert([numlig[nouvelleValeur]])
    return res
    pass

def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    res=matrice[0][numCol]
    cpt=0
    for ligne in matrice:
        cpt+=1
        if cpt!=len(matrice):
            ligne.pop(ligne[numCol])
            ligne.insert(ligne[numCol], ligne+1[numCol])
    matrice[-1][numCol]=nouvelleValeur
    return res
    pass

def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    res=matrice[-1][numCol]
    cpt=0
    for ligne in matrice:
        cpt+=1
        if cpt!=1:
            ligne.pop(ligne[numCol])
            ligne.insert(ligne[numCol], ligne-1[numCol])
    matrice[0][numCol]=nouvelleValeur
    return res
    pass
