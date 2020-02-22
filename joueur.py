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
    joueur["name"] = nom
    joueur["tresor"] = []
    print(joueur)
    return joueur
    pass

def ajouterTresor(joueur,tresor):
    """
    ajoute un trésor à trouver à un joueur (ce trésor sera ajouter en fin de liste) Si le trésor est déjà dans la liste des trésors à trouver la fonction ne fait rien
    paramètres:
        joueur le joueur à modifier
        tresor un entier strictement positif
    la fonction ne retourne rien mais modifie le joueur
    """    
    i=0
    existe=False
    listedetresor=joueur["tresor"]
    while i<len(joueur["tresor"]) or existe==True:
      if tresor==listedetresor[i]:
        existe=True 
      i+=1
    if existe==False:
      listedetresor.append(tresor)
      joueur["tresor"]=listedetresor
    pass

def prochainTresor(joueur):
    """
    retourne le prochain trésor à trouver d'un joueur, retourne None si aucun trésor n'est à trouver
    paramètre:
        joueur le joueur
    résultat un entier représentant le trésor ou None
    """
    listedetresor=joueur["tresor"]
    if len(listedetresor)<1:
      return None
    else:
      return listedetresor[0]
    pass


def tresorTrouve(joueur):
    """ 
    enlève le premier trésor à trouver car le joueur l'a trouvé
    paramètre:
        joueur le joueur
    la fonction ne retourne rien mais modifie le joueur
    """
    listedetresor=joueur["tresor"]
    del listedetresor[0]
    joueur["tresor"]=listedetresor
    pass

def getNbTresorsRestants(joueur):
    """
    retourne le nombre de trésors qu'il reste à trouver
    paramètre: joueur le joueur
    résultat: le nombre de trésors attribués au joueur
    """
    res=len(joueur["tresor"])
    return res
    pass

def getNom(joueur):
    """
    retourne le nom du joueur
    paramètre: joueur le joueur
    résultat: le nom du joueur 
    """
    res=joueur("name")
    return res
    pass
