import argparse
from classes.platzi_url import PlatziUrl
from classes.readme import Readme


def main():
    parser = argparse.ArgumentParser(
        description="Receives a Platzi course url and creates a readme with its respective modules and lessons.")
    parser.add_argument('URL', help='URL used to fetch the information of a Platzi course.')
    parser.add_argument('--name', help='Choose the name of the .md file.')
    parser.add_argument("--path", help="Choose in what directory to put the file.")
    args = parser.parse_args()
    if PlatziUrl.is_platzi_url(args.URL):
        readme = Readme(args.URL, args.name, args.path)
        readme.create_readme()
    else:
        print('The URL is not a URL from a Platzi course.')


main()
