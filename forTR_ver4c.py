# C:\Python27\Scripts
# -*- coding: utf-8 -*-
# Author : MikeChan
# Email  : m7807031@gmail.com

import pandas as pd
import numpy as np
from scipy import optimize
import xlrd, os, sys, locale
from time import sleep, time
import matplotlib.pyplot as plt
import FileDialog


#===== helper func. =====
def draw_parsley_ver4(t=0.05):
    print "              " *2 + "  " + "  _  " + "  " + "              " *2
    sleep(t)
    print "     _/\_     " *2 + "  " + " |_| " + "  " + "     _/\_     " *2
    sleep(t)
    print "   __\  /__   " *2 + "  " + " |:| " + "  " + "   __\  /__   " *2
    sleep(t)
    print "  <_      _>  " *2 + "  " + " |:| " + "  " + "  <_      _>  " *2
    sleep(t)
    print "    |/ )\|    " *2 + "  " + " \:/ " + "  " + "    |/ )\|    " *2
    sleep(t)
    print "      /       " *2 + "  " + "  |  " + "  " + "      /       " *2
    sleep(t)

    print u"        = = = = = = = = = = = = = = = = = = = = = = = = = = =        "
    sleep(t)
    print u"        ||               香菜轉檔(加香腸) version 4c        ||        "
    sleep(t)
    print u"        = = = = = = = = = = = = = = = = = = = = = = = = = = =        "

def draw_parsley_ver3(t=0.05):
    print "     _/\_     " *5
    sleep(t)
    print "   __\  /__   " *5
    sleep(t)
    print "  <_      _>  " *5
    sleep(t)
    print "    |/ )\|    " *5
    sleep(t)
    print "      /       " *5
    sleep(t)
    print u"        = = = = = = = = = = = = = = = = = = = = = = = = = = =        "
    sleep(t)
    print u"        ||               香菜轉檔 version 4.0               ||        "
    sleep(t)
    print u"        = = = = = = = = = = = = = = = = = = = = = = = = = = =        "

def draw_parsley_ver2(t=0.05):
    #===== draw terminal =====
    print u"                               .k.                                     "
    sleep(t)
    print u"                               2                                       "
    sleep(t)
    print u"                              U7 u@r                                   "
    sleep(t)
    print u"                             :MNvGE@EU  7.LNO                          "
    sleep(t)
    print u"                            OMJXGOG@ .@G8Gui5L                         "
    sleep(t)
    print u"                            r@O8kr.  M8kvYNOPYi                        "
    sleep(t)
    print u"              , i           .v@G..iP@GXSSNEZXM@O.                      "
    sleep(t)
    print u"            ri@@@7          LJ..N@FvvUNNqZujBNj5.                      "
    sleep(t)
    print u"          .LqM0X0@@r       v :i  @GP52:OOOL                            "
    sleep(t)
    print u"          @@@@B8MMNEMGEi:@     . qMNM@q                                "
    sleep(t)
    print u"            uJuGqvr825@@@@@      . E1v    J:Pk@J iUL                    "
    sleep(t)
    print u"           .F1121OM@:;@@@,  .@     :BkSq5vYBOLv@ur                   "
    sleep(t)
    print u"          8@@@M8ZNM@0  Y,     Mu   rMFkuS001vS8SMZ                    "
    sleep(t)
    print u"          :J@B0BOOE7            LMv  k@8FuPXkSPZGM1                  "
    sleep(t)
    print u"              M@@@G               7Nr7@5NGOEXSur  :                    "
    sleep(t)
    print u"               P@F             rGMNkjqPO  MO;iMNXN0Fi2SEMU:            "
    sleep(t)
    print u"                                :@051S1jFY51.5U5UkqZqF5kv            "
    sleep(t)
    print u"                                 :@MOOqBB vGqEE8PkPqFu7            "
    sleep(t)
    print u"                                   58@@:   rq@@@@EOkFq0OZ           "
    sleep(t)
    print u"                                    i:       :i@0:@@5ZBB@O          "
    sleep(t)
    print u"                                                      ,ui2k          "
    sleep(t)
    print u"          = = = = = = = = = = = = = = = = = = = = = = = = = = =        "
    sleep(t)
    print u"          ||               香菜轉檔 version 3.0               ||        "
    sleep(t)
    print u"          = = = = = = = = = = = = = = = = = = = = = = = = = = =        "
    sleep(t)

