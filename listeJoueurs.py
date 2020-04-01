import random
from joueur import *

def ListeJoueurs(nomsJoueurs):
    """
    créer une liste de joueurs dont les noms sont dans la liste de noms passés en paramètre
    Attention il s'agit d'une liste de joueurs qui gère la notion de joueur courant
    paramètre: nomsJoueurs une liste de chaines de caractères
    résultat: la liste des joueurs avec un joueur courant mis à 0
    """
    joueurs={}
    ListeJoueurs=[]
    i=0
    for x in nomsJoueurs:
      ListeJoueurs.append(Joueur(x))
    joueurs["listedesjoueurs"]=ListeJoueurs
    joueurs["joueurCourant"]=0
    return joueurs


def ajouterJoueur(joueurs, joueur):
    """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs un liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs["listedesjoueurs"].append(joueur)
    

def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs une liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs["joueurCourant"]=random.choice(list(range(0,len(joueurs["listedesjoueurs"]))))
    

def distribuerTresors(joueurs,nbTresors=24, nbTresorMax=0):
    """
    distribue de manière aléatoire des trésors entre les joueurs.
    paramètres: joueurs la liste des joueurs
                nbTresors le nombre total de trésors à distribuer (on rappelle 
                        que les trésors sont des entiers de 1 à nbTresors)
                nbTresorsMax un entier fixant le nombre maximum de trésor 
                             qu'un joueur aura après la distribution
                             si ce paramètre vaut 0 on distribue le maximum
                             de trésor possible  
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    Tresors= list(range(1,nbTresors+1))
    random.shuffle(Tresors)
    if nbTresorMax==0:
      i=0
      out=False
      while i<len(Tresors):
        cpt=0
        while cpt<len(joueurs["listedesjoueurs"]) and i<len(Tresors):
          ajouterTresor(joueurs["listedesjoueurs"][cpt],Tresors[i])
          cpt+=1
          i+=1
      nbJoueurs=getNbJoueurs(joueurs)
      """
      La partie ci-dessous verifie si les trésors on étaient repartis de façon équitable.
      Et surprime les trésors en trop s'il y a un/des joueur/s qui a/ont en plus
      """
      if nbTresors%nbJoueurs!=0:
        if (nbTresors-1)%nbJoueurs==0:
          tresorTrouve(joueurs["listedesjoueurs"][0])
        elif (nbTresors-2)%nbJoueurs==0:
          tresorTrouve(joueurs["listedesjoueurs"][0])
          tresorTrouve(joueurs["listedesjoueurs"][1])
        elif (nbTresors-3)%nbJoueurs==0:
          tresorTrouve(joueurs["listedesjoueurs"][0])
          tresorTrouve(joueurs["listedesjoueurs"][1])
          tresorTrouve(joueurs["listedesjoueurs"][2])          
    if nbTresorMax!=0:
      i=0
      out=False
      while i<(len(joueurs)*nbTresorMax):
        cpt=0
        while cpt<len(joueurs) and out==False:
          ajouterTresor(joueurs["listedesjoueurs"][cpt],Tresors[i])
          cpt+=1
          if i>len(Tresors):
            out=True
          i+=1
      

def changerJoueurCourant(joueurs):
    """
    passe au joueur suivant (change le joueur courant donc)
    paramètres: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    if (1+joueurs["joueurCourant"])==len(joueurs["listedesjoueurs"]):
      joueurs["joueurCourant"]=0
    else:
      joueurs["joueurCourant"]+=1

def getNbJoueurs(joueurs):
    """
    retourne le nombre de joueurs participant à la partie
    paramètre: joueurs la liste des joueurs
    résultat: le nombre de joueurs de la partie
    """
    return len(joueurs["listedesjoueurs"])

def getJoueurCourant(joueurs):
    """
    retourne le joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le joueur courant
    """
    return joueurs["listedesjoueurs"][joueurs["joueurCourant"]]

def joueurCourantTrouveTresor(joueurs):
    """
    Met à jour le joueur courant lorsqu'il a trouvé un trésor
    c-à-d enlève le trésor de sa liste de trésors à trouver
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    tresorTrouve(joueurs["listedesjoueurs"][joueurs["joueurCourant"]])

def nbTresorsRestantsJoueur(joueurs,numJoueur):
    """
    retourne le nombre de trésors restant pour le joueur dont le numéro 
    est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le nombre de trésors que joueur numJoueur doit encore trouver
    """
    return getNbTresorsRestants(joueurs["listedesjoueurs"][numJoueur])

def numJoueurCourant(joueurs):
    """
    retourne le numéro du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le numéro du joueur courant
    """
    return joueurs["joueurCourant"]

def nomJoueurCourant(joueurs):
    """
    retourne le nom du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le nom du joueur courant
    """
    return getNom(joueurs["listedesjoueurs"][joueurs["joueurCourant"]])

def nomJoueur(joueurs,numJoueur):
    """
    retourne le nom du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le nom du joueur numJoueur
    """
    return getNom(joueurs["listedesjoueurs"][numJoueur])

def prochainTresorJoueur(joueurs,numJoueur):
    """
    retourne le trésor courant du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le prochain trésor du joueur numJoueur (un entier)
    """
    return prochainTresor(joueurs["listedesjoueurs"][numJoueur])

def tresorCourant(joueurs):
    """
    retourne le trésor courant du joueur courant
    paramètre: joueurs la liste des joueurs 
    résultat: le prochain trésor du joueur courant (un entier)
    """
    return prochainTresor(joueurs["listedesjoueurs"][joueurs["joueurCourant"]])

def joueurCourantAFini(joueurs):
    """
    indique si le joueur courant a gagné
    paramètre: joueurs la liste des joueurs 
    résultat: un booleen indiquant si le joueur courant a fini
    """
    if prochainTresor(joueurs["listedesjoueurs"][joueurs["joueurCourant"]])==None:
      return True
    else:
      return False

if __name__=="__main__":
  c=(ListeJoueurs(["Anthony","Hector","Jira"]))
  print(c)
  print(initAleatoireJoueurCourant(c),"\n")
  print(c,"\n")
  print(ajouterJoueur(c,Joueur("Martin")))
  print(c)
  print(distribuerTresors(c,nbTresors=24, nbTresorMax=0))
  print(c)
  print(changerJoueurCourant(c))
  print(c)
  print(getNbJoueurs(c))
  print(getJoueurCourant(c))
  print(joueurCourantTrouveTresor(c))
  print(nbTresorsRestantsJoueur(c,2))
  print(numJoueurCourant(c))
  print(nomJoueurCourant(c))
  print(nomJoueur(c,2))
  print(prochainTresorJoueur(c,2))
  print(c)
  print(tresorCourant(c))
  print(joueurCourantAFini(c))