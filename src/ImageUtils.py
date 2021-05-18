import numpy as np
import os
import matplotlib.pylab as plt
import skimage.io as io
import Kmeans
from enum import Enum


class ReturnCode(Enum):
    SUC = 0
    NO_SUCH_FILE = -1
    INVALID_STEPS = 1
    INVALID_DOTS = 2


def deal_multi_image(dir_path: str, step: int):
    extension_list = ['/*.jpeg', '/*.jpg', "/*.png", "/*.bmp"]
    filepath = dir_path
    for extension in extension_list:
        filepath = dir_path + extension
        coll = io.ImageCollection(filepath)
        if len(coll) != 0:
            deal_image(filepath, step, False, True)
            print(len(coll))
    return ReturnCode.SUC


def deal_image(file_path: str, step: int, dots: int, to_show: bool, to_save: bool, dist_fun_str: str, random: bool):
    coll = io.ImageCollection(file_path)
    if len(coll) == 0:
        return ReturnCode.NO_SUCH_FILE
    for index in range(len(coll)):
        img = np.array(coll[index])
        dx = int(img.shape[0] / step)
        dy = int(img.shape[1] / step)
        if dx == 0 or dy == 0 or step <= 0:
            return ReturnCode.INVALID_STEPS
        if dots == 0 or dots >= img.shape[0] * img.shape[1]:
            return ReturnCode.INVALID_DOTS
        features = []
        for x in range(step):
            for y in range(step):
                Y = np.mean(img[x * dx:(x + 1) * dx, y * dy:(y + 1) * dy, 0])
                U = np.mean(img[x * dx:(x + 1) * dx, y * dy:(y + 1) * dy, 1])
                V = np.mean(img[x * dx:(x + 1) * dx, y * dy:(y + 1) * dy, 2])
                features.append([Y, U, V])
        # i = img.reshape(img.shape[0] * img.shape[1], 3)
        i = features
        dist_fun = str == Kmeans.ecludDist if dist_fun_str == 'ecludDist' else Kmeans.manhattanDist
        (index_in_center, center) = Kmeans.kMeans(i, dist_fun,
                                                  Kmeans.randCenter(i, dots) if random else Kmeans.randCenter(i, dots),
                                                  dots)
        res = []
        for j in index_in_center:
            res.append(center[j])
        print(res)
        ni = np.zeros((img.shape[0], img.shape[1], 3))
        for n in range(len(res)):
            for x in range(dx):
                for y in range(dy):
                    ni[int(n / step) * dx + x, n % step * dy + y] = [x / 255 for x in res[n]]

        if to_show:
            plt.imshow(ni)
            plt.axis('off')
            plt.show()
        if to_save:
            plt.imshow(ni)
            plt.axis('off')
            new_name = file_path.split('.')
            new_name[0] = new_name[0] + '-' + str(index) + '-' + str(step) + '.'
            new_name = "".join(new_name)
            plt.savefig(new_name)
    return ReturnCode.SUC


def deal_images(dir_path: str, save: bool, dist_fun_str: str, random: bool, dots: int):
    extension_list = ['/*.jpeg', '/*.jpg', "/*.png", "/*.bmp"]
    k = dots
    filepath = dir_path
    for extension in extension_list:
        filepath = dir_path + extension
        coll = io.ImageCollection(filepath)
        if len(coll) != 0:
            img_array = np.array(coll[0])
            arr = np.empty((0, img_array.shape[0] * img_array.shape[1],
                            1 if len(img_array.shape) != 3 else img_array.shape[2]))
            for img in coll:
                img_array = np.array(img)
                img_array = img_array.reshape(img_array.shape[0] * img_array.shape[1]
                                              , 1 if len(img_array.shape) != 3 else img_array.shape[2])
                arr = np.concatenate((arr, [img_array]), axis=0)
            dist_fun = str == Kmeans.ecludDist if dist_fun_str == 'ecludDist' else Kmeans.manhattanDist
            (index_in_center, center) = Kmeans.kMeans(arr, dist_fun,
                                                      Kmeans.orderCenter(arr, k) if not random else Kmeans.randCenter(
                                                          arr, k), k)
            # (index_in_center, center) = Kmeans.mul_kMeans(arr, dist_fun, 3, 10)
            for i in range(center.shape[0]):
                s_dir = dir_path + '/imageClass' + str(i)
                if not os.path.exists(s_dir):
                    os.makedirs(s_dir)
                if save:
                    img_form = np.array(coll[0]).shape
                    plt.imshow(np.array(center[i]).reshape(img_form[0], img_form[1],
                                                           img_form[2] if len(img_form) == 3 else 1))
                    plt.axis('off')
                    # plt.show()
                    plt.savefig(s_dir + '/imageOfClass' + str(i) + '.' + extension.split('.')[1])
            for i in range(len(coll)):
                s_dir = dir_path + '/imageClass' + str(index_in_center[i]) + '/' + str(i) + '.' + extension.split('.')[
                    1]
                plt.imshow(coll[i])
                plt.axis('off')
                plt.savefig(s_dir)

    return ReturnCode.SUC
