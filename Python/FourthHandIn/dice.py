class Dice:
    def __init__(self, color):
        self.color = color
        if self.color == 1:
            self.color = "red"
        elif self.color == 2:
            self.color = "green"
        elif self.color == 3:
            self.color = "blue"

    def roll_dice(self, rnd):
        red_values = [0, 0, 4, 4, 8, 8]
        green_values = [2, 2, 3, 3, 7, 7]
        blue_values = [1, 1, 5, 5, 6, 6]
        if self.color == "red":
            return red_values[rnd]
        elif self.color == "green":
            return green_values[rnd]
        elif self.color == "blue":
            return blue_values[rnd]
            


    