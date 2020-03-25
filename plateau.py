# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module plateau
   ~~~~~~~~~~~~~~

   Ce module gère le plateau de jeu.
"""
import math
from matrice import *
from carte import *

def Plateau(nbJoueurs, nbTresors):
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
    resultat: un couple contenant
              - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              - la carte amovible qui n'a pas été placée sur le plateau
    """
    matrice=Matrice(7,7,0)
    setVal(matrice,0,0,Carte(True,False,False,True,0,[1]))
    setVal(matrice,0,2,Carte(True,False,False,False))
    setVal(matrice,0,4,Carte(True,False,False,False))
    if nbJoueurs>1:
      setVal(matrice,0,6,Carte(True,True,False,False,0,[2]))
    else:
      setVal(matrice,0,6,Carte(True,True,False,False))
    setVal(matrice,2,0,Carte(False,False,False,True))
    setVal(matrice,2,2,Carte(False,False,False,True))
    setVal(matrice,2,4,Carte(True,False,False,False))
    setVal(matrice,2,6,Carte(False,True,False,False))
    setVal(matrice,4,0,Carte(False,False,False,True))
    setVal(matrice,4,2,Carte(False,False,True,False))
    setVal(matrice,4,4,Carte(False,True,False,False))
    setVal(matrice,4,6,Carte(False,True,False,False))
    if nbJoueurs>2:
      setVal(matrice,6,0,Carte(False,False,True,True,0,[3]))
    else:
      setVal(matrice,6,0,Carte(False,False,True,True))
    setVal(matrice,6,2,Carte(False,False,True,False))
    setVal(matrice,6,4,Carte(False,False,True,False))
    if nbJoueurs>3:
      setVal(matrice,6,6,Carte(False,True,True,False,0,[4]))
    else:
      setVal(matrice,6,6,Carte(False,True,True,False))
    listedecarte=(creerCartesAmovibles(1,nbTresors))
    if nbTresors>34:
      listedestresors=list(range(35,nbTresors+1))
      random.shuffle(listedestresors)
      for x in matrice:
        cpt=0
        while cpt<len(x) and cpt<len(listedestresors):
          if x[cpt]!=0:
            x[cpt]["tresor"]=listedestresors[0]
            listedestresors.pop(0)
          cpt+=1
    for x in matrice:
      cpt=0
      while cpt<len(x):
        if x[cpt]==0:
          x[cpt]=listedecarte[0]
          listedecarte.pop(0)
        cpt+=1
    return matrice,listedecarte
    



def creerCartesAmovibles(tresorDebut,nbTresors):
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
    aléatoirement nbTresor trésors
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    paramètres: tresorDebut: le numéro du premier trésor à créer
                nbTresors: le nombre total de trésor à créer
    résultat: la liste mélangée aléatoirement des cartes amovibles crée
    """
    listedecarte=[]
    i=0
    while i<34:
      if i<16:
        listedecarte.append(Carte(True,False,False,True))
      elif 16<i<22:
        listedecarte.append(Carte(True,False,False,False))
      else:
        listedecarte.append(Carte(False,True,True,False))
      i+=1
    i=0
    listedestresors=list(range(tresorDebut,nbTresors+1))
    cpt=0
    for x in listedecarte:
      if cpt>=len(listedestresors):
        break
      x["tresor"]=listedestresors[cpt]
      cpt+=1
    random.shuffle(listedecarte)
    return listedecarte



def prendreTresorPlateau(plateau,lig,col,numTresor):
    """
    prend le tresor numTresor qui se trouve sur la carte en lin,col du plateau
    retourne True si l'opération s'est bien passée (le trésor était vraiment sur
    la carte
    paramètres: plateau: le plateau considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    resultat: un booléen indiquant si le trésor était bien sur la carte considérée
    """
    if numTresor==plateau[0][lig][col]["tresor"]:
	    return True
    return False



def getCoordonneesTresor(plateau,numTresor):
    """
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """
    for i_l,l in enumerate(plateau[0]):
      for i_c,c in enumerate(l):
        if numTresor==c["tresor"]:
          return i_l ,i_c
    return None




def getCoordonneesJoueur(plateau,numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
    for i_l,l in enumerate(plateau[0]):
      for i_c,c in enumerate(l):
        if numJoueur==c["pions"]:
          return i_l ,i_c
    return None



def prendrePionPlateau(plateau,lin,col,numJoueur):
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    prendrePion(plateau[0][lin][col],numJoueur)



def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    poserPion(plateau[0][lin][col], numJoueur)
    pass



def accessible(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: un booléen indiquant s'il existe un chemin entre la case de départ
              et la case d'arrivée
    """
"""    c=0
    l=0
    ligC=ligD
    colC=colD
    matricelc=[]
    listedecasesaccessiblesaunord=[[ligD,colD]]
    listedecasesaccessiblesausud=[[ligD,colD]]
    listedecasesaccessiblesalouest=[[ligD,colD]]
    listedecasesaccessiblesalest=[[ligD,colD]]
    arrivee=[ligA,colA]
    Trouve=False
    impossible=False
"""    """for ligne in plateau[0]:
        for colonne in l:
            matricelc.extend([l,c])
            c+=1
        l+=1
    while not Trouve or not impossible:
        if passageNord(plateau)""" """ """
"""    if  ligD==0 or not passageNord(matrice[ligC][colC],matrice[(ligC-1)][colC]):
        impossible=True
    elif ligD!=0 and passageNord(matrice[ligC][colC],matrice[(ligC-1)][colC]):
        listedecasesaccessiblesaunord.extend([(ligD-1),colD])
        ligC=ligC-1
    if arrivee in listedecasesaccessiblesaunord:
        trouve=True""""""
    listedecasesvalides=[[ligD,colD]]
    if  ligC==0 or not passageNord(matrice[ligC][colC],matrice[(ligC-1)][colC]):
        impossible=True
    while not Trouve or not impossible:
    if  ligC==0 or not passageNord(matrice[ligC][colC],matrice[(ligC-1)][colC]):
        impossible=True
        if passageEst(plateau[0][listedecasesvalides[-1][0]][plateau[0][listedecasesvalides[-1][-1]],plateau[0]([listedecasesvalides[-1][0]][plateau[0][listedecasesvalides[-1][-1]]+1)):
            if [ligC,colC] not in listedecasesvalides:
                listedecasesvalides.extend([ligC,colC])
"""




def accessibleDist(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du plateau
    mais la valeur de retour est None s'il n'y a pas de chemin,
    sinon c'est un chemin possible entre ces deux cases sous la forme d'une liste
    de coordonées (couple de (lig,col))
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: une liste de coordonées indiquant un chemin possible entre la case
              de départ et la case d'arrivée
    """
    pass



if __name__ == "__main__":
  p=Plateau(2,49)
  print(p)
  print(prendreTresorPlateau(p,1,1,32))
  print(getCoordonneesTresor(p,22))
  print(getCoordonneesJoueur(p,2))
  print(prendrePionPlateau(p,0,6,2))
  print(p)
