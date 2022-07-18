#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mimetypes
import os
import toml
from pathlib import Path


# Necessary info is located in ".config/user-dirs.dirs" or  XDG_CONFIG_DIR


def get_config_directory():
    return (os.environ["XDG_CONFIG_DIR"]
            if "XDG_CONFIG_DIR" in os.environ else Path.home() / ".config")


# Read default download dir from .config/user-dirs.dirs


def get_download_directory():
    # First check if Download Directory is defined in Path
    if "XDG_DOWNLOAD_DIR" in os.environ:
        return os.environ["XDG_DOWNLOAD_DIR"]

    # If is not defined

    config_path = get_config_directory()

    # user-dirs.dirs file

    dirs_file = config_path / "user-dirs.dirs"  # Concatenate

    #

    with open(dirs_file, "r") as f:
        for line in f.readlines():
            if line.startswith("XDG_DOWNLOAD_DIR"):
                # Split and Replace Quotes
                down = line.split("=")[1].replace('"', "")
                # We don't want /Downloads/ we want /Downloads, so we remove '/' with [:-1]
                full_dir = down.replace("$HOME", str(Path.home()))[:-1]
                return Path(full_dir)

    return None


def list_directory(directory_path):
    try:

        if directory_path is not None and directory_path.is_dir():
            print(f"\nDirectory: {directory_path}\n")
            # List just jpeg/jpg files
            iterator = os.scandir(directory_path)
            index = 0
            for f_ile in iterator:
                if not f_ile.is_dir():

                    mt = mimetypes.guess_type(f_ile.name)

                    if mt[0] == "image/jpeg":
                        if index % 2 == 0:
                            print(index, f' -> "{f_ile.name}"')
                        else:
                            print(index, f_ile.name)
                        index += 1
    except Exception as exception:
        print(exception)


def get_directory(config_file):  # Extract directory from config file ## Precondition: "config_file" exists

    cdata = toml.load(config_file)

    return Path(cdata['directorio'])



def main():
    try:
        project_config = get_config_directory() / "diogenes"  # Config file location

        config_file = project_config / "diogenes.conf"

        if not os.path.isdir(project_config):
            os.mkdir(project_config)

        if not os.path.isfile(config_file):  # Check if config file exists

            cdata = {"directorio": str(get_download_directory())}

            with open(config_file, 'w') as config:
                toml.dump(cdata, config)

        # Read Config File
        dir2list = get_directory(config_file)

        if not os.path.isdir(dir2list):
            os.mkdir(dir2list)

        # List Directory
        list_directory(dir2list)

    except Exception as exception:
        print(exception)


if __name__ == "__main__":
    main()
