
import tkinter as tk
from Agent import Agent
class CityMap:
    def __init__(self,root, width, height):
        self.width = width
        self.height = height
        self.map = [[0] * width for _ in range(height)]
        self.canvas = tk.Canvas(root, width=width, height=height)
        self.canvas.pack()
        self.agents=[]
        # Dessiner la carte
        for i in range(height):
            for j in range(width):
                x1 = j * 20
                y1 = i * 20
                x2 = x1 + 20
                y2 = y1 + 20
                
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
                
    def draw_magasin(self, magasin):
        self.canvas.create_oval(magasin.position[0]-20, magasin.position[1]-20, magasin.position[0]+20, magasin.position[1]+20, fill="green")
        
    def draw_entrepot(self, entrepot):
        self.canvas.create_rectangle(entrepot.position[0]-15, entrepot.position[1]-15, entrepot.position[0]+15, entrepot.position[1]+15, fill="red")
        
    def draw_station(self, station):
        self.canvas.create_rectangle(station.position[0]-18, station.position[1]-18, station.position[0]+18, station.position[1]+18, fill="blue")
    ####
    def create_agents(self):
        agent1 = Agent(60, 50, "yellow", self)
        agent2 = Agent(250, 250, "purple", self)
        self.agents.append(agent1)
        self.agents.append(agent2)
        return self.agents

    def draw_agents( self, agents):
        for agent in agents:
            agent.draw()
    
