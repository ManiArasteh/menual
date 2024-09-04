from argparse import ArgumentParser
import sys

def get_manual(args):
    pass

def main():
    parser = ArgumentParser(prog="Menual", description="Shows a help for an specified command/app")
    parser.add_argument("COMMANDORAPP", help="A command or app to find its user manual")
    subparser = parser.add_subparsers(title="SUBCOMMAND", help="A subcommand")
    getsubparser = subparser.add_parser("get", help="Gets the list of user manuals from the internet (default manuals)")
    getsubparser.set_defaults(func=get_manual)
    parser.parse_args(args=None if sys.argv[1:] else ["--help"])

if __name__ == '__main__':
    main()