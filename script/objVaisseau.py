from PIL import ImageTk 
from PIL import Image 
from PIL import ImageFilter
from .missile import Missile
from .moteurColision import dicoSon
import random
import time

class Vaisseau:
    def __init__(self,moteur,x):
        
        self.moteur = moteur
        self.x = x
        self.y = 500
        self.vitesseMax = 6
        self.x_speed = 0
        self.y_speed = 0
        self.touche_S = 'relache'
        self.touche_F = 'relache'
        self.imgVaisseau = Image.open("assets/images/vaisseau.png") 
        self.imgVaisseau = self.imgVaisseau.rotate(180)
        self.imgVaisseau = self.imgVaisseau.resize((45, 45))
        self.tkimage = ImageTk.PhotoImage(self.imgVaisseau) 
        self.objVaisseau = moteur.canvas.create_image(0,0,anchor='nw', image=self.tkimage)
        self.moteur.canvas.coords(self.objVaisseau,self.x, self.y)
        self.moteur.canvas.pack()
        self.position = []
        self.missiles = []
        self.nbMissile = 10
        self.posChargeur = 0
        self.touchGachete = 'False'
        self.readyGachete = 'True'
        self.time = 0
        self.timeFire = 0

        for i in range(0,self.nbMissile):
            self.missiles.append(Missile(self,self.moteur))

        self.physique()


    def clavierPress(self,event):
        self.touche = event.keysym
        if self.touche == 's':
            self.touche_S = 'push'
            self.x_speed = -self.vitesseMax

        if self.touche == 'f':
            self.touche_F = 'push'
            self.x_speed = self.vitesseMax

        if self.touche == 'c':
            self.touchGachete = 'True'

    def clavierRelache(self,event):
        self.touche = event.keysym
        
        if self.touche == 's':
            self.touche_S = 'relache'
        
        if self.touche == 'f':
            self.touche_F = 'relache'

        if self.touche == 'c':
            self.touchGachete = 'False'

    def traine(self):
        if self.touche_F == 'relache' and self.touche_S == 'relache':
            if self.x_speed > 0:
                self.x_speed = self.x_speed-0.7
            if self.x_speed < 0:
                self.x_speed = self.x_speed+0.7

        if (self.x_speed < 1 and self.x_speed > 0) or (self.x_speed > -1 and self.x_speed < 0) :
            self.x_speed = 0

        if self.position[1] > self.y:
            self.y_speed = -.2
        else:
            self.y_speed = 0

    def miseAfire(self):
        deltaTime = self.time - self.timeFire 
        if self.touchGachete == 'True' and deltaTime > 0.1:
            if self.missiles[self.posChargeur].fireMove == 'False' and self.missiles[self.posChargeur].fireOut == 'False':
                dicoSon['tir'].play()
                self.y_speed = 3
                self.missiles[self.posChargeur].fire(self.position[0]+12,self.position[1])
                self.timeFire = time.time()
                self.posChargeur = self.posChargeur+1
                if self.posChargeur == self.nbMissile:
                    self.posChargeur = 0


    def physique(self):
        self.time = time.time()
        self.position = self.moteur.canvas.coords(self.objVaisseau)
        self.traine()
        self.miseAfire()
        self.moteur.canvas.move(self.objVaisseau,self.x_speed,self.y_speed)

        self.moteur.fenetre.after(10,self.physique)

