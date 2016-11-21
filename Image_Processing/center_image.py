"""
Center images
~~~~~~~~~~~~~~~~
A module to crop and center images. This is a necessary preprocessing step for
the input data to resemble training data.
"""


import numpy as np


def add_padding(img, pad_t, pad_r, pad_b, pad_l):
    """Add padding of zeroes to an image.
    Add padding to an array image.

    :param ndarray img: Numpy array of input image which needs to be padded by
        zeros
    :param int pad_t: Number of pixels of paddding on top of the image
    :param int pad_r: Number of pixels of paddding beneath of the image
    :param int pad_b: Number of pixels of paddding to the right of the image
    :param int pad_l: Number of pixels of paddding to the left of the image

    :return: Numpy array of padded image
    """
    height, width = img.shape

    # Adding padding to the left side.
    pad_left = np.zeros((height, pad_l), dtype=np.int)
    img = np.concatenate((pad_left, img), axis=1)

    # Adding padding to the top.
    pad_up = np.zeros((pad_t, pad_l + width))
    img = np.concatenate((pad_up, img), axis=0)

    # Adding padding to the right.
    pad_right = np.zeros((height + pad_t, pad_r))
    img = np.concatenate((img, pad_right), axis=1)

    # Adding padding to the bottom
    pad_bottom = np.zeros((pad_b, pad_l + width + pad_r))
    img = np.concatenate((img, pad_bottom), axis=0)

    return img


def center_image(img):
    """Return a centered image.

    :param ndarray img: Numpy array of input image which needs to be centered

    :return: Centered image's Numpy array
    """
    col_sum = np.where(np.sum(img, axis=0) > 0)
    row_sum = np.where(np.sum(img, axis=1) > 0)
    y1, y2 = row_sum[0][0], row_sum[0][-1]
    x1, x2 = col_sum[0][0], col_sum[0][-1]

    cropped_image = img[y1 - 1:y2 + 1, x1 - 1:x2 + 1]
    zero_axis_fill = (27 - cropped_image.shape[0])
    one_axis_fill = (27 - cropped_image.shape[1])

    top = zero_axis_fill / 2 + 1
    bottom = zero_axis_fill - top + 1
    left = one_axis_fill / 2 + 1
    right = one_axis_fill - left + 1
    padded_image = add_padding(cropped_image, int(top),
                               int(right), int(bottom), int(left))

    return padded_image