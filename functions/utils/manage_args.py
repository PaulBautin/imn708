# -*- coding: utf-8 -*-
import logging
import os


def verify_file_exists(filename):
    """
    Assert that file exists

    Parameters
    ----------
    filename: str
        Always provide parameter explanations.

    """
    if os.path.isfile(filename):
        file_was_found = True
    if not file_was_found:
        raise ValueError("Can't process this file, it was not found! \n{}"
                         .format(filename))


def verify_file_is_nifti(filename):
    """
    Assert that file is in nifti format

    Parameters
    ----------
    filename: str
        Always provide parameter explanations.

    """

    # Nifti = .nii or .nii.gz
    _, ext = os.path.splitext(filename)

    if ext not in ['.nii', '.gz']:
        logging.warning("Expected nifti file, but extension was not .nii or "
                        ".nii.gz. Continuing, but the loading will probably "
                        "fail!")