import os
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
