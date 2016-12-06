# C:\Python27\Scripts
# -*- coding: utf-8 -*-
# Author : MikeChan
# Email  : m7807031@gmail.com

import pandas as pd
from numpy import abs, rad2deg,deg2rad, arctan, pi, linspace
import xlrd, os
from time import sleep, time
import matplotlib.pyplot as plt
import FileDialog


#===== helper func. =====
def draw_parsley_2(t=0.05):
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
    print u"        ||               香菜轉檔 version 3.1b              ||        "
    sleep(t)
    print u"        = = = = = = = = = = = = = = = = = = = = = = = = = = =        "


def draw_parsley(t=0.05):
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


def read_dir_file(path):
    print u"共 %d 筆檔案" % len(os.listdir(path.rstrip()))
    count = 0

    print os.listdir(path.rstrip())

    for f in os.listdir(path.rstrip()):
        count += 1
        calc_r_and_theta_from_file(path.rstrip().rstrip()+ "\\" + f)
        transfrom_single_file(path.rstrip().rstrip()+ "\\" + f)
        print u"第 %d 筆檔案完成." %count
    return


def calc_r_and_theta_from_file(file_name):
    print u"讀取原始檔案..."
    ori_f = pd.read_excel(file_name)
    print u"計算角度與半徑..."

    data_length = len(ori_f["lidar_e"])
    print u"共 %d 筆資料準備計算."%(data_length)

    tunnel_e = ori_f['tunnel_e'][0]
    tunnel_n = ori_f['tunnel_n'][0]
    tunnel_z = ori_f['tunnel_z'][0]

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
        if i%10000 ==0: print u"共 %d 筆完成尚餘 %d 筆."% (i, data_length-i)

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
            i_theta = rad2deg(arctan(abs(y)/abs(x)))
            r_theta_df['theta'][i] = 90 - i_theta

        # 2nd quadrant
        elif x > 0 and y < 0:
            i_theta = rad2deg(arctan(abs(y)/abs(x)))
            r_theta_df['theta'][i] = i_theta + 90.0

        # 3rd quadrant
        elif x < 0 and y < 0:
            i_theta = rad2deg(arctan(abs(y)/abs(x)))
            r_theta_df['theta'][i] = (90- i_theta) + 180.0

        # 4th quadrant
        elif x < 0 and y > 0:
            i_theta = rad2deg(arctan(abs(y)/abs(x)))
            r_theta_df['theta'][i] = i_theta +270.0

        else:
            print "data error %s: row %d can't be classify by quadrant, deg=nan." %(file_name, i+2)
            r_theta_df['theta'][i] = i_theta
            with open("Error_Log.txt","a+") as err_log:
                err_log.write("Data Error %s: row %d can't be classify by quadrant, deg=nan.\n" %(file_name, i+2))
    print u"theta 計算完畢."

    df_all =  pd.concat([ori_f,r_theta_df], axis=1)

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

    theta = deg2rad(answer_data['deg'] )
    radii = answer_data['deg_meanR']

    ax = plt.subplot(111, projection='polar')
    ax.plot(theta, radii, color='r', linewidth='3')
    ax.grid(True)
    ax.set_rmax(6.0)
    ax.set_rmin(4.0)
    ax.set_theta_zero_location('N')
    ax.set_theta_direction('clockwise')

    plt.show()


#===== main =====
def main():
    STATUS_KEY = -1
    # -1=> 剛啟動; 1=>輸入為檔案; 2=> 輸入為資料夾 ;

    draw_parsley_2()

    while 1:
        read_input_path = raw_input(u"Input File dir or name: ")

        if read_input_path == "pp":
            print u"開啟繪圖模式"
            STATUS_KEY = 9
            break

        elif os.path.isdir(read_input_path):
            print u"取得資料夾位置,進行批次處理作業."
            STATUS_KEY = 2
            break
        elif os.path.isfile(read_input_path):
            print u"取得檔案位置,進行單一檔案轉換."
            STATUS_KEY = 1
            break

        else:
            print u"輸入錯誤,請重新選擇."
            continue

    if STATUS_KEY == 1:
        print u"計算中..."
        calc_r_and_theta_from_file(read_input_path)
        transfrom_single_file(read_input_path)
        print u"完成."


    elif STATUS_KEY == 2:
        read_dir_file(read_input_path)
        print u"全部完成."

    elif STATUS_KEY == 9:
        draw_data_name = raw_input("Input _ANSWER.csv file: ")
        plot_or_not(draw_data_name)
        print u"完成."
    else:
        print "Error operation!"

if __name__ == "__main__": main()
