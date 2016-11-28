


# class StatementBuilder:
#
#
#
#     def output(self):
#

# def build_statement():


if __name__ == '__main__':
    A = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
  <head>
    <title>{title}</title>
    <meta name="generator" content="MetaQuotes Software Corp.">
    <link rel="help" href="http://www.metaquotes.net">
    <style type="text/css" media="screen">
    <!--
    td {{ font: 8pt Tahoma,Arial; }}
    //-->
    </style>
    <style type="text/css" media="print">
    <!--
    td {{ font: 7pt Tahoma,Arial; }}
    //-->
    </style>
    <style type="text/css">
    <!--
    .msdate {{ mso-number-format:"General Date"; }}
    .mspt   {{ mso-number-format:\#\,\#\#0\.00;  }}
    //-->
    </style>
  </head>
<body topmargin=1 marginheight=1>
<div align=center>
<div style="font: 20pt Times New Roman"><b>{company}</b></div><br>

<!--NOCOMMENTS-->
<table cellspacing=1 cellpadding=3 border=0>
<tr align=left>
    <td colspan=2><b>Account: {account}</b></td>
    <td colspan=5><b>Name: {name}</b></td>
    <td colspan=2><b>Currency: {currency}</b></td>
    <td colspan=2><b>Leverage: 1:{leverage}</b></td>
    <td colspan=3 align=right><b>{time}</b></td></tr>

<tr align=left><td colspan=13><b>Closed Transactions:</b></td></tr>
<tr align=center bgcolor="#C0C0C0">
   <td>Ticket</td><td nowrap>Open Time</td><td>Type</td><td>Volume</td><td>Item</td>
   <td>Price</td><td>S / L</td><td>T / P</td><td nowrap>Close Time</td>
   <td>Price</td><td>Commission</td><td>Taxes</td><td>Swap</td><td>Profit</td></tr>
'''
    print(A.format(title='abc', company='oanda'))

    ticket_row = '''
<tr {color}align=right>
<td title="{comment}">{ticket}</td>
<td class=msdate nowrap>{open_time}</td>
<td>{type}</td>
<td>{volume}</td>
<td>{item}</td>
<td style="mso-number-format:0\.{digit};">{open_price}</td>
<td style="mso-number-format:0\.{digit};">{sl}</td>
<td style="mso-number-format:0\.{digit};">{tp}</td>
<td class=msdate nowrap>{close_time}</td>
<td style="mso-number-format:0\.{digit};">{close_price}</td>
<td class=mspt>{commission}</td>
<td class=mspt>{taxes}</td>
<td class=mspt>{swap}</td>
<td class=mspt>{profit}</td>
</tr>
<tr align=right>
<td colspan=10>&nbsp;</td>
<td colspan=4>{comment}</td>
</tr>'''


    'bgcolor=#E0E0E0 '