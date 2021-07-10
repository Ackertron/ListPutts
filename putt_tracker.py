class Putt:
    def __init__(self, success: bool = False, line: str = 'n/a', relative_distance: str = 'n/a'):
        self._success = success
        self._line = line
        self._relative_distance = relative_distance

    def set_success(self, success: bool):
        self._success = success

    def set_relative_distance(self, relative_distance: str):
        if relative_distance.upper() == 'LONG':
            self._relative_distance = 'LONG'
        elif relative_distance.upper() == 'SHORT':
            self._relative_distance = 'SHORT'
        elif relative_distance.upper() == 'GOOD':
            self._relative_distance = 'GOOD'
        else:
            print('Invalid relative distance, valid values are "SHORT" or "LONG"')

    def set_line(self, line: str):
        if line.upper() == 'LEFT':
            self._line = 'LEFT'
        elif line.upper() == 'RIGHT':
            self._line = 'RIGHT'
        elif line.upper() == 'ON_LINE':
            self._line = 'ON_LINE'
        else:
            print('Invalid line, valid values are "LEFT", or "RIGHT"')

    @property
    def success(self):
        return self._success

    @property
    def line(self):
        return self._line

    @property
    def relative_distance(self):
        return self._relative_distance


def tally_results(putts_list):
    missed_left = 0
    missed_right = 0
    missed_long = 0
    missed_short = 0
    made = 0

    for putt in range(0, len(putts_list)):
        if putts_list[putt].line == 'LEFT':
            missed_left += 1
        elif putts_list[putt].line == 'RIGHT':
            missed_right += 1
        else:
            continue

    for putt in range(0, len(putts_list)):
        if putts_list[putt].relative_distance == 'SHORT':
            missed_short += 1
        elif putts_list[putt].relative_distance == 'LONG':
            missed_long += 1
        else:
            continue

    for putt in range(0, len(putts_list)):
        if putts_list[putt].success:
            made += 1

    # We'll be using this a lot
    total_putts = len(putts_list)
    print(("*" * 15) + "Tallied Results" + ("*" * 15))
    print('Total Putts: {}'.format(total_putts))
    print('Made putt percentage: ' + "{:.0%}".format(made / total_putts))
    print('Missed left percentage: ' + "{:.0%}".format(missed_left / total_putts))
    print('Missed right percentage: ' + "{:.0%}".format(missed_right / total_putts))
    print('Missed short percentage: ' + "{:.0%}".format(missed_short / total_putts))
    print('Missed long percentage: ' + "{:.0%}".format(missed_long / total_putts))
    print("*" * 30 + "*" * (len('Tallied Results') + 2))


debug_mode = False
putts_list = []

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
        new_putt_relative_distance = input("What was your relative distance?  "
                                           "Enter 'L' for long, 'S' for short, "
                                           "or 'G' for good distance\n")
        if new_putt_relative_distance.upper() == 'L':
            new_putt.set_relative_distance('LONG')
        elif new_putt_relative_distance.upper() == 'S':
            new_putt.set_relative_distance('SHORT')
        elif new_putt_relative_distance.upper() == 'G':
            new_putt.set_relative_distance('GOOD')
        else:
            print('Invalid relative distance.  Please enter "L", "S", or "G"\n')
            continue

        new_putt_line = input("Which side did you miss?  "
                              "Enter 'L' for left, 'R' for right, "
                              "or 'O' for on line\n")
        if new_putt_line.upper() == 'L':
            new_putt.set_line('LEFT')
        elif new_putt_line.upper() == 'R':
            new_putt.set_line('RIGHT')
        elif new_putt_line.upper() == 'O':
            new_putt.set_line('ON_LINE')
        else:
            print('Invalid line.  Please enter "L", "R" or "O"')
            continue

    else:
        new_putt = Putt(True)

    putts_list.append(new_putt)

tally_results(putts_list)

if debug_mode:
    print("Here's your putts:")
    for i in range(0, len(putt_list)):
        print('Putt {} results:'.format(i))
        print('Result: {}'.format(putt_list[i].success))
        print('Line: {}'.format(putt_list[i].line))
        print('Relative Distance: {}'.format(putt_list[i].relative_distance))
        print('=' * 40)
