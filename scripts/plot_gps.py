# Created by steve on 17-9-11 下午5:39

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    fusion = np.loadtxt('after.csv',delimiter=',')
    before = np.loadtxt('before.csv',delimiter=',')

    plt.figure()
    plt.plot(fusion[:,0],fusion[:,1],'r-*',label='fusion')
    plt.plot(before[:,0],before[:,1],'b-+',label='gps source')
    plt.legend()
    plt.show()


