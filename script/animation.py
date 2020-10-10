

class Animation():
    def __init__(self,objParent,sprite,vitesse):
        self.moteur = objParent.moteur
        self.objParent = objParent
        self.sprite = sprite
        self.vitesse = vitesse
        self.posFrame = 0
        self.objAnimation = self.moteur.canvas.create_image(-200,0,anchor='nw', image=self.sprite[self.posFrame])
        
    def runCyclique(self,position):
        if self.posFrame > 2:
            self.posFrame = 0

        self.moteur.canvas.itemconfigure(self.objAnimation,image=self.sprite[self.posFrame])
        self.moteur.canvas.coords(self.objAnimation,position[0]+13,position[1]+40)
        self.posFrame += 1


