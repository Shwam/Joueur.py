# Generated by Creer at 03:55PM on April 26, 2015 UTC, git hash: '2acbba9c4b682c4de68840c1ca9bec631e9c635f'
# This is where you build your AI for the Checkers game.
from baseAI import BaseAI
from random import shuffle

# @class BaseAI: the basic AI functions that are the same between games
class AI(BaseAI):
    # this is the name you send to the server to play as.
    def get_name(self):
        return "Checkers Python Player"

    # this is called once the game starts and your AI knows its player.id and game. You can initialize your AI here.
    def start(self):
        self.checkers_map = [[False for y in range(self.game.board_width)] for x in range(self.game.board_height)]

        # this is called when the game's state updates, so if you are tracking anything you can update it here.
    def game_updated(self):
        game = self.game

        for x in range(game.board_width):
            for y in range(game.board_height):
                self.checkers_map[x][y] = None

        self.force_checker = None
        self.cant_move = False
        for checker in game.checkers:
            self.checkers_map[checker.x][checker.y] = checker
            if checker.owner is self.player and checker is game.checker_moved:
                if game.checker_moved_jumped:
                    self.force_checker = checker
                else:
                    self.cant_move = True

    # this is called when the game ends, you can clean up your data and dump files here if need be
    # @param {boolean} won == true means you won, won == false means you lost
    # @param {string} reason you won or lost
    def end(self, won, reason):
        pass


    ### Response Functions: functions you must fill out to send data to the game server to actually play the game! ###

    ## This is called every time the AI is asked to respond with a command during their turn
    # @returns <Command> the Command you want to run on the server this turn from a game object's command functions. If you do not return your player's endTurn() then this runTurn function will be called again after the game state updates.
    def run_turn(self):
        if self.cant_move:
            return self.player.end_turn()

        checkers = list(self.player.checkers)

        if self.force_checker != None:
            checkers = [ self.force_checker ]

        shuffle(checkers)

        y_direction = self.player.y_direction # we need to know this so unkinged peices don't try to move in illegal directions

        for checker in checkers:
            neighbors = [ # valid move directions for all peices moving in the direction of their player's y (y_direction)
                {'x': checker.x + 1, 'y': checker.y + y_direction, 'requires jump': False},
                {'x': checker.x - 1, 'y': checker.y + y_direction, 'requires jump': False},
            ]

            if checker.kinged: # add the reversed y_direction neighbors to investigate moving to, because kinged peices can move in reverse
                neighbors.extend([
                    {'x': checker.x + 1, 'y': checker.y - y_direction, 'requires jump': False},
                    {'x': checker.x - 1, 'y': checker.y - y_direction, 'requires jump': False},
                ])

            shuffle(neighbors)

            while len(neighbors) > 0: # try to find a valid neighbor to move to
                neighbor = neighbors.pop()
                if neighbor['x'] >= self.game.board_width or neighbor['x'] < 0 or neighbor['y'] >= self.game.board_height or neighbor['y'] < 0:
                    continue # because we can't use this neighbor as it is out of bounds

                if self.force_checker != None: # then we must jump
                    if neighbor['requires jump']:
                        return checker.move(x=neighbor['x'], y=neighbor['y'])
                else:
                    jumping = self.checkers_map[neighbor['x']][neighbor['y']]
                    if jumping == None: # there's no checker there, so it's valid!
                        return checker.move(x=neighbor['x'], y=neighbor['y'])
                    elif jumping.owner != checker.owner: #there is one to jump so let's try to jump it
                        if not neighbor['requires jump']: # then we have not already jumped to get here, so let's try to jump it
                            dx = neighbor['x'] - checker.x
                            dy = neighbor['y'] - checker.y

                            neighbors.append({'x': neighbor['x'] + dx, 'y': neighbor['y'] + dy, 'requires jump': True})

        # if we got here we couldn't find a valid move for all our checkers :(
        return self.player.end_turn()