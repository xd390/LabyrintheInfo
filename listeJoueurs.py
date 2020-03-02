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
      print(joueurs)
      i+=1
    return joueurs
    pass

ListeJoueurs(["Anthony","Julien","Hector"])

def ajouterJoueur(joueurs, joueur1):
    """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs un liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    nom=joueur.Joueur(joueur1)
    joueurs.append(nom)
ajouterJoueur(["Anthony","Julien","Hector"],"bertrand")
def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs un liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    random.shuffle(joueurs)

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
    print(joueurs)
      