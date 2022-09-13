# -*- coding: utf-8 -*-
import logging
import numpy as np
import matplotlib.pyplot as plt


def mip_img(img, range_axial, range_coronal, range_sagital, val_4d=None):
    """
    blabla
    method: str
        Should be either 'method1' or 'method2'
    """
    # Prepare image for the denoising
    img_data = np.asarray(img.get_fdata())
    img_shape = img_data.shape
    if len(img_shape) == 3:
        mip_axial = np.amin(img_data[:, :, range_axial[0]:range_axial[1]], axis=2)
        mip_coronal = np.amin(img_data[:, range_coronal[0]:range_coronal[1], :], axis=1)
        mip_sagital = np.amin(img_data[range_sagital[0]:range_sagital[1], :, :], axis=0)
    elif len(img_shape) == 4:
        mip_axial = np.amin(img_data[:, :, range_axial[0]:range_axial[1], val_4d], axis=2)
        mip_coronal = np.amin(img_data[:, range_coronal[0]:range_coronal[1], :, val_4d], axis=1)
        mip_sagital = np.amin(img_data[range_sagital[0]:range_sagital[1], :, :, val_4d], axis=0)
    return mip_axial, mip_coronal, mip_sagital

def MIP_img(img, range_axial, range_coronal, range_sagital, val_4d=None):
    """
    blabla
    method: str
        Should be either 'method1' or 'method2'
    """
    # Prepare image for the denoising
    img_data = np.asarray(img.get_fdata())
    img_shape = img_data.shape
    if len(img_shape) == 3:
        MIP_axial = np.amax(img_data[:,:,range_axial[0]:range_axial[1]], axis=2)
        MIP_coronal = np.amax(img_data[:,range_coronal[0]:range_coronal[1],:], axis=1)
        MIP_sagital = np.amax(img_data[range_sagital[0]:range_sagital[1],:,:], axis=0)
    elif len(img_shape) == 4:
        MIP_axial = np.amax(img_data[:,:,range_axial[0]:range_axial[1], val_4d], axis=2)
        MIP_coronal = np.amax(img_data[:,range_coronal[0]:range_coronal[1],:, val_4d], axis=1)
        MIP_sagital = np.amax(img_data[range_sagital[0]:range_sagital[1],:,:, val_4d], axis=0)
    return MIP_axial, MIP_coronal, MIP_sagital



def mip_MIP_viewr(img):
    """
    blabla
    method: str
        Should be either 'method1' or 'method2'
    """
    # Prepare image for the denoising
    img_data = np.asarray(img.get_fdata())
    img_shape = img_data.shape
    print(img_shape)
    mip_axial = np.amin(img_data, axis=2)
    mip_coronal = np.amin(img_data, axis=1)
    mip_sagital = np.amin(img_data, axis=0)
    MIP_axial = np.amax(img_data, axis=2)
    MIP_coronal = np.amax(img_data, axis=1)
    MIP_sagital = np.amax(img_data, axis=0)

    fig, ax = plt.subplots(2, 3)
    ax[0, 0].imshow(mip_axial.T, origin='lower')
    ax[0, 0].set_title("axial mip")
    ax[0, 1].imshow(mip_coronal.T, origin='lower')
    ax[0, 1].set_title("coronal mip")
    ax[0, 2].imshow(mip_sagital.T, origin='lower')
    ax[0, 2].set_title("sagital mip")
    ax[1, 0].imshow(MIP_axial.T, origin='lower')
    ax[1, 0].set_title("axial MIP")
    ax[1, 1].imshow(MIP_coronal.T, origin='lower')
    ax[1, 1].set_title("coronal MIP")
    ax[1, 2].imshow(MIP_sagital.T, origin='lower')
    ax[1, 2].set_title("sagital MIP")
    plt.show()
    #MIP = mp.max(img_data)



def use_img_to_create_something(img, use_method_y):
    """
    blabla
    use_method_y: bool
        If true, use method y. Else, use method x.
    """
    if use_method_y:
        logging.debug("Using method Y!")
        result = 1
    else:
        logging.debug("NOT using method Y!")
        result = 5

    return result