def read_dir_file(path): #讀取指定目標資料夾內所有檔案名稱並產出RESULT 和 ANSWER
    print u"共 %d 筆檔案" % len(os.listdir(path.rstrip()))
    count = 0

    print os.listdir(path.rstrip())

    for f in os.listdir(path.rstrip()):
        count += 1
        read_no_title_data_and_generate_center_file(path.rstrip().rstrip()+ "\\" + f)
        calc_r_and_theta_from_file(path.rstrip().rstrip()+ "\\" + f)
        transfrom_single_file(path.rstrip().rstrip()+ "\\" + f)
        print u"第 %d 筆檔案完成." %count
    return


def circle_fit(lidar_abs_e_arr, lidar_abs_n_arr): #給予 點雲 XY座標 產出擬合圓心 x, y, R, residu
    def calc_R(x,y, xc, yc):
        """ calculate the distance of each 2D points from the center (xc, yc) """
        return np.sqrt((x-xc)**2 + (y-yc)**2)

    def f(c, x, y):
        """ calculate the algebraic distance between the data points and the mean circle centered at c=(xc, yc) """
        Ri = calc_R(x, y, *c)
        return Ri - Ri.mean()

    def leastsq_circle(x,y):
        # coordinates of the barycenter
        x_m = np.mean(x)
        y_m = np.mean(y)
        center_estimate = x_m, y_m
        center, ier = optimize.leastsq(f, center_estimate, args=(x,y))
        xc, yc = center
        Ri       = calc_R(x, y, *center)
        R        = Ri.mean()
        residu   = np.sum((Ri - R)**2)
        return xc, yc, R, residu

    xc,yc,R,residu = leastsq_circle(lidar_abs_e_arr, lidar_abs_n_arr)

    return xc,yc,R,residu


def read_no_title_data_and_generate_center_file(file_name): # 讀取 純點雲資料 產出 圓心檔案 _CENTER
    print u"計算擬合圓心開始."
    ori_f = pd.read_excel(file_name, header=None)
    new_df = pd.DataFrame({"lidar_e": ori_f[0],"lidar_n": ori_f[1],"lidar_z": ori_f[2]})

    new_df_lenth = new_df["lidar_e"].size

    if new_df_lenth >= 100000:
        fit_len = 100000
    else:
        fit_len = new_df_lenth

    # 取全部裡面指定數量的隨機點雲
    lidar_for_fit = new_df.sample(n=fit_len)
    tunnel_z = lidar_for_fit['lidar_z'].mean()

    print u"計算擬合圓心中..."
    xc,yc,R,residu  = circle_fit(lidar_for_fit['lidar_e'], lidar_for_fit['lidar_n'])

    center_df = pd.DataFrame({'tunnel_e': xc, 'tunnel_n':yc, 'tunnel_z': tunnel_z}, index=[0])
    print u"擬合圓心計算完成."
    #all_df = pd.concat([new_df,center_df], axis=1)

    center_df.to_csv('%s_CENTER.csv' %file_name.rstrip(),index=False)
    print u"_CENTER.csv 產出."

