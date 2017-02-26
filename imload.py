import cv2
import pandas as pd
import os
import matplotlib.pyplot as plt
# read data from gt.txt

test_table = pd.read_csv('images/gt.csv')
for _, row in test_table.iterrows():
    img = cv2.resize(cv2.imread(os.path.join('images', row['File']), cv2.IMREAD_COLOR), (32, 32))
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.show()
    break
