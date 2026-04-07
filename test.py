import os
import path
import datetime
import math
import numpy as np
import time
import cv2 as opencv
import random
import matplotlib.pyplot as plt
with os.scandir('.') as entries:
    print(entries)          # <scandir_iterator object at 0x0000021B8C8F3B80>
    for entry in entries:
        print(entry)          # DirEntry object
        print(entry.name)     # file/folder name
        print(entry.is_file())  # True if it's a file
        print(entry.is_dir())   # True if it's a directory
'''
histogram = [1, 2, 3, 4, 5]
plt.hist(histogram, bins=5, edgecolor='black',histtype='barstacked',density=True)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
current_direct = os.getcwd()
print(current_direct)
print(os.listdir(current_direct))
with open('test.js', 'a') as f:
    f.write('console.log("Hello, World!");')
print("File written successfully.")
print(random.randint(2,10))
print(random.choice(['apple', 'banana', 'cherry']))
print(random.sample([1, 2, 3, 4, 5], 3))
print(random.random())
print(random.uniform(1.5, 3.5))
print(random.shuffle([1, 2, 3, 4, 5]))
print(random.seed(42))
print(time.time())
print(time.ctime())
print(time.sleep(2))'''
img = opencv.imread("C:\\Users\\hpdre\\Pictures\\projectimage\\spacedebris1.jpg")
'''
s = opencv.resize(img,(1000,500))
np_img = np.array(img)
np_i = np.array(s)
print(np_i.shape)
print(np_img.shape)
print(np_img.dtype)
print(np_img)
opencv.imshow("This is image",img)
opencv.waitKey(10000)'''
print(opencv.imencode('.jpg', img)[0])
print(opencv.imencode('.jpg', img)[1])
print(opencv.imencode('.jpg', img)[1].shape)
print(opencv.imencode('.jpg', img)[1].dtype)
