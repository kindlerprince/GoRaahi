from django.shortcuts import render
import csv
import json
from urllib.error import URLError,HTTPError
from urllib.request import urlopen
import os
def result_new(x,y,sour,dest,dat):
#for bus
	fp=open(x,'r')
	reader=csv.reader(fp)
	next(reader)
	data1=[]
	for row in reader:
		data1.append(row)
	str1=''
	for row in data1:
		for r in row:
			r=r+','
			str1=str1+''.join(r)+'\n'
	str1=str1[:-2]
	#dict={'file':str1}
	fp.close()
#for flight
	with open(y) as fp:
		reader=csv.reader(fp)
		next(reader)
		str2=''
		for row in reader:
			str2 = str2+''.join(row)+'!\n'

		str2=str2[:-2]
	#dict={'file_bus':str1,'file_flight':str2}
	fp.close()
#for train
	str3=""
	url='https://api.railwayapi.com/v2/between/source/'+sour+'/dest/'+dest+'/date/'+dat+'/apikey/jx16978zj1/'
	#url='https://api.railwayapi.com/v2/between/source/tata/des/hwh/date/27-03-2019/apikey/jx16978zj1/'
	print(url)
	try:
	    conn = urlopen(url)
	except HTTPError as e:
	    # Return code error (e.g. 404, 501, ...)
	    # ...
		print('HTTPError: {}'.format(e.code))
		file_train=sour+dest+dat+'.json'
		print(file_train)
		fp=open(file_train,"r")
		str3=json.load(fp)
		print(str3)
		fp.close()

	except URLError as e:
	    # Not an HTTP-specific error (e.g. connection refused)
	    # ...
	    print('URLError: {}'.format(e.reason))
	else:
	    # 200
	    # ...
	    #print('good')
		source=conn.read()
		str3 = json.loads(source)
		file_train=sour+dest+dat+'.json'
		fp=open(file_train,"w")
		json.dump(str3,fp)
		fp.close()
	#print(str3['trains'])
	ava_dict={}
	i=0
	'''
	for x in str3['trains']:
		#print(x['number'])
		#print(x['from_station']['code'])
		#print(x['to_station']['code'])
		seat_url='https://api.railwayapi.com/v2/check-seat/train/'+x['number']+'/source/'+x['from_station']['code']+'/dest/'+x['to_station']['code']+'/date/08-04-2019/pref/CC/quota/GN/apikey/jx16978zj1/'
		print(seat_url)
		with urlopen(seat_url) as response:
			seat_source=response.read()
		ava_dict[i] = json.loads(seat_source)
		i=i+1
	print(ava_dict)
	'''
	dict={'file_bus':str1,'file_flight':str2,'file_train':str3}
	return dict
	#return render(request,'basicapp/result.html',context=dict)
# Create your views here.

def index(request):
	if(request.method=='POST'):
		sour=request.POST.get('source')
		dest=request.POST.get('destination')
		dat=request.POST.get('j_date')

		submitbutton=request.POST.get('Submit')
		print(sour)
		print(dest)
		print(dat)
		l=dat.split('-')
		if(int(l[0])<10):
			l[0]=l[0][1:]
		bus_dat=l[0]+'_'+l[1][:3]+l[2]
		flight_dat=l[0]+'_'+l[1]+l[2]
		file_bus='sorted_'+sour+'_'+dest+'_'+bus_dat+'.csv'
		file_flight='flight/'+sour+'_'+dest+'_'+flight_dat+'.csv'
		#print(file_flight)
		print(sour)
		print(dest)
		month={"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
		train_dat=l[0]+'-'+month[l[1]]+'-2019'
		#print(train_dat)
		fp=open('city.json','r')
		train_list=json.load(fp)
		fp.close()
		train_sour=train_list[sour]
		train_dest=train_list[dest]
		print(train_sour)
		print(train_dest)
		dict=result_new(file_bus,file_flight,train_sour,train_dest,train_dat)
		dict['source']=sour
		dict['destination']=dest
		dict['date']=dat
		return render(request,'basicapp/result.html',context=dict)
	return render(request,'basicapp/home.html')
def train(request):
	return render(request,'basicapp/train.html')
def stod(request):
	return render(request,'basicapp/stod.html')
def bus(request):
	return render(request,'basicapp/bus.html')
def flight(request):
	return render(request,'basicapp/flight.html')
def signin(request):
	return render(request,'basicapp/signin.html')



def result(request):
#for bus
	fp=open('cheap_copy.csv','r')
	reader=csv.reader(fp)
	next(reader)
	data1=[]
	for row in reader:
		data1.append(row)
	str1=''
	for row in data1:
		for r in row:
			r=r+','
			str1=str1+''.join(r)+'\n'
	str1=str1[:-2]
	dict={'file':str1}
	fp.close()
#for flight
	with open("ixigo.csv") as fp:
		reader=csv.reader(fp)
		next(reader)
		str2=''
		for row in reader:
			str2 = str2+''.join(row)+'!\n'

		str2=str2[:-2]
	#dict={'file_bus':str1,'file_flight':str2}
	fp.close()
#for train
	with urlopen('https://api.railwayapi.com/v2/between/source/tata/dest/hwh/date/30-04-2019/apikey/jx16978zj1/') as response:
		source=response.read()
	str3 = json.loads(source)

	#print(str3['trains'])
	ava_dict={}
	i=0
	for x in str3['trains']:
		#print(x['number'])
		#print(x['from_station']['code'])
		#print(x['to_station']['code'])
		seat_url='https://api.railwayapi.com/v2/check-seat/train/'+x['number']+'/source/'+x['from_station']['code']+'/dest/'+x['to_station']['code']+'/date/30-04-2019/pref/CC/quota/GN/apikey/jx16978zj1/'
		print(seat_url)
		with urlopen(seat_url) as response:
			seat_source=response.read()
		ava_dict[i] = json.loads(seat_source)
		i=i+1
	print(ava_dict)

	dict={'file_bus':str1,'file_flight':str2,'file_train':str3}
	return render(request,'basicapp/result.html',context=dict)
