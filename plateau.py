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
    #Initialisation  des cartes non amoviables
    setVal(matrice,0,0,Carte(True,False,False,True,0,[1]))
    setVal(matrice,0,2,Carte(True,False,False,False,0,[]))
    setVal(matrice,0,4,Carte(True,False,False,False,0,[]))
    if nbJoueurs>1:
      setVal(matrice,0,6,Carte(True,True,False,False,0,[2]))
    else:
      setVal(matrice,0,6,Carte(True,True,False,False,0,[]))
    setVal(matrice,2,0,Carte(False,False,False,True,0,[]))
    setVal(matrice,2,2,Carte(False,False,False,True,0,[]))
    setVal(matrice,2,4,Carte(True,False,False,False,0,[]))
    setVal(matrice,2,6,Carte(False,True,False,False,0,[]))
    setVal(matrice,4,0,Carte(False,False,False,True,0,[]))
    setVal(matrice,4,2,Carte(False,False,True,False,0,[]))
    setVal(matrice,4,4,Carte(False,True,False,False,0,[]))
    setVal(matrice,4,6,Carte(False,True,False,False,0,[]))
    if nbJoueurs>2:
      setVal(matrice,6,0,Carte(False,False,True,True,0,[3]))
    else:
      setVal(matrice,6,0,Carte(False,False,True,True,0,[]))
    setVal(matrice,6,2,Carte(False,False,True,False,0,[]))
    setVal(matrice,6,4,Carte(False,False,True,False,0,[]))
    if nbJoueurs>3:
      setVal(matrice,6,6,Carte(False,True,True,False,0,[4]))
    else:
      setVal(matrice,6,6,Carte(False,True,True,False,0,[]))
    listedecarte=(creerCartesAmovibles(1,nbTresors))
    for x in listedecarte:
      tourneAleatoire(x)
    if nbTresors>34:
      listedestresors=list(range(35,nbTresors+1))
      random.shuffle(listedestresors)
      for x in matrice:
        cpt=0
        while cpt<len(x) and cpt<len(listedestresors):
          if x[cpt]==getVal(matrice,0,0):
            cpt+=1
            continue
          if x[cpt]==getVal(matrice,0,6):
            cpt+=1
            continue
          if x[cpt]==getVal(matrice,6,0):
            cpt+=1
            continue
          if x[cpt]==getVal(matrice,6,6):
            cpt+=1
            continue
          if x[cpt]!=0:
            mettreTresor(x[cpt],listedestresors[0])
            listedestresors.pop(0)
          cpt+=1
    for x in matrice:
      cpt=0
      while cpt<len(x):
        if x[cpt]==0:
          x[cpt]=listedecarte[0]
          listedecarte.pop(0)
        cpt+=1
    return matrice,listedecarte[0]
    



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
        listedecarte.append(Carte(True,False,False,True,0,[]))
      elif 16<i<22:
        listedecarte.append(Carte(True,False,False,False,0,[]))
      else:
        listedecarte.append(Carte(False,True,True,False,0,[]))
      i+=1
    listedestresors=list(range(tresorDebut,nbTresors+1))
    cpt=0
    for x in listedecarte:
      if cpt>=len(listedestresors):
        break
      mettreTresor(x,listedestresors[cpt])
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
    if numTresor==prendreTresor(getVal(plateau,lig,col)):
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
    for i_l,l in enumerate(plateau):
      for i_c,c in enumerate(l):
        if numTresor==getTresor(c):
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
    for i_l,l in enumerate(plateau):
      for i_c,c in enumerate(l):
        if numJoueur in getListePions(c):
          return i_l,i_c
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
    prendrePion(getVal(plateau,lin,col),numJoueur)



