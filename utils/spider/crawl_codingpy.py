"""
关于图片的一些操作：
①图片转化为数组并存为二进制文件；
②从二进制文件中读取数据并重新恢复为图片
"""

from __future__ import print_function
import requests
import numpy as np
import PIL.Image as Image
import pickle as p
import matplotlib.pyplot as pyplot

# Required Packages
# 回归
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets, linear_model

# 热力图
import matplotlib.cm as cm
from matplotlib.colors import LogNorm
def crawl_article():
    urls = ('http://codingpy.com/page/{}'.format(i) for i in range(1, 100))
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }
    for url in urls:
        requests.get(url)
    response = requests.get(urls.__next__(), headers=headers)
    with open('page1.html', 'w') as f:
        f.write(response.text)


class Operation(object):
    image_base_path = "../images/"
    data_base_path = "../data/"

    def image_to_array(self, filenames):
        """
        图片转化为数组并存为二进制文件；
        :param filenames:文件列表
        :return:
        """
        n = filenames.__len__()  # 获取图片的个数
        result = np.array([])  # 创建一个空的一维数组
        print("开始将图片转为数组")
        for i in range(n):
            image = Image.open(self.image_base_path + filenames[i])
            r, g, b = image.split()  # rgb通道分离
            # 注意：下面一定要reshpae(1024)使其变为一维数组，否则拼接的数据会出现错误，导致无法恢复图片
            r_arr = np.array(r).reshape(1024)
            g_arr = np.array(g).reshape(1024)
            b_arr = np.array(b).reshape(1024)
            # 行拼接，类似于接火车；最终结果：共n行，一行3072列，为一张图片的rgb值
            image_arr = np.concatenate((r_arr, g_arr, b_arr))
            result = np.concatenate((result, image_arr))

        result = result.reshape((n, 3072))  # 将一维数组转化为count行3072列的二维数组
        print("转为数组成功，开始保存到文件")
        file_path = self.data_base_path + "data2.bin"
        with open(file_path, mode='wb') as f:
            p.dump(result, f)
        print("保存文件成功")

    def array_to_image(self, filename):
        """
        从二进制文件中读取数据并重新恢复为图片
        :param filename:
        :return:
        """
        with open(self.data_base_path + filename, mode='rb') as f:
            arr = p.load(f)  # 加载并反序列化数据
        rows = arr.shape[0]
        arr = arr.reshape(rows, 3, 32, 32)
        for index in range(rows):
            a = arr[index]
            # 得到RGB通道
            r = Image.fromarray(a[0]).convert('L')
            g = Image.fromarray(a[1]).convert('L')
            b = Image.fromarray(a[2]).convert('L')
            image = Image.merge("RGB", (r, g, b))
            # 显示图片
            pyplot.imshow(image)
            pyplot.show()
            image.save(self.image_base_path + "result" + str(index) + ".png", 'png')


def test1():
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt

    # arr = np.random.rand(3, 4)
    df_obj1 = pd.DataFrame([1,2,3],[3,2,1])
    print(df_obj1)

    def test(df):
        dfData = df.corr()
        plt.subplots(figsize=(9, 9))  # 设置画面大小
        sns.heatmap(dfData, annot=True, vmax=1, square=True, cmap="Blues")
        plt.savefig('../static/hot_map/BluesStateRelation.png')
        plt.show()
    test(df_obj1)


def test2():
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    from matplotlib.colors import LogNorm
    import numpy as np
    x, y = np.random.rand(10), np.random.rand(10)
    z = (np.random.rand(9000000) + np.linspace(0, 1, 9000000)).reshape(3000, 3000)
    plt.imshow(z + 10, extent=(np.amin(x), np.amax(x), np.amin(y), np.amax(y)),
               cmap=cm.hot, norm=LogNorm())
    plt.colorbar()
    plt.show()


class Test3(object):
    """
    Created on Fri Nov 10 21:20:25 2017

    @author: zhoulei
    """
    def __init__(self):
        self.array = [
            [1, 0, 0, 0, 0, 0, 00],
            [0, 2, 0, 0, 0, 0, 00],
            [0, 0, 3, 3, 3, 3, 3],
            [1, 2, 0, 5, 7, 2, 10],
            [1, 3, 0, 5, 7, 2, 10],
            [5, 2, 0, 7, 7, 2, 1],
            [1, 2, 0, 5, 7, 2, 10],
        ]
        self.array2 = np.array(self.array)

    # Function to get data
    def get_data(self, file_name, hour):
        data = pd.read_csv(file_name)
        X_parameter = []
        Y_parameter = []
        Z_parameter = []
        coln = 'wind_' + str(hour)
        for x, y, z in zip(data['x'], data['y'], data[coln]):
            X_parameter.append(int(x))
            Y_parameter.append(int(y))
            Z_parameter.append(float(z))
        return X_parameter, Y_parameter, Z_parameter

        # Function to show Thermodynamic diagram

    def draw_thermodynamic_diagram(self, fileName, hour):
        print(fileName, hour)

        x, y, z = self.get_data(fileName, hour)
        x_min = np.min(x)
        x_max = np.max(x)
        y_min = np.min(y)
        y_max = np.max(y)

        height = y_max - y_min + 1
        width = x_max - x_min + 1
        arr = np.zeros((height, width))  # arr 热力图中的值阵

        for i in range(len(x)):
            arr[y[i] - y_min, x[i] - x_min] = z[i]

            # 热力图默认左上为0,0
            # 所以热力图的显示和arr是一致的
            # 未解决以左下为0,0,
        plt.imshow(arr, extent=(np.amin(x), np.amax(x), np.amax(y), np.amin(y)),
                   cmap=cm.hot, norm=LogNorm())
        plt.colorbar()
        plt.savefig(fileName + '_h' + str(hour) + '.png')  # 先存，再show
        plt.show()

    def run(self):
        for date in range(1, 6):
            fileName = 'compress_reProcess_day' + str(date) + '.csv'
            for hour in range(9, 21):
                self.draw_thermodynamic_diagram(fileName, hour)

    def test1(self):
        plt.matshow(self.array2, cmap='hot')
        plt.colorbar()
        plt.show()

if __name__ == "__main__":
    # test2()
    t = Test3()
    t.test1()
