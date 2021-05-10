import os
import logging
import tkinter
import numpy as np
from imageio import imread
import matplotlib
from numpy import asarray
from PIL import Image
from matplotlib import pyplot as plt
matplotlib.use('TkAgg')
import morphsnakes as ms
matplotlib.use('TkAgg')

# in case you are running on machine without display, e.g. server
if os.environ.get('DISPLAY', '') == '':
    logging.warning('No display found. Using non-interactive Agg backend.')
    matplotlib.use('TkAgg')

#PATH_IMG = 'pseudo_4_max.png'

def visual_callback_2d(background, fig=None):
    """
    Returns a callback than can be passed as the argument `iter_callback`
    of `morphological_geodesic_active_contour` and
    `morphological_chan_vese` for visualizing the evolution
    of the levelsets. Only works for 2D images.
    Parameters
    ----------
    background : (M, N) array
        Image to be plotted as the background of the visual evolution.
    fig : matplotlib.figure.Figure
        Figure where results will be drawn. If not given, a new figure
        will be created.
    Returns
    -------
    callback : Python function
        A function that receives a levelset and updates the current plot
        accordingly. This can be passed as the `iter_callback` argument of
        `morphological_geodesic_active_contour` and
        `morphological_chan_vese`.
    """

    # Prepare the visual environment.
    if fig is None:
        fig = plt.figure()
    fig.clf()
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.imshow(background, cmap=plt.cm.gray)

    ax2 = fig.add_subplot(1, 2, 2)
    ax_u = ax2.imshow(np.zeros_like(background), vmin=0, vmax=1)
    plt.pause(0.001)

    def callback(levelset):

        if ax1.collections:
            del ax1.collections[0]
        ax1.contour(levelset, [0.5], colors='r')
        ax_u.set_data(levelset)
        fig.canvas.draw()
        plt.pause(0.001)

    return callback


def visual_callback_3d(fig=None, plot_each=1):
    """
    Returns a callback than can be passed as the argument `iter_callback`
    of `morphological_geodesic_active_contour` and
    `morphological_chan_vese` for visualizing the evolution
    of the levelsets. Only works for 3D images.
    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure where results will be drawn. If not given, a new figure
        will be created.
    plot_each : positive integer
        The plot will be updated once every `plot_each` calls to the callback
        function.
    Returns
    -------
    callback : Python function
        A function that receives a levelset and updates the current plot
        accordingly. This can be passed as the `iter_callback` argument of
        `morphological_geodesic_active_contour` and
        `morphological_chan_vese`.
    """

    from mpl_toolkits.mplot3d import Axes3D
    # PyMCubes package is required for `visual_callback_3d`
    try:
        import mcubes
    except ImportError:
        raise ImportError("PyMCubes is required for 3D `visual_callback_3d`")

    # Prepare the visual environment.
    if fig is None:
        fig = plt.figure()
    fig.clf()
    ax = fig.add_subplot(111, projection='3d')
    plt.pause(0.001)

    counter = [-1]

    def callback(levelset):

        counter[0] += 1
        if (counter[0] % plot_each) != 0:
            return

        if ax.collections:
            del ax.collections[0]

        coords, triangles = mcubes.marching_cubes(levelset, 0.5)
        ax.plot_trisurf(coords[:, 0], coords[:, 1], coords[:, 2],
                        triangles=triangles)
        plt.pause(0.1)

    return callback

def rgb2gray(img):
    """Convert a RGB image to gray scale."""
    return 0.2989 * img[..., 0] + 0.587 * img[..., 1] + 0.114 * img[..., 2]

def mri(PATH_IMG):
    """
    Example with `morphological_chan_vese` with using the default
    initialization of the level-set.
    """
    logging.info('Running: example_camera (MorphACWE)...')
    # Load the image.
    img = imread(PATH_IMG)/255.0
    # Callback for visual plotting
    callback = visual_callback_2d(img)
    # Morphological Chan-Vese (or ACWE)
    img=  ms.morphological_chan_vese(img, 35,
                               smoothing=3, lambda1=1, lambda2=1,
                               iter_callback=callback)
    return img



def matrixToImg(mat,target_path):
    imgarr = np.array(mat)
    imga = Image.fromarray(imgarr)
    imga.show()
    #imga = Image.fromarray(imgarr*255)
    imga.save(target_path)
    #imga.show()
    print(imga)
    print("Transformed Matrix to Image Synthesis completed")
    #return imgarr    

def generate_mask(PATH_IMG1,PATH_IMG2):
    image1 = mri(PATH_IMG1)
    image2 = mri(PATH_IMG2)
    print("image1 shape = ",image1.shape)
    print("image2 shape = ",image2.shape)
    morphed_array = []
    for x in range(len(image1)):
        row = []
        for y in range(len(image1[0])):
            #t = 255*255*(image1[x][y])*(image2[x][y])
            t = (image1[x][y])*(image2[x][y])
            row.append(t)
        morphed_array.append(row)
    #print(morphed_array)
    # Uncomment the following line to see a 3D example
    # This is skipped by default since mplot3d is VERY slow plotting 3d meshes
    # example_confocal3d()
    logging.info("Done.")
    #plt.show()
    return morphed_array

def boolean_mask(PATH_IMG1,PATH_IMG2):
    mat = generate_mask(PATH_IMG1,PATH_IMG2)
    mask = []
    for x in range(len(mat)):
        row = []
        for y in range(len(mat[0])):
            row.append(bool(mat[x][y]))
        mask.append(row)
    return mask

#if __name__ == '__main__':
logging.basicConfig(level=logging.DEBUG)
    
PATH_IMG1 = 'mask3.png'
PATH_IMG2 = 'mask4.png'
    #morphed_array = generate_mask(PATH_IMG1,PATH_IMG2)
    #mask = matrixToImg(morphed_array,"merged_mask.png")
morphed_array = boolean_mask(PATH_IMG1,PATH_IMG2)
mask = matrixToImg(morphed_array,"merged_mask_3x4.png")
#print(morphed_array)
"""
if __name__ == '__main__':
    image1 = mri(PATH_IMG1)
    image2 = mri(PATH_IMG2)
    print("image1 shape = ",image1.shape)
    print("image2 shape = ",image2.shape)
    image1_array = []
    for x in range(len(image1)):
        row = []
        for y in range(len(image1[0])):
            t = 255*255*(1-image1[x][y])
            row.append(t)
        image1_array.append(row)

    image2_array = []
    for x in range(len(image2)):
        row = []
        for y in range(len(image2[0])):
            t = 255*255*(1-image2[x][y])
            row.append(t)
        image2_array.append(row)

    #mask1 = matrixToImg(image1_array,"mask5.png")
    mask2 = matrixToImg(image2_array,"merger1to4.png")
    ""