#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is a description of the script. This description will appear in the help
when typing
>>> python view_image.py -h

To see the args received, a basic example can be:
>>> python view_image.py 'my_file.nii.gz' 1.0

The complete example can be:
>>> python view_image.py 'my_file.nii.gz' 1.0
        --optional_float 0.001 --optional_int 2
        --group_arg1 'Hello' --group_arg2 'You' --use_option_Y -v
"""

# First import basic python libraries
import argparse
import logging

# Then import yours.
# Encapsulate your methods in sub-files.
# Give them understandable names
# Import by alphabetical order for nicer view.
from matplotlib.pyplot import imshow

from functions.data_processing.rotate_image import rotate_image
from functions.utils.io import load_image
from functions.utils.manage_args import verify_file_exists, verify_file_is_nifti
from functions.utils.image import assert_same_shape
from functions.data_processing.translate_image import translate_image


def _build_arg_parser():
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter)

    p.add_argument('filename_I',
                   help="Image filename to be loaded. Image should be a nifti "
                        "file.")  # Always write a good explanation!
    p.add_argument('filename_J',
                   help="Image filename to be loaded. Image should be a nifti "
                        "file.")  # Always write a good explanation!

    # Typical arg: add debugging prints or not
    p.add_argument('-v', action='store_true', dest='verbose',
                   help='If set, produces verbose output.')

    return p


def main():
    parser = _build_arg_parser()
    args = parser.parse_args()
    print("****\n"
          "Args that were received in the main method: \n{}\n"
          "****".format(args))

    # 1. Verifications
    verify_file_exists(args.filename_I)
    from_nifti_i = verify_file_is_nifti(args.filename_I)
    verify_file_exists(args.filename_J)
    from_nifti_j = verify_file_is_nifti(args.filename_J)

    logging_level = 'DEBUG' if args.verbose else 'INFO'
    logging.basicConfig(level=logging_level)

    # 2. Load data
    logging.info("Loading data")
    img_I = load_image(args.filename_I, from_nifti_i)
    img_J = load_image(args.filename_J, from_nifti_j)
    ###########code should work with 2d image
    ###########code should work with one image as input
    # 3. Process data
    p = 200.5
    q = 300.5
    translate_image(img_I, p, q)
    rotate_image(img_I, 45)


if __name__ == "__main__":
    main()
