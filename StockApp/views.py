#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
import tushare as ts
# Create your views here.
from echarts import *
import json


def index(request):
    return render(request, 'index.html')


def getchartjson(request):
	data = get_hist_data_list('002426',start='2016-01-01',end='2016-07-01')
	
	k_data = dict(
		data=data,
		code='002426'
	)

	
	return HttpResponse( json.dumps(k_data),content_type="application/json")



def get_hist_data_list(code,start=None,end=None):
	orange_data = None
	if start==None and end==None:
		orange_data =  ts.get_hist_data(code)
	else:
		orange_data =  ts.get_hist_data(code,start=start,end=end)


	quotes = [[index,row['open'],row['close'],row['low'],row['high']] for index,row in orange_data.iterrows() ]
	quotes.reverse()
	return quotes

def splice_stock_data(data):
	stock_date = [i[0] for i in data]
	stock_value = [i[1:len(i)] for i in data]
	return (stock_date,stock_value)