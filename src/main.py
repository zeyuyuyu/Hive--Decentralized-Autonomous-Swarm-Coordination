import random
import time
from typing import List, Tuple

class Swarm:
    def __init__(self, num_bots: int, arena_size: Tuple[int, int]):
        self.bots = [Bot(i, arena_size) for i in range(num_bots)]
        self.arena_size = arena_size

    def run(self):
        while True:
            for bot in self.bots:
                bot.update()
            time.sleep(0.1)

class Bot:
    def __init__(self, id: int, arena_size: Tuple[int, int]):
        self.id = id
        self.x, self.y = random.randint(0, arena_size[0]), random.randint(0, arena_size[1])
        self.velocity_x, self.velocity_y = random.uniform(-1, 1), random.uniform(-1, 1)
        self.neighbors: List[Bot] = []

    def update(self):
        self.find_neighbors()
        self.coordinate_with_neighbors()
        self.move()

    def find_neighbors(self):
        self.neighbors = [bot for bot in swarm.bots if bot != self and (bot.x - self.x)**2 + (bot.y - self.y)**2 < 100]

    def coordinate_with_neighbors(self):
        if self.neighbors:
            total_x, total_y = sum(n.x for n in self.neighbors), sum(n.y for n in self.neighbors)
            self.velocity_x = (total_x / len(self.neighbors)) - self.x
            self.velocity_y = (total_y / len(self.neighbors)) - self.y

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.x = max(0, min(self.x, swarm.arena_size[0]))
        self.y = max(0, min(self.y, swarm.arena_size[1]))

if __name__ == '__main__':
    swarm = Swarm(num_bots=50, arena_size=(800, 600))
    swarm.run()