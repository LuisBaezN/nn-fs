import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":
    print("> Program initiated")
    data = pd.read_csv('DB/mnist_train.csv')

    size = 1_000

    data = np.array(data)
    m, n = data.shape

    data_sample = data[0:size].T
    data_filtrated = data_sample[1:n]
    data_filtrated = data_filtrated / 255.

    for i in range(3):
        current_image = data_filtrated[:, i, None]
        current_image = current_image.reshape((28, 28)) * 255
        plt.gray()
        plt.imshow(current_image, interpolation='nearest')
        #plt.show()
        plt.savefig(f'images/{i}.png', bbox_inches='tight')