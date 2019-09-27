import argparse as ap
import data_viz
import get_data
import sys
import os


def parseArgs():
    '''
    Argument Parser, expect 3 arguments: Output file name, plot type and
    the column number to generate stats.
    '''
    parser = ap.ArgumentParser(description="Get plot type, output filename",
                               prog='viz')

    parser.add_argument('-o',
                        '--out_file',
                        type=str,
                        help="Output file name",
                        required=True)

    parser.add_argument('-t',
                        '--plot_type',
                        type=str,
                        help="Type of plot to produce <hist/box/combo>",
                        required=True)

    # Change this to a optional option,
    parser.add_argument('-c',
                        '--column',
                        type=int,
                        default=0,
                        help="Column index in the input file",
                        required=False)

    return parser.parse_args()


def main():
    '''
    Main function, takes arguments and generates plot as requested
    '''
    args = parseArgs()
    A = get_data.read_stdin_col(args.column)

    if len(A) == 0:
        raise ValueError('Input column contains no element, exiting')
        sys.exit(1)

    if (args.plot_type == 'box'):
        data_viz.boxplot(A, args.out_file)
    elif (args.plot_type == 'hist'):
        data_viz.histogram(A, args.out_file)
    elif (args.plot_type == 'combo'):
        data_viz.combo(A, args.out_file)
    else:
        raise ValueError('Invalid plot type. Please enter <hist/box/combo>')
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
