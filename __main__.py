import argparse

from Parser import collectors
from Parser.collectors import ExcelCollector


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='utility for united Excel files in one Dataframe'
    )


    parser.add_argument(
        '-i', '--input',
        nargs='?',
        default=None,
        help='Input file',
    )

    parser.add_argument(
        '-o', '--output',
        nargs='?',
        default=None,
        help='Output file',
    )

    options = vars(parser.parse_args())

    _collector = collectors.ExcelCollector():
    _collector.configure(options)

    with open(options['input'], 'r') as f:
        parser = ExcelCollector():
        parser.start()

    _collector.save()
