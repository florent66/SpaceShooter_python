from PIL import ImageTk
from .dico import *
from .dicoDynamique import *


class BarreVie():
    def __init__(self):
        print('moteur')
        self.moteur = get_Moteur()
        self.x = 700
        self.y = 45
        self.vie = D_VIE
        self.epaisseurVie = 16
        self.couleur = 'green'
        self.vieSize= self.vie/1.1
        self.objBarreVie = self.moteur.canvas.create_rectangle(self.x, self.y, self.x+self.vieSize, self.y + self.epaisseurVie,fill='red')
        ##Creation decoration barre de vie
        self.imgDecoBarre = D_IMAGE['barreVie'] 
        self.imgDecoBarre = self.imgDecoBarre.resize((175,75))
        self.tkimage = ImageTk.PhotoImage(self.imgDecoBarre) 
        self.objDecoBarre = self.moteur.canvas.create_image(0,0,anchor='nw', image=self.tkimage)
        self.moteur.canvas.coords(self.objDecoBarre,self.x-80, self.y-33)

    def baisse(self,dommage):
        self.vie = self.vie - dommage
        self.vieSize= self.vie/1.1
        self.moteur.canvas.coords(self.objBarreVie,self.x, self.y, self.x+self.vieSize, self.y + self.epaisseurVie)
        # self.objBarreVie = self.moteur.canvas.create_rectangle(self.x, self.y, self.x+self.vieSize, self.y+50,fill='red')

    # def physique(self):
    #     # self.moteur.canvas.move(self.objBarreVie,self.x+self.vieSize, 0)
        
    #     self.moteur.fenetre.after(100,self.physique)
    def changeCouleur(self,couleur):
        self.couleur = couleur
        self.moteur.canvas.itemconfigure(self.objBarreVie,fill=couleur) 


