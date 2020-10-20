## Fichier Tout faire une sorte glabal contenant les imformations a l 'instant "t" du jeu
from .dico import *
##Les Globals ici#######

##Dictionnaire des positions des objets
colisionMissile = {}
colisionPanda = {}
colisionVaisseau = {}

##Etat pause ou non
pause = False 
Moteur = 'rien'


####################################################################################
##Fonction qui analyse les collision entre les objets Missile/Panda
##Si collision on appel la methode miseAfire() des objects
def moteurMissilePanda():
    # global colisionMissile
    # global colisionPanda

    ##Traitement entre missile et panda
    for cle,valeur in colisionMissile.items():
        objMissile = cle
        objMissileVal = valeur
        for objPanda,objPandaVal in colisionPanda.items():
            if objMissileVal[0] < objPandaVal[0] + objPandaVal[2] and objMissileVal[0]+objMissileVal[2] > objPandaVal[0]:
                if objMissileVal[1] < objPandaVal[1] + objPandaVal[3] and objMissileVal[1]+objMissileVal[3] > objPandaVal[1]:
                    objMissile.miseAfire()
                    objPanda.miseAfire()
                    

    ##Traitement entre vaisseau et panda
    for cle,valeur in colisionPanda.items():
        objMissile = cle
        objMissileVal = valeur
        for objPanda,objPandaVal in colisionVaisseau.items():
            if objMissileVal[0] < objPandaVal[0] + objPandaVal[2] and objMissileVal[0]+objMissileVal[2] > objPandaVal[0]:
                if objMissileVal[1] < objPandaVal[1] + objPandaVal[3] and objMissileVal[1]+objMissileVal[3] > objPandaVal[1]:
                    Moteur.barreVie.baisse(0.1)
                    Moteur.barreVie.changeCouleur('green')



def AjoutcolisionPanda(obj,position,cage):
    global colisionPanda
    colisionPanda[obj] = position + cage

def AjoutcolisionMissile(obj,position,cage):
    global colisionMissile
    colisionMissile[obj] = position + cage
    ##Le moteur de colision est appele ici
    moteurMissilePanda()  

def AjoutcolisionVaisseau(obj,position,cage):
    global colisionVaisseau
    colisionVaisseau[obj] = position + cage
####################################################################################

## Getter Setter de l 'etat PAUSE
def get_Pause():
    global pause
    return pause

def set_Pause(actionPause):
    global pause
    pause = actionPause

## Getter Setter de l 'etat PAUSE
def get_Moteur():
    global Moteur
    return Moteur

def set_Moteur(moteur):
    print('setmoteur')
    global Moteur
    Moteur = moteur




                



