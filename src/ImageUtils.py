import numpy as np
import matplotlib.pylab as plt
import skimage.io as io
import Kmeans


def deal_multi_image(dir_path: str, step: int):
    extension_list = ['/*.jpeg', '/*.jpg', "/*.png", "/*.bmp"]
    filepath = dir_path
    for extension in extension_list:
        filepath = dir_path + extension
        coll = io.ImageCollection(filepath)
        if len(coll) != 0:
            deal_image(filepath, step, False, True)
            print(len(coll))
    return 1


def deal_image(file_path: str, step: int, to_show: bool, to_save: bool):
    coll = io.ImageCollection(file_path)
    if len(coll) == 0:
        return
    for index in range(len(coll)):
        img = np.array(coll[index])
        dx = int(img.shape[0] / step)
        dy = int(img.shape[1] / step)
        features = []
        for x in range(step):
            for y in range(step):
                Y = np.mean(img[x * dx:(x + 1) * dx, y * dy:(y + 1) * dy, 0])
                U = np.mean(img[x * dx:(x + 1) * dx, y * dy:(y + 1) * dy, 1])
                V = np.mean(img[x * dx:(x + 1) * dx, y * dy:(y + 1) * dy, 2])
                features.append([Y, U, V])
        # i = img.reshape(img.shape[0] * img.shape[1], 3)
        i = features
        (index_in_center, center) = Kmeans.kMeans(i, Kmeans.ecludDist, Kmeans.randCenter(i, 3), 3)
        res = []
        for j in index_in_center:
            res.append(center[j])
        print(res)
        ni = np.zeros((img.shape[0], img.shape[1], 3))
        for n in range(len(res)):
            for x in range(dx):
                for y in range(dy):
                    ni[int(n / step) * dx + x, n % step * dy + y] = [x / 255 for x in res[n]]
        print(res)
        if to_show:
            plt.imshow(ni)
            plt.axis('off')
            plt.show()
        if to_save:
            plt.imshow(ni)
            new_name = file_path.split('.')
            new_name[0] = new_name[0] + str(index) + '-' + str(step) + '.'
            new_name = "".join(new_name)
            plt.axis('off')
            plt.savefig(new_name)


def deal_images(dir_path: str):
    extension_list = ['/*.jpeg', '/*.jpg', "/*.png", "/*.bmp"]
    filepath = dir_path
    for extension in extension_list:
        filepath = dir_path + extension
        coll = io.ImageCollection(filepath)
        if len(coll) != 0:
            arr = np.array(coll)
            arr.reshape(arr.shape[0], arr.shape[1]*arr.shape[2])
    return
