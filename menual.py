from argparse import ArgumentParser
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import sys

def get_manual(args):
    save_path = '~/.menual/'
    response1 = requests.get("https://maniarasteh.github.io/menual/")
    soup = BeautifulSoup(response1.content, 'html.parser')
    a_element = soup.find('a')
    response = requests.get(a_element['href'], stream=True)
    # Get the total file size from the headers (if available)
    total_size = int(response.headers.get('content-length', 0))
    # Open the file in binary mode and write chunks to it
    with open(save_path, "wb") as file:
        # Initialize tqdm progress bar with the total size
        with tqdm(total=total_size, unit="B", unit_scale=True, desc="Downloading", ascii=True) as progress_bar:
            # Download the file in chunks
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:  # Filter out keep-alive chunks
                    file.write(chunk)
                    progress_bar.update(len(chunk))

def main():
    parser = ArgumentParser(prog="Menual", description="Shows a help for an specified command/app")
    parser.add_argument("COMMANDORAPP", nargs='?', help="A command or app to find its user manual")
    subparser = parser.add_subparsers(title="SUBCOMMAND", help="A subcommand")
    getsubparser = subparser.add_parser("get", help="Gets the list of user manuals from the internet")
    getsubparser.set_defaults(func=get_manual)
    args = parser.parse_args(args=None if sys.argv[1:] else ["--help"])
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()