def calc_r_and_theta_from_file(file_name, center_file_name): #讀取 純點雲資料 和 圓心資料 產出 帶檔頭的 _RESULT
    print u"純點雲檔案讀取中..."

    if file_name.rstrip().endswith(".xlsx"):
        ori_f = pd.read_excel('%s' %file_name.rstrip(), header=None)
    elif file_name.rstrip().endswith(".csv"):
        ori_f = pd.read_csv('%s' %file_name.rstrip(), header=None)
    else:
        ori_f = pd.DataFrame({'a':[1,2,3]})

    ori_f = ori_f.rename(columns={0:'lidar_e', 1:'lidar_n', 2:'lidar_z'})


    print u"圓心檔案讀取中..."
    center_f = pd.read_csv(center_file_name)


    print u"計算角度與半徑..."
    data_length = len(ori_f["lidar_e"])
    print u"共 %d 筆資料準備計算."%(data_length)

    tunnel_e = center_f['tunnel_e'][0]
    tunnel_n = center_f['tunnel_n'][0]
    tunnel_z = center_f['tunnel_z'][0]

    r_theta_dict = {'radius':[float(i) for i in range(data_length)], 'theta':[float(i) for i in range(data_length)]}
    r_theta_df = pd.DataFrame(r_theta_dict)
    #print r_theta_df.head()
    # create dataframe likes:
    #      redius     theta
    # 0      0.0       0.0
    # 1      1.0       1.0
    # 2      2.0       2.0

    print u"計算 radius...."
    # 計算對應 index 的 radius
    r_theta_df['radius'] = (    (ori_f['lidar_e'] - tunnel_e)**2  +  (ori_f['lidar_n'] - tunnel_n)**2     )   ** 0.5
    #print r_theta_df.head()
    # enter dataframe likes:
    #      radius  theta
    # 0  5.425958    0.0
    # 1  5.442800    1.0
    # 2  5.438896    2.0
    # 3  5.439481    3.0
    print u"radius 計算完畢."


    print u"計算 theta..."
    for i in range(data_length):
        if i%10000 ==0: print u"共 %d 筆完成,尚餘 %d 筆."% (i, data_length-i)

        x = float(ori_f['lidar_e'][i] - tunnel_e)
        y = float(ori_f['lidar_n'][i] - tunnel_n)
        r = float(r_theta_df['radius'][i])



        if x == 0 and y ==0: # 點雲為圓心
            r_theta_df['theta'][i] = 'nan'

        elif x == 0 and y > 0: # x=0 y>0
            r_theta_df['theta'][i] = 0

        elif x == 0 and y < 0: # x=0 y<0
            r_theta_df['theta'][i] = 180

        elif x > 0 and y== 0: # x>0 y=0
            r_theta_df['theta'][i] = 90

        elif x < 0 and y == 0: # x<0 y=0
            r_theta_df['theta'][i] = 270

        # 1st quadrant
        elif x > 0 and y > 0:
            i_theta = np.rad2deg(np.arctan(np.abs(y)/np.abs(x)))
            r_theta_df['theta'][i] = 90 - i_theta

        # 2nd quadrant
        elif x > 0 and y < 0:
            i_theta = np.rad2deg(np.arctan(np.abs(y)/np.abs(x)))
            r_theta_df['theta'][i] = i_theta + 90.0

        # 3rd quadrant
        elif x < 0 and y < 0:
            i_theta = np.rad2deg(np.arctan(np.abs(y)/np.abs(x)))
            r_theta_df['theta'][i] = (90- i_theta) + 180.0

        # 4th quadrant
        elif x < 0 and y > 0:
            i_theta = np.rad2deg(np.arctan(np.abs(y)/np.abs(x)))
            r_theta_df['theta'][i] = i_theta +270.0

        else:
            print "data error %s: row %d can't be classify by quadrant, deg=nan." %(file_name, i+2)
            r_theta_df['theta'][i] = i_theta
            with open("Error_Log.txt","a+") as err_log:
                err_log.write("Data Error %s: row %d can't be classify by quadrant, deg=nan.\n" %(file_name, i+2))

    print u"theta 計算完畢."

    df_all =  pd.concat([ori_f,center_f, r_theta_df], axis=1)

    print u"_RESULT.csv 產出."
    df_all.to_csv('%s_RESULT.csv' %file_name.rstrip(), index=False)
    return

