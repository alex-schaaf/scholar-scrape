import sys
import json

from scholarly import scholarly


if __name__ == "__main__":
    arguments = sys.argv[1:]
    author_name = " ".join(arguments)

    search_query = scholarly.search_author(author_name)
    first_author = next(search_query)
    author = scholarly.fill(first_author)

    publications = [pub for pub in author["publications"]]

    with open("publications_raw.json", "w") as file:
        json.dump(publications, file)
