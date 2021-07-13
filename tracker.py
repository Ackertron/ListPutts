
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