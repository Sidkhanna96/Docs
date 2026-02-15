"""
Dropbox

Space Panorama

This question is usually used in a phone screen.

The sky is divided into a big grid and we are snapping pictures of the grid pieces.
Each image has a row number and a column number corresponding to its place in the grid.
We want to save the images to a disk, and read them too!
Assume each piece of data is 1 MB.
Write an API to do this.
"""

"""
We also want to have constant-time access to the last file we saved. If we haven't saved all the files yet,
then just return any file that we haven't saved. Assume the sky is 1000 x 1000.
"""

from collections import defaultdict


class SpacePanorama:
    def __init__(self):
        self.imageLocation = defaultdict(str)

    def _save_image(self, file_name, image_data):
        pass

    def snap(self, r, c, image_data):
        self.imageLocation[(r, c)] = "./{r}_{c}.jpg"

        self._save_image(self.imageLocation[(r, c)], image_data)
