
STATEMENT_HTML_TEMP = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
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

{closed_transactions}

<tr align=right>
    <td colspan=10>&nbsp;</td>
    <td class=mspt>{sum_commission_closed}</td>
    <td class=mspt>{sum_taxes_closed}</td>
    <td class=mspt>{sum_swap_closed}</td>
    <td class=mspt>{sum_profit_closed}</td>
</tr>

<tr align=right>
    <td colspan=12 align=right><b>Closed P/L:</b></td>
    <td colspan=2 align=right title="Commission + Swap + Profit + Taxes" class=mspt><b>{sum_all_closed}</b></td>
</tr>

<tr align=left><td colspan=14><b>Open Trades:</b></td></tr>
<tr align=center bgcolor="#C0C0C0">
    <td>Ticket</td><td nowrap>Open Time</td><td>Type</td><td>Volume</td><td>Item</td>
    <td>Price</td><td>S / L</td><td>T / P</td><td>&nbsp;</td>
    <td>Price</td><td>Commission</td><td>Taxes</td><td>Swap</td><td>Profit</td></tr>

{open_trades}

<tr align=right>
    <td colspan=10>&nbsp;</td>
    <td class=mspt>{sum_commission_open}</td>
    <td class=mspt>{sum_taxes_open}</td>
    <td class=mspt>{sum_swap_open}</td>
    <td class=mspt>{sum_profit_open}</td>
</tr>
<tr><td colspan=10>&nbsp;</td><td colspan=2 align=right><b>Floating P/L:</b></td>
    <td colspan=2 align=right title="Commission + Swap + Profit" class=mspt><b>{sum_all_open}</b></td></tr>

<tr align=left><td colspan=14><b>Working Orders:</b></td></tr>
<tr align=center bgcolor="#C0C0C0">
    <td>Ticket</td><td nowrap>Open Time</td><td>Type</td><td>Volume</td><td>Item</td>
    <td>Price</td><td>S / L</td><td>T / P</td><td colspan=2 nowrap>Market Price</td><td colspan=4>&nbsp;</td></tr>

{working_orders}


<tr><td colspan=14 style="font: 1pt arial">&nbsp;</td></tr>

<tr align=left><td colspan=14><b>Summary:</b></td></tr>
<tr align=right>
    <td colspan=2><b>Deposit/Withdrawal:</b></td>
    <td colspan=2 class=mspt><b>0.00</b></td>
    <td colspan=4><b>Credit Facility:</b></td>
    <td class=mspt><b>0.00</b></td>
    <td colspan=5>&nbsp;</td></tr>
    
<tr align=right>
    <td colspan=2><b>Closed Trade P/L:</b></td>
    <td colspan=2 class=mspt><b>{sum_all_closed}</b></td>
    <td colspan=4><b>Floating P/L:</b></td>
    <td class=mspt><b>{sum_all_open}</b></td>
    <td colspan=3><b>Margin:</b></td>
    <td colspan=2 class=mspt><b>9 927.60</b></td></tr>

<tr align=right>
    <td colspan=2><b>Balance:</b></td>
    <td colspan=2 class=mspt><b>864 105.55</b></td>
    <td colspan=4><b>Equity:</b></td>
    <td class=mspt><b>809 008.50</b></td>
    <td colspan=3><b>Free Margin:</b></td>
    <td colspan=2 class=mspt><b>799 080.90</b></td></tr>
    
<tr><td colspan=14 style="font: 1pt arial">&nbsp;</td></tr>
<tr align=left><td colspan=14><b>Details:</b></td></tr>

<tr align=center>
<td colspan=14><img src="StatementDetailed_20670001.gif" width=820 height=200 border=0 alt="Graph"></td>
</tr>

<tr align=right>
    <td colspan=2><b>Gross Profit:</b></td>
    <td colspan=2 class=mspt><b>663 397.73</b></td>
    <td colspan=4><b>Gross Loss:</b></td>
    <td class=mspt><b>773 951.32</b></td>
    <td colspan=3><b>Total Net Profit:</b></td>
    <td colspan=2 class=mspt><b>{sum_all_closed}</b></td></tr>
    
<tr align=right>
    <td colspan=2><b>Profit Factor:</b></td>
    <td colspan=2 class=mspt><b>0.86</b></td>
    <td colspan=4><b>Expected Payoff:</b></td>
    <td class=mspt><b>-59.92</b></td>
    <td colspan=5>&nbsp;</td></tr>
    
