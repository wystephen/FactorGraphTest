# Created by steve on 17-9-11 下午5:39

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


if __name__ == '__main__':
    fusion = np.loadtxt('after.csv',delimiter=',')
    before = np.loadtxt('before.csv',delimiter=',')

    src_gps = np.loadtxt('/home/steve/Data/GPSIMUTest/out_gps.csv',
                     delimiter=',')


    # plt.figure()
    # plt.plot(fusion[:,0],fusion[:,1],'r-*',label='fusion')
    # plt.plot(before[:,0],before[:,1],'b-+',label='gps source')
    # plt.legend()
    # plt.show()
    fig  = plt.figure()
    ax = fig.add_subplot(111,projection='3d')

    ax.plot(fusion[:,0],fusion[:,1],fusion[:,2],'r-*',label = 'fusion')
    ax.plot(before[:,0],before[:,1],before[:,2],'b-+',label='gps')
    ax.plot(src_gps[:,1],src_gps[:,2],src_gps[:,3],'g-+',label='source gps')
    plt.legend()
    plt.show()


