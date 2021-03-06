# Generated by Creer at 07:24PM on February 04, 2016 UTC, git hash: '955970b8006ac45cc438822363db1bc1242d9868'
# This is a simple class to represent the WeatherStation object in the game. You can extend it by adding utility functions here in this file.

from games.anarchy.building import Building

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add addtional import(s) here
# <<-- /Creer-Merge: imports -->>

class WeatherStation(Building):
    """The class representing the WeatherStation in the Anarchy game.

    Can be bribed to change the next Forecast in some way.
    """

    def __init__(self):
        """Initializes a WeatherStation with basic logic as provided by the Creer code generator."""
        Building.__init__(self)

        # private attributes to hold the properties so they appear read only




    def intensify(self, negative=False):
        """ Bribe the weathermen to intensity the next Forecast by 1 or -1

        Args:
            negative (Optional[bool]): By default the intensity will be increased by 1, setting this to true decreases the intensity by 1.

        Returns:
            bool: true if the intensity was changed, false otherwise
        """
        return self._run_on_server('intensify', negative=negative)


    def rotate(self, counterclockwise=False):
        """ Bribe the weathermen to change the direction of the next Forecast by rotating it clockwise or counterclockwise.

        Args:
            counterclockwise (Optional[bool]): By default the direction will be rotated clockwise. If you set this to true we will rotate the forecast counterclockwise instead.

        Returns:
            bool: true if the rotation worked, false otherwise.
        """
        return self._run_on_server('rotate', counterclockwise=counterclockwise)


    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
