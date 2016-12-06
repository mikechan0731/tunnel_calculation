# C:\Python27\Scripts
# -*- coding: utf-8 -*-
# Author : MikeChan
# Email  : m7807031@gmail.com

import pandas as pd
import math, xlrd, os
from time import sleep

t = 0.01
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

# ===== file dir or name checker ======
STATUS_KEY = -1
# -1=> 剛啟動; 1=>輸入為檔案; 2=> 輸入為資料夾 ;

while 1:
    read_input_path = raw_input(u"Input File dir or name: ")

    if os.path.isdir(read_input_path):
        print u"取得資料夾位置，進行批次處理作業。"
        STATUS_KEY = 2
        break
    elif os.path.isfile(read_input_path):
        print u"取得檔案位置，進行單一檔案轉換。"
        STATUS_KEY = 1
        break
    else:
        print u"輸入錯誤，請重新選擇。"
#================================


def read_dir_file(path):
    print u"共 %d 筆檔案" % len(os.listdir(path.rstrip()))
    count = 0

    print os.listdir(path.rstrip())

    for f in os.listdir(path.rstrip()):
        count += 1
        transfrom_single_file( path.rstrip().rstrip()+ "\\" + f)
        print u"第 %d 筆檔案完成。" %count
    return

def transfrom_single_file(file_name):
    #===== open file =====
    ori_f = pd.read_excel(file_name)

    #===== variable =====
    data_len = ori_f["r"].size
    arr = []

    #===== helper func. =====
    data_dict = {}
    for i in range(360):
        data_dict[str("%s")%i] = []

    #===== main =====
    for i in range(data_len):
        try:
            now_theta = int(round(ori_f[u'θ'][i]))
        except:
            print u"!!檔案缺失!! %s =>缺失於第%d列" %(file_name, i+2)
            with open("Error_Log.txt","a+"):
                print u"!!檔案缺失!! %s =>缺失於第%d列" %(file_name, i+2)

        if now_theta ==360:
            data_dict['0'].append(ori_f['r'][i])
        else:
            data_dict[str(now_theta)].append(ori_f['r'][i])

    for key in data_dict:
        if len(data_dict[key]) ==0:
            deg_avg = 'nan'
        else:
            deg_avg = float(sum(data_dict[key])/len(data_dict[key]))

        arr.append([int(key), int(len(data_dict[key])), float(deg_avg)])

    deg = [i[0] for i in arr]
    num = [i[1] for i in arr]
    deg_avg =[i[2] for i in arr]

    df = pd.DataFrame({'deg': deg, 'num': num, 'deg_avg': deg_avg})
    sorted_df = df.sort_values(by='deg')

    new_fn = file_name[:-5]
    sorted_df.to_csv('%s_RESULT.csv' %new_fn, index=False)

    return


#===== main =====
if STATUS_KEY == 1:
    print u"計算中..."
    transfrom_single_file(read_input_path)
    print u"完成。"
elif STATUS_KEY == 2:
    read_dir_file(read_input_path)
    print u"全部完成。"
else:
    print "Error operation!"
