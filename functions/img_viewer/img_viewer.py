# -*- coding: utf-8 -*-
import logging
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RangeSlider, Button
import numpy as np

from functions.data_processing.compute_mip import mip_img, MIP_img



def viewer(img):
    """
    Inspired by https://matplotlib.org/stable/gallery/widgets/slider_demo.html
    method: str
        Should be either 'method1' or 'method2'
    """
    # Prepare image for the denoising
    img_data = img.get_fdata()
    img_shape = np.asarray(img_data.shape)
    print(img_shape)
    if len(img_shape) == 3:
        viewer3d(img_data, img_shape, img)
        logging.info("3d data")
    elif len(img_shape) == 4:
        viewer4d(img_data, img_shape, img)
        logging.info("4d data")
    else:
        logging.error("image is neither 3D or 4D")


def viewer3d(img_data, img_shape, img):
    """
    blabla
    use_method_y: bool
        If true, use method y. Else, use method x.
    """
    # Define initial parameters
    pos_init = img_shape // 2
    range_axial, range_coronal, range_sagital = [25,30], [25,30], [25,30]

    fig, ax = plt.subplots(1, 3)
    img_view_axial = ax[0].imshow(img_data[:, :, pos_init[2]].T, origin='lower')
    ax[0].set_title("Axial slice of image")
    img_view_coronal = ax[1].imshow(img_data[:, pos_init[1], :].T, origin='lower')
    ax[1].set_title("Coronal slice of image")
    img_view_sagital = ax[2].imshow(img_data[pos_init[0], :, :].T, origin='lower')
    ax[2].set_title("Sagital slice of image")

    # adjust the main plot to make room for the sliders
    plt.subplots_adjust(bottom=0.5)

    # Make a horizontal slider to control the position.
    axPos_axial = plt.axes([0.25, 0.1, 0.65, 0.03])
    pos_slider_axial = RangeSlider(
        ax=axPos_axial,
        label='Slice position [axial]',
        valmin=0,
        valmax=img_shape[2] - 1,
        valstep=1,
    )
    # Make a horizontal slider to control the position.
    axPos_coronal = plt.axes([0.25, 0.2, 0.65, 0.03])
    pos_slider_coronal = RangeSlider(
        ax=axPos_coronal,
        label='Slice position [coronal]',
        valmin=0,
        valmax=img_shape[1] - 1,
        valstep=1,
    )
    # Make a horizontal slider to control the position.
    axPos_sagital = plt.axes([0.25, 0.3, 0.65, 0.03])
    pos_slider_sagital = RangeSlider(
        ax=axPos_sagital,
        label='Slice position [sagital]',
        valmin=0,
        valmax=img_shape[0] - 1,
        valstep=1,
    )
    # Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
    mip_button = plt.axes([0.15, 0.01, 0.3, 0.05])
    button_mip = Button(mip_button, 'View mip', hovercolor='0.975')
    # Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
    MIP_button = plt.axes([0.55, 0.01, 0.3, 0.05])
    button_MIP = Button(MIP_button, 'View MIP', hovercolor='0.975')

    # The function to be called anytime a slider's value changes
    def view_mip(event):
        range_axial = [int(pos_slider_axial.val[0]), int(pos_slider_axial.val[1])]
        range_coronal = [int(pos_slider_coronal.val[0]), int(pos_slider_coronal.val[1])]
        range_sagital = [int(pos_slider_sagital.val[0]), int(pos_slider_sagital.val[1])]
        mip_axial, mip_coronal, mip_sagital = mip_img(img, range_axial, range_coronal, range_sagital)
        img_view_axial.set_data(mip_axial.T)
        img_view_coronal.set_data(mip_coronal.T)
        img_view_sagital.set_data(mip_sagital.T)
        fig.canvas.draw_idle()

    # The function to be called anytime a slider's value changes
    def view_MIP(event):
        range_axial = [int(pos_slider_axial.val[0]), int(pos_slider_axial.val[1])]
        range_coronal = [int(pos_slider_coronal.val[0]), int(pos_slider_coronal.val[1])]
        range_sagital = [int(pos_slider_sagital.val[0]), int(pos_slider_sagital.val[1])]
        MIP_axial, MIP_coronal, MIP_sagital = MIP_img(img, range_axial, range_coronal, range_sagital)
        img_view_axial.set_data(MIP_axial.T)
        img_view_coronal.set_data(MIP_coronal.T)
        img_view_sagital.set_data(MIP_sagital.T)
        fig.canvas.draw_idle()


    # The function to be called anytime a slider's value changes
    def update(val):
        img_view_axial.set_data(img_data[:, :, int(pos_slider_axial.val[0])].T)
        img_view_coronal.set_data(img_data[:, int(pos_slider_coronal.val[0]), :].T)
        img_view_sagital.set_data(img_data[int(pos_slider_sagital.val[0]), :, :].T)
        fig.canvas.draw_idle()

    # register the update function with each slider
    button_mip.on_clicked(view_mip)
    button_MIP.on_clicked(view_MIP)
    pos_slider_axial.on_changed(update)
    pos_slider_coronal.on_changed(update)
    pos_slider_sagital.on_changed(update)
    plt.show()


