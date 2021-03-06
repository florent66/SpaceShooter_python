from PIL import ImageTk 
import random
import time

from ..projectiles.missile import Missile
from ..effects.animation import Animation
from ..dictionnaires.dico import *
from ..dictionnaires.dicoDynamique import *
from ..base import Base
from ..explosionPhysique import ExplosionPhysique


class Vaisseau(Base,ExplosionPhysique):
    def __init__(self,x):
        self.moteur = get_Moteur()

        ##Initialisation des variables
        self.cage = D_CONF_VAISSEAU['cage']
        self.position_zone = True
        self.touche_G = 'RELACHE'
        self.touche_D = 'RELACHE'
        self.touche_SPACE = 'RELACHE'
        self.missiles = D_CONF_VAISSEAU['missiles']
        self.posChargeur = 0
        self.touchGachete = False
        self.readyGachete = True
        self.modelMissile = D_CONF_VAISSEAU['modelMissile']

        #############TODO###########################################
        ##Creation la flamme (sprite)
        self.spriteFlamme = []
        #self.moteur.canvas.create_rectangle(self.x, self.y, self.x+self.cage[0], self.y+self.cage[1],fill='red')
        for i in range(1,4):
            self.imgFlammeOrigine = D_CONF_VAISSEAU['D_SPRITE_FLAMME'][str(i)]
            self.imgFlamme = self.imgFlammeOrigine.resize((20,self.cage[1]))
            self.tkimageFlamme = ImageTk.PhotoImage(self.imgFlamme)
            self.spriteFlamme.append(self.tkimageFlamme)

        self.flammeAnimation = Animation(self,self.spriteFlamme,10,[0,0])
        
        #########################################################
        # ##Creation mode1
        # self.imgMode1 = D_IMAGE['mode1'] 
        # self.imgimgMode1 = self.imgMode1.resize((self.cage[0]*3,self.cage[1]*3))
        # self.tkimage2 = ImageTk.PhotoImage(self.imgimgMode1) 
        # self.objimgMode1 = moteur.canvas.create_image(0,0,anchor='nw', image=self.tkimage2)
        # self.moteur.canvas.coords(self.objimgMode1,self.x, self.y)

        #############TODO###########################################
        ##Creation mode1 (sprite) on tourne à 360
        self.spriteMode1 = []
        for i in range(0,360):
            self.imgmode1Origine = D_CONF_VAISSEAU['imgModeSpeed']
            self.imgmode1 = self.imgmode1Origine.resize((self.cage[0]*3,self.cage[1]*3))
            self.imgmode1 = self.imgmode1.rotate(i)
            self.tkimage = ImageTk.PhotoImage(self.imgmode1)
            self.spriteMode1.append(self.tkimage)

        self.mode1Animation = Animation(self,self.spriteMode1,10,[0,0])
        
        #########################################################
        ##Creation vaisseau
        self.imgVaisseau = D_CONF_VAISSEAU['image']
        self.imgVaisseau = self.imgVaisseau.rotate(180)
        self.imgVaisseau = self.imgVaisseau.resize((self.cage[0],self.cage[1]))
        self.tkimage = ImageTk.PhotoImage(self.imgVaisseau) 
        self.obj = self.moteur.canvas.create_image(0,0,anchor='nw', image=self.tkimage)

        self.loadMissile()

        Base.__init__(self,self.obj,x,500,D_CONF_VAISSEAU)
        ExplosionPhysique.__init__(self,D_CONF_VAISSEAU)

        self.refresh() #on double le refresh

    def loadMissile(self):
            for i in range(0,D_CONF_VAISSEAU['nbMissile']):
                self.missiles['basic'].append(Missile(D_OBJ_MISSILE_1))
                self.missiles['best'].append(Missile(D_OBJ_MISSILE_2))

    def clavierPress(self,event):
        self.touche = event.keysym
        if self.touche == D_CONF_VAISSEAU['toucheGauche']:
            self.touche_G = 'PUSH'   

        if self.touche == D_CONF_VAISSEAU['toucheDroite']:
            self.touche_D = 'PUSH'

        if self.touche == D_CONF_VAISSEAU['toucheSpace']:
            self.touche_SPACE = 'PUSH'
            

        if self.touche == D_CONF_VAISSEAU['toucheTir']:
            self.touchGachete = True

    def clavierRelache(self,event):
        self.touche = event.keysym
        if self.touche == D_CONF_VAISSEAU['toucheGauche']:
            self.touche_G = 'RELACHE'
        
        if self.touche == D_CONF_VAISSEAU['toucheDroite']:
            self.touche_D = 'RELACHE'

        if self.touche == D_CONF_VAISSEAU['toucheSpace']:
            self.touche_SPACE = 'RELACHE'

        if self.touche == D_CONF_VAISSEAU['toucheTir']:
            self.touchGachete = False

    def physique(self):
        ##on calcul et controle la resistance de frottement si une des vitesses est a 0
        ## car pb 0/x :)
        if self.x_speed == 0:
            resitanceX = 0
        else:
            if self.x_speed > 0:
                resitanceX = -(self.x_speed/15)**2
            else:
                resitanceX = (self.x_speed/15)**2

        if self.y_speed == 0:
            resitanceY = 0
        else:
            if self.y_speed > 0:
                resitanceY = -(self.y_speed/10)**2
            else:
                resitanceY = (self.y_speed/10)**2


        ##On ajoute prend compte l 'acceleration et la traine meme dans l'espace
        if self.touche_G == 'PUSH':
            self.x_acc = -.2
            if self.touche_SPACE == 'PUSH':
                self.x_acc = -.5

        if self.touche_D == 'PUSH':
            self.x_acc = .2
            if self.touche_SPACE == 'PUSH':
                self.x_acc = .5

        if self.touche_SPACE == 'PUSH':
            self.y_acc = -0.12

        ##On passe un coup de freinage constant sur l 'axe x si on relache les touches
        if self.touche_D == 'RELACHE' and self.touche_G == 'RELACHE':
            self.x_acc = 0
            if self.x_speed > 0:
                self.x_speed = self.x_speed-D_CONF_VAISSEAU['vTraine']
            if self.x_speed < 0:
                self.x_speed = self.x_speed+D_CONF_VAISSEAU['vTraine']

            #On stabilise a 0 si resudu de vitesse 
            if (self.x_speed < .5 and self.x_speed > 0) or (self.x_speed > -.5 and self.x_speed < 0) :
                self.x_speed = 0


        ##On si trop haut ou trop bas dans la zone initial##
        if self.position[1] > self.y and self.touche_SPACE == 'RELACHE':
            self.y_acc = -0.02
        
        if self.position[1] < self.y and self.touche_SPACE == 'RELACHE':  
            self.y_acc = 0.05

        ##Dans la zone y est ou pas ?##
        if self.position[1] < self.y + 5 and self.position[1] > self.y - 5:
            self.position_zone = True ## on est dans la zoneY pour stabiliser
        else:
            self.position_zone = False


        ##Application des accelerations et traine dans l'espace !!
        self.y_speed = self.y_speed + self.y_acc  + resitanceY
        self.x_speed = self.x_speed + self.x_acc + resitanceX


        if self.position_zone and ((self.y_speed < .1 and self.y_speed > 0) or (self.y_speed > -.1 and self.y_speed < 0)):
            self.y_acc = 0
            self.y_speed = 0


    def miseAfire(self):
        deltaTime = self.time - self.timeFire 
        try:
            objMissile = self.missiles[self.modelMissile][self.posChargeur]
        except:
            pass
        
        if self.touchGachete and deltaTime > objMissile.D_OBJ_MISSILE_X['deltaTir']:  
            if objMissile.fireMove == False and objMissile.fireOut == False:
                # D_AUDIO['tir'].play()
                correctionPosMissile = (self.cage[0] - objMissile.D_OBJ_MISSILE_X['cage'][0])/2
                self.y_speed = self.y_speed + 0.2
                self.y_acc = .8
                objMissile.fire(self.position[0]+correctionPosMissile,self.position[1])
                self.timeFire = time.time()
                self.posChargeur = self.posChargeur+1
                if self.posChargeur == D_CONF_VAISSEAU['nbMissile']:
                    self.posChargeur = 0

    def gestionAnimation(self):
        if (self.touche_SPACE == 'PUSH'):
            self.mode1Animation.display(True)
            self.mode1Animation.rotationDroite(45)
        else:
            self.mode1Animation.display(False)

        self.flammeAnimation.runCyclique(self.position)
        self.mode1Animation.refreshPosition(self.position[0]-45,self.position[1]-42)


    def refreshObj(self):
        self.gestionAnimation()
        self.physique()
        self.miseAfire()
        AjoutcolisionVaisseau(self,self.position,self.cage)
        
