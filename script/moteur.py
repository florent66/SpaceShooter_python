#!/usr/bin/python3 -u

import sys
from Tkinter import * 
from PIL import ImageTk 
from PIL import Image 
from PIL import ImageFilter
from .objVaisseau import Vaisseau
from .panda import Panda
import random
import time
from .moteurColision import set_Pause,get_Pause,dicoSon




# for line in sys.stdin:
#     print('dddd'+line)
#     fichier = open("data.txt", "a")
#     fichier.write(line)
#     fichier.close()
# print('oki')
# premiereChaine = input("Veuillez saisir un nombre : ")
# secondeChaine = input("Veuillez saisir un autre nombre : ")

# a = float(premiereChaine)
# b = float(secondeChaine)

# print("a + b = ", a + b)
# print("a - b = ", a - b)
# print("a * b = ", a * b)
# print("a / b = ", a / b)


# from playsound import playsound

# playsound('zik.mp3')
# wave.open("./zik.mp3","r") 
# playsound.playsound('zik.mp3', True)
# import http.server
 
# PORT = 8080
# server_address = ("", PORT)

# server = http.server.HTTPServer
# handler = http.server.CGIHTTPRequestHandler
# handler.cgi_directories = ["/"]
# print("Serveur actif sur le port :", PORT)

# httpd = server(server_address, handler)
# httpd.serve_forever()
##creation class vaisseau


class Moteur:
    def __init__(self):
        self.fenetre = Tk()
        self.canvas = Canvas(self.fenetre, width=800, height=600, background='black')
        self.ImageTk = ImageTk
        self.canvas.pack()
        self.canvas.focus_set()
        self.pause = self.canvas.create_text(-200, 200,text='PAUSE',fill='white',width='200')
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

########"A GARDER##############"

# def start():
#     global x
#     canvas.move(image,x,.1)
#     fenetre.after(1,start)

# def bouge(mouvement):
#         global x
#         x = mouvement


# def clavier(event):
#     touche = event.keysym
    
#     print(touche)
#     if touche == 's':
#         start()

#     ## vaisseau x-1
#     if touche == 'w':
#         bouge(-1)
#         ajoutobj(canvas)

#     ## vaisseau x+1
#     if touche == 'n':
#         bouge(1)
# #######################################################################
# fenetre = Tk()
# canvas = Canvas(fenetre, width=800, height=600, background='yellow')

# ##les label
# label = Label(fenetre, text="Hello World")
# label.pack()
# bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
# bouton.pack()

# ligne1 = canvas.create_line(75, 0, 75, 120)
# ligne2 = canvas.create_line(0, 60, 150, 60)
# txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")

# ##Creation background
# photo = PhotoImage(file="space.png")
# image = canvas.create_image(0,-200,anchor=NW, image=photo)
# canvas.focus_set()
# canvas.bind("<Key>", clavier)
# canvas.pack()

# ##creation vaisseau


# objVaisseau = []
# for i in range(0,10):
#   objVaisseau.append(Vaisseau())


# fenetre.mainloop()
######################################################################

            



