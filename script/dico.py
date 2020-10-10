import pygame
from PIL import Image
##On prepare bien le mixer sinon il y a des plantages
pygame.mixer.pre_init(44100,-16,2,2048)
pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)
pygame.mixer.pre_init(44100,-16,2,2048)
pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)
pygame.mixer.pre_init(44100,-16,2,2048)
pygame.init()
pygame.init()
pygame.init()
#une derniere
pygame.init()

pygame.mixer.init(44100, -16, 2, 2048)


D_NOM_JEU = "Rafale 2"

D_SIZE_CANVAS = {
    'largeur' : 800,
    'hauteur' : 600
}

D_POSITION_INIT = [-200,-200]

D_AUDIO = {
    'tir' : pygame.mixer.Sound('assets/sons/tir.wav'),
    'explosion' : pygame.mixer.Sound('assets/sons/explosion.wav'),
    'zik' : pygame.mixer.Sound('assets/sons/zik.ogg')
}

D_IMAGE = {
    'vaisseau' : Image.open("assets/images/vaisseau.png"),
    'background' : Image.open("assets/images/decor.jpg"),
    'panda' : Image.open("assets/images/panda.png")
}

D_SPRITE_FLAMME = {
    '0' : Image.open("assets/images/sprite_Flamme/flamme_1.png"),
    '1' : Image.open("assets/images/sprite_Flamme/flamme_2.png"),
    '2' : Image.open("assets/images/sprite_Flamme/flamme_3.png"),
    '3' : Image.open("assets/images/sprite_Flamme/flamme_4.png")
}

##Conf vaisseau
D_CONF_VAISSEAU = {
    'timeRefresh' : 10,
    'vTraine' : .3,
    'vRecentrageH' : .2,
    'vRecentrageB' : .8,
    'timeDeltaTir' : 0.1,
    'nbMissile' : 15,
    'toucheGauche' : 's',
    'toucheDroite' : 'f',
    'toucheTir' : 'l',
    'toucheSpace' : 'space'
}

D_CONF_MISSILE = {
    'nbEplosion' : 5,
}