def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    poserPion(getVal(plateau,lin,col), numJoueur)
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
	#une quasi copie conforme de la première partie de accessibleDist (qui est déjà détaillée) pour obtenir une liste de coordonnées sur lesquelles le pion peut aller (listedecasesaccessibles). Un simple "if coordonnée de l'arrivé in listedecasesaccessibles" et on renvoit True si oui, False sinon.
    fin=False
    ligC=ligD
    colC=colD
    nord=[]
    sud=[]
    est=[]
    ouest=[]
    cpt=0
    trouve=False
    listedecasesaccessibles=[[ligD, colD]]
    while not fin and not trouve:
        for c in listedecasesaccessibles:
            if (c[0]-1)>=0:
                if [c[0]-1, c[1]] not in listedecasesaccessibles:
                    if passageNord(plateau[c[0]][c[1]], plateau[c[0]-1][c[1]])==True:
                        nord.append([c[0]-1, c[1]])
                        cpt+=1
            if (c[0]+1)<7:
                if [c[0]+1, c[1]] not in listedecasesaccessibles:
                    if passageSud(plateau[c[0]][c[1]], plateau[c[0]+1][c[1]])==True:
                        sud.append([c[0]+1, c[1]])
                        cpt+=1
            if (c[1]-1)>=0:
                if [c[0], c[1]-1] not in listedecasesaccessibles:
                    if passageOuest(plateau[c[0]][c[1]], plateau[c[0]][c[1]-1])==True:
                        ouest.append([c[0], c[1]-1])
                        cpt+=1
            if (c[1]+1)<7:
                if [c[0], c[1]+1] not in listedecasesaccessibles:
                    if passageEst(plateau[c[0]][c[1]], plateau[c[0]][c[1]+1])==True:
                        est.append([c[0], c[1]+1])
                        cpt+=1
            if nord!=[]:
                if nord[0] not in listedecasesaccessibles:
                    listedecasesaccessibles.extend(nord)
                nord=[]
                ligC-=1
            if [ligA, colA] in listedecasesaccessibles:
                trouve=True
                return True
            if sud!=[]:
                if sud[0] not in listedecasesaccessibles:
                    listedecasesaccessibles.extend(sud)
                sud=[]
                ligC+=1
            if [ligA, colA] in listedecasesaccessibles:
                trouve=True
                return True
            if est!=[]:
                if est[0] not in listedecasesaccessibles:
                    listedecasesaccessibles.extend(est)
                est=[]
                colC+=1
            if [ligA, colA] in listedecasesaccessibles:
                trouve=True
                return True
            if ouest!=[]:
                if ouest[0] not in listedecasesaccessibles:
                    listedecasesaccessibles.extend(ouest)
                ouest=[]
                colC-=1
            if [ligA, colA] in listedecasesaccessibles:
                trouve=True
                return True
        if cpt==0:
            fin=True
        cpt=0
    return False



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
    fin=False
    ligC=ligD
    colC=colD
    nord=[]			#on créé 4 listes vides dans lesquelles on placera la nouvelle coordoné se trouvant sur une carte adjacente à la carte parcourue dans la liste de cases accessible. (selon si elle se trouve au nord, au sud, à l'est ou à l'ouest)
    sud=[]
    est=[]
    ouest=[]
    cpt=0
    trouve=False
    listedecasesaccessibles=[[ligD, colD]]
    while not fin and not trouve:				#tant qu'on ne trouve pas la coordonée d'arriver ou qu'on a pas parcouru toutes les valeurs de la liste de cases accessible, on réitère.
        for c in listedecasesaccessibles: 			#pour chaque coordonée de la liste de cases accessible (avec seulement la coordoné de départ comme premier indice) :
            if (c[0]-1)>=0:		#si la ligne existe (n'est pas inférieure à 0)
                if [c[0]-1, c[1]] not in listedecasesaccessibles:
                    if passageNord(plateau[c[0]][c[1]], plateau[c[0]-1][c[1]])==True:
                        nord.append([c[0]-1, c[1]])
                        cpt+=1
            if (c[0]+1)<7:		#si la ligne existe (n'est pas supérieure à 7)
                if [c[0]+1, c[1]] not in listedecasesaccessibles:
                    if passageSud(plateau[c[0]][c[1]], plateau[c[0]+1][c[1]])==True:
                        sud.append([c[0]+1, c[1]])
                        cpt+=1
            if (c[1]-1)>=0:		#si la colonne existe (n'est pas inférieure à 0)
                if [c[0], c[1]-1] not in listedecasesaccessibles:
                    if passageOuest(plateau[c[0]][c[1]], plateau[c[0]][c[1]-1])==True:
                        ouest.append([c[0], c[1]-1])
                        cpt+=1
            if (c[1]+1)<7:		#si la colonne existe (n'est pas supérieure à 7)
                if [c[0], c[1]+1] not in listedecasesaccessibles:
                    if passageEst(plateau[c[0]][c[1]], plateau[c[0]][c[1]+1])==True:
                        est.append([c[0], c[1]+1])
                        cpt+=1
            if nord!=[]:
                if nord[0] not in listedecasesaccessibles:
                    listedecasesaccessibles.extend(nord)
                nord=[]
                ligC-=1
            if [ligA, colA] in listedecasesaccessibles:
                trouve=True
                break
            if sud!=[]:
                if sud[0] not in listedecasesaccessibles:
                    listedecasesaccessibles.extend(sud)
                sud=[]
                ligC+=1
            if [ligA, colA] in listedecasesaccessibles:
                trouve=True
                break
            if est!=[]:
                if est[0] not in listedecasesaccessibles:
                    listedecasesaccessibles.extend(est)
                est=[]
                colC+=1
            if [ligA, colA] in listedecasesaccessibles:
                trouve=True
                break
            if ouest!=[]:
                if ouest[0] not in listedecasesaccessibles:
                    listedecasesaccessibles.extend(ouest)
                ouest=[]
                colC-=1
            if [ligA, colA] in listedecasesaccessibles:
                trouve=True
                break
        if cpt==0:		#Si cpt==0 à ce stade de la boucle, cela signifie qu'il n'y a plus aucune carte sur laquelle le pion peut aller et qui n'est pas déjà dans "listedecasesaccessibles". Donc on sort de la while avec le fin=True
            fin=True
        cpt=0
    if trouve==False:
        return  None 		#On return None par défaut sauf si l'arrivé est dans la liste de cases accessible
    aux=[]
    cpt=1			#on initialise cpt à 1 pour accéder directement à l'indice suivant l'indice actuel de la boucle qui suit.
    for i in range(-1, -len(listedecasesaccessibles), -1):
        aux.append(listedecasesaccessibles[i])
    aux.append([ligD, colD])				#création d'une liste de coordonées partant du trésor et allant vers le pion. Dans la boucle qui suit, l'idée est de prendre uniquement les valeurs qui se trouvent sur le chemin menant au pion. Lorsque l'on tombe sur une de ces valeurs, on l'ajoute à la liste de coordonées "chemin". On obtient donc l'équivalent de aux (une liste de coordonnées allant du trésor au pion) mais dans laquelle il n'y a que les coordonnées du chemin le plus rapide.
    chemin=[aux[0]]			#lors de la création d'un liste de valeurs présente dans une liste parcouru dans une boucle for A L'ENVERS, (-1, -len(liste), -1), la première valeur de la liste n'est pas prise, on initie donc le chemin à cette valeur.
    if len(aux)==2:		#s'il n'y a que 2 coordonnées dans la liste de coordonnées, cela signifie que le chemin le plus rapide est aux[0] puis aux[1]
        return [aux[0], aux[1]]
    elif len(aux)>2:
        for i in range(len(aux)-1):
            if cpt<len(aux):
                if chemin[-1][0]==aux[cpt][0]:
                    if chemin[-1][1]==(aux[cpt][1]+1) or chemin[-1][1]==(aux[cpt][1]-1):
                        if [aux[cpt][0], aux[cpt][1]] not in chemin:
                            chemin.append([aux[cpt][0], aux[cpt][1]])
                elif chemin[-1][1]==aux[cpt][1]:
                    if chemin[-1][0]==(aux[cpt][0]+1) or chemin[-1][0]==(aux[cpt][0]-1):
                        if [aux[cpt][0], aux[cpt][1]] not in chemin:
                            chemin.append([aux[cpt][0], aux[cpt][1]])
            if [ligA, colA] in chemin and [ligD, colD] in chemin:
                break
            cpt+=1
    aux=[]
    for i in range(-1, -len(chemin), -1):			#Une dernière boucle pour remettre la liste de coordonnées à l'endroit puis la renvoyer.
        aux.append(chemin[i])
    aux.append(chemin[0])					#("return aux" serait plus rapide mais ça fait plus propre de rappeler que la variable qu'on veut retourner depuis le début est "chemin", alors je met tout dans chemin et je retourne chemin).
    chemin=aux
    return chemin



if __name__ == "__main__":
  x=Plateau(4,49)
  p=x[0]
  print(p,"\n")
  print(getVal(p,0,3),"\n")
  print(prendreTresorPlateau(p,0,0,32))
  print(getCoordonneesTresor(p,22))
  print(getCoordonneesJoueur(p,2))
  print(prendrePionPlateau(p,0,6,2))
  print(poserPionPlateau(p,2,4,5))
  print(p)
  print(accessible(p,0,0,0,3))
  x=accessibleDist(p,0,0,0,3)
  print(x)
  print(getCoordonneesJoueur(p,1))