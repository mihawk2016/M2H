from to_statement.statement_templet import CLOSED_ROW, DOUBLE_ROW_COLOR, NO_TRANSACTIONS, STATEMENT_HTML_TEMP


def closed_table(table):
    table_list = list(table.values)
    length = len(table_list)
    if length <= 0:
        return NO_TRANSACTIONS
    rows = [closed_row(row, table_list[row]) for row in range(length)]
    return ''.join(rows)


def closed_row(index, ticket_row):
    digits = len(ticket_row[6]) - ticket_row[6].find('.') - 1
    return CLOSED_ROW.format(
        color='' if index % 2 == 0 else DOUBLE_ROW_COLOR,
        digit='0' * digits,
        comment=ticket_row[13],
        ticket=ticket_row[0],
        open_time=ticket_row[2],
        type=ticket_row[3],
        volume=ticket_row[5],
        item=ticket_row[4],
        open_price=ticket_row[6],
        sl='0.' + '0' * digits,
        tp='0.' + '0' * digits,
        close_time=ticket_row[7],
        close_price=ticket_row[8],
        commission=ticket_row[9],
        taxes=ticket_row[10],
        swap=ticket_row[11],
        profit=ticket_row[12]
    )



def statement_file(file_time, closed_transactions, sum_commission_closed, sum_taxes_closed,
                   sum_swap_closed, sum_profit_closed, open_trades=NO_TRANSACTIONS,
                   sum_commission_open=0, sum_taxes_open=0, sum_swap_open=0, sum_profit_open=0,
                   working_orders=NO_TRANSACTIONS,
                   title='Statement: test', company='Alpha Growth Management Co., Ltd. - IIG',
                   account=0000, name='TEST', currency='USD', leverage=100,
                   ):

    return STATEMENT_HTML_TEMP.format(
        title=title,
        company=company,
        account=str(account),
        name=name,
        currency=currency,
        leverage=str(leverage),
        time=file_time,
        closed_transactions=closed_transactions,
        sum_commission_closed=money_format(sum_commission_closed),
        sum_taxes_closed=money_format(sum_taxes_closed),
        sum_swap_closed=money_format(sum_swap_closed),
        sum_profit_closed=money_format(sum_profit_closed),
        sum_all_closed=money_format(sum_commission_closed + sum_taxes_closed + sum_swap_closed + sum_profit_closed),
        open_trades=open_trades,
        sum_commission_open=money_format(sum_commission_open),
        sum_taxes_open=money_format(sum_taxes_open),
        sum_swap_open=money_format(sum_swap_open),
        sum_profit_open=money_format(sum_profit_open),
        sum_all_open=money_format(sum_commission_open + sum_taxes_open + sum_swap_open + sum_profit_open),
        working_orders=working_orders
    )


def money_format(money):
    return '{:,.2f}'.format(money).replace(',', ' ')

if __name__ == '__main__':
    print('main')





