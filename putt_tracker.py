class Putt:
    def __init__(self, success: bool = False, line: str = 'n/a', relative_distance:str = 'n/a'):
        self._success = success
        self._line = line
        self._relative_distance = relative_distance

    def set_success(self, success: bool):
        self._success = success

    def set_line(self, line: str):
        if line.upper() == 'LEFT':
            self._line = 'LEFT'
        elif line.upper() == 'RIGHT':
            self._line = 'RIGHT'
        else:
            print('Invalid line, valid values are "LEFT", or "RIGHT"')

    def set_relative_distance(self, relative_distance: str):
        if relative_distance.upper() == 'LONG':
            self._relative_distance = 'LONG'
        elif relative_distance.upper() == 'SHORT':
            self._relative_distance = 'SHORT'
        else:
            print('Invalid relative distance, valid values are "SHORT" or "LONG"')

    @property
    def success(self):
        return self._success

    @property
    def line(self):
        return self._line

    @property
    def relative_distance(self):
        return self._relative_distance


putt_list = []

while True:
    new_putt_result = input("Please enter result of putt.  "
                            "Enter '0' for miss, '1' for make.\n "
                            "Enter 'Q' to tally results\n")

    if new_putt_result.upper() == '0':
        new_putt_success = False
    elif new_putt_result.upper() == '1':
        new_putt_success = True
    elif new_putt_result.upper() == 'Q':
        break
    else:
        print("Invalid entry.  Enter '0' for a miss, '1' for a make, or 'Q' to quit")
        continue
    new_putt = Putt(new_putt_success)
    if not new_putt_success:
        new_putt_line = input("Which side did you miss?  "
                              "Enter 'L' for left or 'R' for right\n")
        if new_putt_line.upper() == 'L':
            new_putt.set_line('LEFT')
        elif new_putt_line.upper() == 'R':
            new_putt.set_line('RIGHT')
        else:
            print('Invalid line.  Please enter "L" or "R"')
            continue

        new_putt_relative_distance = input("What was your relative distance?  "
                                           "Enter 'L' for long, or 'S' for short\n")
        if new_putt_relative_distance.upper() == 'L':
            new_putt.set_relative_distance('LONG')
        elif new_putt_relative_distance.upper() == 'S':
            new_putt.set_relative_distance('SHORT')
        else:
            print('Invalid relative distance.  Please enter "L", or "S"\n')
            continue
    else:
        new_putt = Putt(True)

    putt_list.append(new_putt)

print("Here's your putts:")
for i in range(0, len(putt_list)):
    print('Putt {} results:'.format(i))
    print('Result: {}'.format(putt_list[i].success))
    print('Line: {}'.format(putt_list[i].line))
    print('Relative Distance: {}'.format(putt_list[i].relative_distance))
    print('=' * 40)
