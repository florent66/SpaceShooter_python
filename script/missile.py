from PIL import ImageTk 
from PIL import Image 
from PIL import ImageFilter
import random
from .explosion import Explosion
from .moteurColision import AjoutcolisionMissile
from .moteurColision import dicoSon
from .moteurColision import get_Pause

import time

nbExplosion = 5

class Missile:
    def __init__(self,vaisseau,moteur):
        global nbExplosion
        self.moteur = moteur
        self.papaVaisseau = vaisseau
        self.cage = [20,20]
        self.x = -100
        self.y = 550
        self.x_speed = 0
        self.y_speed = 0
        self.fireMove = 'False'
        self.fireOut = 'False'
        self.vitesseMax = 0
        

        self.imgMissile = Image.open("assets/images/missile.png") 
        self.imgMissile = self.imgMissile.resize((self.cage[0], self.cage[1]))
        self.tkimage = ImageTk.PhotoImage(self.imgMissile) 
        self.objMissile = moteur.canvas.create_image(0,0,anchor='nw', image=self.tkimage)
        self.moteur.canvas.coords(self.objMissile,self.x, self.y)
        # self.moteur.canvas.create_rectangle(self.x-50, self.y-50, self.x+50, self.y+50,fill='red')
        self.moteur.canvas.pack()
        self.position = []
        self.explosions = []
        self.nbExplosion = nbExplosion

        for i in range(0,self.nbExplosion):
            self.explosions.append(Explosion(self,self.moteur,"assets/images/explosion.png"))

        self.physique()

    def fire(self,x,y) :
        self.fireMove = 'True'
        self.moteur.canvas.coords(self.objMissile,x,y)
        self.vitesseMax=20

    def fireColision(self):
        AjoutcolisionMissile(self,self.position,self.cage)
        if self.position[1] < 0:
            self.fireMove = 'False'
            self.vitesseMax=0
            self.moteur.canvas.coords(self.objMissile,self.x, self.y)

        # if self.position[1] < 50:
        #     self.miseAfire()
        #     self.moteur.canvas.coords(self.objMissile,self.x, self.y)

    def miseAfire(self):
        self.fireMove = 'False'
        self.vitesseMax=0
        self.moteur.canvas.coords(self.objMissile,self.x, self.y)
        # dicoSon['explosion'].play()
        for u in range(0,self.nbExplosion):
            self.explosions[u].fire(self.position[0],self.position[1])  

    def physique(self):
        if get_Pause() == 'false':
            self.position = self.moteur.canvas.coords(self.objMissile)
            self.fireColision()
            self.moteur.canvas.move(self.objMissile,0,-self.vitesseMax)
        self.moteur.fenetre.after(20,self.physique)