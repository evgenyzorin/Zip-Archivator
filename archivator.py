import os
import zipfile


DIR_PATH = os.path.abspath("")
SAVE_PATH = os.path.abspath("Output")
SEP_PATH = os.sep


def make_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)


def get_files(path):
    return [
        file
        for file in os.listdir(path)
        if (os.path.isfile(file) and file.split(".")[-1] == "step")
    ]


def get_readme(path):
    return "".join(
        file
        for file in os.listdir(path)
        if (os.path.isfile(file) and file.split(".")[-1] == "pdf")
    )


def zip_files():
    for file in get_files(DIR_PATH):
        zip_name = file.split(".")[0]
        with zipfile.ZipFile(f"{SAVE_PATH}{SEP_PATH}{zip_name}.zip", "w") as zipper:
            zipper.write(file)
            zipper.write(get_readme(DIR_PATH))


if __name__ == "__main__":
    make_dir(SAVE_PATH)
    zip_files()
