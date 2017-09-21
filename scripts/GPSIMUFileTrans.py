# Created by steve on 17-9-21 下午7:17
'''
                   _ooOoo_ 
                  o8888888o 
                  88" . "88 
                  (| -_- |) 
                  O\  =  /O 
               ____/`---'\____ 
             .'  \\|     |//  `. 
            /  \\|||  :  |||//  \ 
           /  _||||| -:- |||||-  \ 
           |   | \\\  -  /// |   | 
           | \_|  ''\---/''  |   | 
           \  .-\__  `-`  ___/-. / 
         ___`. .'  /--.--\  `. . __ 
      ."" '<  `.___\_<|>_/___.'  >'"". 
     | | :  `- \`.;`\ _ /`;.`/ - ` : | | 
     \  \ `-.   \_ __\ /__ _/   .-` /  / 
======`-.____`-.___\_____/___.-`____.-'====== 
                   `=---=' 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
         佛祖保佑       永无BUG 
'''


import numpy as np
import scipy as sp

import matplotlib.pyplot as plt


if __name__ == '__main__':
    imu = np.loadtxt('/home/steve/Data/GPSIMUTest/src_imu.csv',
                     delimiter=',')
    gps = np.loadtxt('/home/steve/Data/GPSIMUTest/out_gps.csv',
                     delimiter=',')
    imu = imu[22:,:]
    # print(imu.sum())
    # print(imu.shape)
    # print(imu)
    # print(gps.shape)
    # print(gps)

    f = open('csvtest.csv','w')
    f.write('0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0')

    plt.figure()
    plt.title('imu time')
    plt.plot(imu[:,0],'.r')
    # plt.plot(gps[:,0])
    plt.show()

    imu_time_interval = (imu[-1,0]-imu[0,0])/float(imu.shape[1])


    imu_index = 0
    gps_index = 0





