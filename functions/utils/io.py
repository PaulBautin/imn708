# -*- coding: utf-8 -*-
import nibabel as nib
import numpy as np
import os



def _load_nifti(filename):
    img = nib.load(filename)
    return img


def _load_png_jpg(filename):
    raise NotImplementedError


def load_image(filename, from_nifti=False):
    """
    Always provide method expanation.
    In this example, I used an optional variable just to show you it
    exists. Define methods as you wish.

    Parameters
    ----------
    filename: str
        Always provide parameter explanations.
    from_nifti: bool
        If this value is true, we will load the image from nibabel. Else,
        (default), we expect value to be loadable from matplotlib (ex, png,
        jpg).

    Returns
    -------
    img: np.ndarray
        The loaded image, as a numpy array.
    """
    if from_nifti:
        return _load_nifti(filename)
    else:
        return _load_png_jpg(filename)