def transfrom_single_file(file_name):
    print u"計算每一度的平均半徑..."
    #===== open file =====
    ori_f = pd.read_csv('%s_RESULT.csv' %file_name.rstrip())

    #===== variable =====
    data_len = ori_f["radius"].size
    arr = []

    #===== helper func. =====
    data_dict = {}
    for i in range(360):
        data_dict[str("%s")%i] = []

    #===== main =====
    for i in range(data_len):
        try:
            now_theta = int(round(ori_f[u'theta'][i]))
        except:
            print u"!!DATA MISSING!!%s: missing at row %d " %(file_name, i+2)
            with open("Error_Log.txt","a+") as err_log:
                print >>err_log, u"!!DATA MISSING!!%s: missing at row %d " %(file_name, i+2)
            continue

        if now_theta ==360:
            data_dict['0'].append(ori_f['radius'][i])
        else:
            data_dict[str(now_theta)].append(ori_f['radius'][i])

    for key in data_dict:
        if len(data_dict[key]) ==0:
            deg_meanR = 'nan'
        else:
            deg_meanR = float(sum(data_dict[key])/len(data_dict[key]))

        arr.append([int(key), int(len(data_dict[key])), float(deg_meanR)])

    deg = [i[0] for i in arr]
    num = [i[1] for i in arr]
    deg_meanR =[i[2] for i in arr]

    df = pd.DataFrame({'deg': deg, 'num': num, 'deg_meanR': deg_meanR})
    sorted_df = df.sort_values(by='deg')
    print u"平均半徑計算完畢."

    #print sorted_df.head()

    sorted_df.loc[sorted_df['num'] <=10, 'deg_meanR' ] = ''

    new_fn = file_name
    sorted_df.to_csv('%s_ANSWER.csv' %new_fn.rstrip(), index=False)
    print u"_ANSWER.CSV 產出."
    return

def plot_or_not(file_name):
    answer_data = pd.read_csv(file_name.rstrip())

    theta = np.deg2rad(answer_data['deg'])
    radii = answer_data['deg_meanR']

    ax = plt.subplot(111, projection='polar')
    ax.plot(theta, radii, color='r', linewidth='3')
    ax.grid(True)
    ax.set_rmax(6.0)
    ax.set_rmin(5.0)
    ax.set_theta_zero_location('N')
    ax.set_theta_direction('clockwise')

    plt.show()

def plot_replacement(file_name):
    answer_data = pd.read_csv(file_name.rstrip())
    theta = np.deg2rad(answer_data['deg'])
    radii = answer_data['deg_meanR']


    fig = plt.figure()
    fig.subplots_adjust(top=0.87)
    fig.suptitle("Tunnel_z", fontsize=14, fontweight="bold")
    ax = fig.add_subplot(111, projection='polar')

    #template variable
    theta_360 = np.deg2rad(np.arange(360))
    r0 = np.array([0 for i in range(360)])
    r_break_max = np.array([15 for i in range(360)])
    r_break_min = np.array([-15 for i in range(360)])



    #標準指示圓
    ax.plot(theta_360, r0, 'g', linewidth='4')
    ax.plot(theta_360, r_break_max, 'y', linewidth='4')
    ax.plot(theta_360, r_break_min, 'y', linewidth='4')
    ax.plot()


    ax.plot(theta, radii, color='r', linewidth='3')


    ax.grid(False)
    ax.set_rmax(30)
    ax.set_rmin(-30)
    #ax.set_rgrids([7.5, 15, 22.5, 30, 37.5,],angle=0.)
    ax.set_xticks(np.pi/180. * np.linspace(0.0,  360.0, 16, endpoint=False))
    ax.set_yticks([-30,-22.5,-15,-7.5,0, 7.5, 15, 22.5, 30])
    ax.set_theta_zero_location('N')
    ax.set_theta_direction('clockwise')
    ax.set_xticklabels(['0', '22.5', '45', '67.5', '90', '112.5', '135', '157.5', '180',
                        '202.5', '225', '247.5', '270', '292.5', '315', '337.5'])



    plt.show()

