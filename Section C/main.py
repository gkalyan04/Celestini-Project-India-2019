import cv2
import numpy as np
import math
import time
import matplotlib.pyplot as plt

list_of_folders = ['Adirondack', 'ArtL', 'Jadeplant',
                   'Motorcycle', 'MotorcycleE', 'Piano',
                   'PianoL', 'Pipes', 'Playroom', 'Playtable',
                   'PlaytableP', 'Recycle', 'Shelves', 'Teddy',
                   'Vintage']
start = time.time()

costs = []

def ssd(left, right, window_length, window_width):
    cost = 0
    cost_arr = []
    for d in range(100):
        for j in range(window_length):
            for i in range(window_width):
                if (i + d < window_width):
                    cost = cost + math.pow(left[j, i] - right[j, i - d], 2)
        cost_arr.append({"cost": cost, "d": d})
        cost = 0
    print(cost_arr)
    min_cost = min(cost_arr, key=lambda x: x['cost'])
    print('Minimum Cost SSD: ', min_cost['cost'])
    print('D: ', min_cost['d'])


def sad(left, right, window_length, window_width):
    cost = 0
    cost_arr = []
    for d in range(window_width/4):
        for j in range(window_length):
            for i in range(window_width):
                if (i + d < window_width):
                    cost = cost + abs(int(left[j, i]) - int(right[j, i - d]))
        cost_arr.append({"cost": cost, "d": d})
        cost = 0
    min_cost = min(cost_arr, key=lambda x: x['cost'])
    print('Minimum Cost SAD: ', min_cost['cost'] * 100 / (window_length * window_width))
    print('D: ', min_cost['d'])
    return min_cost['cost']/ (100*window_length * window_width)


def zmncc(left, right, window_length, window_width):
    def get_average(img, wl, ww):
        s = 0
        for j in range(wl):
            for i in range(ww):
                s += img[j][i]
        return float(s) / (ww * wl)

    def get_standard_deviation(img, wl, ww):
        s = 0
        avg = get_average(img, wl, ww)
        for j in range(wl):
            for i in range(ww):
                s += (img[j][i] - avg) ** 2
        return (s / (wl * ww)) ** 0.5

    def zncc(img1, img2, wl, ww):
        stdDeviation1 = get_standard_deviation(img1, wl, ww)
        stdDeviation2 = get_standard_deviation(img2, wl, ww)
        avg1 = get_average(img1, wl, ww)
        avg2 = get_average(img2, wl, ww)
        cost_arr = []

        s = 0
        for d in range(100):
            for j in range(wl):
                for i in range(ww):
                    if i + d < wl:
                        s += (img1[j][i] - avg1) * (img2[j][i - d] - avg2)
            cost_arr.append({"cost": float(s) / (wl * ww * stdDeviation1 * stdDeviation2), "d": d})
            s = 0
        min_cost = min(cost_arr, key=lambda x: x['cost'])
        print('Minimum Cost SAD: ', min_cost['cost'])
        print('Horizontal Disparity: ', min_cost['d'])

    zncc(right, left, window_length, window_width)


for file in list_of_folders:
    fileLeft = 'MiddEval3/trainingQ/' + file + '/im0.png'
    fileRight = 'MiddEval3/trainingQ/'+ file + '/im1.png'
    left = cv2.imread(fileLeft, 0)
    right = cv2.imread(fileRight, 0)
    ww = left.shape[1]
    wl = left.shape[0]

    stereo = cv2.StereoBM_create(numDisparities=64, blockSize=7)
    disparity = stereo.compute(left, right)
    plt.imshow(disparity, 'gray')
    plt.show()
    print("--------------------------------------------------------------")
    print("Processing...",file )
    print("--------------------------------------------------------------")
    costs.append(sad(left, right, wl, ww))

print("--------------------------------------------------------------")
print("Processing...", "Average")
print("--------------------------------------------------------------")
print("Average Cost: ", min(costs))
end = time.time()
print('Time taken: ', end-start)
