import numpy as np
from PIL import Image, ImageEnhance
import os
import shutil
import time

def new_dir(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.makedirs(dir)

def get_file(dir):
    for file in os.listdir(dir):
        if file.endswith(".jpg"):
            return file

def create_resized(dir):
    img = Image.open(f"{dir}/{get_file(dir)}")
    for i in range(11):
        size = 2**i
        img.resize((size, size)).save(f"{dir}/{size}.jpg")

#-------------------------------------------------------------------------------

def enhance(path, res):
    img = Image.open(path)
    init_res = img.size[0]
    new_dir("output")
    shutil.copy(path, f"output/original-{img.size[0]}.jpg")

    while img.size[0]*2 <= res:
        arr = np.array(img)
        new_arr = np.zeros((arr.shape[0]*2, arr.shape[1]*2, 3), dtype=np.uint8)
        max_i = arr.shape[0]-1
        max_j = arr.shape[1]-1
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                new_arr[i*2, j*2] = np.average((
                    arr[i-(i>0),j-(j>0)],
                    arr[i, j-(j>0)],
                    arr[i-(i>0), j],
                    arr[i, j],arr[i, j],arr[i, j],arr[i, j],
                ), axis=0)
                new_arr[i*2+1, j*2] = np.average((
                    arr[i+(i<max_i), j-(j>0)],
                    arr[i, j-(j>0)],
                    arr[i+(i<max_i), j],
                    arr[i, j],arr[i, j],arr[i, j],arr[i, j],
                ), axis=0)
                new_arr[i*2, j*2+1] = np.average((
                    arr[i-(i>0), j+(j<max_j)],
                    arr[i, j+(j<max_j)],
                    arr[i-(i>0), j],
                    arr[i, j], arr[i, j],arr[i, j],arr[i, j],
                ), axis=0)
                new_arr[i*2+1, j*2+1] = np.average((
                    arr[i+(i<max_i), j+(j<max_j)],
                    arr[i, j+(j<max_j)],
                    arr[i+(i<max_i), j],
                    arr[i, j],arr[i, j],arr[i, j],arr[i, j],
                ), axis=0)

        img = ImageEnhance.Color(Image.fromarray(new_arr)).enhance(1.02)
        img = ImageEnhance.Contrast(img).enhance(1.02)
        img = ImageEnhance.Brightness(img).enhance(1.05)

    Image.fromarray(new_arr).save(f"output/{init_res}-{img.size[0]}.jpg")

#-------------------------------------------------------------------------------
startTime = time.time()
enhance("tests/img1/64.jpg", 2048)
print(f'Done in: {round(time.time() - startTime,4)}s')