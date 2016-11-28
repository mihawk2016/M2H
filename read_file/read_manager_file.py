
from bs4 import BeautifulSoup
import pandas as pd
import os
import time


def read_manager_file(file):
    file_time = time.strftime('%Y %B %d, %H:%M', time.localtime(os.stat(file).st_mtime))
    try:
        table = pd.read_html(file)[0]
    except:
        print('the file type is not supported')
        return None
    ncol = table.shape[1]
    first_row = table[0][0]
    if ncol == 17 and first_row.find('Closed Trades Report') >= 0: # closed trades report
        pass
    elif ncol == 23 and first_row.find('Raw Report') >= 0: # raw report
        pass
    else:
        print('the file type is not supported')
        return None






if __name__ == '__main__':
    file = ['../TEST_FILE/Closed Trades Report.htm', '../TEST_FILE/Raw Report.htm']
    # a = BeautifulSoup(open(file), 'lxml')
    # print(a)

    # b = pd.read_html(file[1])[0]
    # print(b, b.shape)

    read_manager_file(file[1])
    float('12 3'.replace(' ', ''))


