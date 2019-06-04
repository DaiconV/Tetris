import tetris_exceptions


class TetrisGameState:
    """
    Class containing information on the current state of Tetris game.
    """

    def __init__(self, height: int = 24, width: int = 10):
        """
        TetrisGameState Class constructor.

        :param height: height of screen
        :type: int
        :param width: width of screen
        :type: int
        :raises: InvalidDimensionsError
        """
        if height < 4 or width < 4:
            raise tetris_exceptions.InvalidDimensionsError()

        self.height = height
        self.width = width
        self.screen = [[chr]]

    def get_height(self):
        """
        Returns height of screen.

        :return: height of screen
        :rtype: int
        """
        return self.height

    def get_width(self):
        """
        Returns width of screen.

        :return: width of screen
        :rtype: int
        """
        return self.height

    def update_screen(self):
        """
        Updates screen by dropping pieces still in motion by one unit.
        """
        pass
