import os
import struct
import png
from array import array

# 文件路径
train_images = "./test/mnist_data/MNIST_train-images-idx3-ubyte"
train_labels = './test/mnist_data/MNIST_train-labels-idx1-ubyte'
# test_images = './t10k-images-idx3-ubyte'
# test_labels = './t10k-labels-idx1-ubyte'
train_folder = '/test/mnist_data/train'
# test_folder = './test'

# 创建目录
if not os.path.exists(train_folder):
    os.makedirs(train_folder)
# if not os.path.exists(test_folder):
#     os.makedirs(test_folder)

train_folders = [os.path.join(train_folder, str(i)) for i in range(10)]
# test_folders = [os.path.join(test_folder, str(i)) for i in range(10)]

for dir in train_folders:
    if not os.path.exists(dir):
        os.makedirs(dir)
# for dir in test_folders:
#     if not os.path.exists(dir):
#         os.makedirs(dir)

# 打开文件
train_imgs = open(train_images, 'rb') # 以二进制读模式打开文件
train_labs = open(train_labels, 'rb')
# test_imgs = open(test_images, 'rb')
# test_labs = open(test_labels, 'rb')

# 读取数据
struct.unpack('>IIII', train_imgs.read(16)) # 大端模式，每次读取16字节
struct.unpack('>II', train_labs.read(8)) # 大端模式，每次读取8字节
# struct.unpack('>IIII', test_imgs.read(16))
# struct.unpack('>II', test_labs.read(8))

train_img = array('B', train_imgs.read()) # 无符号字节array数组类型
train_lab = array('b', train_labs.read()) # 有符号字节array数据类型
# test_img = array('B', test_imgs.read())
# test_lab = array('b', test_labs.read())

train_imgs.close() # 关闭文件
train_labs.close()
# test_imgs.close()
# test_imgs.close()

# 保存图像
for (i, label) in enumerate(train_lab):
    filename = os.path.join(train_folders[label], str(i) + '.png')
    print('writing ' + filename)
    with open(filename, 'wb') as img:
        image = png.Writer(28, 28, greyscale=True)
        data = [train_img[(i*28*28 + j*28) : (i*28*28 + (j+1)*28)] for j in range(28)]
        image.write(img, data) # 保存训练图像

"""        
for (i, label) in enumerate(test_lab):
    filename = os.path.join(test_folders[label], str(i) + '.png')
    print('writing ' + filename)
    with open(filename, 'wb') as img:
        image = png.Writer(28, 28, greyscale=True)
        data = [test_img[(i*28*28 + j*28) : (i*28*28 + (j+1)*28)] for j in range(28)]
        image.write(img, data) # 保存测试图像
"""