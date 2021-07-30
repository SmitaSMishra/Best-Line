import pandas as cv
import math

def squared_error(X,w0,w1):
    loss = 0
    for point in X:
        loss += math.pow(point[1] -((w1 * point[0]) + w0),2)
    return loss

def best_line(X):
    w0 = w1 = dw0 = dw1 = 0
    alpha = 0.0001
    print(squared_error(X,w0,w1))
    while dw0 >= 0 and dw1 >= 0:
        dw0 = dw1 = 0
        for point in X:
            dw0 += -2 * (point[1] - ((w1 * point[0]) + w0))
            dw1 += -2 * (point[1] - ((w1 * point[0]) + w0)) * point[0]
        w0 -= alpha * dw0
        w1 -= alpha * dw1
        print(dw0,dw1)
        print(squared_error(X, w0, w1))
    return w0,w1

def parse_file(filename):
    f = open(filename)
    x_arr = []
    y_arr = []
    for each in f:
        x_and_y = each.strip().split()
        x_arr.append(float(x_and_y[0]))
        y_arr.append(float(x_and_y[1]))
    return x_arr, y_arr

def main():
    data_list = []
    X,Y = parse_file("data.txt")
    for i in range(len(X)):
        data_list.append((X[i],Y[i]))
    print(data_list)
    print(best_line(data_list))

main()