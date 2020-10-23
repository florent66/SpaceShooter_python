from PIL import ImageTk 
from PIL import Image 
from PIL import ImageFilter
from .dicoDynamique import *
import random
import time

class Explosion:
    def __init__(self,image):
        self.moteur = get_Moteur()
        self.x = -100
        self.y = 500
        self.x_speed = 0
        self.y_speed = 0
        self.imgExplosion= Image.open(image) 
        self.imgExplosion = self.imgExplosion.resize((int(random.uniform(2,10)),int(random.uniform(2,10))))
        self.tkimage = ImageTk.PhotoImage(self.imgExplosion) 
        self.obj= self.moteur.canvas.create_image(0,0,anchor='nw', image=self.tkimage)
        self.moteur.canvas.coords(self.obj,self.x, self.y)
        self.moteur.canvas.pack()
        self.position = []
        self.physique()

    def fire(self,x,y) :
        self.moteur.canvas.coords(self.obj,x,y)
        self.x_speed = random.uniform(-5,5) 
        self.y_speed = random.uniform(1,-6) 

    # def fireColision(self):
    #     if self.position[0] > 600:
    #         self.moteur.canvas.coords(self.obj,self.x, self.y)
    #         self.x_speed = 0
    #         self.y_speed = 0

    def physique(self):
        if get_Pause() == False:
            self.position = self.moteur.canvas.coords(self.obj)
            # self.fireColision()
            self.moteur.canvas.move(self.obj,self.x_speed,self.y_speed )
        self.moteur.fenetre.after(20,self.physique)