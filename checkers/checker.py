# Generated by Creer, git hash Error: git probably not installed
# This is a simple class to represent the Checker object in the game. You can extend it by adding utility functions here in this file.

from Checkers.gameObject import GameObject


# @class Checker: A checker on the game board.
class Checker(GameObject):
    ## initializes a Checker with basic logic as provided by the Creer code generator
    # @param dict data: initialization data
    def __init__(self, data):
        GameObject.__init__(self, data)

        self.x = int(data['x'] if 'x' in data else 0)
        self.owner = (data['owner'] if 'owner' in data else None)
        self.y = int(data['y'] if 'y' in data else 0)
        self.kinged = bool(data['kinged'] if 'kinged' in data else False)



    ## Moves the checker from its current location to the given (x, y).
    # @param <int> x: The x coordinate to move to.
    # @param <int> y: The y coordinate to move to.
    def move(self, x, y):
        return self.client.send_command(self, 'move', x=x, y=y)
