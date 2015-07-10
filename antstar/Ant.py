from antstar.AntBrain import AntBrain
from antstar.AntFeeler import AntFeeler


class Ant:

    def __init__(self, start_position, end_position, grid):
        self._position = start_position
        self._feeler = AntFeeler(self, grid)
        self._brain = AntBrain(self, start_position, end_position)

    def get_position(self):
        return self._position

    def move_to(self, vector):
        self._brain.update_home_vector(vector)
        self._position = (self._position[0] + vector[0], self._position[1] + vector[1])
        self._brain.has_moved()

    def get_feeler(self):
        return self._feeler

    def move(self):
        self._brain.advance()