<tr align=right>
    <td colspan=2><b>Absolute Drawdown:</b></td>
    <td colspan=2 class=mspt><b>110 553.59</b></td>
    <td colspan=4><b>Maximal Drawdown:</b></td>
    <td class=mspt><b>183 551.73 (17.52%)</b></td>
    <td colspan=3><b>Relative Drawdown:</b></td>
    <td colspan=2 class=mspt><b>17.52% (183 551.73)</b></td></tr>

<tr><td colspan=14 style="font: 1pt arial">&nbsp;</td></tr>
    
<tr align=right>
    <td colspan=2><b>Total Trades:</b></td>
    <td colspan=2 class=mspt><b>1845</b></td>
    <td colspan=4><b>Short Positions (won %):</b></td>
    <td class=mspt><b>987 (60.69%)</b></td>
    <td colspan=3><b>Long Positions (won %):</b></td>
    <td colspan=2 class=mspt><b>858 (55.94%)</b></td></tr>

<tr align=right>
    <td colspan=8><b>Profit Trades (% of total):</b></td>
    <td class=mspt><b>1079 (58.48%)</b></td>
    <td colspan=3><b>Loss trades (% of total):</b></td>
    <td colspan=2 class=mspt><b>766 (41.52%)</b></td></tr>

<tr align=right>
    <td colspan=2><b>Largest</b></td>
    <td colspan=6><b>profit trade:</b></td>
    <td class=mspt><b>13 273.34</b></td>
    <td colspan=3><b>loss trade:</b></td>
    <td colspan=2 class=mspt><b>-38 837.33</b></td></tr>

<tr align=right>
    <td colspan=2><b>Average</b></td>
    <td colspan=6><b>profit trade:</b></td>
    <td class=mspt><b>614.83</b></td>
    <td colspan=3><b>loss trade:</b></td>
    <td colspan=2 class=mspt><b>-1 010.38</b></td></tr>

<tr align=right>
    <td colspan=2><b>Maximum</b></td>
    <td colspan=6><b>consecutive wins ($):</b></td>
    <td class=mspt><b>22 (18 139.88)</b></td>
    <td colspan=3><b>consecutive losses ($):</b></td>
    <td colspan=2 class=mspt><b>18 (-8 709.05)</b></td></tr>

<tr align=right>
    <td colspan=2><b>Maximal</b></td>
    <td colspan=6><b>consecutive profit (count):</b></td>
    <td class=mspt><b>20 642.12 (19)</b></td>
    <td colspan=3><b>consecutive loss (count):</b></td>
    <td colspan=2 class=mspt><b>-64 411.45 (8)</b></td></tr>

<tr align=right>
    <td colspan=2><b>Average</b></td>
    <td colspan=6><b>consecutive wins:</b></td>
    <td class=mspt><b>3</b></td>
    <td colspan=3><b>consecutive losses:</b></td>
    <td colspan=2 class=mspt><b>2</b></td></tr>
</table>
</div></body></html>
'''

SPACE = '&nbsp;'

NO_TRANSACTIONS = '<tr align=right><td colspan=13 align=center>No transactions</td></tr>'

DOUBLE_ROW_COLOR = 'bgcolor=#E0E0E0 '

CLOSED_ROW = '''<tr {color}align=right>
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
<tr {color}align=right>
<td colspan=10>&nbsp;</td>
<td colspan=4>{comment}</td>
</tr>'''

OPEN_ROW = '''<tr {color}align=right>
<td title="{comment}">{ticket}</td>
<td class=msdate nowrap>{open_time}</td>
<td>{type}</td>
<td>{volume}</td>
<td>{item}</td>
<td style="mso-number-format:0\.{digit};">{open_price}</td>
<td style="mso-number-format:0\.{digit};">{sl}</td>
<td style="mso-number-format:0\.{digit};">{tp}</td>
<td class=msdate nowrap>&nbsp;</td>
<td style="mso-number-format:0\.{digit};">{close_price}</td>
<td class=mspt>{commission}</td>
<td class=mspt>{taxes}</td>
<td class=mspt>{swap}</td>
<td class=mspt>{profit}</td>
</tr>
<tr {color}align=right>
<td colspan=10>&nbsp;</td>
<td colspan=4>{comment}</td>
</tr>'''

WORKING_ROW = '''<tr {color}align=right>
<td title="{comment}">{ticket}</td>
<td class=msdate nowrap>{open_time}</td>
<td>{type}</td>
<td>{volume}</td>
<td>{item}</td>
<td style="mso-number-format:0\.{digit};">{open_price}</td>
<td style="mso-number-format:0\.{digit};">{sl}</td>
<td style="mso-number-format:0\.{digit};">{tp}</td>
<td class=msdate nowrap>&nbsp;</td>
<td style="mso-number-format:0\.{digit};">{close_price}</td>
<td colspan=4></td>
</tr>'''