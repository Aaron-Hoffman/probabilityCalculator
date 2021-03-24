import copy
import random


class Hat:

    def __init__(self, **args):
        self.contents = []
        for arg in args:
            for i in range(args[f'{arg}']):
                self.contents.append(arg)

    def draw(self, number):
        contents = self.contents
        if number > len(contents):
            return contents
        balls_drawn = []
        for i in range(number):
            ball = random.choice(contents)
            contents.remove(ball)
            balls_drawn.append(ball)
        return balls_drawn


hat = Hat(red=5, blue=3, green=6)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successful = conduct_experiment(
        hat, expected_balls, num_balls_drawn, num_experiments)
    return num_successful / num_experiments


def conduct_experiment(hat=Hat, expected_balls={}, num_balls_drawn=0, num_experiments=0):
    num_successful = 0
    while num_experiments > 0:
        num_experiments -= 1
        new_hat = copy.deepcopy(hat)
        drawn = new_hat.draw(num_balls_drawn)
        successful = []
        for colour in expected_balls:
            if expected_balls[f'{colour}'] > drawn.count(colour):
                successful.append(False)
            else:
                successful.append(True)
        print(successful)
        if False not in successful:
            num_successful += 1
    return num_successful


print(experiment(hat=hat, expected_balls={
      'green': 2, 'blue': 1}, num_balls_drawn=3, num_experiments=10))
