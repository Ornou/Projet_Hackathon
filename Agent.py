import heapq
from math import sqrt

class Agent:
    def __init__(self, x, y,color,city_map):
        self.x = x
        self.y = y
        self.battery = 100
        self.color = color
        self.city_map = city_map
    def draw(self):
        size = 10
        points = [
            self.x - size, self.y + size,
            self.x + size, self.y + size,
            self.x, self.y - size,
            ]
        self.city_map.canvas.create_polygon(points, fill=self.color)

    def run(self):
        while True:
            if self.battery <= 0:
                self.city_map.agents.remove(self)
                break
            if self.current_task is None:
                task = self.choose_task()
                if task is not None:
                    self.current_task = task
                    task.status = "in progress"
            else:
                self.complete_task()

            if self.battery <= 30:
                self.check_recharge_station()

            self.draw()
            self.city_map.canvas.update()
            
    def move(self, dx, dy):
    # Déplacer l'agent de dx sur l'axe des x et dy sur l'axe des y
        new_x = self.x + dx
        new_y = self.y + dy

    # Vérifier si les nouvelles coordonnées sont dans les limites de la carte
        if new_x >= 0 and new_x < self.city_map.width and new_y >= 0 and new_y < self.city_map.height:
            self.x = new_x
            self.y = new_y
            self.update_battery(dx, dy)

    def move_to_destination(self, x, y):
    # Déterminer le chemin le plus court vers la destination en utilisant l'algorithme A*
        start_node = (x, y)
        goal_node = (self.x, self.y)
        frontier = []
        heapq.heappush(frontier, (0, start_node))
        came_from = {start_node: None}
        cost_so_far = {start_node: 0}

        while frontier:
            current_node = heapq.heappop(frontier)[1]

            if current_node == goal_node:
                break

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_node = (current_node[0] + dx, current_node[1] + dy)
                new_cost = cost_so_far[current_node] + sqrt(dx ** 2 + dy ** 2)

                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + sqrt((next_node[0] - goal_node[0]) ** 2 + (next_node[1] - goal_node[1]) ** 2)
                    heapq.heappush(frontier, (priority, next_node))
                    came_from[next_node] = current_node

    # Déplacer l'agent le long du chemin trouvé
        path = []
        current_node = goal_node
        while current_node != start_node:
            path.append(current_node)
            current_node = came_from[current_node]
        path.append(start_node)
        path.reverse()

        for i in range(len(path) - 1):
            x, y = path[i]
            next_x, next_y = path[i + 1]
            self.move(next_x - x, next_y - y)


    def update_battery(self, dx, dy):
        distance = abs(dx) + abs(dy)
        self.battery -= distance

    def check_recharge_station(self):
        for station in self.city_map.stations_recharge:
            if abs(self.position[0] - station.position[0]) + abs(self.position[1] - station.position[1]) <= station.range:
                self.battery = 100
                break
    def choose_task(self):
        best_reward = 0
        best_task = None
        for task in self.city_map.tasks:
            if task.status != "available":
                continue
            reward = task.reward - self.city_map.distance(self.position, task.destination)
            if reward > best_reward:
                best_reward = reward
                best_task = task
        return best_task
    def follow_path(self, path):
        for dx, dy in path:
            self.move(dx, dy)

    def complete_task(self):
        task = self.current_task
    # Vérifier si l'agent est à proximité de la destination
        if abs(self.x - task.destination[0]) + abs(self.y - task.destination[1]) <= 1:
        # Mettre à jour la récompense totale de l'agent
            self.total_reward += task.reward
        # Retirer la tâche de la liste des tâches en cours
            self.current_task = None
        else:
        # Suivre le chemin jusqu'à la destination
            dx = dy = 0
            if self.x < task.destination[0]:
                dx = 1
            elif self.x > task.destination[0]:
                dx = -1
            if self.y < task.destination[1]:
                dy = 1
            elif self.y > task.destination[1]:
                dy = -1
            self.move(dx, dy)
    
        

