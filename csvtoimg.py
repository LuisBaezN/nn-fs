import pandas as pd
import numpy as np
from PIL import Image
#from matplotlib import pyplot as plt

if __name__ == "__main__":
    print("> Program initiated")
    data = pd.read_csv('DB/mnist_train.csv')

    size = 60_000 # 1_000

    data = np.array(data)
    m, n = data.shape

    for i in range(size):
        label = data[i,0]
        img = data[i,1:]
        t_img = img.reshape((28,28))

        image = Image.fromarray(t_img.astype('uint8'))
        image.save(f'DBi/img{i+1}-{label}.jpg')
        #image.show()

        porcentaje = ((i+1)*100)/size
        if porcentaje % 5 == 0:
            print(f'{int(porcentaje)}%')