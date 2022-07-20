#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import toml
import os
import functions


class Configurator:

    def __init__(self, path, configfile):
        self.path = path
        self.configfile = configfile
        self.check_file()  # Check if file exists at class init

    def read(self):

        cfile = self.path / self.configfile
        return toml.load(cfile)

    def check_file(self):

        if not self.path.exists():
            os.makedirs(self.path)

        cfile = self.path / self.configfile

        if not cfile.exists():  # Default Dir
            cdata = {"directorio": str(functions.get_download_directory())}

            with open(cfile, 'w') as file_write:
                toml.dump(cdata, file_write)

    def save(self, cdata):

        cfile = self.path / self.configfile

        with open(cfile, 'w') as file_write:
            toml.dump(cdata, file_write)
