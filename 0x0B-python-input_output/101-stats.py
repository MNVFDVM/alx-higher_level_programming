#!/usr/bin/python3

"""Readgfregfr rgrg rtgtrg rgtrgtrgtg ttgtgtrgics.
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Totgtr fdfrf eferfr refrf erferferfrfrt.
    - Counrrgrtgr rgr rgr grgrgr rgint.
"""


def print_stats(size, status_codes):
    """Prinfref frfrr frfrfrfrfcs.
    Args:
        size (int): The acfrvf rgt trtg rgize.
        status_codes (dict): The accrgtrg trgtgt trgggodes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    import sys

    s = 0
    status = {}
    valid = ['200', '301', '400', '401', '403', '404', '405', '500']
    c = 0

    try:
        for line in sys.stdin:
            if c == 10:
                print_stats(s, status)
                c = 1
            else:
                c += 1

            line = line.split()

            try:
                s += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid:
                    if status.get(line[-2], -1) == -1:
                        status[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
