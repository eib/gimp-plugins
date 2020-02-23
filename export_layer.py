#!/usr/bin/env python
# -*- coding: <utf-8> -*-
# Author: Ethan Blackwelder
# Copyright 2020 Ethan Blackwelder
# License: MIT (http://eib.mit-license.org/)
# Version 0.1
# GIMP compatibilty ???
# PyGIMP plugins to export layers:
#  - export the active layer
#  - export the selected layer


from gimpfu import *
import os

_MAX_COMPRESSION = 9
_DESKTOP_DIR = os.path.expanduser("~/Desktop")

def export_selected_layer(img, layer, dir, filename):
    path = _sanitize_filepath(dir, filename)
    _export_layer_as_png(img, layer, path)

def export_active_layer(img, dir, filename):
    path = _sanitize_filepath(dir, filename)
    _export_layer_as_png(img, img.active_layer, path)


def _export_layer_as_png(img, layer, path):
    interlace = False
    compression = _MAX_COMPRESSION
    bkgd = True  # Write bKGD chunk?
    gama = True  # Write gAMA chunk?
    offs = True  # Write oFFs chunk?
    phys = True  # Write pHYs chunk?
    time = True  # Write tIME chunk?
    pdb.file_png_save(img, layer, path, path, interlace, compression, bkgd, gama, offs, phys, time)    

def _sanitize_filepath(dir, filename):
    filename = filename if filename.lower().endswith(".png") else (filename + ".png")
    return os.path.normpath(os.path.join(dir, filename))


register(
    proc_name=("python-fu-export-active-layer"),
    blurb=("Export Active Layer (PNG)"),
    help=("Exports the active Layer as PNG."),
    author=("Ethan Blackwelder"),
    copyright=("Ethan Blackwelder"),
    date=("2020"),
    label=("Export Active Layer (PNG)"),
    imagetypes=("*"),
    params=[
        (PF_IMAGE, "img", "Image", None),
        (PF_DIRNAME, "dir", "Directory", _DESKTOP_DIR),
        (PF_FILE, "filename", "filename", None),
        ],
    results=[],
    function=(export_active_layer),
    menu=("<Image>/Layer"),
    domain=("gimp20-python", gimp.locale_directory)
    )

register(
    proc_name=("python-fu-export-selected-layer"),
    blurb=("Export Selected Layer (PNG)"),
    help=("Exports the selected layer as PNG."),
    author=("Ethan Blackwelder"),
    copyright=("Ethan Blackwelder"),
    date=("2013"),
    label=("Export Selected Layer (PNG)"),
    imagetypes=("*"),
    params=[
        (PF_IMAGE, "img", "Image", None),
        (PF_LAYER, "layer", "Ignored", None),
        (PF_DIRNAME, "dir", "Directory", _DESKTOP_DIR),
        (PF_FILE, "filename", "filename", None),
        ],
    results=[],
    function=(export_selected_layer), 
    menu=("<Layers>"), 
    domain=("gimp20-python", gimp.locale_directory)
    )

main()
