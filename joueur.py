# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module joueur
   ~~~~~~~~~~~~~
   
   Ce module gère un joueur. 
"""

def Joueur(nom):
    """
    creer un nouveau joueur portant le nom passé en paramètre. Ce joueur possède une liste de trésors à trouver vide
    paramètre: nom une chaine de caractères
    retourne le joueur ainsi créé
    """
    joueur={}
    joueur["name"]=nom
    joueur["tresor"] = []
    return joueur

def ajouterTresor(joueur,tresor):
    """
    ajoute un trésor à trouver à un joueur (ce trésor sera ajouter en fin de liste) Si le trésor est déjà dans la liste des trésors à trouver la fonction ne fait rien
    paramètres:
        joueur le joueur à modifier
        tresor un entier strictement positif
    la fonction ne retourne rien mais modifie le joueur
    """    
    existe=False
    if tresor in joueur["tresor"]:
      existe=True
    if existe==False:
      joueur["tresor"].append(tresor)

def prochainTresor(joueur):
    """
    retourne le prochain trésor à trouver d'un joueur, retourne None si aucun trésor n'est à trouver
    paramètre:
        joueur le joueur
    résultat un entier représentant le trésor ou None
    """
    if len(joueur["tresor"])<1:
      return None
    else:
      return joueur["tresor"][0]

def tresorTrouve(joueur):
    """ 
    enlève le premier trésor à trouver car le joueur l'a trouvé
    paramètre:
        joueur le joueur
    la fonction ne retourne rien mais modifie le joueur
    """
    del joueur["tresor"][0]
    
def getNbTresorsRestants(joueur):
    """
    retourne le nombre de trésors qu'il reste à trouver
    paramètre: joueur le joueur
    résultat: le nombre de trésors attribués au joueur
    """
    return len(joueur["tresor"]) 


def getNom(joueur):
    """
    retourne le nom du joueur
    paramètre: joueur le joueur
    résultat: le nom du joueur 
    """
    return joueur["name"]

if __name__=="__main__":
  print(Joueur("Anthony"))
  c=Joueur("anthony")
  print(ajouterTresor(c,1))
  print(ajouterTresor(c,2))
  print(prochainTresor(c))
  print(tresorTrouve(c))
  print(prochainTresor(c))
  print(getNbTresorsRestants(c))
  print(getNom(c))
