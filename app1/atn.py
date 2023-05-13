import zk
from zk import ZK, const
import pandas as pd
import calendar
import pandas as pd
from datetime import datetime, timedelta, time

class AT():
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
        for i in range(0,len(date)):
            name1.append(jk.get(f'{user_id2[i]}'))
            
        df = {
            "emp_id" : user_id2,
            "employee_id" : user_id2,
            "Name" : name1,
            "Date_Time" : date
        }
        df = pd.DataFrame.from_dict(df)
        df[['date', 'time']] = df['Date_Time'].apply(lambda x: pd.Series(str(x).split(" ")))
    #     df.drop(columns=[r"Date/Time"], inplace=True)
        conn.enable_device()       
        if conn:
            conn.disconnect()
        return df