import sys
import json


if __name__ == "__main__":
    fp = sys.argv[1]
    with open(fp, "r") as file:
        publications = json.load(file)

    cleaned = []
    for pub in publications:
        bib = pub["bib"]
        bib["pub_year"] = int(bib["pub_year"])
        bib["num_citations"] = pub["num_citations"]
        cleaned.append(bib)

    with open("publications.json", "w") as file:
        json.dump(cleaned, file)
