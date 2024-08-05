import pandas as pd
import datetime
import smtplib

#enter your authentication details
GMAIL_ID = ''
GMAIL_PASS=''

def sendEmail(to,sub,msg):
    print(f"Email is sent to {to} with subject{sub},and with message {msg}")
    s=smtplib.SMTP('smtp.gamil.com', 587 )
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PASS)
    s.sendmail(GMAIL_ID,to,f"Subject{sub} \n\n {msg}")
if __name__=="__main__":
    df = pd.read_excel("D:\Python\Automatic wisher\.venv\data.xlsx")
    # print(df)
    today=datetime.datetime.now().strftime("%d-%m")
    yearNow=datetime.datetime.now().strftime("%y")
    # print(today)
writeInd=[]
for index, item in df.iterrows():
    # print(index, item["Name"])
    
    bday = item["Birthday"].strftime("%d-%m")
    # print(bday)
    if(bday==today and yearNow not in str(item['Year'])):
        sendEmail(item['Email'],'Happy birthday to you',item['Dialogue'])
        writeInd.append(index)
print(writeInd)  
for i in writeInd:
    yr = df.loc[i,'Year']
    df.loc[i,'Year'] = str(yr) + ',' + str(yearNow)
    # print(df.loc[i,'Year']) 
print(df)