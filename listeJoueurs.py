import random
import joueur

def ListeJoueurs(nomsJoueurs):
    """
    créer une liste de joueurs dont les noms sont dans la liste de noms passés en paramètre
    Attention il s'agit d'une liste de joueurs qui gère la notion de joueur courant
    paramètre: nomsJoueurs une liste de chaines de caractères
    résultat: la liste des joueurs avec un joueur courant mis à 0
    """
    joueurs=[]
    i=0
    while i<len(nomsJoueurs):
      nom=joueur.Joueur(nomsJoueurs[i])
      joueurs.append(nom)
      i+=1
    return joueurs


def ajouterJoueur(joueurs, joueur1):
    """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs un liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    nom=joueur.Joueur(joueur1)
    joueurs.append(nom)

def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs un liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    random.shuffle(joueurs)
    i=0
    while i<len(joueurs):
      joueurs[i]["numJoueur"]=i
      i+=1
    

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
        while cpt<len(joueurs) and out==False:
          joueur.ajouterTresor(joueurs[cpt],Tresors[i])
          cpt+=1
          if i>len(Tresors):
            out=True
          i+=1
    if nbTresorMax!=0:
      if len(joueurs)*nbTresorMax>nbTresors:
        print("il n'y a pas assez de trésor")
      i=0
      out=False
      while i<(len(joueurs)*nbTresorMax):
        cpt=0
        while cpt<len(joueurs) and out==False:
          joueur.ajouterTresor(joueurs[cpt],Tresors[i])
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
    cpt=joueurs[0]
    joueurs.pop(0)
    joueurs.append(cpt)

def getNbJoueurs(joueurs):
    """
    retourne le nombre de joueurs participant à la partie
    paramètre: joueurs la liste des joueurs
    résultat: le nombre de joueurs de la partie
    """
    return len(joueurs)

def getJoueurCourant(joueurs):
    """
    retourne le joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le joueur courant
    """
    return joueurs[0]

def joueurCourantTrouveTresor(joueurs):
    """
    Met à jour le joueur courant lorsqu'il a trouvé un trésor
    c-à-d enlève le trésor de sa liste de trésors à trouver
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueur.tresorTrouve(joueurs[0])

def nbTresorsRestantsJoueur(joueurs,numJoueur):
    """
    retourne le nombre de trésors restant pour le joueur dont le numéro 
    est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le nombre de trésors que joueur numJoueur doit encore trouver
    """
    return len(joueurs[numJoueur]["tresor"])

def numJoueurCourant(joueurs):
    """
    retourne le numéro du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le numéro du joueur courant
    """
    return joueurs[0]["numJoueur"]

def nomJoueurCourant(joueurs):
    """
    retourne le nom du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le nom du joueur courant
    """
    return joueur.getNom(joueurs[0])

def nomJoueur(joueurs,numJoueur):
    """
    retourne le nom du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le nom du joueur numJoueur
    """
    test=False
    i=0
    while i<len(joueurs) and test==False:
      if joueurs[i]["numJoueur"]==numJoueur:
        test=True
      i+=1
    return joueur.getNom(joueurs[i-1])

def prochainTresorJoueur(joueurs,numJoueur):
    """
    retourne le trésor courant du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le prochain trésor du joueur numJoueur (un entier)
    """
    test=False
    i=0
    while i<len(joueurs) and test==False:
      if joueurs[i]["numJoueur"]==numJoueur:
        test=True
      i+=1
    return joueur.prochainTresor(joueurs[i-1])

def tresorCourant(joueurs):
    """
    retourne le trésor courant du joueur courant
    paramètre: joueurs la liste des joueurs 
    résultat: le prochain trésor du joueur courant (un entier)
    """
    return joueur.prochainTresor(joueurs[0])

def joueurCourantAFini(joueurs):
    """
    indique si le joueur courant a gagné
    paramètre: joueurs la liste des joueurs 
    résultat: un booleen indiquant si le joueur courant a fini
    """
    if joueur.prochainTresor(joueurs[0])==None:
      return True
    else:
      return False

if __name__=="__main__":
  c=(ListeJoueurs(["Anthony","Hector","Jira"]))
  print(c)
  print(ajouterJoueur(c, "Jean marc"))
  print(initAleatoireJoueurCourant(c))
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