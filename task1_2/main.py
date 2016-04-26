import argparse
import generate_file

__parser__ = argparse.ArgumentParser()
__parser__.add_argument('-cs', '--count_str', type=int, default=10,
           help='Count of string in the file')
__parser__.add_argument('-cf', '--count_field', type=int, default=8,
           help='Count of field in the string')
__parser__.add_argument('-ls', '--line-separator', type=str, default='\n',
           help='Line separator')
__parser__.add_argument('-fs', '--field-separator', type=str, default='\t',
           help='Field separator')
__parser__.add_argument('-n', '--numeric', action="store_true",default=False,
           help='Interpret part of string as numbers')
__cmd__ = __parser__.parse_args()

def main():
    generate_file.generate_file(__cmd__.count_str, __cmd__.count_field,
                  __cmd__.line_separator, __cmd__.field_separator,
                  __cmd__.numeric)

if __name__ == "__main__":
    main()