import os
import numpy as np
from skimage.io import imread
from ._reader import FormatReader


class ImagetiffServiceBuilder:
    """Service builder for the imagetiff reader"""

    def __init__(self):
        self._instance = None

    def __call__(self, **_ignored):
        if not self._instance:
            self._instance = ImagetiffReaderService()
        return self._instance


class ImagetiffReaderService(FormatReader):
    """Reader for Tiff images

    """
    def __init__(self):
        super().__init__()

    @staticmethod
    def read(filename):
        return imread(filename)


class MovietxtServiceBuilder:
    """Service builder for the imagetiff reader"""

    def __init__(self):
        self._instance = None

    def __call__(self, **_ignored):
        if not self._instance:
            self._instance = MovietxtReaderService()
        return self._instance


class MovietxtReaderService(FormatReader):
    """Reader for Tiff images"""
    def __init__(self):
        super().__init__()

    @staticmethod
    def files(filename):
        dir_ = os.path.dirname(filename)
        filenames = [filename]
        with open(filename, 'r') as file_content:
            for line in file_content:
                filenames.append(os.path.join(dir_, line.strip()))
        return filenames

    @staticmethod
    def read(filename):
        files = MovietxtReaderService.files(filename)
        frames = []
        for file in files:
            frames.append(imread(file))
        return np.stack(frames)
