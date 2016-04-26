import argparse
import task_1 as task

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", type=str,
                        help="input file name")
    parser.add_argument("-o", "--output", type=str,
                        help="output file name")
    parser.add_argument("-b", "--bufferSize", type=int,
                        help="size buffer for merged sort")
    parser.add_argument("-l", "--lineSeparator", default="\n", type=str,
                        help=r"default is \n")
    parser.add_argument("-t", "--fieldSeparator", default="\t", type=str,
                        help=r"default is \t")
    parser.add_argument("-k", "--keys", default=None, type=str,
                        help="list keys for sort, default is all fields")
    parser.add_argument("-n", "--numeric", type=bool, default=False,
                        help=r"default is False")
    parser.add_argument("-r", "--reverse", type=bool, default=False,
                        help=r"default is False")
    parser.add_argument("-c", "--checked", type=bool, default=False,
                        help="check data without sorted")

    args = parser.parse_args()

    if not args.keys is None:
        args.keys = [int(key) for key in args.keys.split(",")]

    result = task.sortBigFile(args.input, args.output, args.bufferSize,
                                args.lineSeparator, args.fieldSeparator,
                                args.keys, args.numeric, args.reverse, args.checked)
    if args.checked:
        print result

if __name__ == "__main__":
    main()