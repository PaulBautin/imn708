# -*- coding: utf-8 -*-
import logging
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from mpl_toolkits import mplot3d


def trans_rigid():
    xv, yv, zv = generate_3d_grid()
    transformation = transfo(xv, yv, zv, theta=0, omega=0, phi=0, p=0, q=0, r=0)
    apply_transfo(xv, yv, zv, transformation)
    similitude(xv, yv, zv, s=5)


def generate_3d_grid():
    """
    blabla
    method: str
        Should be either 'method1' or 'method2'
    """
    x = np.arange(0, 20)
    y = np.arange(0, 20)
    z = np.arange(0, 5)
    xv, yv, zv = np.meshgrid(x, y, z)
    return xv, yv, zv


def transfo(xv, yv, zv, theta=0, omega=0, phi=0, p=0, q=0, r=0):
    """
    blabla
    method: str
        Should be either 'method1' or 'method2'
    """
    rot_x = np.matrix([[1, 0, 0, 0], [0, np.cos(theta), np.sin(theta), 0], [0, -np.sin(theta), np.cos(theta), 0], [0, 0, 0, 1]])
    rot_y = np.matrix([[np.cos(omega), 0, -np.sin(omega), 0], [0, 1, 0, 0], [np.sin(omega), 0, np.cos(omega), 0], [0, 0, 0, 1]])
    rot_z = np.matrix([[np.cos(phi), -np.sin(phi), 0, 0], [np.sin(phi), np.cos(phi), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    t = np.matrix([[1, 0, 0, p], [0, 1, 0, q], [0, 0, 1, r], [0, 0, 0, 0]])
    transformation = rot_x @ rot_y @ rot_z + t
    return transformation


def apply_transfo(xv, yv, zv, transformation):
    """
    blabla
    method: str
        Should be either 'method1' or 'method2'
    """
    # fig = plt.figure(figsize=(12, 12))
    ax = plt.axes(projection='3d')
    xv_t = transformation[0, 0] * xv + transformation[0, 1] * yv + transformation[0, 2] * zv + transformation[0, 3]
    yv_t = transformation[1, 0] * xv + transformation[1, 1] * yv + transformation[1, 2] * zv + transformation[1, 3]
    zv_t = transformation[2, 0] * xv + transformation[2, 1] * yv + transformation[2, 2] * zv + transformation[2, 3]
    ax.scatter3D(xv_t, yv_t, zv_t)
    plt.show()


def similitude(xv, yv, zv, s):
    """
    blabla
    method: str
        Should be either 'method1' or 'method2'
    """
    # fig = plt.figure(figsize=(12, 12))
    ax = plt.axes(projection='3d')
    xv_t = s * xv
    yv_t = s * yv
    zv_t = s * zv
    ax.scatter3D(xv_t, yv_t, zv_t)
    plt.show()



def plot_hist2d(hist_2d, xedges, yedges, img_I, img_J):
    fig, ax = plt.subplots(1,3, figsize=(17,5))
    i = ax[0].imshow(img_I)
    ax[0].set_title("image I")
    ax[0].set_xlabel("position x")
    ax[0].set_ylabel("position y")
    j = ax[1].imshow(img_J)
    ax[1].set_title("image J")
    ax[1].set_xlabel("position x")
    ax[1].set_ylabel("position y")
    hist = ax[2].imshow(hist_2d, interpolation='nearest', origin='lower', extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], norm=colors.LogNorm())
    ax[2].set_title("joint histogram")
    ax[2].set_xlabel("image I intensity")
    ax[2].set_ylabel("image J intensity")
    plt.colorbar(i, ax=ax[0], shrink=0.8)
    plt.colorbar(j, ax=ax[1], shrink=0.8)
    plt.colorbar(hist, ax=ax[2], shrink=0.8)
    plt.show()


def assert_sum(hist_2d, img):
    print(img.shape[0]*img.shape[1])
    if np.sum(hist_2d) == img.shape[0]*img.shape[0]:
        print("Histogram is of right shape!")
    else:
        print("Histogram is not of right shape.")




