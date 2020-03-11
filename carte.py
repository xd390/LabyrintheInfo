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
c=carte

def Carte( nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """
    patern=None
    c={}

    if nord==True:
        if est==True:
            c={"nord" : nord, "est" : est, "sud" : sud, "ouest" : ouest, "tresor" : tresor, "pions" : pions, "patern" : "╗" }
            return c
        elif sud==True:
            c={"nord" : nord, "est" : est, "sud" : sud, "ouest" : ouest, "tresor" : tresor, "pions" : pions, "patern" : '═' }
        elif ouest==True:
            c={"nord" : nord, "est" : est, "sud" : sud, "ouest" : ouest, "tresor" : tresor, "pions" : pions, "patern" : '╔' }
        else:
            c={"nord" : nord, "est" : est, "sud" : sud, "ouest" : ouest, "tresor" : tresor, "pions" : pions, "patern" : "╦" }
        return c
    elif est==True:
        if sud==True:
            c={"nord" : nord, "est" : est, "sud" : sud, "ouest" : ouest, "tresor" : tresor, "pions" : pions, "patern" : '╝' }
        elif ouest==True:
            c={"nord" : nord, "est" : est, "sud" : sud, "ouest" : ouest, "tresor" : tresor, "pions" : pions, "patern" : '║' }
        else:
            c={"nord" : nord, "est" : est, "sud" : sud, "ouest" : ouest, "tresor" : tresor, "pions" : pions, "patern" : '╣' }
        return c
    elif sud==True:
        if ouest==True:
            c={"nord" : nord, "est" : est, "sud" : sud, "ouest" : ouest, "tresor" : tresor, "pions" : pions, "patern" : '╚' }
        else:
            c={"nord" : nord, "est" : est, "sud" : sud, "ouest" : ouest, "tresor" : tresor, "pions" : pions, "patern" : '╩' }
            return c
    elif ouest==True:
        c={"nord" : nord, "est" : est, "sud" : sud, "ouest" : ouest, "tresor" : tresor, "pions" : pions, "patern" : '╠' }
        return c
    elif nord==True and nord==sud and sud==est and est==ouest:
        c={"nord" : nord, "est" : est, "sud" : sud, "ouest" : ouest, "tresor" : tresor, "pions" : pions, "patern" : '╬' }
        return c
    else:
        c={"nord" : nord, "est" : est, "sud" : sud, "ouest" : ouest, "tresor" : tresor, "pions" : pions, "patern" : 'Ø' }
        return c


    """for i in listeCartes:           #Lorsqu'il y a un mur, je met True et False s'il n'y en a pas.
        if i==╬:
            nord=False
            est=False
            sud=False
            ouest=False
        elif i==╦:
            nord=True
            est=False
            sud=False
            ouest=False
        elif i==╣:
            nord=False
            est=True
            sud=False
            ouest=False
        elif i==╗:
            nord=True
            est=True
            sud=False
            ouest=False
        elif i==╩:
            nord=False
            est=False
            sud=True
            ouest=False
        elif i==═:
            nord=True
            est=False
            sud=True
            ouest=False
        elif i==╝:
            nord=False
            est=True
            sud=True
            ouest=False
        elif i==╠:
            nord=False
            est=False
            sud=False
            ouest=True
        elif i==╔:
            nord=True
            est=False
            sud=False
            ouest=True
        elif i==║:
            nord=False
            est=True
            sud=False
            ouest=True
        elif i==╚:
            nord=False
            est=False
            sud=True
            ouest=True
        elif i==Ø:"""

    pass

def estValide(c):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
    paramètre: c une carte
    """
    cpt=0
    for key, value in c.keys():
        if value==True:
            cpt+=1
        if cpt>=3:
            return False
    return True


def murNord(c):
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
    if c["nord"]==True:
        return True
    else:
        return False


def murSud(c):
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """
    if c["sud"]==True:
        return True
    else:
        return False


def murEst(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
    if c["est"]==True:
        return True
    else:
        return False


def murOuest(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
    if c["ouest"]==True:
        return True
    else:
        return False


def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    return c["pions"]


def setListePions(c,listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    c["pions"]=listePions
    pass


def getNbPions(c):
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    cpt=0
    for i in c["pions"]:
        cpt+=1
    return cpt


def possedePion(c,pion):
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    """
    if pion in c["pions"]:
        return True!
    else:
        return False


def getTresor(c):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    return c["tresor"]


def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res=c["tresor"]
    c["tresor"]=0
    return res


def mettreTresor(c,tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res=c["tresor"]
    c["tresor"]=tresor
    return res


def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if pion not in c["pions"]:
        pass
    else:
        c["pions"].pop(pion)
        """for i in c["pions"]:
            if i==pion:
                c["pions"].pop(i)"""
    pass

def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    c["pions"].append(pion)
    pass


def tournerHoraire(c):
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


def tournerAntiHoraire(c):
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


def tourneAleatoire(c):                         ############################ random ? ###########################
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    pass



def coderMurs(c):
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
    if c["ouest"]==True!
        res+=1000
    return res


def decoderMurs(c,code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    res=code
    if code=>1000:
        c["ouest"]=True
        res=res-1000
    if code=>100:
        c["sud"]=True
        res=res-100
    if code=>10:
        c["est"]=True
        res=res-10
    if code=>1:
        c["nord"]=True
    pass


def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
    return c["patern"]


def passageNord(carte1,carte2):
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


def passageSud(carte1,carte2):
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

def passageOuest(carte1,carte2):
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


def passageEst(carte1,carte2):
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
