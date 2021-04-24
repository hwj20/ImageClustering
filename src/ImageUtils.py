import numpy as np
import matplotlib.pylab as plt
import skimage.io as io


def deal_multi_image(dir_path: str):
    extension_list = ['/*.jpeg', '/*.jpg', "/*.png", "/*.bmp"]
    filepath = dir_path
    for extension in extension_list:
        filepath = filepath + extension + ':'
    # filepath.pop()      # delete the last ':'
    print(filepath)
    coll = io.ImageCollection(filepath)
    print(len(coll))
    # plt.imshow(coll[0])
    # plt.imshow(np.array(coll[0]))
    # plt.show()

    return np.array(coll)


def deal_image(file_path: str):

    coll = io.ImageCollection(file_path)
    if len(coll) == 0:
        return
    img = np.array(coll[0])

    return


def deal_images(file_path: str):

   return