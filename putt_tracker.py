import os
import shot
import tracker

debug_mode = False
putts_list = []

while True:
    os.system('clear')
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
    new_putt = shot.Shot(new_putt_success)
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
        new_putt = shot.Shot(True)

    putts_list.append(new_putt)

tracker.tally_results(putts_list)

if debug_mode:
    print("Here's your putts:")
    for i in range(0, len(putts_list)):
        print('Putt {} results:'.format(i))
        print('Result: {}'.format(putts_list[i].success))
        print('Line: {}'.format(putts_list[i].line))
        print('Relative Distance: {}'.format(putts_list[i].relative_distance))
        print('=' * 40)
