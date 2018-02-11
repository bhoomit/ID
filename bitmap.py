import PIL
import requests
import numpy as np
from io import StringIO
import scipy.misc

rows = [26, 26, 26, 26, 24]
matrix = np.empty((0, 128, 3), int)
url = "https://www.random.org/integers/?num={0}&min=0&max=255&col=384&base=10&format=plain&rnd=new"
for r in rows:
    response = requests.get(url.format(r * 128 * 3)) # 128 cols * 3 RGB
    string = StringIO(response.text)
    matrix = np.append(matrix, np.loadtxt(string))
matrix = np.reshape(matrix, (128, 128, 3))
scipy.misc.imsave('outfile.bmp', matrix)
# scipy.misc.imshow(matrix)
