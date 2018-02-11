import requests
import numpy as np
from io import StringIO
import scipy.io.wavfile

rate = 500
channels = 3
seconds = 3
url = "https://www.random.org/integers/?num={0}&min=100000&max=1000000000&col=1&base=10&format=plain&rnd=new"
response = requests.get(url.format(rate * seconds * channels))
data = np.loadtxt(StringIO(response.text))
data = np.reshape(data, (rate*seconds, channels))
scipy.io.wavfile.write('outfile.wav', rate, data)
