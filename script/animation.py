

class Animation():
    def __init__(self,objParent,sprite,vitesse,xy):
        self.moteur = objParent.moteur
        self.objParent = objParent
        self.spriteAnimation = sprite
        self.vitesse = vitesse
        self.posFrame = 0
        self.objAnimation = self.moteur.canvas.create_image(xy,anchor='nw', image=self.spriteAnimation[self.posFrame])
        self.angle = 0
        
    def runCyclique(self,position):
        if self.posFrame > 2:
            self.posFrame = 0

        self.moteur.canvas.itemconfigure(self.objAnimation,image=self.spriteAnimation[self.posFrame])
        self.moteur.canvas.coords(self.objAnimation,position[0]+13,position[1]+40)
        self.posFrame += 1

    def rotationDroite(self,vitesse):
        self.angle += vitesse
        if self.angle > 359:
            self.angle = 0

        self.moteur.canvas.itemconfigure(self.objAnimation,image=self.spriteAnimation[self.angle])

    def display(self,modeAffichage):
        if modeAffichage == True:
            self.moteur.canvas.itemconfigure(self.objAnimation, state="normal")

        if modeAffichage == False:
            self.moteur.canvas.itemconfigure(self.objAnimation, state="hidden")


    def refreshPosition(self,positionx,positiony):
        self.moteur.canvas.coords(self.objAnimation,positionx,positiony)

    def move(self,x,y):
        self.moteur.canvas.move(self.objAnimation,x,y)

    def getCoords(self):
        return self.moteur.canvas.coords(self.objAnimation)

    def setCoords(self,x,y):
        self.moteur.canvas.coords(self.objAnimation,x,y)

