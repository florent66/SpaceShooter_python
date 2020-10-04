#!/usr/bin/python3 -u

import sys
from Tkinter import * 
from tkMessageBox import *
from PIL import ImageTk 
from PIL import Image 
from PIL import ImageFilter
from .decor import Decor
from .objVaisseau import Vaisseau
from .panda import Panda
import random
import time
from .moteurColision import set_Pause,get_Pause,dicoSon


class Moteur:
    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.title('Rafale 2')
        self.fenetre.rowconfigure(0, weight=1)
        self.fenetre.columnconfigure(0, weight=1)

        self.canvas = Canvas(self.fenetre, width=800, height=600, background='black')
        self.ImageTk = ImageTk
        self.canvas.focus_set()
        self.pause = self.canvas.create_text(-200, 200,text='PAUSE',fill='white',width='200')

        self.decor = Decor(self)
        self.vaisseau = Vaisseau(self,200)
        self.panda = Panda(self,200,300)
        self.panda2 = Panda(self,500,300)
        self.panda2 = Panda(self,100,200)
        self.panda2 = Panda(self,220,30)
        self.panda2 = Panda(self,600,100)
        self.panda2 = Panda(self,420,220)
        # self.vaisseau2 = Vaisseau(self,100)
        # self.vaisseau3 = Vaisseau(self,300)
        self.canvas.bind("<Key>", self.clavierPress)
        self.canvas.bind("<KeyRelease>", self.clavierRelache)

        # dicoSon['zik'].play()
        ###########################################################
        # logo = PhotoImage(file='assets/images/panda.png')
        # menubar = Menu(self.fenetre,bg='red')
        # menu1 = Menu(menubar, tearoff=0)
        # menu1.add_command(image=logo,command=self.alert,label="Creer")
        # menu1.add_command(label="Editer", command=self.alert)
        # menu1.add_separator()
        # menu1.add_command(label="Quitter", command=self.fenetre.quit)
        # menubar.add_cascade(label="Fichier", menu=menu1)

        # menu2 = Menu(menubar, tearoff=0)
        # menu2.add_command(label="Couper", command=self.alert)
        # menu2.add_command(label="Copier", command=self.alert)
        # menu2.add_command(label="Coller", command=self.alert)
        # menubar.add_cascade(label="Editer", menu=menu2)

        # menu3 = Menu(menubar, tearoff=0)
        # menu3.add_command(label="A propos", command=self.alert)
        # menubar.add_cascade(label="Aide", menu=menu3)

        # self.fenetre.config(menu=menubar)

        # self.fenetre.config(menu=menubar)
        # showinfo("alerte", "Bravo!")
        ###########################################################
        self.fenetre.mainloop()

    def clavierPress(self,event):
        etatPause = get_Pause()
        if etatPause == 'false':
            self.vaisseau.clavierPress(event)
        if event.keysym == 'p':
            if etatPause == 'false':
                set_Pause('true')
                self.canvas.coords(self.pause,200,200 )
            else:
                set_Pause('false')
                self.canvas.coords(self.pause,-200,200 )
        # self.vaisseau2.clavierPress(event)
        # self.vaisseau3.clavierPress(event)

    def clavierRelache(self,event):
        self.vaisseau.clavierRelache(event)
        # self.vaisseau2.clavierRelache(event)
        # self.vaisseau3.clavierRelache(event)

    def alert(self):
        print('alert')




