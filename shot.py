class Shot:
    def __init__(self, success: bool = False, line: str = 'n/a', relative_distance: str = 'n/a'):
        self._success = success
        self._line = line
        self._relative_distance = relative_distance

    def set_success(self, success: bool) -> None:
        self._success = success

    def set_relative_distance(self, relative_distance: str) -> None:
        if relative_distance.upper() == 'LONG':
            self._relative_distance = 'LONG'
        elif relative_distance.upper() == 'SHORT':
            self._relative_distance = 'SHORT'
        elif relative_distance.upper() == 'GOOD':
            self._relative_distance = 'GOOD'
        else:
            print('Invalid relative distance, valid values are "SHORT" or "LONG"')

    def set_line(self, line: str) -> None:
        if line.upper() == 'LEFT':
            self._line = 'LEFT'
        elif line.upper() == 'RIGHT':
            self._line = 'RIGHT'
        elif line.upper() == 'ON_LINE':
            self._line = 'ON_LINE'
        else:
            print('Invalid line, valid values are "LEFT", or "RIGHT"')

    @property
    def success(self) -> bool:
        return self._success

    @property
    def line(self) -> str:
        return self._line

    @property
    def relative_distance(self) -> str:
        return self._relative_distance