def viewer4d(img_data, img_shape, img):
    """
    blabla
    use_method_y: bool
        If true, use method y. Else, use method x.
    """
    # Define initial parameters
    pos_init = img_shape // 2

    fig, ax = plt.subplots(1, 3)
    img_view_axial = ax[0].imshow(img_data[:, :, pos_init[2], pos_init[3]].T, origin='lower')
    ax[0].set_title("Axial slice of image")
    img_view_coronal = ax[1].imshow(img_data[:, pos_init[1], :, pos_init[3]].T, origin='lower')
    ax[1].set_title("Coronal slice of image")
    img_view_sagital = ax[2].imshow(img_data[pos_init[0], :, :, pos_init[3]].T, origin='lower')
    ax[2].set_title("Sagital slice of image")

    # adjust the main plot to make room for the sliders
    plt.subplots_adjust(bottom=0.5)

    # Make a horizontal slider to control the position.
    axPos_axial = plt.axes([0.25, 0.1, 0.65, 0.03])
    pos_slider_axial = RangeSlider(
        ax=axPos_axial,
        label='Slice position [axial]',
        valmin=0,
        valmax=img_shape[2] - 1,
        valstep=1,
    )
    # Make a horizontal slider to control the position.
    axPos_coronal = plt.axes([0.25, 0.2, 0.65, 0.03])
    pos_slider_coronal = RangeSlider(
        ax=axPos_coronal,
        label='Slice position [coronal]',
        valmin=0,
        valmax=img_shape[1] - 1,
        valstep=1,
    )
    # Make a horizontal slider to control the position.
    axPos_sagital = plt.axes([0.25, 0.3, 0.65, 0.03])
    pos_slider_sagital = RangeSlider(
        ax=axPos_sagital,
        label='Slice position [sagital]',
        valmin=0,
        valmax=img_shape[0] - 1,
        valstep=1,
    )
    # Make a horizontal slider to control the position.
    axPos_4d = plt.axes([0.25, 0.4, 0.65, 0.03])
    pos_slider_4d = Slider(
        ax=axPos_4d,
        label='Slice position [4d]',
        valmin=0,
        valmax=img_shape[3] - 1,
        valinit=0,
        valstep=1,
    )

    # Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
    mip_button = plt.axes([0.15, 0.01, 0.3, 0.05])
    button_mip = Button(mip_button, 'View mip', hovercolor='0.975')
    # Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
    MIP_button = plt.axes([0.55, 0.01, 0.3, 0.05])
    button_MIP = Button(MIP_button, 'View MIP', hovercolor='0.975')

    # The function to be called anytime a slider's value changes
    def view_mip(event):
        range_axial = [int(pos_slider_axial.val[0]), int(pos_slider_axial.val[1])]
        range_coronal = [int(pos_slider_coronal.val[0]), int(pos_slider_coronal.val[1])]
        range_sagital = [int(pos_slider_sagital.val[0]), int(pos_slider_sagital.val[1])]
        val_4d = int(pos_slider_4d.val)
        mip_axial, mip_coronal, mip_sagital = mip_img(img, range_axial, range_coronal, range_sagital, val_4d)
        img_view_axial.set_data(mip_axial.T)
        img_view_coronal.set_data(mip_coronal.T)
        img_view_sagital.set_data(mip_sagital.T)
        fig.canvas.draw_idle()

    # The function to be called anytime a slider's value changes
    def view_MIP(event):
        range_axial = [int(pos_slider_axial.val[0]), int(pos_slider_axial.val[1])]
        range_coronal = [int(pos_slider_coronal.val[0]), int(pos_slider_coronal.val[1])]
        range_sagital = [int(pos_slider_sagital.val[0]), int(pos_slider_sagital.val[1])]
        val_4d = int(pos_slider_4d.val)
        MIP_axial, MIP_coronal, MIP_sagital = MIP_img(img, range_axial, range_coronal, range_sagital, val_4d)
        img_view_axial.set_data(MIP_axial.T)
        img_view_coronal.set_data(MIP_coronal.T)
        img_view_sagital.set_data(MIP_sagital.T)
        fig.canvas.draw_idle()

    # The function to be called anytime a slider's value changes
    def update(val):
        img_view_axial.set_data(img_data[:, :, int(pos_slider_axial.val[0]), int(pos_slider_4d.val)].T)
        img_view_coronal.set_data(img_data[:, int(pos_slider_coronal.val[0]), :, int(pos_slider_4d.val)].T)
        img_view_sagital.set_data(img_data[int(pos_slider_sagital.val[0]), :, :, int(pos_slider_4d.val)].T)
        fig.canvas.draw_idle()

    # register the update function with each slider
    button_mip.on_clicked(view_mip)
    button_MIP.on_clicked(view_MIP)
    pos_slider_4d.on_changed(update)
    pos_slider_axial.on_changed(update)
    pos_slider_coronal.on_changed(update)
    pos_slider_sagital.on_changed(update)
    plt.show()

