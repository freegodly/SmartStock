#coding:utf-8

import tushare as ts
import json


def getchartjson(request,code_str):
	data = get_hist_data_list(code_str,start='2016-01-01',end='2016-07-01')
	
	k_data = dict(
		data=data,
		code=code_str
	)

	
	return HttpResponse( json.dumps(k_data),content_type="application/json")



def get_hist_data_list(code,start=None,end=None):
	orange_data = None
	if start==None and end==None:
		orange_data =  ts.get_h_data(code)
	else:
		orange_data =  ts.get_h_data(code,start=start,end=end)


	quotes = [[index.strftime('%Y-%m-%d'),row['open'],row['close'],row['low'],row['high'],row['volume'],row['amount']] for index,row in orange_data.iterrows() ]
	quotes.reverse()
	return quotes

def splice_stock_data(data):
	stock_date = [i[0] for i in data]
	stock_value = [i[1:len(i)] for i in data]
	return (stock_date,stock_value)