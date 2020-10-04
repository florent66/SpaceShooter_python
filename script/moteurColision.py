import pygame
from threading import Timer
# pygame.mixer.pre_init(frequency=44100)
# pygame.mixer.pre_init(44100,-16,2,2048)
pygame.mixer.init(22050, -16, 2, 64)
pygame.init()
# pygame.mixer.init(frequency=44100)

# print('colision')
dicoSon = {
    'tir' : pygame.mixer.Sound('assets/sons/tir.wav'),
    'explosion' : pygame.mixer.Sound('assets/sons/explosion.wav'),
    'zik' : pygame.mixer.Sound('assets/sons/zik.wav'),
}

colisionMissile = {}
colisionPanda = {}
colisionVaisseau = {}

pause = 'false'


def moteurMissilePanda():
    # print('colision')
    global colisionMissile
    global colisionPanda

    ##Traitement entre missile et panda
    for cle,valeur in colisionMissile.items():
        objMissile = cle
        objMissileVal = valeur
        for objPanda,objPandaVal in colisionPanda.items():
            if objMissileVal[0] < objPandaVal[0] + objPandaVal[2] and objMissileVal[0]+objMissileVal[2] > objPandaVal[0]:
                if objMissileVal[1] < objPandaVal[1] + objPandaVal[3]+10 and objMissileVal[1]+objMissileVal[3] > objPandaVal[1]:
                    objMissile.miseAfire()
                    objPanda.miseAfire()
            # else:
            #     print('------')

#     t = Timer(0.001, moteurMissilePanda)
#     t.start()

# moteurMissilePanda()


def AjoutcolisionPanda(obj,position,cage):
    global colisionPanda
    colisionPanda[obj] = position + cage

def AjoutcolisionMissile(obj,position,cage):
    global colisionMissile
    colisionMissile[obj] = position + cage
    moteurMissilePanda()

def AjoutcolisionVaisseau(obj,position):
    global colisionVaisseau
    colisionVaisseau[obj] = position




########################################################
def Pause():
    global pause
    pause = 'true'

def get_Pause():
    global pause
    return pause

def set_Pause(actionPause):
    global pause
    pause = actionPause



                



