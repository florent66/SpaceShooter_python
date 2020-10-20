#!/usr/bin/python3 -u

# -Le but de ce fichier est d'importer les principaux modules
# -Le moteur Tkinter ne prend pas en compte les interractions exterieurs

import sys
from tkinter import * 
from PIL import ImageTk 
from PIL import Image 
from PIL import ImageFilter
from .decor import Decor
from .objVaisseau import Vaisseau
from .panda import Panda
from .barreVie import BarreVie
import random
import time
from .dicoDynamique import *
from .dico import * ##D_


class Moteur:
    def __init__(self):
        set_Moteur(self) ## on rend le moteur dispo partout
        self.fenetre = Tk()
        self.fenetre.title(D_NOM_JEU)
        self.fenetre.rowconfigure(0, weight=1)
        self.fenetre.columnconfigure(0, weight=1)
        self.canvas = Canvas(self.fenetre, width=D_SIZE_CANVAS['largeur'], height=D_SIZE_CANVAS['hauteur'], background='black')
        self.ImageTk = ImageTk
        self.canvas.focus_set()
        

        ##Generation des objets tKinter
        self.creationObjets()

        ##Ecouteurs clavier press et relache
        self.canvas.bind("<Key>", self.clavierPress)
        self.canvas.bind("<KeyRelease>", self.clavierRelache)
    
        self.fenetre.mainloop()
        ## On ne peux plus rien faire au dela Tout est defini dans la construction
        ##########################################################################
        ##########################################################################
    
    ##Intentiation de tous les objets Tkinter
    def creationObjets(self):
        self.decor = Decor(self)
        # self.vaisseau2 = Vaisseau(self,100)
        # self.vaisseau3 = Vaisseau(self,300)
        self.panda = Panda(200,100,[45,45])
        self.panda2 = Panda(500,300,[45,45])
        # self.panda2 = Panda(self,100,200,[45,45])
        # self.panda2 = Panda(self,220,30,[45,45])
        # self.panda2 = Panda(self,480,110,[45,45])
        # self.panda2 = Panda(self,420,220,[45,45])
        # self.panda2 = Panda(self,546,199,[45,45])
        # self.panda2 = Panda(self,545,220,[45,45])
        # self.panda2 = Panda(self,100,175,[45,45])
        # self.panda2 = Panda(self,420,220,[45,45])
        # self.panda2 = Panda(self,22,354,[45,45])
        # self.panda2 = Panda(self,35,220,[55,45])

        self.vaisseau = Vaisseau(200)
        self.barreVie = BarreVie ()

        self.pause = self.canvas.create_text(D_POSITION_INIT,text='PAUSE',fill='white',width='200')
        # D_AUDIO['zik'].play()

    def clavierPress(self,event):
        
        etatPause = get_Pause()
        if etatPause == False:
            self.vaisseau.clavierPress(event)
        if event.keysym == 'p':
            if etatPause == False:
                set_Pause(True)
                self.canvas.coords(self.pause,200,200 )
            else:
                set_Pause(False)
                self.canvas.coords(self.pause,-200,-200 )
        # self.vaisseau2.clavierPress(event)
        # self.vaisseau3.clavierPress(event)

    def clavierRelache(self,event):
        self.vaisseau.clavierRelache(event)
        # self.vaisseau2.clavierRelache(event)
        # self.vaisseau3.clavierRelache(event)

    def alert(self):
        print('alert')




