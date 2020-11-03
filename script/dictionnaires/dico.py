import pygame
from PIL import Image
# from .moteur import Moteur

# D_Moteur = Moteur ## the moteur mis à disposition
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
global Moteur



D_NOM_JEU = "Rafale 2"
D_VIE = 100

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
    'background' : Image.open("assets/images/decor.jpg"),
    'panda' : Image.open("assets/images/panda.png"),
    'mode1' : Image.open("assets/images/mode1.png"),
    'barreVie' : Image.open("assets/images/barrevie.png")
}

D_SPRITE_FLAMME = {
    '0' : Image.open("assets/images/sprite_Flamme/flamme_1.png"),
    '1' : Image.open("assets/images/sprite_Flamme/flamme_2.png"),
    '2' : Image.open("assets/images/sprite_Flamme/flamme_3.png"),
    '3' : Image.open("assets/images/sprite_Flamme/flamme_4.png")
}

##Conf vaisseau
D_CONF_VAISSEAU = {
    'id' : 'vaisseau',
    'vie' : 2,
    'image' : Image.open("assets/images/vaisseau.png"),
    'imgModeSpeed' : Image.open("assets/images/mode1.png"),
    'timeRefresh' : 10,
    'vTraine' : .3,
    'vRecentrageH' : .2,
    'vRecentrageB' : .8,
    'timeDeltaTir' : 0.1,
    'nbMissile' : 10,
    'toucheGauche' : 's',
    'toucheDroite' : 'f',
    'toucheTir' : 'l',
    'toucheSpace' : 'space',
    'cage' : [45,45],
    'missiles' : {'basic':[],'best':[]},
    'modelMissile' : 'best',
    'nbExplosion' : 5,
    'imgExplosion' : "assets/images/explosion.png",
    'D_SPRITE_FLAMME' : {
        '0' : Image.open("assets/images/sprite_Flamme/flamme_1.png"),
        '1' : Image.open("assets/images/sprite_Flamme/flamme_2.png"),
        '2' : Image.open("assets/images/sprite_Flamme/flamme_3.png"),
        '3' : Image.open("assets/images/sprite_Flamme/flamme_4.png")
    },
    'D_ANIMATION' : {
        'repos' : [-200,-10000,200,200],
        '1' : [-200,-10000,200,200]
    }
}

D_CONF_PANDA = {
    'id' : 'panda',
    'vie' : 100,
    'image' : Image.open("assets/images/panda.png"),
    'imgModeSpeed' : Image.open("assets/images/mode1.png"),
    'timeRefresh' : 10,
    'vTraine' : .3,
    'vRecentrageH' : .2,
    'vRecentrageB' : .8,
    'timeDeltaTir' : 0.1,
    'nbMissile' : 10,
    'toucheGauche' : 's',
    'toucheDroite' : 'f',
    'toucheTir' : 'l',
    'toucheSpace' : 'space',
    'cage' : [45,45],
    'missiles' : {'basic':[],'best':[]},
    'modelMissile' : 'best',
    'nbExplosion' : 5,
    'imgExplosion' : "assets/images/panda.png",
    'D_SPRITE_FLAMME' : {
        '0' : Image.open("assets/images/sprite_Flamme/flamme_1.png"),
        '1' : Image.open("assets/images/sprite_Flamme/flamme_2.png"),
        '2' : Image.open("assets/images/sprite_Flamme/flamme_3.png"),
        '3' : Image.open("assets/images/sprite_Flamme/flamme_4.png")
    },
    'D_ANIMATION' : {
        'repos' : [-200,200,200,200],
        '1' : [-200,200,200,200],
        '2' : [420,-100,200,50],
        '3' : [620,-150,300,200],
        '4' : [-100,-150,30,30],
    }
}

D_CONF_MISSILE = {
    'nbEplosion' : 5,
}

D_OBJ_MISSILE_1 = {
    'id' : 'missile_classic',
    'vie' : 2,
    'image' : Image.open("assets/images/missile.png"),
    'imgExplosion' : "assets/images/explosion.png",
    'nbExplosion' : 5,
    'speed' : 15,
    'cage' : [20,20],
    'deltaTir' : 0.1,
    'D_ANIMATION' : {
        'repos' : [-200,-500,200,200],
        '1' : [-200,-500,200,200]
    }
}

D_OBJ_MISSILE_2 = {
    'id' : 'missile_best',
    'vie' : 2,
    'image' : Image.open("assets/images/missile2.png"),
    'imgExplosion' : "assets/images/explosion.png",
    'nbExplosion' : 15,
    'speed' : 5,
    'cage' : [70,40],
    'deltaTir' : 0.5,
    'D_ANIMATION' : {
        'repos' : [-200,-500,200,200],
        '1' : [-200,-500,200,200]
    }
}

D_OBJ_EXPLOSION = {
    'id' : 'explosion',
    'vie' : 2,
    'image' : Image.open("assets/images/missile2.png"),
    'imgExplosion' : "assets/images/explosion.png",
    'nbExplosion' : 15,
    'speed' : 5,
    'cage' : [70,40],
    'deltaTir' : 0.5,
    'D_ANIMATION' : {
        'repos' : [-200,-700,200,200],
        '1' : [-200,-700,200,200]
    }
}

