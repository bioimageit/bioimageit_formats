import os
import pandas as pd
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
            if file != filename:
                frames.append(imread(file))
        return np.stack(frames)


class TableCSVServiceBuilder:
    """Service builder for the tablecsv reader"""

    def __init__(self):
        self._instance = None

    def __call__(self, **_ignored):
        if not self._instance:
            self._instance = TableCSVReaderService()
        return self._instance


class TableCSVReaderService(FormatReader):
    """Reader for Tiff images

    """
    def __init__(self):
        super().__init__()

    @staticmethod
    def read(filename):
        return pd.read_csv(filename)


class ArrayCSVServiceBuilder:
    """Service builder for the arraycsv reader"""

    def __init__(self):
        self._instance = None

    def __call__(self, **_ignored):
        if not self._instance:
            self._instance = ArrayCSVReaderService()
        return self._instance


class ArrayCSVReaderService(FormatReader):
    """Reader for Tiff images

    """
    def __init__(self):
        super().__init__()

    @staticmethod
    def read(filename):
        return pd.read_csv(filename, nrows=1)


class NumberCSVServiceBuilder:
    """Service builder for the numbercsv reader"""

    def __init__(self):
        self._instance = None

    def __call__(self, **_ignored):
        if not self._instance:
            self._instance = NumberCSVReaderService()
        return self._instance


class NumberCSVReaderService(FormatReader):
    """Reader for Tiff images

    """
    def __init__(self):
        super().__init__()

    @staticmethod
    def read(filename):
        return pd.read_csv(filename, nrows=1)        