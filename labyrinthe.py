# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module labyrinthe
   ~~~~~~~~~~~~~~~~~
   
   Ce module gère sur le jeu du labyrinthe (observation et mise à jour du jeu).
"""

from listeJoueurs import *
from plateau import *


def Labyrinthe(nomsJoueurs=["joueur1","joueurs2"],nbTresors=24, nbTresorsMax=0):
    """
    permet de créer un labyrinthe avec nbJoueurs joueurs, nbTresors trésors
    chacun des joueurs aura au plus nbTresorMax à trouver
    si ce dernier paramètre est à 0, on distribuera le maximum de trésors possible 
    à chaque joueur en restant équitable
    un joueur courant est choisi et la phase est initialisée
    paramètres: nomsJoueurs est la liste des noms des joueurs participant à la partie (entre 1 et 4)
                nbTresors le nombre de trésors différents il en faut au moins 12 et au plus 49
                nbTresorMax le nombre de trésors maximum distribué à chaque joueur
    résultat: le labyrinthe crée
    """
    labyrinthe={"listedejoueur":ListeJoueurs(nomsJoueurs),"plateau": Plateau(len(nomsJoueurs),nbTresors),"phase":1,"coupInterdit": None }
    distribuerTresors(labyrinthe["listedejoueur"],nbTresors, nbTresorsMax)
    initAleatoireJoueurCourant(labyrinthe["listedejoueur"])
    return labyrinthe

def getPlateau(labyrinthe):
    """
    retourne la matrice représentant le plateau de jeu
    paramètre: labyrinthe le labyrinthe considéré
    résultat: la matrice représentant le plateau de ce labyrinthe
    """
    return labyrinthe["plateau"][0]

def getNbParticipants(labyrinthe):
    """
    retourne le nombre de joueurs engagés dans la partie
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de joueurs de la partie
    """
    return getNbJoueurs(labyrinthe["listedejoueur"])

def getNomJoueurCourant(labyrinthe):
    """
    retourne le nom du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nom du joueurs courant
    """
    return nomJoueurCourant(labyrinthe["listedejoueur"])

def getNumJoueurCourant(labyrinthe):
    """
    retourne le numero du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numero du joueurs courant
    """
    return numJoueurCourant(labyrinthe["listedejoueur"])

def getPhase(labyrinthe): 
    """
    retourne la phase du jeu courante
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numéro de la phase de jeu courante
    """   
    return labyrinthe["phase"]


def changerPhase(labyrinthe): 
    """
    change de phase de jeu en passant la suivante
    paramètre: labyrinthe le labyrinthe considéré
    la fonction ne retourne rien mais modifie le labyrinthe
    """    
    if getPhase(labyrinthe)==1:
      labyrinthe["phase"]=2
    else:
      labyrinthe["phase"]=1


def getNbTresors(labyrinthe):
    """
    retourne le nombre de trésors qu'il reste sur le labyrinthe
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de trésors sur le plateau
    """
    cpt=0
    for l in labyrinthe["plateau"][0]:
      for c in l:
        if getTresor(c)!=0:
          cpt+=1
    return cpt
    

def getListeJoueurs(labyrinthe):
    """
    retourne la liste joueur structures qui gèrent les joueurs et leurs trésors
    paramètre: labyrinthe le labyrinthe considéré
    résultat: les joueurs sous la forme de la structure implémentée dans listeJoueurs.py    
    """
    return labyrinthe["listedejoueur"]


def enleverTresor(labyrinthe,lin,col,numTresor):
    """
    enleve le trésor numTresor du plateau du labyrinthe. 
    Si l'opération s'est bien passée le nombre total de trésors dans le labyrinthe
    est diminué de 1
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    la fonction ne retourne rien mais modifie le labyrinthe
    """
    prendreTresorPlateau(labyrinthe["plateau"][0],lin,col,numTresor)
    pass
    

def prendreJoueurCourant(labyrinthe,lin,col):
    """
    enlève le joueur courant de la carte qui se trouve sur la case lin,col du plateau
    si le joueur ne s'y trouve pas la fonction ne fait rien
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe    
    """
    prendrePionPlateau(labyrinthe["plateau"],lin,col,getNumJoueurCourant(labyrinthe))
    pass
    
def poserJoueurCourant(labyrinthe,lin,col):
    """
    pose le joueur courant sur la case lin,col du plateau
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe     
    """
    poserPionPlateau(labyrinthe["plateau"],lin,col,getNumJoueurCourant(labyrinthe))
    pass

def getCarteAJouer(labyrinthe):
    """
    donne la carte à jouer
    paramètre: labyrinthe: le labyrinthe considéré
    résultat: la carte à jouer    
    """    
    return labyrinthe["plateau"][1]

def coupInterdit(labyrinthe,direction,rangee):
    """ 
    retourne True si le coup proposé correspond au coup interdit
    elle retourne False sinon
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    résultat: un booléen indiquant si le coup est interdit ou non
    """
    if labyrinthe["coupInterdit"]==None:
      return False
    elif labyrinthe["coupInterdit"]==(direction,rangee):
      return True
    else:
      return False

def jouerCarte(labyrinthe,direction,rangee):
    """
    fonction qui joue la carte amovible dans la direction et sur la rangée passées 
    en paramètres. Cette fonction
       - met à jour le plateau du labyrinthe
       - met à jour la carte à jouer
       - met à jour la nouvelle direction interdite
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe
    """
    p=labyrinthe["plateau"][0]
    if direction=="N":
      x=decalageColonneEnBas(p, rangee, getCarteAJouer(labyrinthe))
      labyrinthe["plateau"]=p,x
      labyrinthe["coupInterdit"]=("S",rangee)  
    elif direction=="S":
      x=decalageColonneEnHaut(p, rangee, getCarteAJouer(labyrinthe))
      labyrinthe["plateau"]=p,x
      labyrinthe["coupInterdit"]=("N",rangee)
    elif direction=="E":
      x=decalageLigneAGauche(p, rangee, getCarteAJouer(labyrinthe))
      labyrinthe["plateau"]=p,x
      labyrinthe["coupInterdit"]=("O",rangee)
    elif direction=="O":
      x=decalageLigneADroite(p, rangee, getCarteAJouer(labyrinthe))
      labyrinthe["plateau"]=p,x
      labyrinthe["coupInterdit"]=("E",rangee)




def tournerCarte(labyrinthe,sens='H'):
    """
    tourne la carte à jouer dans le sens indiqué en paramètre (H horaire A antihoraire)
    paramètres: labyritnthe: le labyrinthe considéré
                sens: un caractère indiquant le sens dans lequel tourner la carte
     Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe    
    """
    if sens=='H':
      tournerHoraire(getCarteAJouer)
    else:
      tournerAntiHoraire(getCarteAJouer)

def getTresorCourant(labyrinthe):
    """
    retourne le numéro du trésor que doit cherche le joueur courant
    paramètre: labyritnthe: le labyrinthe considéré 
    resultat: le numéro du trésor recherché par le joueur courant
    """
    return tresorCourant(getListeJoueurs(labyrinthe))

def getCoordonneesTresorCourant(labyrinthe):
    """
    donne les coordonnées du trésor que le joueur courant doit trouver
    paramètre: labyritnthe: le labyrinthe considéré 
    resultat: les coordonnées du trésor à chercher ou None si celui-ci 
              n'est pas sur le plateau
    """
    return getCoordonneesTresor(labyrinthe["plateau"][0],getTresorCourant(labyrinthe))


def getCoordonneesJoueurCourant(labyrinthe):
    """
    donne les coordonnées du joueur courant sur le plateau
    paramètre: labyritnthe: le labyrinthe considéré 
    resultat: les coordonnées du joueur courant ou None si celui-ci 
              n'est pas sur le plateau
    """
    return getCoordonneesJoueur(labyrinthe["plateau"][0],getNumJoueurCourant(labyrinthe))


def executerActionPhase1(labyrinthe,action,rangee):
    """
    exécute une action de jeu de la phase 1
    paramètres: labyrinthe: le labyrinthe considéré
                action: un caractère indiquant l'action à effecter
                        si action vaut 'T' => faire tourner la carte à jouer
                        si action est une des lettres N E S O et rangee est un des chiffre 1,3,5 
                        => insèrer la carte à jouer à la direction action sur la rangée rangee
                           et faire le nécessaire pour passer en phase 2
    résultat: un entier qui vaut
              0 si l'action demandée était valide et demandait de tourner la carte
              1 si l'action demandée était valide et demandait d'insérer la carte
              2 si l'action est interdite car l'opposée de l'action précédente
              3 si action et rangee sont des entiers positifs
              4 dans tous les autres cas
    """
    if action=="T":
      tournerHoraire(getCarteAJouer(labyrinthe))
      return 0
    elif action in ["N","E","S","O"] and rangee in [1,3,5]:
      if coupInterdit(labyrinthe,action,rangee)==False:
        jouerCarte(labyrinthe,action,rangee)
        changerPhase(labyrinthe)
        return 1
      else:
        return 2
    elif isinstance(action,int)==True and isinstance(rangee,int)==True:
      if action>0 and rangee>0:
        return 3
    else:
      return 4

def accessibleDistJoueurCourant(labyrinthe, ligA,colA):
    """
    verifie si le joueur courant peut accéder la case ligA,colA
    si c'est le cas la fonction retourne une liste représentant un chemin possible
    sinon ce n'est pas le cas, la fonction retourne None
    paramètres: labyrinthe le labyrinthe considéré
                ligA la ligne de la case d'arrivée
                colA la colonne de la case d'arrivée
    résultat: une liste de couples d'entier représentant un chemin que le joueur
              courant atteigne la case d'arrivée s'il existe None si pas de chemin
    """
    c=getCoordonneesJoueurCourant(labyrinthe)
    x=c[0]
    y=c[1]
    print(x, y)
    if accessible(labyrinthe["plateau"][0],x,y,ligA,colA)==True:
      return accessibleDist(labyrinthe["plateau"][0],x,y,ligA,colA)
    else:
      return None



def finirTour(labyrinthe):
    """
    vérifie si le joueur courant vient de trouver un trésor (si oui fait le nécessaire)
    vérifie si la partie est terminée, si ce n'est pas le cas passe au joueur suivant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: un entier qui vaut
              0 si le joueur courant n'a pas trouvé de trésor
              1 si le joueur courant a trouvé un trésor mais la partie n'est pas terminée
              2 si le joueur courant a trouvé son dernier trésor (la partie est donc terminée)
    """
    changerPhase(labyrinthe)
    i=getCoordonneesTresorCourant(labyrinthe)
    if getCoordonneesJoueurCourant(labyrinthe)==(i):
      enleverTresor(labyrinthe,i[0],i[1],getTresorCourant(labyrinthe))
      joueurCourantTrouveTresor(getListeJoueurs(labyrinthe))
      if joueurCourantAFini(getListeJoueurs(labyrinthe))==True:
        return 2
      else:
        changerJoueurCourant(getListeJoueurs(labyrinthe))
        return 1
    else:
      changerJoueurCourant(getListeJoueurs(labyrinthe))
      return 0
    pass

if __name__=="__main__":
  L=Labyrinthe(["hector","anthony","Jira"],24,0)
  print(getPlateau(L))
  print(getNbParticipants(L))  
  print(getNomJoueurCourant(L))
  print(getNumJoueurCourant(L))
  print(getListeJoueurs(L))
  print(getPhase(L))
  print(L,"\n")
  print(getNbTresors(L))
  print(getCarteAJouer(L))
  print(accessibleDistJoueurCourant(L,0,3))
  print(executerActionPhase1(L,1,3))
  print(getCoordonneesJoueurCourant(L))
  print(getCoordonneesTresorCourant(L))
  print(getListeJoueurs(L))
  print(getNumJoueurCourant(L))

