import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, val in kwargs.items():
            self.contents += [key] * val

    def draw(self, number):
        if number >= len(self.contents): return self.contents # since all contents is returned, no need to make a copy

        draw = []
        while len(draw) != number:
            drawn = random.choice(self.contents)
            self.contents.remove(drawn)
            draw.append(drawn)

        return draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for x in range(0, num_experiments):
        subhat = copy.deepcopy(hat) # a copy of the object is required for every iteration
        draw = subhat.draw(num_balls_drawn)
        success += 1 if all([True if draw.count(ball) >= expected_balls[ball] else False for ball in expected_balls]) else 0

    return round(success / num_experiments, 3)