#====== test code =====
def test_multi_center(file_name): # 讀取 純點雲資料 產出 圓心檔案 _CENTER
    print u"計算擬合圓心開始."
    ori_f = pd.read_excel(file_name, header=None)
    new_df = pd.DataFrame({"lidar_e": ori_f[0],"lidar_n": ori_f[1],"lidar_z": ori_f[2]})

    new_df_lenth = new_df["lidar_e"].size

    if new_df_lenth >= 100000:
        fit_len = 100000
    else:
        fit_len = new_df_lenth


    test_count = 10000
    center_df = pd.DataFrame({'tunnel_e': 0.0, 'tunnel_n':0.0, 'tunnel_z': 0.0}, index=[i for i in range(test_count)])
    for i in range(test_count):
        # 取全部裡面指定數量的隨機點雲
        lidar_for_fit = new_df.sample(n=fit_len)
        tunnel_z = lidar_for_fit['lidar_z'].mean()


        print u"計算擬合圓心中..."
        xc,yc,R,residu  = circle_fit(lidar_for_fit['lidar_e'], lidar_for_fit['lidar_n'])

        center_df["tunnel_e"][i] = xc
        center_df["tunnel_n"][i] = yc
        center_df["tunnel_z"][i] = tunnel_z
        print u"第%s次擬合圓心計算完成." %(i)
        #all_df = pd.concat([new_df,center_df], axis=1)

    print center_df.head(5)



#===== main =====
def main():
    STATUS_KEY = 0
    CENTER_KEY = 0
    draw_parsley_ver4()

    while 1:
        read_input_file = raw_input(u"Enter lidar file without header: ").rstrip()

        if read_input_file == "pp":
            STATUS_KEY = 6
            break
        elif read_input_file == "test":
            STATUS_KEY = 666
            break

        elif os.path.isfile(read_input_file) and str(read_input_file).rstrip().endswith(".xlsx"):
            print u"點雲檔案正確."
            STATUS_KEY =1

            while 1:
                read_center_file = raw_input(u"Enter center file(if not, I will generate one): ")
                if str(read_center_file).rstrip().endswith("_CENTER.csv"):
                    print u"圓心檔案正確."
                    CENTER_KEY = 1
                    break
                elif read_center_file.rstrip() == "" :
                    print u"無圓心檔案,自動產出圓心檔."
                    CENTER_KEY = 0
                    break
                else:
                    print u"圓心檔案輸入錯誤，請重新輸入"
                    continue
            break
        else:
            print u"檔案錯誤,請重新輸入檔案."
            continue


    if STATUS_KEY == 1 and CENTER_KEY== 1:
        print u"使用指定圓心檔案產出 _RESULT 與 _ANSWER"
        calc_r_and_theta_from_file(read_input_file, read_center_file)
        transfrom_single_file(read_input_file)
        print u"完成."

    elif STATUS_KEY == 1 and CENTER_KEY == 0:
        print u"使用檔案產出擬合圓心檔案_CENTER."
        read_no_title_data_and_generate_center_file(read_input_file)
        #print u"使用檔案產出_CENTER, _RESULT 與 _ANSWER"
        print u"完成."

    elif STATUS_KEY==6:
        print u"繪圖模式開啟"
        draw_data_name = raw_input("Input _ANSWER.csv file: ")
        #plot_or_not(draw_data_name.rstrip())
        plot_replacement(draw_data_name.rstrip())

        '''
        try:
            plot_or_not(draw_data_name.rstrip())
            print u"完成."
        except:
            print u"檔案錯誤，處罰你等待 3 秒，好好思考人生吧！"
            sleep(3)
        '''

    elif STATUS_KEY ==666:
        print u"測試模式開啟"
        test_multi_center("data/179.75-1212.xlsx")



    else:
        print u"執行錯誤, 請重新輸入."




if __name__ == "__main__": main()
