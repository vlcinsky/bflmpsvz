"""Print `blfmpsvz` plus user specified message

Usage:
    bflmpsvz <message>
"""


def main(msg=""):
    print("bflmpsvz-2nd-generation: " + msg)


def script():
    from docopt import docopt
    args = docopt(__doc__)
    msg = args["<message>"]
    main(msg)


if __name__ == "__main__":
    script()
