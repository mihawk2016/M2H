from functools import reduce

import pandas as pd
import os
import time

from to_statement.statement_builder import closed_table, statement_file

SELECT_COLUMN = ['Deal', 'Login', 'Open Time', 'Type', 'Symbol', 'Volume', 'Open Price', 'Close Time', 'Close Price',
                 'Commission', 'Taxes', 'Swap', 'Profit', 'Comment']


def read_manager_file(file):
    file_time = time.strftime('%Y %B %d, %H:%M', time.localtime(os.stat(file).st_mtime))
    try:
        table = pd.read_html(file)[0]
    except:
        # the file type is not supported
        return None
    ncol = table.shape[1]
    first_row = table[0][0]
    table.columns = table.iloc[[1], :].values[0]
    if ncol == 17 and first_row.find('Closed Trades Report') >= 0:
        SELECT_COLUMN.append('Name')
        table = table.loc[2:(table.shape[0] - 2), SELECT_COLUMN]
    elif ncol == 23 and first_row.find('Raw Report') >= 0:
        table = table.loc[2:(table.shape[0] - 7), SELECT_COLUMN]
        table = table.fillna('')
        table = table.loc[list(map(lambda x: x != '', table.Swap.values)), :]
        # print(table.Type not in ['buy', 'sell'])
    else:
        # the file type is not supported
        return None
    table.Comment = table.Comment + ' | Login: ' + table.Login
    closed = closed_table(table)
    sum_commission = sum_money(table.Commission)
    sum_taxes = sum_money(table.Taxes)
    sum_swap = sum_money(table.Swap)
    sum_profit = sum_money(table.Profit)
    html_content = statement_file(
        file_time=file_time, closed_transactions=closed, sum_commission_closed=sum_commission,
        sum_taxes_closed=sum_taxes, sum_swap_closed=sum_swap, sum_profit_closed=sum_profit)
    with open('test.htm', mode='w') as f:
        f.write(html_content)
    return None


def sum_money(money_strings):
    return sum([convert_money(money) for money in money_strings])


def convert_money(money_str):
    return float(money_str.replace(' ', ''))

    # row = table.iloc[[0], ]
    # print(row['Deal'], list(table.values)[0][0])
    # table.sort_values('Open Time')

# Todo:
#   1. 记录按Open Time或者Close Time排序
#   2. 对挂单的处理
#   3.



if __name__ == '__main__':
    file = ['../TEST_FILE/Closed Trades Report.htm', '../TEST_FILE/Raw Report.htm']
    # a = BeautifulSoup(open(file), 'lxml')
    # print(a)

    # b = pd.read_html(file[1])[0]
    # print(b, b.shape)

    read_manager_file(file[1])


    # float('12 3'.replace(' ', ''))
    # print(list(map(lambda x: x.find('stop') >= 0 or x.find('limit') >= 0, ['buy', 'sell', 'buy stop'])))
    # import re
    # print(re.('stop|limit', 'buy stop'))
