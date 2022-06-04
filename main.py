import numpy as np
from PIL import Image
import os
import shutil

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

def enhance1(path, incr):
    img = Image.open(path)
    init_res = img.size[0]
    shutil.copy(path, f"output/original-{img.size[0]}.jpg")

    for _ in range(incr):
        arr = np.array(img)
        new_arr = np.zeros((arr.shape[0]*2, arr.shape[1]*2, 3), dtype=np.uint8)
        max_i = arr.shape[0]-1
        max_j = arr.shape[1]-1
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                new_arr[i*2, j*2] = np.average((
                    arr[i-(i>0),j-(j>0)],
                    arr[i-(i>0), j],
                    arr[i, j],
                ), axis=0)
                new_arr[i*2+1, j*2] = np.average((
                    arr[i+(i<max_i), j-(j>0)],
                    arr[i, j-(j>0)],
                    arr[i, j],
                ), axis=0)
                new_arr[i*2, j*2+1] = np.average((
                    arr[i-(i>0), j+(j<max_j)],
                    arr[i, j+(j<max_j)], 
                    arr[i, j],
                ), axis=0)
                new_arr[i*2+1, j*2+1] = np.average((
                    arr[i+(i<max_i), j+(j<max_j)],
                    arr[i+(i<max_i), j], 
                    arr[i, j],
                ), axis=0)
        
        img = Image.fromarray(new_arr)

    Image.fromarray(new_arr).save(f"output/1_{init_res}-{img.size[0]}.jpg")

#-------------------------------------------------------------------------------

def enhance2(path, incr):
    img = Image.open(path)
    init_res = img.size[0]
    shutil.copy(path, f"output/original-{img.size[0]}.jpg")

    for _ in range(incr):
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
                    arr[i, j],
                ), axis=0)
                new_arr[i*2+1, j*2] = np.average((
                    arr[i+(i<max_i), j-(j>0)],
                    arr[i, j-(j>0)],
                    arr[i+(i<max_i), j],
                    arr[i, j],
                ), axis=0)
                new_arr[i*2, j*2+1] = np.average((
                    arr[i-(i>0), j+(j<max_j)],
                    arr[i, j+(j<max_j)], 
                    arr[i-(i>0), j], 
                    arr[i, j],
                ), axis=0)
                new_arr[i*2+1, j*2+1] = np.average((
                    arr[i+(i<max_i), j+(j<max_j)],
                    arr[i, j+(j<max_j)], 
                    arr[i+(i<max_i), j], 
                    arr[i, j],
                ), axis=0)
        
        img = Image.fromarray(new_arr)

    Image.fromarray(new_arr).save(f"output/2_{init_res}-{img.size[0]}.jpg")

#-------------------------------------------------------------------------------

def enhance3(path, incr):
    img = Image.open(path)
    init_res = img.size[0]
    shutil.copy(path, f"output/original-{img.size[0]}.jpg")

    for _ in range(incr):
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
                    arr[i, j],arr[i, j],
                ), axis=0)
                new_arr[i*2+1, j*2] = np.average((
                    arr[i+(i<max_i), j-(j>0)],
                    arr[i, j-(j>0)],
                    arr[i+(i<max_i), j],
                    arr[i, j],arr[i, j],
                ), axis=0)
                new_arr[i*2, j*2+1] = np.average((
                    arr[i-(i>0), j+(j<max_j)],
                    arr[i, j+(j<max_j)], 
                    arr[i-(i>0), j], 
                    arr[i, j], arr[i, j],
                ), axis=0)
                new_arr[i*2+1, j*2+1] = np.average((
                    arr[i+(i<max_i), j+(j<max_j)],
                    arr[i, j+(j<max_j)], 
                    arr[i+(i<max_i), j], 
                    arr[i, j],arr[i, j],
                ), axis=0)
        
        img = Image.fromarray(new_arr)

    Image.fromarray(new_arr).save(f"output/3_{init_res}-{img.size[0]}.jpg")

#-------------------------------------------------------------------------------

def enhance4(path, res):
    img = Image.open(path)
    init_res = img.size[0]
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
                    arr[i, j],arr[i, j],arr[i, j],
                ), axis=0)
                new_arr[i*2+1, j*2] = np.average((
                    arr[i+(i<max_i), j-(j>0)],
                    arr[i, j-(j>0)],
                    arr[i+(i<max_i), j],
                    arr[i, j],arr[i, j],arr[i, j],
                ), axis=0)
                new_arr[i*2, j*2+1] = np.average((
                    arr[i-(i>0), j+(j<max_j)],
                    arr[i, j+(j<max_j)], 
                    arr[i-(i>0), j], 
                    arr[i, j], arr[i, j],arr[i, j],
                ), axis=0)
                new_arr[i*2+1, j*2+1] = np.average((
                    arr[i+(i<max_i), j+(j<max_j)],
                    arr[i, j+(j<max_j)], 
                    arr[i+(i<max_i), j], 
                    arr[i, j],arr[i, j],arr[i, j],
                ), axis=0)
        
        img = Image.fromarray(new_arr)

    Image.fromarray(new_arr).save(f"output/4_{init_res}-{img.size[0]}.jpg")

#-------------------------------------------------------------------------------

# create_resized("tests")
enhance4("tests/32.jpg", 1024)