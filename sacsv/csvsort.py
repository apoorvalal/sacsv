import argh
import sys
import csv


@argh.arg("-c", "--columns", nargs="+", type=str)
def main(columns=None):
    reader = csv.reader(sys.stdin)
    header = next(reader)

    if columns is None:
        key = lambda r: r
    else:
        indices = tuple(header.index(c) for c in columns)
        key = lambda r: tuple(r[index] for index in indices)

    writer = csv.writer(sys.stdout)
    writer.writerow(header)

    for record in sorted(tuple(reader), key=key):
        writer.writerow(record)


def dispatch():
    argh.dispatch_command(main)


if __name__ == "__main__":
    dispatch()
