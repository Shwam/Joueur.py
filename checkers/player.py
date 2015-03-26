# Generated by Creer, git hash Error: git probably not installed
# This is a simple class to represent the Player object in the game. You can extend it by adding utility functions here in this file.

from Checkers.gameObject import GameObject


# @class Player: A player in this game. Every AI controls one player.
class Player(GameObject):
    ## initializes a Player with basic logic as provided by the Creer code generator
    # @param dict data: initialization data
    def __init__(self, data):
        GameObject.__init__(self, data)

        self.name = str(data['name'] if 'name' in data else "Anonymous")
        self.client_type = str(data['clientType'] if 'clientType' in data else "")



    ## Tells the server that this player is done with their turn.
    def end_turn(self):
        return self.client.send_command(self, 'endTurn')
