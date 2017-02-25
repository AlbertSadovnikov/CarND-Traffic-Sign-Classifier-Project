import os
import sys
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

if os.path.exists('./data'):
    print('data folder already exists')
    sys.exit(0)

os.mkdir('./data')

data_url = 'https://d17h27t6h515a5.cloudfront.net/topher/2017/February/5898cd6f_traffic-signs-data/traffic-signs-data' \
           '.zip '

print('Downloading and extracting %s' % data_url)

with urlopen(data_url) as zip_resp:
    with ZipFile(BytesIO(zip_resp.read())) as zip_file:
        zip_file.extractall('./data')
