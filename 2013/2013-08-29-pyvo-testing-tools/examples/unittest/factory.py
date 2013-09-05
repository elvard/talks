class Car(object):
    def __init__(self):
        self.is_damaged = False
        self.damage = 0

    def hit_wall(self, velocity=None):
        if velocity > 10:
            self.is_damaged = True

        self.damage = min(100, velocity/120*100)
