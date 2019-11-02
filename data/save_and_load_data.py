import numpy as np


def save_data():
    arr1 = np.array([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ])
    arr2 = np.array([11,22,33])
    np.savez("hallo.npz", arr1, arr2, data1=arr1, data2=arr2)


def load_data():
    f = np.load("hallo.npz")
    arr1 = f['data1']
    arr2 = f['data2']
    print(arr1)
    print(arr2)


if __name__ == '__main__':
    save_data()
    load_data()
