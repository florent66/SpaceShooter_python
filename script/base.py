from .dictionnaires.dicoDynamique import *
from .dictionnaires.dico import *
import time
import random

class Base:
    def __init__(self,obj,x,y,D_OBJ_X):
        self.id = D_OBJ_X['id']
        self.obj = obj
        self.vie = D_OBJ_X['vie']
        self.D_OBJ_X = D_OBJ_X
        self.vieSize= self.vie/3
        self.x = x
        self.y = y
        self.xOUT = -500
        self.yOUT = -500
        self.x_speed = 0
        self.y_speed = 0
        self.x_acc = 0
        self.y_acc = 0
        self.vitesseMax = 0
        self.time = 0
        self.angle = 0
        self.timeFire = 0
        self.fireMove = False
        self.fireOut = False
        self.position = [0,0]
        self.startAnime = 0 #position de depart animation
        self.endAnime = 0 #position de fin animation


        self.numAnimation = D_OBJ_X['D_ANIMATION']
        self.lenAnimation = len(self.numAnimation)-1
        self.indexAnimation = 1
        self.timeChangeAnimation = 3 #on change d 'animation toute les x secondes
        self.timeStartAnimation = self.time #on change d 'animation toute les x secondes

        # try:
        #     self.numAnimation = D_OBJ_X['D_ANIMATION']
        # except:
        #     self.numAnimation = False


       
        self.moteur.canvas.coords(self.obj,self.x, self.y)

        ##creation barre de vie pour chaque obj
        if self.id == 'panda':
            self.objBarreVie = self.moteur.canvas.create_rectangle(self.x, self.y, self.x+self.vieSize, self.y + 5,fill='red')


        self.moteur.canvas.pack()
        self.refresh()

    def refresh(self):
        if get_Pause() == False:
            self.vieSize= self.vie/3
            
            self.time = time.time()
            self.pilotageAutomatique()
            self.position = self.moteur.canvas.coords(self.obj)
            self.colision()
            
            self.refreshObj()
        self.moteur.fenetre.after(20,self.refresh)


    def pilotageAutomatique(self):
        # print (self.id)
        if self.id == 'panda':
            deltaTime = self.time - self.timeStartAnimation
            # print(deltaTime)
            if (deltaTime > 10):
                # print('changement')
                self.indexAnimation = round(random.uniform(1,self.lenAnimation))
                self.timeStartAnimation = self.time

            self.moteur.canvas.coords(self.objBarreVie,self.position[0], self.position[1], self.position[0]+self.vieSize, self.position[1] + 5)
            # print (self.id)
            # print (self.numAnimation)
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

            if (self.position[0] < self.numAnimation[str(self.indexAnimation)][2]):
                self.x_acc = 0.2
            if (self.position[0] > self.numAnimation[str(self.indexAnimation)][2]):
                self.x_acc = -.2
            if (self.position[1] < self.numAnimation[str(self.indexAnimation)][3]):
                self.y_acc = .3
            if (self.position[1] > self.numAnimation[str(self.indexAnimation)][3]):
                self.y_acc = -.3
                
            self.y_speed = self.y_speed + self.y_acc  + resitanceY
            self.x_speed = self.x_speed + self.x_acc + resitanceX
            
            self.moteur.canvas.move(self.obj,self.x_speed,self.y_speed)
            
        else:
            self.moteur.canvas.move(self.obj,self.x_speed,self.y_speed)

    def refreshObj(self):
        pass

    def colision(self):
        pass

