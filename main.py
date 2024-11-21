import glob
import yaml
import os
import regex as re
import shutil

def load_metadata(path):
    with open(path+"/metadata.txt", "r") as file:
        metadata = yaml.safe_load(file)

    return metadata



if __name__ == "__main__":
    base_path = "../database/data/fro/*"
    paths = glob.glob(base_path)

    genres = {"romanProse": "roman.*en prose", "romanVers": "roman.*en vers", "chGeste": "chanson de geste.*"}

    for genre in genres.keys():
        os.makedirs(genre)

    for path in paths:
        metadata = load_metadata(path)

        workGenre = re.sub(r"[^\p{L}\p{P}\p{M}]+", " ", metadata["workGenre"].lower())

        for genre in genres.items():
            if re.match(genre[1], workGenre):
                shutil.copytree(path, "./"+genre[0]+"/"+path.split("/")[-1])


