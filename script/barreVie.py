class BarreVie():
    def __init__(self,moteur,x,y,vie):
        self.moteur = moteur
        self.x = x
        self.y = y
        self.vie = vie
        self.vieSize= vie*1.5
        self.objBarreVie = self.moteur.canvas.create_rectangle(self.x, self.y, self.x+self.vieSize, self.y+10,fill='red')
