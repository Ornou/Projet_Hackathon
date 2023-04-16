from CityObject import *
from CityMap import CityMap
import tkinter as tk
from CityObject import CityObject
from Agent import Agent
magasins = [
    Magasin("Magasin1", (90, 215)),
    Magasin("Magasin2", (140, 80)),
    Magasin("Magasin3", (70, 130)),
    Magasin("Magasin4", (200, 30)),
    Magasin("Magasin5", (195, 170))
]

entrepots = [
    Entrepot("Entrepot1", (280, 200)),
    Entrepot("Entrepot2", (30, 30))
]

stations_recharge = [
    StationRecharge("Station1", (100, 30)),
    StationRecharge("Station2", (30, 170)),
    StationRecharge("Station3", (270, 70)),
    StationRecharge("Station4", (190, 280))
]


# Définir les dimensions de la carte et les positions des agents
WIDTH = 300
HEIGHT = 300


root = tk.Tk()


city_map = CityMap(root,WIDTH, HEIGHT)

for magasin in magasins:
    city_map.draw_magasin(magasin)

for entrepot in entrepots:
    city_map.draw_entrepot(entrepot)

for station in stations_recharge:
    city_map.draw_station(station)

agents = city_map.create_agents()
city_map.draw_agents(agents)


root.mainloop()
