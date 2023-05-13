from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
import time
# from atn import AT
# Create your views here.

from django.shortcuts import render
from  rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime
from django.db.models import Count
from django.db import connection

####################################

import zk
from zk import ZK, const
import pandas as pd
import calendar
import pandas as pd
from datetime import datetime, timedelta, time
import threading

# Create a lock object
lock = threading.Lock()

def machine1(ip,port,name,password,user_id):
    conn = None
    zk = ZK(ip, port,timeout=10)
    try:
        print('Connecting to device ...')
        conn = zk.connect()
        print('Disabling device ...')
        conn.disable_device()
        print ('Firmware Version: : {}'.format(conn.get_firmware_version()))
    except Exception as e:
        print ("Process terminate : {}".format(e))
    #   
    print(123)
    user = conn.get_users()
    print(1234)
    print(user)
    try:
        conn.set_user(uid=None, name=str(name), privilege=str(0), password=str(password), group_id=str(''), user_id=str(user_id), card=0)
        conn.enable_device()       
        if conn:
            conn.disconnect()
    except:
        conn.enable_device()       
        if conn:
            conn.disconnect()
    return JsonResponse({'Succes': "1"})

def machine(ip,port):
    conn = None
    zk = ZK(ip, port,timeout=10)
    try:
        print('Connecting to device ...')
        conn = zk.connect()
        print('Disabling device ...')
        conn.disable_device()
        print ('Firmware Version: : {}'.format(conn.get_firmware_version()))
    except Exception as e:
        print ("Process terminate : {}".format(e))
    date = []
    user_id2 = []
    for attendance in conn.get_attendance():
        if attendance is None:
            # implement here timeout logic
            pass
        else:
            date.append(attendance.timestamp)
            user_id2.append(attendance.user_id)   
    name = []
    user_id1 = []
    jk = {}
    users = conn.get_users()
    for user in users:

        name.append(user.name)
        user_id1.append(user.user_id)
        jk[f'{user.user_id}'] = user.name
    name1 = []
    with lock:
        for i in range(0,len(date)):
            name1.append(jk.get(f'{user_id2[i]}'))
        
    df = {
        "employee_id_id" : user_id2,
        "Name" : name1,
        "Date_Time" : date
    }
    df = pd.DataFrame.from_dict(df)
    df[['date', 'time']] = df['Date_Time'].apply(lambda x: pd.Series(str(x).split(" ")))
#     df.drop(columns=[r"Date/Time"], inplace=True)
    with lock:
        conn.enable_device()       
        if conn:
            conn.disconnect()
    return df

def employ(request):
    if request.method=="POST":
        ip = request.POST.get('ip')
        ip1 = Device.objects.get(IP= ip)
        ip2 = str(ip1) 
        port1 = int(ip1.port)
        device = ip1.device_id
        print(ip1,port1,device)
        conn = machine(ip,port1)
        print(len(conn))
        for i in range(0,len(conn)):
            conn['Name'][i]
        
        
        # print(port)
        return HttpResponse("done")
     
    data = Device.objects.values_list('IP', flat=True)
    print(data)
    context = {
        'data':data
    }
    template = loader.get_template('employ.html')
    return HttpResponse(template.render(context, request))
    
from django.http import JsonResponse
    
    
def employdetail(requrest,deviceid):
    try:
        print(deviceid)
        device = Device.objects.get(device_id= deviceid)
        ip = device.IP
        port = int(device.port)
        com_id = device.company_id
        device_id = deviceid
        zk = ZK(ip,port,timeout=10)
        conn = None
        try:
            print('Connecting to device ...')
            conn = zk.connect()
            print('Disabling device ...')
            conn.disable_device()
            print ('Firmware Version: : {}'.format(conn.get_firmware_version()))
            
        except Exception as e:
            print ("Process terminate : {}".format(e))
        user = conn.get_users()
        name= []
        uid = []
        device_id1 =[]
        password = []
        card_no = []
        df1 = []
        for i in user:
            name.append(i.name)
            uid.append(i.uid)
            device_id1.append(device_id)
            password.append('12345')
            card_no.append('0')
            df = {
            'name': i.name,
            'device_id': device_id,
            'employee_uid': i.uid,
            'password': '12345',
            'card_no' : '0',
            
            }
            df1.append(df)
        conn.disconnect()
        # df = df = pd.DataFrame.from_dict(df)
        # df = df.to_json()
        
        return JsonResponse({'data':df1})
    
    except:
        return JsonResponse({'Error':"device Not Avaiable"})
        
        
def newemployee(requrest,id):    
    data = NewEmployee.objects.filter(device_id =id)
    print(data)
    users = []
    for i in data:
        try:
            name = i.name
            password = str(i.password)
            employee_uid = str(i.employee_uid)
            print(i.name)
            print(i.device_id.device_id)
            print(i.password)
            print(i.employee_uid)
          
            device = Device.objects.get(device_id=id)
            port = int(device.port)
            print(port)
            ip = device.IP
            # print(type(ip))#,,employee_uid,port,ip
            machine1(ip, port, name, password, employee_uid)
            data1 = NewEmployee.objects.get(name=name)
            data1.delete()
        except:
            users.append(i.name)
            # return JsonResponse({'Error': f"{users} ID Already Exists"})
    
    return JsonResponse({'Success': "1"})
    

# conn.set_user(uid=10011, name=str('zk1bhai1'), privilege=str(0), password=str(12345), group_id=str(''), user_id=str(121212), card=str(0))

from sqlalchemy import create_engine
import pymysql
import pandas as pd

def attandance(request,id):
    device = Device.objects.get(device_id=id)
    df = machine(str(device.IP), int(device.port))
    dis  = Device.objects.get(device_id=device.device_id)
    print(dis)
    for index, row in df.iterrows():
        # device = Device.objects.get(device_id=id)
        employee_id = int(row['employee_id_id'])
        name = str(row['Name'])
        date_time = str(row['Date_Time'])
        date = str(row['date'])
        time = str(row['time'])
        # device_id = Device.objects.get(device_id=row['device_id'])
        # company_id = row['company_id']
        AT = Attandance(employee_id_id=employee_id,device_id=dis,company_id=device.company_id,name=name,Date=date,time=time,Date_Time=date_time)
        AT.save()  
    for row in Attandance.objects.filter(device_id=id).reverse():
        if Attandance.objects.filter(Date_Time=row.Date_Time).count() > 1:
            row.delete()
        # assuming which duplicate is removed doesn't matter...
    
    return  JsonResponse({'success':1})

        
    # except:
    #     return  JsonResponse({'Error': f"{device.IP} Not Connected" })
    
    
def delete_dub(request,id):
   

    # assuming which duplicate is removed doesn't matter...
    for row in Attandance.objects.filter(device_id=id).reverse():
        if Attandance.objects.filter(Date_Time=row.Date_Time).count() > 1:
            row.delete()
    return HttpResponse('Done')

def fresh(request,ip,port):
    df = machine(ip,port)
    df = df.to_json()
    return JsonResponse({'df':df})
    # return HttpResponse(df)





