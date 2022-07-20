#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mimetypes
import os
 
def list_images(directory_path):
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



