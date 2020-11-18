#! usr/bin/env python3

import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Arguments:
        suffix {[str]} -- [suffix if the file name to be found]
        path {[str]} -- [path of the file system]

    Returns:
        [str] -- [a list of paths]
    """
    if suffix == "":
        return []

    if not os.path.isdir(path):
        return "Invalid Directory"

    dir_paths = os.listdir(path)
    if dir_paths:

        dir_folders = [file for file in dir_paths if str(".") not in file]
        dir_files = [file for file in dir_paths if str("." + suffix) in file]

        for folder in dir_folders:
            dir_files.extend(find_files(suffix, os.path.join(path, folder)))

        return dir_files


def main():

    root_path = os.getcwd() + "/testdir"
    print(find_files("", root_path))
    print(find_files("c", root_path))
    print(find_files("h", root_path))
    print(find_files("x", root_path))

    path = "./solution/problem2/problem2.py"
    suffix = ".py"
    print(find_files(path, suffix))


if __name__ == "__main__":
    main()
