import matplotlib
import numpy
import numpy as np
import matplotlib.pylab as plt
import skimage.io as io


def read_image(path: str):
    coll = io.ImageCollection(path)
    print(len(coll))
    # plt.imshow(coll[0])
    plt.imshow(numpy.array(coll[0]))
    plt.show()


read_image("test/*.jpeg")

