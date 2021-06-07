# GIMP Plugin Scripts (Python)
Plugins I created to optimize my GIMP experience.

### Motivation
While I can do all these actions manually, creating plugins and binding them to keyboard shortcuts saves time. ⏰

This is especially true when processing multiple images in a similar way.

### Plugins in this repo
* Exporting the active layer as JPG
* Exporting a specific layer as JPG
* Create a new, scaled layer from visible
* Create a new, scaled layer from a specific layer
* Adding watermark/copyright text

### Usage
* Pick one of the GIMP "plug-ins" directories (found in GIMP's "Preferences > Folders > Plug-Ins" list).
* Copy the ".py" files to that directory.
* Restart GIMP.
* You should be able to see the new menu items:
   * File > Export Active Layer > as JPG
   * Image > Add Watermark Text
   * Layer > Create Scaled Layer From Visible
* and the new Layer context menu items (right-clicking on a layer in "Layers" Dialog):
   * Duplicate to Scaled Layer
   * Export as JPEG
* Bonus points for adding keyboard shortcuts (in "Preferences > Interface > Configure Keyboard Shortcuts...").

### Want to work on your own plugins?
* [GIMP-Python docs](https://www.gimp.org/docs/python/index.html)
* [libgimp 2.0 API](https://developer.gimp.org/api/2.0/libgimp/libgimp-image.html)
* [GIMP PDB docs](http://oldhome.schmorp.de/marc/pdb/index.html)


License: http://eib.mit-license.org/
