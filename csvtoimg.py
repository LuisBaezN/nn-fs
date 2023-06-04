import sys

import pandas as pd
import numpy as np
from PIL import Image

if __name__ == "__main__":
    print("> Program initiated")

    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = 'train'

    data = pd.read_csv(f'DB/mnist_{name}.csv')

    data = np.array(data)
    m, n = data.shape

    if len(sys.argv) > 2:
        size = sys.argv[2]
    else:
        size = m

    for i in range(size):
        label = data[i,0]
        img = data[i,1:]
        t_img = img.reshape((28,28))

        image = Image.fromarray(t_img.astype('uint8'))
        image.save(f'DB{name}/img{i+1}-{label}.jpg')
        #image.show()

        porcentaje = ((i+1)*100)/size
        if porcentaje % 5 == 0:
            print(f'{int(porcentaje)}%')