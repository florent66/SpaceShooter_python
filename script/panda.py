from PIL import ImageTk  
from PIL import Image 
from PIL import ImageFilter
import random
from .explosion import Explosion
from .dicoDynamique import *
from .dico  import *
import time
# from tkMessageBox import *
# from Tkinter import * 
##test premier commit

class Panda:
    def __init__(self,moteur,x,y):
        self.moteur = moteur
        self.cage = [30,30]
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
        self.imgPandaOrigine = D_IMAGE['panda']
        self.spritePanda = []
        #self.moteur.canvas.create_rectangle(self.x, self.y, self.x+self.cage[0], self.y+self.cage[1],fill='red')
        for i in range(0,360):
            self.imgPanda = self.imgPandaOrigine.resize((self.cage[0],self.cage[1]))
            self.imgPanda = self.imgPanda.rotate(i)
            self.tkimage = ImageTk.PhotoImage(self.imgPanda)
            self.spritePanda.append(self.tkimage)
 
        self.objPanda = self.moteur.canvas.create_image(0,0,anchor='nw', image=self.spritePanda[0])
        
        #self.moteur.canvas.itemconfigure(self.objPanda, state="hidden") #pour agir sur les options ici idden ou "normal"
        self.moteur.canvas.coords(self.objPanda,self.x, self.y)
        
        
        self.moteur.canvas.pack()
        self.position = []
        self.explosions = []
        self.nbExplosion = 5
        self.time = 0
        self.timeFire = 0
        self.angle = 0

        for i in range(0,self.nbExplosion):
            self.explosions.append(Explosion(self,self.moteur,"assets/images/panda.png"))

        self.physique()

    def fireColision(self):
        AjoutcolisionPanda(self,self.position,self.cage)
        deltaTime = self.time - self.timeFire 
        
        # if deltaTime > 0.01:
        self.angle += 4
        if self.angle > 359:
            self.angle = 0

        self.timeFire = time.time()
        self.moteur.canvas.itemconfigure(self.objPanda,image=self.spritePanda[self.angle]) 


    def miseAfire(self):
        # self.moteur.canvas.coords(self.objPanda,-200, 0)
        # self.moteur.canvas.delete(self.objPanda)
        # dicoSon['explosion'].play()
        self.moteur.canvas.pack()
        for u in range(0,self.nbExplosion):
            self.explosions[u].fire(self.position[0],self.position[1])

        self.moteur.canvas.itemconfigure(self.objPanda,image=self.spritePanda[220]) 

    def physique(self):
        self.time = time.time()
        if get_Pause() == False:
            self.position = self.moteur.canvas.coords(self.objPanda)
            self.fireColision()
            self.moteur.canvas.move(self.objPanda,0,0)
        self.moteur.fenetre.after(10,self.physique)