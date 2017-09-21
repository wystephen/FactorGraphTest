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
    imu = imu[22:, :]
    # print(imu.sum())
    # print(imu.shape)
    # print(imu)
    print(gps.shape)
    # print(gps)
    print('mean imu time:',np.mean(imu[:,0]))
    print('mean gps time:',np.mean(gps[:,0]))

    f = open('csvtest.csv', 'w')
    f.write('i,{0},{1},{2},'
            '0.0,0.0,0.0,1.0,'
            '0.0,0.0,0.0\n'.format(
        gps[0,1],
        gps[0,2],
        gps[0,3]
    ))

    plt.figure()
    plt.title('imu time')
    plt.plot(imu[:, 0], '.r')
    plt.plot(gps[:, 0])

    imu_time_interval = (imu[-1, 0] - imu[0, 0]) / float(imu.shape[0])

    print("time interval :", imu_time_interval)

    imu_index = 0
    gps_index = 0

    while (True):
        if gps_index > (gps.shape[0] - 2) or imu_index > (imu.shape[0] - 2):
            break

        if imu[imu_index, 0] < gps[gps_index, 0]:
            f.write('0,{0},{1},{2},{3},{4},{5}\n'.format(
                imu[imu_index, 1],
                imu[imu_index, 2],
                imu[imu_index, 3],
                imu[imu_index, 4],
                imu[imu_index, 5],
                imu[imu_index, 6]
            ))
            imu_index += 1
        else:
            f.write('1,{0},{1},{2},0.0,0.0,0.0,1.0\n'.format(
                gps[gps_index, 1],
                gps[gps_index, 2],
                gps[gps_index, 3]
            ))
            gps_index += 1

    plt.show()
