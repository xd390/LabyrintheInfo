# -*- coding: utf-8 -*-
"""
        Projet Labyrinthe
        Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module carte
   ~~~~~~~~~~~~

   Ce module gère les cartes du labyrinthe.
"""
import random

#Hector

"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']

def Carte( nord, est, sud, ouest, tresor=0, pions=[]):          #marche
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """
    return {"nord" : nord, "est" : est, "sud" : sud, "ouest" : ouest, "tresor" : tresor, "pions" : pions }



def estValide(c):                               #marche
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
    paramètre: c une carte"""
    cpt=0
    if c["nord"]==True:
        cpt+=1
    if c["ouest"]==True:
        cpt+=1
    if c["sud"]==True:
        cpt+=1
    if c["est"]==True:
        cpt+=1
    if cpt>2:
        return False
    else:
        return True

def murNord(c):                                 #marche
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
    return c["nord"]==True

def murSud(c):                                  #marche
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """
    return c["sud"]==True

def murEst(c):                                  #marche
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
    return c["est"]==True

def murOuest(c):                                #marche
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
    return c["ouest"]==True

def getListePions(c):                           #marche
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    return c["pions"]

def setListePions(c,listePions):                #marche
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    c["pions"]=listePions
    pass


def getNbPions(c):                              #marche
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    return len(c["pions"])


def possedePion(c,pion):                        #marche
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    """
    if pion in c["pions"]:
        return True
    else:
        return False


def getTresor(c):                               #marche
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    return c["tresor"]


def prendreTresor(c):                           #marche
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res=c["tresor"]
    c["tresor"]=0
    return res


def mettreTresor(c,tresor):                     #marche
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res=c["tresor"]
    c["tresor"]=tresor
    return res


def prendrePion(c, pion):                       #marche
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    for i in c["pions"]:
        if i==pion:
            c["pions"].pop()
    print(c["pions"])
    pass"""
    aux=[]
    i=0
    while i<len(c["pions"]):
      if c["pions"][i]!=pion:
        aux.append(i)
      i+=1
    c["pions"]=aux


def poserPion(c, pion):                         #marche
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    verif=False
    for x in c["pions"]:
      if x==pion:
        verif=True
    if verif!=True:    
      c["pions"].append(pion)
    pass

def tournerHoraire(c):                          #marche
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    aux=c["nord"]
    c["nord"]=c["ouest"]
    c["ouest"]=c["sud"]
    c["sud"]=c["est"]
    c["est"]=aux
    pass


def tournerAntiHoraire(c):                      #marche
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    aux=c["nord"]
    c["nord"]=c["est"]
    c["est"]=c["sud"]
    c["sud"]=c["ouest"]
    c["ouest"]=aux
    pass


def tourneAleatoire(c):                         #marche
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    rng=random.choice([0,1,2,3])
    for i in range(rng):
        tournerHoraire(c)
    pass



def coderMurs(c):                           #marche
    """
    code les murs sous la forme d'un entier dont le codage binaire
    est de la forme bNbEbSbO où bN, bE, bS et bO valent
       soit 0 s'il n'y a pas de mur dans dans la direction correspondante
       soit 1 s'il y a un mur dans la direction correspondante
    bN est le chiffre des unité, BE des dizaine, etc...
    le code obtenu permet d'obtenir l'indice du caractère semi-graphique
    correspondant à la carte dans la liste listeCartes au début de ce fichier
    paramètre c une carte
    retourne un entier indice du caractère semi-graphique de la carte
    """
    res=0
    if c["nord"]==True:
        res+=1
    if c["est"]==True:
        res==10
    if c["sud"]==True:
        res==100
    if c["ouest"]==True:
        res+=1000
    return res


def decoderMurs(c,code):                    #marche
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    res=code
    if code>=1000:
        c["ouest"]=True
        res=res-1000
    if code>=100:
        c["sud"]=True
        res=res-100
    if code>=10:
        c["est"]=True
        res=res-10
    if code>=1:
        c["nord"]=True
    pass


def toChar(c):                              #marche
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
    code=coderMurs(c)
    if code==1100:
        return '╚'
    elif code==1010:
        return '║'
    elif code==1001:
        return '╔'
    elif code==1000:
        return '╠'
    elif code==110:
        return '╝'
    elif code==101:
        return '═'
    elif code==100:
        return '╩'
    elif code==11:
        return '╗'
    elif code==10:
        return '╣'
    elif code==1:
        return '╦'
    elif code==0:
        return '╬'
    else:
        return 'Ø'



def passageNord(carte1,carte2):             #marche
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    if carte2["sud"]==False and carte2["sud"]==carte1["nord"]:
        return True
    else:
        return False


def passageSud(carte1,carte2):              #marche
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    if carte2["nord"]==False and carte2["nord"]==carte1["sud"]:
        return True
    else:
        return False

def passageOuest(carte1,carte2):            #marche
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    if carte2["est"]==False and carte2["est"]==carte1["ouest"]:
        return True
    else:
        return False


def passageEst(carte1,carte2):              #marche
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    if carte2["ouest"]==False and carte2["ouest"]==carte1["est"]:
        return True
    else:
        return False

c=Carte(True,True,False,False)

if __name__=="__main__":
    Carte(True, True, False, False)
    print(c)
    print(estValide(c))
    print(murNord(c))
    print(murSud(c))
    print(murEst(c))
    print(murOuest(c))
    print(getListePions(c))
    print(setListePions(c,[2,1]))
    print(getNbPions(c))
    print(possedePion(c,3))
    print(getTresor(c))
    print(prendreTresor(c))
    print(mettreTresor(c,1))
    print(prendrePion(c,2))
    print(poserPion(c,2))
    print(tournerHoraire(c))
    print(tournerAntiHoraire(c))
    print(tourneAleatoire(c))
    print(coderMurs(c))
    print(decoderMurs(c,coderMurs(c)))
    print(toChar(c))
    print(passageNord(c,c))
    print(passageSud(c,c))
    print(passageOuest(c,c))
