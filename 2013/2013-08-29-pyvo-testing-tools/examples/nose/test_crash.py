from nose import with_setup


class Car(object):
    def __init__(self):
        self.is_damaged = False
        self.damage = 0

    def hit_wall(self, velocity=None):
        if velocity > 10:
            self.is_damaged = True

        self.damage = min(100, velocity/120*100)


def setup_func():
    global car
    car = Car()
    car.hit_wall(velocity=120)


@with_setup(setup_func)
def test_crash():
    global car
    assert car.is_damaged is False