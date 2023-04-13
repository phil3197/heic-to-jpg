# ImageMagick needs to be installed!
import os, subprocess, shutil

class FileContainer:

    def __init__(self, file_name, file_path) -> None:
        self.file_name = file_name
        self.file_path = file_path


current_dir = os.getcwd()


def read_files():
    heic_files = []
    for r, d, f in os.walk(current_dir):
        del d[:]
        for file in f:
            if file.lower().endswith(".heic"):
                heic_files.append(FileContainer(file,os.path.join(r, file)))

    return heic_files

def convert_files(files):
    for file in files:
        print('Converting %s...' % file.file_path)
        subprocess.run(["magick", "%s" % file.file_name, "%s" % (file.file_name[0:-5] + '.jpg')])

def move_files(files):
    final_directory = os.path.join(current_dir, r'heic')
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)

    for file in files:
        dst_path = os.path.join(final_directory, file.file_name)
        shutil.move(file.file_name, dst_path)


files = read_files()
convert_files(files)
move_files(files)