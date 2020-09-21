#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the relevant libraries
import pandas as pd
from pandas import datetime
from datetime import date
from matplotlib import pyplot
import numpy as np


# In[2]:


# read and parse data 
df = pd.read_excel('C:\\Users\\akshu\\Downloads\\Internship.xlsx', header=0, squeeze=True)


# In[3]:


# Renaming the columns 
df.columns = ['flowid', 'date','Time','Count']


# In[4]:


# The format of Data Variable is inconsistent hence making it consistent
df.date


# In[5]:


# Checking for null values in date column
df.date.loc[df.date.isnull() == True]


# In[6]:


# Dropping the Null Values/Missing Values
df.drop([7985,9488],inplace = True)


# In[7]:


df.date.isnull().sum()


# In[8]:


# Since the format of the date variable in not consistent let's make it consisitent
date = pd.to_datetime(df['date'])


# In[9]:


# Concatenating the date variable with a consistent format with the df dataset.
df = pd.concat([df, date], axis=1)


# In[10]:


df.head()


# In[11]:


# Renaming the columns
df.columns = ['flowid', 'date','Time','Count','datenew']



# In[12]:


# Creating a string varible dateneww for analysis which is in string format 
w = df['datenew']
w.tolist()
wt = []
for l in w:
    gr = l.strftime("%Y/%m/%d")
    wt.append(gr)


# In[13]:


datenewww = pd.DataFrame(wt)
df = pd.concat([df,  datenewww], axis=1)


# In[14]:


# Renaming the columns
df.columns = ['flowid', 'date','Time','Count','datenew','dateneww']


# In[15]:


df['dateneww']


# In[16]:


# Now we are doing the Exploratory Data Analysis to see if the inflow and outflow of people are dependent on the weekday 
# We are finding the weekday from the Date Variable i.e datenew

from datetime import datetime
data = []
for i in range(10081):
           data.append(df.datenew[i].weekday())
           


# In[17]:


# Droping the column date which is in inconsistent format
df.drop('date', axis=1, inplace=True)


# In[18]:


# O means Monday 
# 1 means Tuesday
# 2 means Wednesday
# 3 means Thursday 
# 4 means Friday
# 5 means Saturday
# 6 means Sunday


# In[19]:


data


# In[20]:


# Converting the list to Pandas DataFrame
dayofweek = pd.DataFrame(data)


# In[21]:


# Concatenating the column Dayofweek with df dataset
df = pd.concat([df, dayofweek], axis=1)
 


# In[22]:


df.head()


# In[23]:


# Naming the columns of the df dataset
df.columns = ['flowid', 'Time','Count','datenew','dateneww','dayofweek']


# In[24]:


# Hence for our analysis lets divide our day of the week column into weekdays and weekends
# weekdays is denoted by True
# weekends is denoted by False

I = [0,1,2,3,4,5]

df['weekdayFlag'] = np.where(df['dayofweek'].isin(I), 1 , 0)




# In[25]:


# For our analysis let's also parse month from the date variable since the inflow and outflow of people vary with the month
from datetime import datetime
data = []
for i in range(10081):
           data.append(df.datenew[i].month)


# In[26]:


month = pd.DataFrame(data)


# In[27]:


df = pd.concat([df, month], axis=1)


# In[28]:


df.columns = ['flowid', 'Time','Count','datenew','dateneww','dayofweek','weekdayFlag','month']


# In[29]:


df.head()


# In[30]:


# From the df data separating the inflow and outflow data
# Output Data is defined as out_df
# Input Data is defined as in_df
out_df = df.loc[df['flowid'] == 7]

in_df = df.loc[df['flowid'] == 9]


# In[31]:


# Let's find the peak hours flag for Inflow and Outflow Data on weekend and weekday
# Let's subset the data for weekdays and weekends for each month


# In[32]:


# Subsetting the data for each month
inflowdatamonth1 = in_df.loc[in_df['month']== 1].reset_index()
inflowdatamonth2 = in_df.loc[in_df['month']== 2].reset_index()
inflowdatamonth3 = in_df.loc[in_df['month']== 3].reset_index()
inflowdatamonth4 = in_df.loc[in_df['month']== 4].reset_index()
inflowdatamonth5 = in_df.loc[in_df['month']== 5].reset_index()
inflowdatamonth6 = in_df.loc[in_df['month']== 6].reset_index()
inflowdatamonth7 = in_df.loc[in_df['month']== 7].reset_index()
inflowdatamonth8 = in_df.loc[in_df['month']== 8].reset_index()
inflowdatamonth9 = in_df.loc[in_df['month']== 9].reset_index()
inflowdatamonth10 = in_df.loc[in_df['month']== 10].reset_index()
inflowdatamonth11 = in_df.loc[in_df['month']== 11].reset_index()
inflowdatamonth12 = in_df.loc[in_df['month']== 12].reset_index()


# In[33]:


# Subsetting the data for weekday and weekend
inflowdatamonth1weekday = inflowdatamonth1.loc[inflowdatamonth1['weekdayFlag']== True].reset_index()
inflowdatamonth1weekend = inflowdatamonth1.loc[inflowdatamonth1['weekdayFlag']== False].reset_index()
inflowdatamonth2weekday = inflowdatamonth2.loc[inflowdatamonth2['weekdayFlag']== True].reset_index()
inflowdatamonth2weekend = inflowdatamonth2.loc[inflowdatamonth2['weekdayFlag']== False].reset_index()

inflowdatamonth3weekday = inflowdatamonth3.loc[inflowdatamonth3['weekdayFlag']== True].reset_index()
inflowdatamonth3weekend = inflowdatamonth3.loc[inflowdatamonth3['weekdayFlag']== False].reset_index()
inflowdatamonth4weekday = inflowdatamonth4.loc[inflowdatamonth4['weekdayFlag']== True].reset_index()
inflowdatamonth4weekend = inflowdatamonth4.loc[inflowdatamonth4['weekdayFlag']== False].reset_index()

inflowdatamonth5weekday = inflowdatamonth5.loc[inflowdatamonth5['weekdayFlag']== True].reset_index()
inflowdatamonth5weekend = inflowdatamonth5.loc[inflowdatamonth5['weekdayFlag']== False].reset_index()
inflowdatamonth6weekday = inflowdatamonth6.loc[inflowdatamonth6['weekdayFlag']== True].reset_index()
inflowdatamonth6weekend = inflowdatamonth6.loc[inflowdatamonth6['weekdayFlag']== False].reset_index()

inflowdatamonth7weekday = inflowdatamonth7.loc[inflowdatamonth7['weekdayFlag']== True].reset_index()
inflowdatamonth7weekend = inflowdatamonth7.loc[inflowdatamonth7['weekdayFlag']== False].reset_index()
inflowdatamonth8weekday = inflowdatamonth8.loc[inflowdatamonth8['weekdayFlag']== True].reset_index()
inflowdatamonth8weekend = inflowdatamonth8.loc[inflowdatamonth8['weekdayFlag']== False].reset_index()

inflowdatamonth9weekday = inflowdatamonth9.loc[inflowdatamonth9['weekdayFlag']== True].reset_index()
inflowdatamonth9weekend = inflowdatamonth9.loc[inflowdatamonth9['weekdayFlag']== False].reset_index()
inflowdatamonth10weekday = inflowdatamonth10.loc[inflowdatamonth10['weekdayFlag']== True].reset_index()
inflowdatamonth10weekend = inflowdatamonth10.loc[inflowdatamonth10['weekdayFlag']== False].reset_index()
inflowdatamonth11weekday = inflowdatamonth11.loc[inflowdatamonth11['weekdayFlag']== True].reset_index()
inflowdatamonth11weekend = inflowdatamonth11.loc[inflowdatamonth11['weekdayFlag']== False].reset_index()
inflowdatamonth12weekday = inflowdatamonth12.loc[inflowdatamonth12['weekdayFlag']== True].reset_index()
inflowdatamonth12weekend = inflowdatamonth12.loc[inflowdatamonth12['weekdayFlag']== False].reset_index()


# In[34]:


# Drawing the pivot table for inflow data for each month with time column and mean number of people entering during that tym
pivot1 = inflowdatamonth1weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot2 = inflowdatamonth1weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot3 = inflowdatamonth2weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot4 = inflowdatamonth2weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot5 = inflowdatamonth3weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot6 = inflowdatamonth3weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot7 = inflowdatamonth4weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot8 = inflowdatamonth4weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot9 = inflowdatamonth5weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot10 = inflowdatamonth5weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot11 = inflowdatamonth6weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot12 = inflowdatamonth6weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot13 = inflowdatamonth7weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot14 = inflowdatamonth7weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot15 = inflowdatamonth8weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot16 = inflowdatamonth8weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot17 = inflowdatamonth9weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot18 = inflowdatamonth9weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot19 = inflowdatamonth10weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot20 = inflowdatamonth10weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot21 = inflowdatamonth11weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot22 = inflowdatamonth11weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot23 = inflowdatamonth12weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivot24 = inflowdatamonth12weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})


# In[35]:


#Calculating mean and median
mean1 = pivot1.mean()    
median1 = pivot1.median()
mean2 = pivot2.mean()
median2 = pivot2.median()
mean3 = pivot3.mean()
median3 = pivot3.median()
mean4 = pivot4.mean()
median4 = pivot4.median()
mean5 = pivot5.mean()
median5 = pivot5.median()
mean6 = pivot6.mean()
median6 = pivot6.median()
mean7 = pivot7.mean()
median7 = pivot7.median()
mean8 = pivot8.mean()
median8 = pivot8.median()
mean9 = pivot9.mean()
median9 = pivot9.median()
mean10 = pivot10.mean()
median10 = pivot10.median()
mean11 = pivot11.mean()
median11 = pivot11.median()
mean12 = pivot12.mean()
median12 = pivot12.median()
mean13 = pivot13.mean()
median13 = pivot13.median()
mean14 = pivot14.mean()
median14 = pivot14.median()
mean15 = pivot15.mean()
median15 = pivot15.median()
mean16 = pivot16.mean()
median16 = pivot16.median()
mean17 = pivot17.mean()
median17 = pivot17.median()
mean18 = pivot18.mean()
median18 = pivot18.median()
mean19 = pivot19.mean()
median19 = pivot19.median()
mean20 = pivot20.mean()
median20 = pivot20.median()
mean21 = pivot21.mean()
median21 = pivot21.median()
mean22 = pivot22.mean()
median22 = pivot22.median()
mean23 = pivot23.mean()
median23 = pivot23.median()
mean24 = pivot24.mean()
median24 = pivot24.median()


# In[36]:


#Calculating the peak hours for each subset of data
PeakHours1 = inflowdatamonth1weekday.loc[inflowdatamonth1weekday['Count']>int(mean1)]
PeakhoursTiminginflow1 = PeakHours1['Time']
PeakhoursTiminginflow1.reset_index(drop = True, inplace= True)
PeakhoursTiminginflow1
L = PeakhoursTiminginflow1
inflowdatamonth1weekday['PeakFlag'] = np.where(inflowdatamonth1weekday['Time'].isin(L), True , False)

PeakHours2 = inflowdatamonth1weekend.loc[inflowdatamonth1weekend['Count']>int(mean2)]
PeakhoursTiminginflow2 = PeakHours2['Time']
PeakhoursTiminginflow2.reset_index(drop = True, inplace= True)
PeakhoursTiminginflow2
L1 = PeakhoursTiminginflow2
inflowdatamonth1weekend['PeakFlag'] = np.where(inflowdatamonth1weekend['Time'].isin(L1), True , False)

PeakHours3 = inflowdatamonth2weekday.loc[inflowdatamonth2weekday['Count']>int(mean3)]
PeakhoursTiminginflow3 = PeakHours3['Time']
PeakhoursTiminginflow3.reset_index(drop = True, inplace= True)
PeakhoursTiminginflow3
L2 = PeakhoursTiminginflow3
inflowdatamonth2weekday['PeakFlag'] = np.where(inflowdatamonth2weekday['Time'].isin(L2), True , False)

#PeakHours4 = inflowdatamonth2weekend.loc[inflowdatamonth2weekend['Count']>int(mean4)]
#PeakhoursTiminginflow4 = PeakHours4['Time']
#PeakhoursTiminginflow4.reset_index(drop = True, inplace= True)
#PeakhoursTiminginflow4
#L3 = PeakhoursTiminginflow4
#inflowdatamonth2weekend['PeakFlag'] = np.where(inflowdatamonth2weekend['Time'].isin(L3), True , False)



PeakHours5 = inflowdatamonth3weekday.loc[inflowdatamonth3weekday['Count']>int(mean5)]
PeakhoursTiminginflow5 = PeakHours5['Time']
PeakhoursTiminginflow5.reset_index(drop = True, inplace= True)
PeakhoursTiminginflow5
L4 = PeakhoursTiminginflow5
inflowdatamonth3weekday['PeakFlag'] = np.where(inflowdatamonth3weekday['Time'].isin(L4), True , False)

#PeakHours6 = inflowdatamonth3weekend.loc[inflowdatamonth3weekend['Count']>int(mean6)]
#PeakhoursTiminginflow6 = PeakHours6['Time']
#PeakhoursTiminginflow6.reset_index(drop = True, inplace= True)
#PeakhoursTiminginflow6
#L5 = PeakhoursTiminginflow6
#inflowdatamonth3weekend['PeakFlag'] = np.where(inflowdatamonth3weekend['Time'].isin(L5), True , False)



PeakHours7 = inflowdatamonth4weekday.loc[inflowdatamonth4weekday['Count']>int(mean7)]
PeakhoursTiminginflow7 = PeakHours7['Time']
PeakhoursTiminginflow7.reset_index(drop = True, inplace= True)
PeakhoursTiminginflow7
L6 = PeakhoursTiminginflow7
inflowdatamonth4weekday['PeakFlag'] = np.where(inflowdatamonth4weekday['Time'].isin(L6), True , False)



PeakHours8 = inflowdatamonth4weekend.loc[inflowdatamonth4weekend['Count']>int(mean8)]
PeakhoursTiminginflow8 = PeakHours8['Time']
PeakhoursTiminginflow8.reset_index(drop = True, inplace= True)
PeakhoursTiminginflow8
L8 = PeakhoursTiminginflow8
inflowdatamonth4weekend['PeakFlag'] = np.where(inflowdatamonth4weekend['Time'].isin(L8), True , False)

PeakHours9 = inflowdatamonth5weekday.loc[inflowdatamonth5weekday['Count']>int(mean9)]
PeakhoursTiminginflow9 = PeakHours9['Time']
PeakhoursTiminginflow9.reset_index(drop = True, inplace= True)
PeakhoursTiminginflow9
L9 = PeakhoursTiminginflow9
inflowdatamonth5weekday['PeakFlag'] = np.where(inflowdatamonth5weekday['Time'].isin(L9), True , False)

PeakHours10 = inflowdatamonth5weekend.loc[inflowdatamonth5weekend['Count']>int(mean10)]
PeakhoursTiminginflow10 = PeakHours10['Time']
PeakhoursTiminginflow10.reset_index(drop = True, inplace= True)
PeakhoursTiminginflow10
L10 = PeakhoursTiminginflow10
inflowdatamonth5weekend['PeakFlag'] = np.where(inflowdatamonth5weekend['Time'].isin(L10), True , False)

PeakHours11 = inflowdatamonth6weekday.loc[inflowdatamonth6weekday['Count']>int(mean11)]
PeakhoursTiminginflow11 = PeakHours11['Time']
PeakhoursTiminginflow11.reset_index(drop = True, inplace= True)
PeakhoursTiminginflow11
L11 = PeakhoursTiminginflow11
inflowdatamonth6weekday['PeakFlag'] = np.where(inflowdatamonth6weekday['Time'].isin(L11), True , False)

#PeakHours12 = inflowdatamonth6weekend.loc[inflowdatamonth6weekend['Count']>int(mean12)]
#PeakhoursTiminginflow12 = PeakHours12['Time']
#PeakhoursTiminginflow12.reset_index(drop = True, inplace= True)
#PeakhoursTiminginflow12
#L12 = PeakhoursTiminginflow12
#inflowdatamonth6weekend['PeakFlag'] = np.where(inflowdatamonth6weekend['Time'].isin(L12), True , False)

PeakHours13 = inflowdatamonth7weekday.loc[inflowdatamonth7weekday['Count']>int(mean13)]
PeakhoursTiminginflow13 = PeakHours13['Time']
PeakhoursTiminginflow13.reset_index(drop = True, inplace= True)
PeakhoursTiminginflow13
L13 = PeakhoursTiminginflow13
inflowdatamonth7weekday['PeakFlag'] = np.where(inflowdatamonth7weekday['Time'].isin(L13), True , False)


PeakHours14 = inflowdatamonth7weekend.loc[inflowdatamonth7weekend['Count']>int(mean14)]
PeakhoursTiminginflow14 = PeakHours14['Time']
PeakhoursTiminginflow14.reset_index(drop = True, inplace= True)
PeakhoursTiminginflow14
L14 = PeakhoursTiminginflow14

inflowdatamonth7weekend['PeakFlag'] = np.where(inflowdatamonth7weekend['Time'].isin(L14), True , False)


PeakHours15 = inflowdatamonth8weekday.loc[inflowdatamonth8weekday['Count']>int(mean15)]
PeakhoursTiminginflow15 = PeakHours15['Time']
PeakhoursTiminginflow15.reset_index(drop = True, inplace= True)
PeakhoursTiminginflow15
L15 = PeakhoursTiminginflow15
inflowdatamonth8weekday['PeakFlag'] = np.where(inflowdatamonth8weekday['Time'].isin(L15), True , False)


PeakHours16 = inflowdatamonth8weekend.loc[inflowdatamonth8weekend['Count']>int(mean16)]
PeakhoursTiminginflow16 = PeakHours16['Time']
PeakhoursTiminginflow16.reset_index(drop = True, inplace= True)
PeakhoursTiminginflow16
L16 = PeakhoursTiminginflow16
inflowdatamonth8weekend['PeakFlag'] = np.where(inflowdatamonth8weekend['Time'].isin(L16), True , False)



PeakHours17 = inflowdatamonth9weekday.loc[inflowdatamonth9weekday['Count']>int(mean17)]
PeakhoursTiminginflow17 = PeakHours17['Time']
PeakhoursTiminginflow17.reset_index(drop = True, inplace= True)
PeakhoursTiminginflow17
L17 = PeakhoursTiminginflow17
inflowdatamonth9weekday['PeakFlag'] = np.where(inflowdatamonth9weekday['Time'].isin(L17), True , False)


PeakHours18 = inflowdatamonth9weekend.loc[inflowdatamonth9weekend['Count']>int(mean18)]
PeakhoursTiminginflow18 = PeakHours18['Time']
PeakhoursTiminginflow18.reset_index(drop = True, inplace= True)
PeakhoursTiminginflow18
L18 = PeakhoursTiminginflow18
inflowdatamonth9weekend['PeakFlag'] = np.where(inflowdatamonth9weekend['Time'].isin(L18), True , False)


PeakHours19 = inflowdatamonth10weekday.loc[inflowdatamonth10weekday['Count']>int(mean19)]
PeakhoursTiminginflow19 = PeakHours19['Time']
PeakhoursTiminginflow19.reset_index(drop = True, inplace= True)
PeakhoursTiminginflow19
L19 = PeakhoursTiminginflow19
inflowdatamonth10weekday['PeakFlag'] = np.where(inflowdatamonth10weekday['Time'].isin(L19), True , False)

PeakHours20 = inflowdatamonth10weekend.loc[inflowdatamonth10weekend['Count']>int(mean20)]
PeakhoursTiminginflow20 = PeakHours20['Time']
PeakhoursTiminginflow20.reset_index(drop = True, inplace= True)
PeakhoursTiminginflow20
L20 = PeakhoursTiminginflow20
inflowdatamonth10weekend['PeakFlag'] = np.where(inflowdatamonth10weekend['Time'].isin(L20), True , False)

PeakHours21 = inflowdatamonth11weekday.loc[inflowdatamonth11weekday['Count']>int(mean21)]
PeakhoursTiminginflow21 = PeakHours21['Time']
PeakhoursTiminginflow21.reset_index(drop = True, inplace= True)
PeakhoursTiminginflow21
L21 = PeakhoursTiminginflow21
inflowdatamonth11weekday['PeakFlag'] = np.where(inflowdatamonth11weekday['Time'].isin(L21), True , False)

#PeakHours22 = inflowdatamonth11weekend.loc[inflowdatamonth11weekend['Count']>int(mean22)]
#PeakhoursTiminginflow22 = PeakHours22['Time']
#PeakhoursTiminginflow22.reset_index(drop = True, inplace= True)
#PeakhoursTiminginflow22
#L22 = PeakhoursTiminginflow22
#inflowdatamonth11weekend['PeakFlag'] = np.where(inflowdatamonth11weekend['Time'].isin(L22), True , False)

PeakHours23 = inflowdatamonth12weekday.loc[inflowdatamonth12weekday['Count']>int(mean23)]
PeakhoursTiminginflow23 = PeakHours23['Time']
PeakhoursTiminginflow23.reset_index(drop = True, inplace= True)
PeakhoursTiminginflow23
L23 = PeakhoursTiminginflow23
inflowdatamonth12weekday['PeakFlag'] = np.where(inflowdatamonth12weekday['Time'].isin(L23), True , False)


#PeakHours24 = inflowdatamonth12weekend.loc[inflowdatamonth12weekend['Count']>int(mean24)]
#PeakhoursTiminginflow24 = PeakHours2['Time']
#PeakhoursTiminginflow24.reset_index(drop = True, inplace= True)
#PeakhoursTiminginflow24
#L24 = PeakhoursTiminginflow24
#inflowdatamonth12weekend['PeakFlag'] = np.where(inflowdatamonth12weekend['Time'].isin(L24), True , False)





# In[37]:



# Let's subset the data into peak and non-peak hours for month 1 
inflowdatamonth1weekdayPeak = inflowdatamonth1weekday.loc[inflowdatamonth1weekday['PeakFlag']== True]

inflowdatamonth1weekdayNonPeak = inflowdatamonth1weekday.loc[inflowdatamonth1weekday['PeakFlag']== False]

inflowdatamonth1weekendPeak = inflowdatamonth1weekend.loc[inflowdatamonth1weekend['PeakFlag']== True]

inflowdatamonth1weekendNonPeak = inflowdatamonth1weekend.loc[inflowdatamonth1weekend['PeakFlag']== False]


# In[38]:


pivot25 = pd.pivot_table(data = inflowdatamonth1weekdayPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')
pivot26 = pd.pivot_table(data = inflowdatamonth1weekdayNonPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')
pivot27 = pd.pivot_table(data = inflowdatamonth1weekendPeak ,index= ['datenew','Time'],values=['Count'], aggfunc='sum')
pivot28 = pd.pivot_table(data = inflowdatamonth1weekendNonPeak  ,index=['datenew','Time'],values=['Count'], aggfunc='sum')


# In[39]:


pivot25.head()


# In[40]:


IRR25 = ((pivot25.quantile(0.75,axis =0) - pivot25.quantile(0.25,axis = 0)))
IRR26 =  (pivot26.quantile(0.75,axis =0 ) - pivot26.quantile(0.25,axis = 0))
IRR27 =  (pivot27.quantile(0.75,axis =0 ) - pivot27.quantile(0.25,axis = 0))
IRR28 =  (pivot28.quantile(0.75,axis =0 ) - pivot28.quantile(0.25,axis = 0))
Event1 = pivot25.loc[pivot25['Count']>max(int(IRR25*1.5), int(mean1))]
Event2 = pivot26.loc[pivot26['Count']>max(int(IRR26*1.5), int(mean1))]
Event3 = pivot27.loc[pivot27['Count']> max(int(IRR27*1.5),int(mean2))]
Event4 = pivot28.loc[pivot28['Count']>  max(int(IRR28*1.5), int(mean2))]


# In[41]:


pivot25.plot(title='InFlow on weekdays in peak hours in Jan', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()


# In[42]:



pivot26.plot(title='InFlow on weekdays in nonpeak hours in Jan', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()


# In[43]:


pivot27.head()


# In[44]:



pivot27.plot(title='InFlow on weekends in peak hours in Jan', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()


# In[45]:


pivot28.head()


# In[46]:



pivot28.plot(title='InFlow on weekends in non peak hours in Jan', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()


# In[47]:


# Let's subset the data into peak and non-peak hours for month 2
inflowdatamonth2weekdayPeak = inflowdatamonth2weekday.loc[inflowdatamonth2weekday['PeakFlag']== True]

inflowdatamonth2weekdayNonPeak = inflowdatamonth2weekday.loc[inflowdatamonth2weekday['PeakFlag']== False]


# In[48]:


pivot29 = pd.pivot_table(data = inflowdatamonth2weekdayPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')
pivot30 = pd.pivot_table(data = inflowdatamonth2weekdayNonPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')


# In[49]:


IRR29 = ((pivot29.quantile(0.75,axis =0) - pivot29.quantile(0.25,axis = 0)))
IRR30 =  (pivot30.quantile(0.75,axis =0 ) - pivot30.quantile(0.25,axis = 0))
Event5 = pivot29.loc[pivot29['Count']>max(int(IRR29*1.5),int(mean3))]
Event6 = pivot30.loc[pivot30['Count']>max(int(IRR30*1.5), int(mean3))]


# In[50]:



pivot29.plot(title='InFlow on weekdays in peak hours in Feb', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()


# In[51]:


pivot30.plot(title='InFlow on weekdays in non peak hours in Feb', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()


# In[52]:


# Let's subset the data into peak and non-peak hours for month 3
inflowdatamonth3weekdayPeak = inflowdatamonth3weekday.loc[inflowdatamonth3weekday['PeakFlag']== True]

inflowdatamonth3weekdayNonPeak = inflowdatamonth3weekday.loc[inflowdatamonth3weekday['PeakFlag']== False]

pivot31 = pd.pivot_table(data = inflowdatamonth3weekdayPeak, index=['datenew','Time'], values=['Count'], aggfunc='sum')
pivot32 = pd.pivot_table(data = inflowdatamonth3weekdayNonPeak, index = ['datenew', 'Time'],values=['Count'], aggfunc='sum')


# In[53]:


IRR31 = ((pivot31.quantile(0.75,axis =0) - pivot31.quantile(0.25,axis = 0)))
IRR32 =  (pivot32.quantile(0.75,axis =0 ) - pivot32.quantile(0.25,axis = 0))
Event7 = pivot31.loc[pivot31['Count']>max(int(IRR31*1.5),int(mean5))]
Event8 = pivot32.loc[pivot32['Count']>max(int(IRR32*1.5), int(mean5))]


# In[54]:


pivot31.plot(title='InFlow on weekdays in peak hours in March', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()


# In[55]:


pivot32.plot(title='InFlow on weekdays in non-peak hours in March', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()


# In[56]:




# Let's subset the data into peak and non-peak hours for month 4
inflowdatamonth4weekdayPeak = inflowdatamonth4weekday.loc[inflowdatamonth4weekday['PeakFlag']== True]

inflowdatamonth4weekdayNonPeak = inflowdatamonth4weekday.loc[inflowdatamonth4weekday['PeakFlag']== False]

inflowdatamonth4weekendPeak = inflowdatamonth4weekend.loc[inflowdatamonth4weekend['PeakFlag']== True]

inflowdatamonth4weekendNonPeak = inflowdatamonth4weekend.loc[inflowdatamonth4weekend['PeakFlag']== False]


pivot33 = pd.pivot_table(data = inflowdatamonth4weekdayPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')
pivot34 = pd.pivot_table(data =inflowdatamonth4weekdayNonPeak , index=['datenew','Time'] ,values=['Count'], aggfunc='sum')
pivot35 = pd.pivot_table(data = inflowdatamonth4weekendPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')
pivot36 = pd.pivot_table (data = inflowdatamonth4weekendNonPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')

IRR33 = ((pivot33.quantile(0.75,axis =0) - pivot33.quantile(0.25,axis = 0)))
IRR34 =  (pivot34.quantile(0.75,axis =0 ) - pivot34.quantile(0.25,axis = 0))
IRR35 = ((pivot35.quantile(0.75,axis =0) - pivot35.quantile(0.25,axis = 0)))
IRR36 =  (pivot36.quantile(0.75,axis =0 ) - pivot36.quantile(0.25,axis = 0))
Event9 = pivot33.loc[pivot33['Count']>max(int(IRR33*1.5),int(mean7))]
Event10 = pivot34.loc[pivot34['Count']>max(int(IRR34*1.5), int(mean7))]
Event11 = pivot35.loc[pivot35['Count']>max(int(IRR35*1.5),int(mean8))]
Event12 = pivot36.loc[pivot36['Count']>max(int(IRR36*1.5), int(mean8))]



# In[57]:


pivot33.plot(title='InFlow on weekdays in peak hours in April', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()
pivot34.plot(title='InFlow on weekdays in non- peak hours in April', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()
pivot35.plot(title='InFlow on weekends in peak hours in April', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()
pivot36.plot(title='InFlow on weekends in non- peak hours in April', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()


# In[58]:



# Let's subset the data into peak and non-peak hours for month 5
inflowdatamonth5weekdayPeak = inflowdatamonth5weekday.loc[inflowdatamonth5weekday['PeakFlag']== True]

inflowdatamonth5weekdayNonPeak = inflowdatamonth5weekday.loc[inflowdatamonth5weekday['PeakFlag']== False]

inflowdatamonth5weekendPeak = inflowdatamonth5weekend.loc[inflowdatamonth5weekend['PeakFlag']== True]

inflowdatamonth5weekendNonPeak = inflowdatamonth5weekend.loc[inflowdatamonth5weekend['PeakFlag']== False]

pivot37 = pd.pivot_table(data = inflowdatamonth5weekdayPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')
pivot38 = pd.pivot_table(data = inflowdatamonth5weekdayNonPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')
pivot39 = pd.pivot_table(data = inflowdatamonth5weekendPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')
pivot40 = pd.pivot_table(data = inflowdatamonth5weekendNonPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')


IRR37 = ((pivot37.quantile(0.75,axis =0) - pivot37.quantile(0.25,axis = 0)))
IRR38 =  (pivot38.quantile(0.75,axis =0 ) - pivot38.quantile(0.25,axis = 0))
IRR39 = ((pivot39.quantile(0.75,axis =0) - pivot39.quantile(0.25,axis = 0)))
IRR40 =  (pivot40.quantile(0.75,axis =0 ) - pivot40.quantile(0.25,axis = 0))

Event13 = pivot37.loc[pivot37['Count']>max(int(IRR37*1.5),int(mean9))]
Event14 = pivot38.loc[pivot38['Count']>max(int(IRR38*1.5), int(mean9))]
Event15 = pivot39.loc[pivot39['Count']>max(int(IRR39*1.5),int(mean10))]
Event16 = pivot40.loc[pivot40['Count']>max(int(IRR40*1.5), int(mean10))]


# In[59]:


pivot37.plot(title='InFlow on weekdays in peak hours in May', color = {'green'},figsize = (20,5) )
pyplot.tight_layout()
pyplot.show()
pivot38.plot(title='InFlow on weekdays in non peak hours in May', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()


# In[60]:


# Let's subset the data into peak and non-peak hours for month 6
inflowdatamonth6weekdayPeak = inflowdatamonth6weekday.loc[inflowdatamonth6weekday['PeakFlag']== True]

inflowdatamonth6weekdayNonPeak = inflowdatamonth6weekday.loc[inflowdatamonth6weekday['PeakFlag']== False]


# In[61]:



pivot41 = pd.pivot_table(data = inflowdatamonth6weekdayPeak ,index=['datenew', 'Time'], values=['Count'], aggfunc='sum')
pivot42 = pd.pivot_table(data = inflowdatamonth6weekdayNonPeak , index= ['datenew','Time'],values=['Count'], aggfunc='sum')
IRR41 = ((pivot41.quantile(0.75,axis =0) - pivot41.quantile(0.25,axis = 0)))
IRR42 =  (pivot42.quantile(0.75,axis =0 ) - pivot42.quantile(0.25,axis = 0))

Event17 = pivot41.loc[pivot41['Count']>max(int(IRR41*1.5),int(mean11))]
Event18 = pivot41.loc[pivot41['Count']>max(int(IRR42*1.5), int(mean11))]


# In[62]:


pivot41.plot(title='InFlow on weekdays in peak hours in June', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()
pivot42.plot(title='InFlow on weekdays in non peak hours in June', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()


# In[63]:




inflowdatamonth7weekdayPeak = inflowdatamonth7weekday.loc[inflowdatamonth7weekday['PeakFlag']== True]
pivot43 = pd.pivot_table(data = inflowdatamonth7weekdayPeak,index=['datenew','Time'], values=['Count'], aggfunc='sum')
IRR43 = ((pivot43.quantile(0.75,axis =0) - pivot43.quantile(0.25,axis = 0)))
Event19 = pivot43.loc[pivot43['Count']>max(int(IRR43*1.5),int(mean13))]




# In[64]:


pivot43.plot(title='InFlow on weekdays in peak hours in July', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()


# In[65]:


# Let's subset the data into peak and non-peak hours for month 7
inflowdatamonth7weekdayNonPeak = inflowdatamonth7weekday.loc[inflowdatamonth7weekday['PeakFlag']== False]

inflowdatamonth7weekendPeak = inflowdatamonth7weekend.loc[inflowdatamonth7weekend['PeakFlag']== True]

inflowdatamonth7weekendNonPeak = inflowdatamonth7weekend.loc[inflowdatamonth7weekend['PeakFlag']== False]

pivot44 = pd.pivot_table(data = inflowdatamonth7weekdayNonPeak,index=['datenew','Time'], values=['Count'], aggfunc='sum')
pivot45 = pd.pivot_table(data = inflowdatamonth7weekendPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')
pivot46 = pd.pivot_table(data = inflowdatamonth7weekendNonPeak,index=['datenew', 'Time'], values=['Count'], aggfunc='sum')

IRR44 = ((pivot44.quantile(0.75,axis =0) - pivot44.quantile(0.25,axis = 0)))
IRR45 = ((pivot45.quantile(0.75,axis =0) - pivot45.quantile(0.25,axis = 0)))

IRR46 = ((pivot46.quantile(0.75,axis =0) - pivot46.quantile(0.25,axis = 0)))
Event20 = pivot44.loc[pivot44['Count']>max(int(IRR44*1.5),int(mean13))]
Event21 = pivot45.loc[pivot45['Count']>max(int(IRR45*1.5),int(mean14))]
Event22 = pivot46.loc[pivot46['Count']>max(int(IRR46*1.5),int(mean14))]




# In[66]:


pivot44.plot(title='InFlow on weekdays in nonpeak hours in July', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivot45.plot(title='InFlow on weekends in peak hours in July', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivot46.plot(title='InFlow on weekends in non peak hours in July', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()


# In[67]:


inflowdatamonth8weekdayPeak = inflowdatamonth8weekday.loc[inflowdatamonth8weekday['PeakFlag']== True]
inflowdatamonth8weekdayNonPeak = inflowdatamonth8weekday.loc[inflowdatamonth8weekday['PeakFlag']== False]
inflowdatamonth8weekendPeak = inflowdatamonth8weekend.loc[inflowdatamonth8weekend['PeakFlag']== True]
inflowdatamonth8weekendNonPeak = inflowdatamonth8weekend.loc[inflowdatamonth8weekend['PeakFlag']== False]
pivot47 =pd.pivot_table(data = inflowdatamonth8weekdayPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')
pivot48 = pd.pivot_table( data = inflowdatamonth8weekdayNonPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')
pivot49 = pd.pivot_table(data = inflowdatamonth8weekendPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')
pivot50 = pd.pivot_table(data = inflowdatamonth8weekendNonPeak,index=['datenew','Time'], values=['Count'], aggfunc='sum')

IRR47 = ((pivot47.quantile(0.75,axis =0) - pivot47.quantile(0.25,axis = 0)))
IRR48 = ((pivot48.quantile(0.75,axis =0) - pivot48.quantile(0.25,axis = 0)))

IRR49 = ((pivot49.quantile(0.75,axis =0) - pivot49.quantile(0.25,axis = 0)))
IRR50 = ((pivot50.quantile(0.75,axis =0) - pivot50.quantile(0.25,axis = 0)))
Event23 = pivot47.loc[pivot47['Count']>max(int(IRR47*1.5),int(mean15))]
Event24 = pivot48.loc[pivot48['Count']>max(int(IRR48*1.5),int(mean15))]
Event25 = pivot49.loc[pivot49['Count']>max(int(IRR49*1.5),int(mean16))]
Event26 = pivot50.loc[pivot50['Count']>max(int(IRR50*1.5),int(mean16))]



# In[68]:


pivot47.plot(title='InFlow on weekdays in peak hours in August', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivot48.plot(title='InFlow on weekdays in non-peak hours in August', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivot49.plot(title='InFlow on weekends in peak hours in August ', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivot50.plot(title='InFlow on weekends in non-peak hours in August', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()


# In[69]:


inflowdatamonth9weekdayPeak = inflowdatamonth9weekday.loc[inflowdatamonth9weekday['PeakFlag']== True]
inflowdatamonth9weekdayNonPeak = inflowdatamonth9weekday.loc[inflowdatamonth9weekday['PeakFlag']== False]
inflowdatamonth9weekendPeak = inflowdatamonth9weekend.loc[inflowdatamonth9weekend['PeakFlag']== True]
inflowdatamonth9weekendNonPeak = inflowdatamonth9weekend.loc[inflowdatamonth9weekend['PeakFlag']== False]
pivot51 = pd.pivot_table(data = inflowdatamonth9weekdayPeak , index= ['datenew','Time'],values=['Count'], aggfunc='sum')
pivot52 = pd.pivot_table(data = inflowdatamonth9weekdayNonPeak ,index= ['datenew','Time'],values=['Count'], aggfunc='sum')
pivot53 = pd.pivot_table(data = inflowdatamonth9weekendPeak,index= ['datenew', 'Time'] ,values=['Count'], aggfunc='sum')
pivot54 = pd.pivot_table(data = inflowdatamonth9weekendNonPeak,index=['datenew','Time'],values=['Count'], aggfunc='sum')

IRR51 = ((pivot51.quantile(0.75,axis =0) - pivot51.quantile(0.25,axis = 0)))
IRR52 = ((pivot52.quantile(0.75,axis =0) - pivot52.quantile(0.25,axis = 0)))

IRR53 = ((pivot53.quantile(0.75,axis =0) - pivot53.quantile(0.25,axis = 0)))
IRR54 = ((pivot54.quantile(0.75,axis =0) - pivot54.quantile(0.25,axis = 0)))

Event27 = pivot51.loc[pivot51['Count']>max(int(IRR51*1.5),int(mean17))]
Event28 = pivot52.loc[pivot52['Count']>max(int(IRR52*1.5),int(mean17))]
Event29 = pivot53.loc[pivot53['Count']>max(int(IRR53*1.5),int(mean18))]
Event30 = pivot54.loc[pivot54['Count']>max(int(IRR54*1.5),int(mean18))]


# In[70]:


inflowdatamonth10weekdayPeak = inflowdatamonth10weekday.loc[inflowdatamonth10weekday['PeakFlag']== True]
inflowdatamonth10weekdayNonPeak = inflowdatamonth10weekday.loc[inflowdatamonth10weekday['PeakFlag']== False]
inflowdatamonth10weekendPeak = inflowdatamonth10weekend.loc[inflowdatamonth10weekend['PeakFlag']== True]
inflowdatamonth10weekendNonPeak = inflowdatamonth10weekend.loc[inflowdatamonth10weekend['PeakFlag']== False]
pivot55 = pd.pivot_table(inflowdatamonth10weekdayPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')
pivot56 = pd.pivot_table(inflowdatamonth10weekdayNonPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')
pivot57 = pd.pivot_table(inflowdatamonth10weekendPeak,index=['datenew','Time'], values=['Count'], aggfunc='sum')
pivot58 = pd.pivot_table(inflowdatamonth10weekendNonPeak,index= ['datenew','Time'] ,values=['Count'], aggfunc='sum')

IRR55 = ((pivot55.quantile(0.75,axis =0) - pivot55.quantile(0.25,axis = 0)))
IRR56 = ((pivot56.quantile(0.75,axis =0) - pivot56.quantile(0.25,axis = 0)))
IRR57 = ((pivot57.quantile(0.75,axis =0) - pivot57.quantile(0.25,axis = 0)))
IRR58 = ((pivot58.quantile(0.75,axis =0) - pivot58.quantile(0.25,axis = 0)))





# In[71]:


Event31 = pivot55.loc[pivot55['Count']>max(int(IRR55*1.5),int(mean19))]
Event32 = pivot56.loc[pivot56['Count']>max(int(IRR56*1.5),int(mean19))]
Event33 = pivot57.loc[pivot57['Count']>max(int(IRR57*1.5),int(mean20))]
Event34 = pivot58.loc[pivot58['Count']>max(int(IRR58*1.5),int(mean20))]


# In[72]:


inflowdatamonth11weekdayPeak = inflowdatamonth11weekday.loc[inflowdatamonth11weekday['PeakFlag']== True]
inflowdatamonth11weekdayNonPeak = inflowdatamonth11weekday.loc[inflowdatamonth11weekday['PeakFlag']== False]
#inflowdatamonth11weekendPeak = inflowdatamonth11weekend.loc[inflowdatamonth11weekend['PeakFlag']== True]
#inflowdatamonth11weekendNonPeak = inflowdatamonth11weekend.loc[inflowdatamonth11weekend['PeakFlag']== False]
pivot59 = pd.pivot_table(data =inflowdatamonth11weekdayPeak , index= ['datenew','Time'] ,values=['Count'], aggfunc='sum')
pivot60 = pd.pivot_table(data = inflowdatamonth11weekdayNonPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')
#pivot61 = inflowdatamonth11weekendPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
#pivot62 = inflowdatamonth11weekendNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
IRR59 = ((pivot59.quantile(0.75,axis =0) - pivot59.quantile(0.25,axis = 0)))
IRR60 = ((pivot60.quantile(0.75,axis =0) - pivot60.quantile(0.25,axis = 0)))

Event35 = pivot59.loc[pivot59['Count']>max(int(IRR59*1.5),int(mean21))]
Event36 = pivot60.loc[pivot60['Count']>max(int(IRR60*1.5),int(mean21))]



# In[73]:


pivot47.plot(title='InFlow on weekdays in peak hours in Aug', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivot48.plot(title='InFlow on weekdays in non peak hours in Aug', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivot49.plot(title='InFlow on weekends in peak hours in Aug', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivot50.plot(title='InFlow on weekends in non peak hours in Aug', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()


# In[74]:


pivot51.plot(title='InFlow on weekdays in peak hours in Sept', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivot52.plot(title='InFlow on weekdays in non peak hours in Sept', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivot53.plot(title='InFlow on weekends in peak hours in Sept', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivot54.plot(title='InFlow on weekends in non peak hours in Sept', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()


# In[75]:


pivot55.plot(title='InFlow on weekdays in peak hours in Oct', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivot56.plot(title='InFlow on weekdays in non peak hours in Oct', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivot57.plot(title='InFlow on weekends in peak hours in Oct', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivot58.plot(title='InFlow on weekends in non peak hours in Oct', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()


# In[76]:


pivot59.plot(title='InFlow on weekdays in peak hours in Nov', color = {'green'}, figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivot60.plot(title='InFlow on weekdays in non peak hours in Nov', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()


# In[77]:


inflowdatamonth12weekdayPeak = inflowdatamonth12weekday.loc[inflowdatamonth12weekday['PeakFlag']== True]
inflowdatamonth12weekdayNonPeak = inflowdatamonth12weekday.loc[inflowdatamonth12weekday['PeakFlag']== False]
#inflowdatamonth12weekendPeak = inflowdatamonth12weekend.loc[inflowdatamonth12weekend['PeakFlag']== True]
#inflowdatamonth12weekendNonPeak = inflowdatamonth12weekend.loc[inflowdatamonth12weekend['PeakFlag']== False]
pivot61 = pd.pivot_table(data = inflowdatamonth12weekdayPeak ,index= ['datenew','Time'] ,values=['Count'], aggfunc='sum')
pivot62 = pd.pivot_table(data = inflowdatamonth12weekdayNonPeak ,index=['datenew','Time'] ,values=['Count'], aggfunc='sum')
#pivot63 = pd.pivot_table(data = inflowdatamonth12weekendPeak.pivot_table, index=['datenew','Time'], values=['Count'], aggfunc='sum')
#pivot64 =  pd_pivot_table(data = inflowdatamonth12weekendNonPeak.pivot_table,index= ['datenew','Time'], values=['Count'], aggfunc='sum')


IRR61 = ((pivot61.quantile(0.75,axis =0) - pivot61.quantile(0.25,axis = 0)))
IRR62 = ((pivot62.quantile(0.75,axis =0) - pivot62.quantile(0.25,axis = 0)))

Event37 = pivot61.loc[pivot61['Count']>max(int(IRR61*1.5),int(mean23))]
Event38 = pivot62.loc[pivot62['Count']>max(int(IRR62*1.5),int(mean23))]


# In[78]:


pivot61.plot(title='InFlow on weekdays in peak hours in Dec', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivot62.plot(title='InFlow on weekdays in non peak hours in Dec', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()


# In[79]:


# On the basis of the Analysis done above on the inflow data the following dates could be identified as dates with events
Event = [Event1, Event2, Event3, Event4, Event5,Event6,Event7,Event8,Event9,Event10,Event11, Event12, Event13,Event14,Event15, Event16, Event17, Event18,Event19,Event20,Event21,Event22,Event23,Event24,Event25,Event26,Event27, Event28, Event29,Event30,Event31,Event32,Event33,Event34,Event35, Event36,Event37,Event38]
Event_df = pd.concat(Event)


# In[80]:


Event_df.count()


# In[81]:


Event_df.head(50)


# In[82]:


#Outflow Data
# Subsetting the Outflow Data for each month
outflowdatamonth1 = out_df.loc[out_df['month']== 1].reset_index()
outflowdatamonth2 = out_df.loc[out_df['month']== 2].reset_index()
outflowdatamonth3 = out_df.loc[out_df['month']== 3].reset_index()
outflowdatamonth4 = out_df.loc[out_df['month']== 4].reset_index()
outflowdatamonth5 = out_df.loc[out_df['month']== 5].reset_index()
outflowdatamonth6 = out_df.loc[out_df['month']== 6].reset_index()
outflowdatamonth7 = out_df.loc[out_df['month']== 7].reset_index()
outflowdatamonth8 = out_df.loc[out_df['month']== 8].reset_index()
outflowdatamonth9 = out_df.loc[out_df['month']== 9].reset_index()
outflowdatamonth10 = out_df.loc[out_df['month']== 10].reset_index()
outflowdatamonth11 = out_df.loc[out_df['month']== 11].reset_index()
outflowdatamonth12 = out_df.loc[out_df['month']== 12].reset_index()


# In[83]:


# Subsetting the Outflow Data into Weekday and Weekend 
outflowdatamonth1weekday = outflowdatamonth1.loc[outflowdatamonth1['weekdayFlag']== True].reset_index()
outflowdatamonth1weekend = outflowdatamonth1.loc[outflowdatamonth1['weekdayFlag']== False].reset_index()
outflowdatamonth2weekday = outflowdatamonth2.loc[outflowdatamonth2['weekdayFlag']== True].reset_index()
outflowdatamonth2weekend = outflowdatamonth2.loc[outflowdatamonth2['weekdayFlag']== False].reset_index()

outflowdatamonth3weekday = outflowdatamonth3.loc[outflowdatamonth3['weekdayFlag']== True].reset_index()
outflowdatamonth3weekend = outflowdatamonth3.loc[outflowdatamonth3['weekdayFlag']== False].reset_index()
outflowdatamonth4weekday = outflowdatamonth4.loc[outflowdatamonth4['weekdayFlag']== True].reset_index()
outflowdatamonth4weekend = outflowdatamonth4.loc[outflowdatamonth4['weekdayFlag']== False].reset_index()

outflowdatamonth5weekday = outflowdatamonth5.loc[outflowdatamonth5['weekdayFlag']== True].reset_index()
outflowdatamonth5weekend = outflowdatamonth5.loc[outflowdatamonth5['weekdayFlag']== False].reset_index()
outflowdatamonth6weekday = outflowdatamonth6.loc[outflowdatamonth6['weekdayFlag']== True].reset_index()
outflowdatamonth6weekend = outflowdatamonth6.loc[outflowdatamonth6['weekdayFlag']== False].reset_index()

outflowdatamonth7weekday = outflowdatamonth7.loc[outflowdatamonth7['weekdayFlag']== True].reset_index()
outflowdatamonth7weekend = outflowdatamonth7.loc[outflowdatamonth7['weekdayFlag']== False].reset_index()
outflowdatamonth8weekday = outflowdatamonth8.loc[outflowdatamonth8['weekdayFlag']== True].reset_index()
outflowdatamonth8weekend = outflowdatamonth8.loc[outflowdatamonth8['weekdayFlag']== False].reset_index()

outflowdatamonth9weekday = outflowdatamonth9.loc[outflowdatamonth9['weekdayFlag']== True].reset_index()
outflowdatamonth9weekend = outflowdatamonth9.loc[outflowdatamonth9['weekdayFlag']== False].reset_index()
outflowdatamonth10weekday = outflowdatamonth10.loc[outflowdatamonth10['weekdayFlag']== True].reset_index()
outflowdatamonth10weekend = outflowdatamonth10.loc[outflowdatamonth10['weekdayFlag']== False].reset_index()
outflowdatamonth11weekday = outflowdatamonth11.loc[outflowdatamonth11['weekdayFlag']== True].reset_index()
outflowdatamonth11weekend = outflowdatamonth11.loc[outflowdatamonth11['weekdayFlag']== False].reset_index()
outflowdatamonth12weekday = outflowdatamonth12.loc[outflowdatamonth12['weekdayFlag']== True].reset_index()
outflowdatamonth12weekend = outflowdatamonth12.loc[outflowdatamonth12['weekdayFlag']== False].reset_index()


# In[84]:


# Drawing the pivot table for outflow data for each month calculating the mean number of people entering the conference hall 

pivoto1 = outflowdatamonth1weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto2 = outflowdatamonth1weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto3 = outflowdatamonth2weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto4 = outflowdatamonth2weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto5 = outflowdatamonth3weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto6 = outflowdatamonth3weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto7 = outflowdatamonth4weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto8 = outflowdatamonth4weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto9 = outflowdatamonth5weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto10 = outflowdatamonth5weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto11 = outflowdatamonth6weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto12 = outflowdatamonth6weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto13 = outflowdatamonth7weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto14 = outflowdatamonth7weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto15 = outflowdatamonth8weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto16 = outflowdatamonth8weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto17 = outflowdatamonth9weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto18 = outflowdatamonth9weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto19 = outflowdatamonth10weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto20 = outflowdatamonth10weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto21 = outflowdatamonth11weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto22 = outflowdatamonth11weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto23 = outflowdatamonth12weekday.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})
pivoto24 = outflowdatamonth12weekend.pivot_table(index=['Time'], values=['Count'], aggfunc={'mean'})


# In[85]:


#Calculating mean and median
meano1 = pivoto1.mean()    
mediano1 = pivoto1.median()
meano2 = pivoto2.mean()
mediano2 = pivoto2.median()
meano3 = pivoto3.mean()
mediano3 = pivoto3.median()
meano4 = pivoto4.mean()
mediano4 = pivoto4.median()
meano5 = pivoto5.mean()
mediano5 = pivoto5.median()
meano6 = pivoto6.mean()
mediano6 = pivoto6.median()
meano7 = pivoto7.mean()
mediano7 = pivot7.median()
meano8 = pivoto8.mean()
mediano8 = pivoto8.median()
meano9 = pivoto9.mean()
mediano9 = pivoto9.median()
meano10 = pivoto10.mean()
mediano10 = pivoto10.median()
meano11 = pivoto11.mean()
mediano11 = pivoto11.median()
meano12 = pivoto12.mean()
mediano12 = pivoto12.median()
meano13 = pivoto13.mean()
mediano13 = pivoto13.median()
meano14 = pivoto14.mean()
mediano14 = pivoto14.median()
meano15 = pivoto15.mean()
mediano15 = pivoto15.median()
meano16 = pivoto16.mean()
mediano16 = pivoto16.median()
meano17 = pivoto17.mean()
mediano17 = pivoto17.median()
meano18 = pivoto18.mean()
mediano18 = pivoto18.median()
meano19 = pivoto19.mean()
mediano19 = pivoto19.median()
meano20 = pivoto20.mean()
mediano20 = pivoto20.median()
meano21 = pivoto21.mean()
mediano21 = pivoto21.median()
meano22 = pivoto22.mean()
mediano22 = pivoto22.median()
meano23 = pivoto23.mean()
mediano23 = pivoto23.median()
meano24 = pivoto24.mean()
mediano24 = pivoto24.median()


# In[86]:


# Calculating the peak and non-peak hours for each subset of data
PeakHourso1 = outflowdatamonth1weekday.loc[outflowdatamonth1weekday['Count']>int(meano1)]
PeakhoursTimingoutflow1 = PeakHourso1['Time']
PeakhoursTimingoutflow1.reset_index(drop = True, inplace= True)
PeakhoursTimingoutflow1
Lo1 = PeakhoursTimingoutflow1
outflowdatamonth1weekday['PeakFlag'] = np.where(outflowdatamonth1weekday['Time'].isin(Lo1), True , False)

PeakHourso2 = outflowdatamonth1weekend.loc[outflowdatamonth1weekend['Count']>int(meano2)]
PeakhoursTimingoutflow2 = PeakHourso2['Time']
PeakhoursTimingoutflow2.reset_index(drop = True, inplace= True)
PeakhoursTimingoutflow2
Lo2 = PeakhoursTimingoutflow2
outflowdatamonth1weekend['PeakFlag'] = np.where(outflowdatamonth1weekend['Time'].isin(Lo2), True , False)

PeakHourso3 = outflowdatamonth2weekday.loc[outflowdatamonth2weekday['Count']>int(meano3)]
PeakhoursTimingoutflow3 = PeakHourso3['Time']
PeakhoursTimingoutflow3.reset_index(drop = True, inplace= True)
PeakhoursTimingoutflow3
Lo3 = PeakhoursTimingoutflow3
outflowdatamonth2weekday['PeakFlag'] = np.where(outflowdatamonth2weekday['Time'].isin(Lo3), True , False)

#PeakHourso4 = outflowdatamonth2weekend.loc[outflowdatamonth2weekend['Count']>int(meano4)]
#PeakhoursTimingoutflow4 = PeakHourso4['Time']
#PeakhoursTimingoutflow4.reset_index(drop = True, inplace= True)
#PeakhoursTimingoutflow4
#Lo4 = PeakhoursTimingoutflow4
#outflowdatamonth2weekend['PeakFlag'] = np.where(outflowdatamonth2weekend['Time'].isin(Lo4), True , False)


PeakHourso5 = outflowdatamonth3weekday.loc[outflowdatamonth3weekday['Count']>int(meano5)]
PeakhoursTimingoutflow5 = PeakHourso5['Time']
PeakhoursTimingoutflow5.reset_index(drop = True, inplace= True)
PeakhoursTimingoutflow5
Lo5 = PeakhoursTimingoutflow5
outflowdatamonth3weekday['PeakFlag'] = np.where(outflowdatamonth3weekday['Time'].isin(Lo5), True , False)

#PeakHourso6 = outflowdatamonth3weekend.loc[outflowdatamonth3weekend['Count']>int(meano6)]
#PeakhoursTimingoutflow6 = PeakHourso6['Time']
#PeakhoursTimingoutflow6.reset_index(drop = True, inplace= True)
#PeakhoursTimingoutflow6
#Lo6 = PeakhoursTimingoutflow6
#outflowdatamonth3weekend['PeakFlag'] = np.where(outflowdatamonth3weekend['Time'].isin(Lo6), True , False)



PeakHourso7 = outflowdatamonth4weekday.loc[outflowdatamonth4weekday['Count']>int(meano7)]
PeakhoursTimingoutflow7 = PeakHourso7['Time']
PeakhoursTimingoutflow7.reset_index(drop = True, inplace= True)
PeakhoursTimingoutflow7
Lo7 = PeakhoursTimingoutflow7
outflowdatamonth4weekday['PeakFlag'] = np.where(outflowdatamonth4weekday['Time'].isin(Lo7), True , False)



PeakHourso8 = outflowdatamonth4weekend.loc[outflowdatamonth4weekend['Count']>int(meano8)]
PeakhoursTimingoutflow8 = PeakHourso8['Time']
PeakhoursTimingoutflow8.reset_index(drop = True, inplace= True)
PeakhoursTimingoutflow8
Lo8 = PeakhoursTimingoutflow8
outflowdatamonth4weekend['PeakFlag'] = np.where(outflowdatamonth4weekend['Time'].isin(Lo8), True , False)

PeakHourso9 = outflowdatamonth5weekday.loc[outflowdatamonth5weekday['Count']>int(meano9)]
PeakhoursTimingoutflow9 = PeakHourso9['Time']
PeakhoursTimingoutflow9.reset_index(drop = True, inplace= True)
PeakhoursTimingoutflow9
Lo9 = PeakhoursTimingoutflow9
outflowdatamonth5weekday['PeakFlag'] = np.where(outflowdatamonth5weekday['Time'].isin(Lo9), True , False)

PeakHourso10 = outflowdatamonth5weekend.loc[outflowdatamonth5weekend['Count']>int(meano10)]
PeakhoursTimingoutflow10 = PeakHourso10['Time']
PeakhoursTimingoutflow10.reset_index(drop = True, inplace= True)
PeakhoursTimingoutflow10
Lo10 = PeakhoursTimingoutflow10
outflowdatamonth5weekend['PeakFlag'] = np.where(outflowdatamonth5weekend['Time'].isin(Lo10), True , False)

PeakHourso11 = outflowdatamonth6weekday.loc[outflowdatamonth6weekday['Count']>int(meano11)]
PeakhoursTimingoutflow11 = PeakHourso11['Time']
PeakhoursTimingoutflow11.reset_index(drop = True, inplace= True)
PeakhoursTimingoutflow11
Lo11 = PeakhoursTimingoutflow11
outflowdatamonth6weekday['PeakFlag'] = np.where(outflowdatamonth6weekday['Time'].isin(Lo11), True , False)

#PeakHourso12 = outflowdatamonth6weekend.loc[outflowdatamonth6weekend['Count']>int(meano12)]
#PeakhoursTimingoutflow12 = PeakHourso12['Time']
#PeakhoursTimingoutflow12.reset_index(drop = True, inplace= True)
#PeakhoursTimingoutflow12
#Lo12 = PeakhoursTimingoutflow12
#outflowdatamonth6weekend['PeakFlag'] = np.where(outflowdatamonth6weekend['Time'].isin(Lo12), True , False)

PeakHourso13 = outflowdatamonth7weekday.loc[outflowdatamonth7weekday['Count']>int(meano13)]
PeakhoursTimingoutflow13 = PeakHourso13['Time']
PeakhoursTimingoutflow13.reset_index(drop = True, inplace= True)
PeakhoursTimingoutflow13
Lo13 = PeakhoursTimingoutflow13
outflowdatamonth7weekday['PeakFlag'] = np.where(outflowdatamonth7weekday['Time'].isin(Lo13), True , False)


PeakHourso14 = outflowdatamonth7weekend.loc[outflowdatamonth7weekend['Count']>int(meano14)]
PeakhoursTimingoutflow14 = PeakHourso14['Time']
PeakhoursTimingoutflow14.reset_index(drop = True, inplace= True)
PeakhoursTimingoutflow14
Lo14 = PeakhoursTimingoutflow14
outflowdatamonth7weekend['PeakFlag'] = np.where(outflowdatamonth7weekend['Time'].isin(Lo14), True , False)


PeakHourso15 = outflowdatamonth8weekday.loc[outflowdatamonth8weekday['Count']>int(meano15)]
PeakhoursTimingoutflow15 = PeakHourso15['Time']
PeakhoursTimingoutflow15.reset_index(drop = True, inplace= True)
PeakhoursTimingoutflow15
Lo15 = PeakhoursTimingoutflow15
outflowdatamonth8weekday['PeakFlag'] = np.where(outflowdatamonth8weekday['Time'].isin(Lo15), True , False)


#PeakHourso16 = outflowdatamonth8weekend.loc[outflowdatamonth8weekend['Count']>int(meano16)]
#PeakhoursTimingoutflowo16 = PeakHourso16['Time']
#PeakhoursTimingoutflow16.reset_index(drop = True, inplace= True)
#PeakhoursTimingoutflow16
#Lo16 = PeakhoursTimingoutflow16
#outflowdatamonth8weekend['PeakFlag'] = np.where(outflowdatamonth8weekend['Time'].isin(Lo16), True , False)



PeakHourso17 = outflowdatamonth9weekday.loc[outflowdatamonth9weekday['Count']>int(meano17)]
PeakhoursTimingoutflow17 = PeakHourso17['Time']
PeakhoursTimingoutflow17.reset_index(drop = True, inplace= True)
PeakhoursTimingoutflow17
Lo17 = PeakhoursTimingoutflow17
outflowdatamonth9weekday['PeakFlag'] = np.where(outflowdatamonth9weekday['Time'].isin(Lo17), True , False)


PeakHourso18 = outflowdatamonth9weekend.loc[outflowdatamonth9weekend['Count']>int(meano18)]
PeakhoursTimingoutflow18 = PeakHourso18['Time']
PeakhoursTimingoutflow18.reset_index(drop = True, inplace= True)
PeakhoursTimingoutflow18
Lo18 = PeakhoursTimingoutflow18
outflowdatamonth9weekend['PeakFlag'] = np.where(outflowdatamonth9weekend['Time'].isin(Lo18), True , False)


PeakHourso19 = outflowdatamonth10weekday.loc[outflowdatamonth10weekday['Count']>int(meano19)]
PeakhoursTimingoutflow19 = PeakHourso19['Time']
PeakhoursTimingoutflow19.reset_index(drop = True, inplace= True)
PeakhoursTimingoutflow19
Lo19 = PeakhoursTimingoutflow19
outflowdatamonth10weekday['PeakFlag'] = np.where(outflowdatamonth10weekday['Time'].isin(Lo19), True , False)

PeakHourso20 = outflowdatamonth10weekend.loc[outflowdatamonth10weekend['Count']>int(meano20)]
PeakhoursTimingoutflow20 = PeakHourso20['Time']
PeakhoursTimingoutflow20.reset_index(drop = True, inplace= True)
PeakhoursTimingoutflow20
Lo20 = PeakhoursTimingoutflow20
outflowdatamonth10weekend['PeakFlag'] = np.where(outflowdatamonth10weekend['Time'].isin(Lo20), True , False)

PeakHourso21 = outflowdatamonth11weekday.loc[outflowdatamonth11weekday['Count']>int(meano21)]
PeakhoursTimingoutflow21 = PeakHourso21['Time']
PeakhoursTimingoutflow21.reset_index(drop = True, inplace= True)
PeakhoursTimingoutflow21
Lo21 = PeakhoursTimingoutflow21
outflowdatamonth11weekday['PeakFlag'] = np.where(outflowdatamonth11weekday['Time'].isin(Lo21), True , False)

#PeakHourso22 = outflowdatamonth11weekend.loc[outflowdatamonth11weekend['Count']>int(meano22)]
#PeakhoursTimingoutflow22 = PeakHourso22['Time']
#PeakhoursTimingoutflow22.reset_index(drop = True, inplace= True)
#PeakhoursTimingoutflow22
#Lo22 = PeakhoursTimingoutflowo22
#outflowdatamonth11weekend['PeakFlag'] = np.where(outflowdatamonth11weekend['Time'].isin(Lo22), True , False)

PeakHourso23 = outflowdatamonth12weekday.loc[outflowdatamonth12weekday['Count']>int(meano23)]
PeakhoursTimingoutflow23 = PeakHourso23['Time']
PeakhoursTimingoutflow23.reset_index(drop = True, inplace= True)
PeakhoursTimingoutflow23
Lo23 = PeakhoursTimingoutflow23
outflowdatamonth12weekday['PeakFlag'] = np.where(outflowdatamonth12weekday['Time'].isin(Lo23), True , False)


#PeakHourso24 = outflowdatamonth12weekend.loc[outflowdatamonth12weekend['Count']>int(meano24)]
#PeakhoursTimingoutflow24 = PeakHourso24['Time']
#PeakhoursTimingoutflow24.reset_index(drop = True, inplace= True)
#PeakhoursTimingoutflow24
#Lo24 = PeakhoursTimingoutflow24
#outflowdatamonth12weekend['PeakFlag'] = np.where(outflowdatamonth12weekend['Time'].isin(Lo24), True , False)


# In[87]:


# Let's subset the data into peak and non-peak hours for month 1 
outflowdatamonth1weekdayPeak = outflowdatamonth1weekday.loc[outflowdatamonth1weekday['PeakFlag']== True]

outflowdatamonth1weekdayNonPeak = outflowdatamonth1weekday.loc[outflowdatamonth1weekday['PeakFlag']== False]

outflowdatamonth1weekendPeak = outflowdatamonth1weekend.loc[outflowdatamonth1weekend['PeakFlag']== True]

outflowdatamonth1weekendNonPeak = outflowdatamonth1weekend.loc[outflowdatamonth1weekend['PeakFlag']== False]

# Let's subset the data into peak and non-peak hours for month 2
outflowdatamonth2weekdayPeak = outflowdatamonth2weekday.loc[outflowdatamonth2weekday['PeakFlag']== True]

outflowdatamonth2weekdayNonPeak = outflowdatamonth2weekday.loc[outflowdatamonth2weekday['PeakFlag']== False]

#Let's subset the data into peak and non-peak hours for month 3
outflowdatamonth3weekdayPeak = outflowdatamonth3weekday.loc[outflowdatamonth3weekday['PeakFlag']== True]

outflowdatamonth3weekdayNonPeak = outflowdatamonth3weekday.loc[outflowdatamonth3weekday['PeakFlag']== False]


# Let's subset the data into peak and non-peak hours for month 4
outflowdatamonth4weekdayPeak = outflowdatamonth4weekday.loc[outflowdatamonth4weekday['PeakFlag']== True]

outflowdatamonth4weekdayNonPeak = outflowdatamonth4weekday.loc[outflowdatamonth4weekday['PeakFlag']== False]

outflowdatamonth4weekendPeak = outflowdatamonth4weekend.loc[outflowdatamonth4weekend['PeakFlag']== True]

outflowdatamonth4weekendNonPeak = outflowdatamonth4weekend.loc[outflowdatamonth4weekend['PeakFlag']== False]

# Let's subset the data into peak and non-peak hours for month 5
outflowdatamonth5weekdayPeak = outflowdatamonth5weekday.loc[outflowdatamonth5weekday['PeakFlag']== True]

outflowdatamonth5weekdayNonPeak = outflowdatamonth5weekday.loc[outflowdatamonth5weekday['PeakFlag']== False]

outflowdatamonth5weekendPeak = outflowdatamonth5weekend.loc[outflowdatamonth5weekend['PeakFlag']== True]

outflowdatamonth5weekendNonPeak = outflowdatamonth5weekend.loc[outflowdatamonth5weekend['PeakFlag']== False]

# Let's subset the data into peak and non-peak hours for month 6
outflowdatamonth6weekdayPeak = outflowdatamonth6weekday.loc[outflowdatamonth6weekday['PeakFlag']== True]

outflowdatamonth6weekdayNonPeak = outflowdatamonth6weekday.loc[outflowdatamonth6weekday['PeakFlag']== False]

# Let's subset the data into peak and non-peak hours for month 7
outflowdatamonth7weekdayPeak = outflowdatamonth7weekday.loc[outflowdatamonth7weekday['PeakFlag']== True]

outflowdatamonth7weekdayNonPeak = outflowdatamonth7weekday.loc[outflowdatamonth7weekday['PeakFlag']== False]

outflowdatamonth7weekendPeak = outflowdatamonth7weekend.loc[outflowdatamonth7weekend['PeakFlag']== True]

outflowdatamonth7weekendNonPeak = outflowdatamonth7weekend.loc[outflowdatamonth7weekend['PeakFlag']== False]

# Let's subset the data into peak and non-peak hours for month 8
outflowdatamonth8weekdayPeak = outflowdatamonth8weekday.loc[outflowdatamonth8weekday['PeakFlag']== True]
outflowdatamonth8weekdayNonPeak = outflowdatamonth8weekday.loc[outflowdatamonth8weekday['PeakFlag']== False]


# Let's subset the data into peak and non-peak hours for month 9
outflowdatamonth9weekdayPeak = outflowdatamonth9weekday.loc[outflowdatamonth9weekday['PeakFlag']== True]
outflowdatamonth9weekdayNonPeak = outflowdatamonth9weekday.loc[outflowdatamonth9weekday['PeakFlag']== False]

outflowdatamonth9weekendPeak = outflowdatamonth9weekend.loc[outflowdatamonth9weekend['PeakFlag']== True]
outflowdatamonth9weekendNonPeak = outflowdatamonth9weekend.loc[outflowdatamonth9weekend['PeakFlag']== False]

# Let's subset the data into peak and non-peak hours for month 10
outflowdatamonth10weekdayPeak = outflowdatamonth10weekday.loc[outflowdatamonth10weekday['PeakFlag']== True]
outflowdatamonth10weekdayNonPeak = outflowdatamonth10weekday.loc[outflowdatamonth10weekday['PeakFlag']== False]

outflowdatamonth10weekendPeak = outflowdatamonth10weekend.loc[outflowdatamonth10weekend['PeakFlag']== True]
outflowdatamonth10weekendNonPeak = outflowdatamonth10weekend.loc[outflowdatamonth10weekend['PeakFlag']== False]


# Let's subset the data into peak and non-peak hours for month 11
outflowdatamonth11weekdayPeak = outflowdatamonth11weekday.loc[outflowdatamonth11weekday['PeakFlag']== True]
outflowdatamonth11weekdayNonPeak = outflowdatamonth11weekday.loc[outflowdatamonth11weekday['PeakFlag']== False]

# Let's subset the data into peak and non-peak hours for month 12
outflowdatamonth12weekdayPeak = outflowdatamonth12weekday.loc[outflowdatamonth12weekday['PeakFlag']== True]
outflowdatamonth12weekdayNonPeak = outflowdatamonth12weekday.loc[outflowdatamonth12weekday['PeakFlag']== False]


# In[88]:


# Pivot Table for month 1 
pivoto25 = pd.pivot_table(data = outflowdatamonth1weekdayPeak , index= ['datenew','Time'] ,values=['Count'], aggfunc='sum')
pivoto26 = pd.pivot_table(data = outflowdatamonth1weekdayNonPeak ,index=['datenew', 'Time'], values=['Count'], aggfunc='sum')
pivoto27 = pd.pivot_table(data = outflowdatamonth1weekendPeak ,index= ['datenew', 'Time'],values=['Count'], aggfunc='sum')
pivoto28 = pd.pivot_table(data = outflowdatamonth1weekendNonPeak, index= ['datenew', 'Time'] ,values=['Count'], aggfunc='sum')



# Pivot Table for month 2 
pivoto29 = pd.pivot_table(data = outflowdatamonth2weekdayPeak ,index= ['datenew', 'Time'] ,values=['Count'], aggfunc='sum')
pivoto30 = pd.pivot_table(data = outflowdatamonth2weekdayNonPeak ,index= ['datenew', 'Time'], values=['Count'], aggfunc='sum')



# Pivot Table for month 3 
pivoto31 = pd.pivot_table( data = outflowdatamonth3weekdayPeak ,index= ['datenew',  'Time'] ,values=['Count'], aggfunc='sum')
pivoto32 = pd .pivot_table(data = outflowdatamonth3weekdayNonPeak, index= ['datenew','Time'], values=['Count'], aggfunc='sum')



# Pivot Table for month 4 
pivoto33 = pd.pivot_table( data = outflowdatamonth4weekdayPeak ,index= ['datenew','Time'], values=['Count'], aggfunc='sum')
pivoto34 = pd.pivot_table(  data = outflowdatamonth4weekdayNonPeak ,index= ['datenew', 'Time'] ,values=['Count'], aggfunc='sum')
pivoto35 = pd.pivot_table(data = outflowdatamonth4weekendPeak ,index= ['datenew','Time'], values=['Count'], aggfunc='sum')
pivoto36 = pd.pivot_table( data = outflowdatamonth4weekendNonPeak ,index= ['datenew','Time'] ,values=['Count'], aggfunc='sum')



# Pivot Table for month 5 
pivoto37 = pd.pivot_table(data = outflowdatamonth5weekdayPeak ,index=['datenew','Time'] ,values=['Count'], aggfunc='sum')
pivoto38 = pd.pivot_table( data = outflowdatamonth5weekdayNonPeak ,index= ['datenew','Time'] ,values=['Count'], aggfunc='sum')
pivoto39 = pd.pivot_table(data = outflowdatamonth5weekendPeak ,index=['datenew', 'Time'],values=['Count'], aggfunc='sum')
pivoto40 = pd.pivot_table(data = outflowdatamonth5weekendNonPeak , index=['datenew', 'Time'],values=['Count'], aggfunc='sum')



# Pivot Table for month 6
pivoto41 = pd.pivot_table(data = outflowdatamonth6weekdayPeak ,index=['datenew','Time'] ,values=['Count'], aggfunc='sum')
pivoto42 = pd.pivot_table(data = outflowdatamonth6weekdayNonPeak, index= ['datenew', 'Time'] ,values=['Count'], aggfunc='sum')



# Pivot Table for month 7

pivoto43 = pd.pivot_table(data = outflowdatamonth7weekdayPeak ,index= ['datenew','Time'] ,values=['Count'], aggfunc='sum')
pivoto44 = pd.pivot_table(data = outflowdatamonth7weekdayNonPeak, index=['datenew','Time'],values=['Count'], aggfunc='sum')
pivoto45 = pd.pivot_table(data = outflowdatamonth7weekendPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')
pivoto46 = pd.pivot_table(data = outflowdatamonth7weekendNonPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')




# Pivot Table for month 8

pivoto47 = pd.pivot_table(data = outflowdatamonth8weekdayPeak ,index=['datenew','Time'] ,values=['Count'], aggfunc='sum')
pivoto48 = pd.pivot_table(data = outflowdatamonth8weekdayNonPeak , index=['datenew','Time'] , values=['Count'], aggfunc='sum')


# Pivot Table for month 9

pivoto49 = pd.pivot_table(data = outflowdatamonth9weekdayPeak ,index= ['datenew','Time'], values=['Count'], aggfunc='sum')
pivoto50 = pd.pivot_table(data = outflowdatamonth9weekdayNonPeak ,index=['datenew' ,'Time'], values=['Count'], aggfunc='sum')
pivoto51 = pd.pivot_table(data = outflowdatamonth9weekendPeak ,index= ['datenew','Time'], values=['Count'], aggfunc='sum')
pivoto52 = pd.pivot_table(data = outflowdatamonth9weekendNonPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')


# Pivot Table for month 10

pivoto53 = pd.pivot_table(data = outflowdatamonth10weekdayPeak ,index= ['datenew','Time'] ,values=['Count'], aggfunc='sum')
pivoto54 = pd.pivot_table(data = outflowdatamonth10weekdayNonPeak ,index= ['datenew','Time'], values=['Count'], aggfunc='sum')

pivoto55 = pd.pivot_table(data = outflowdatamonth10weekendPeak ,index= ['datenew','Time'], values=['Count'], aggfunc='sum')
pivoto56 = pd.pivot_table( data =outflowdatamonth10weekendNonPeak  ,index= ['datenew','Time'], values=['Count'], aggfunc='sum')



# Let's subset the data into peak and non-peak hours for month 11
pivoto57 = pd.pivot_table(data = outflowdatamonth11weekdayPeak ,index= ['datenew','Time'] ,values=['Count'], aggfunc='sum')
pivoto58 = pd.pivot_table(data = outflowdatamonth11weekdayNonPeak ,index=['datenew','Time'] , values=['Count'], aggfunc='sum')


# Let's subset the data into peak and non-peak hours for month 12
pivoto59 = pd.pivot_table(data = outflowdatamonth12weekdayPeak , index=['datenew','Time'], values=['Count'], aggfunc='sum')
pivoto60 = pd.pivot_table(data = outflowdatamonth12weekdayNonPeak ,index=['datenew','Time'], values=['Count'], aggfunc='sum')


# In[89]:


IRRo25 = ((pivoto25.quantile(0.75,axis =0) - pivoto25.quantile(0.25,axis = 0)))
IRRo26 = ((pivoto26.quantile(0.75,axis =0) - pivoto26.quantile(0.25,axis = 0)))
IRRo27 = ((pivoto27.quantile(0.75,axis =0) - pivoto27.quantile(0.25,axis = 0)))
IRRo28 = ((pivoto28.quantile(0.75,axis =0) - pivoto28.quantile(0.25,axis = 0)))
IRRo29 = ((pivoto29.quantile(0.75,axis =0) - pivoto29.quantile(0.25,axis = 0)))
IRRo30 = ((pivoto30.quantile(0.75,axis =0) - pivoto30.quantile(0.25,axis = 0)))
IRRo31 = ((pivoto31.quantile(0.75,axis =0) - pivoto31.quantile(0.25,axis = 0)))
IRRo32 = ((pivoto32.quantile(0.75,axis =0) - pivoto32.quantile(0.25,axis = 0)))
IRRo33 = ((pivoto33.quantile(0.75,axis =0) - pivoto33.quantile(0.25,axis = 0)))
IRRo34 = ((pivoto34.quantile(0.75,axis =0) - pivoto34.quantile(0.25,axis = 0)))
IRRo35 = ((pivoto35.quantile(0.75,axis =0) - pivoto35.quantile(0.25,axis = 0)))
IRRo36 = ((pivoto36.quantile(0.75,axis =0) - pivoto36.quantile(0.25,axis = 0)))
IRRo37 = ((pivoto37.quantile(0.75,axis =0) - pivoto37.quantile(0.25,axis = 0)))
IRRo38 = ((pivoto38.quantile(0.75,axis =0) - pivoto38.quantile(0.25,axis = 0)))
IRRo39 = ((pivoto39.quantile(0.75,axis =0) - pivoto39.quantile(0.25,axis = 0)))
IRRo40 = ((pivoto40.quantile(0.75,axis =0) - pivoto40.quantile(0.25,axis = 0)))
IRRo41 = ((pivoto41.quantile(0.75,axis =0) - pivoto41.quantile(0.25,axis = 0)))
IRRo42 = ((pivoto42.quantile(0.75,axis =0) - pivoto42.quantile(0.25,axis = 0)))
IRRo43 = ((pivoto43.quantile(0.75,axis =0) - pivoto43.quantile(0.25,axis = 0)))
IRRo44 = ((pivoto44.quantile(0.75,axis =0) - pivoto44.quantile(0.25,axis = 0)))
IRRo45 = ((pivoto45.quantile(0.75,axis =0) - pivoto45.quantile(0.25,axis = 0)))
IRRo46 = ((pivoto46.quantile(0.75,axis =0) - pivoto46.quantile(0.25,axis = 0)))
IRRo47 = ((pivoto47.quantile(0.75,axis =0) - pivoto47.quantile(0.25,axis = 0)))
IRRo48 = ((pivoto48.quantile(0.75,axis =0) - pivoto48.quantile(0.25,axis = 0)))
IRRo49 = ((pivoto49.quantile(0.75,axis =0) - pivoto49.quantile(0.25,axis = 0)))
IRRo50 = ((pivoto50.quantile(0.75,axis =0) - pivoto50.quantile(0.25,axis = 0)))
IRRo51 = ((pivoto51.quantile(0.75,axis =0) - pivoto51.quantile(0.25,axis = 0)))
IRRo52 = ((pivoto52.quantile(0.75,axis =0) - pivoto52.quantile(0.25,axis = 0)))
IRRo53 = ((pivoto53.quantile(0.75,axis =0) - pivoto53.quantile(0.25,axis = 0)))
IRRo54 = ((pivoto54.quantile(0.75,axis =0) - pivoto54.quantile(0.25,axis = 0)))
IRRo55 = ((pivoto55.quantile(0.75,axis =0) - pivoto55.quantile(0.25,axis = 0)))
IRRo56 = ((pivoto56.quantile(0.75,axis =0) - pivoto56.quantile(0.25,axis = 0)))
IRRo57 = ((pivoto57.quantile(0.75,axis =0) - pivoto57.quantile(0.25,axis = 0)))
IRRo58 = ((pivoto58.quantile(0.75,axis =0) - pivoto58.quantile(0.25,axis = 0)))
IRRo59 = ((pivoto59.quantile(0.75,axis =0) - pivoto59.quantile(0.25,axis = 0)))
IRRo60 = ((pivoto60.quantile(0.75,axis =0) - pivoto60.quantile(0.25,axis = 0)))


# In[90]:


Evento1 = pivoto25.loc[pivoto25['Count']>max(int(IRRo25*1.5),int(meano1))]
Evento2 = pivoto26.loc[pivoto26['Count']>max(int(IRRo26*1.5),int(meano1))]
Evento3 = pivoto27.loc[pivoto27['Count']>max(int(IRRo27*1.5),int(meano2))]
Evento4 = pivoto28.loc[pivoto28['Count']>max(int(IRRo28*1.5),int(meano2))]
Evento5 = pivoto29.loc[pivoto29['Count']>max(int(IRRo29*1.5),int(meano3))]
Evento6 = pivoto30.loc[pivoto30['Count']>max(int(IRRo30*1.5),int(meano3))]
Evento7 = pivoto31.loc[pivoto31['Count']>max(int(IRRo31*1.5),int(meano5))]
Evento8 = pivoto32.loc[pivoto32['Count']>max(int(IRRo32*1.5),int(meano5))]
Evento9 = pivoto33.loc[pivoto33['Count']>max(int(IRRo33*1.5),int(meano7))]
Evento10 = pivoto34.loc[pivoto34['Count']>max(int(IRRo34*1.5),int(meano7))]
Evento11 = pivoto35.loc[pivoto35['Count']>max(int(IRRo35*1.5),int(meano8))]
Evento12 = pivoto36.loc[pivoto36['Count']>max(int(IRRo36*1.5),int(meano8))]
Evento13 = pivoto37.loc[pivoto37['Count']>max(int(IRRo37*1.5),int(meano9))]
Evento14 = pivoto38.loc[pivoto38['Count']>max(int(IRRo38*1.5),int(meano9))]
Evento15 = pivoto39.loc[pivoto39['Count']>max(int(IRRo39*1.5),int(meano10))]
Evento16 = pivoto40.loc[pivoto40['Count']>max(int(IRRo40*1.5),int(meano10))]
Evento17 = pivoto41.loc[pivoto41['Count']>max(int(IRRo41*1.5),int(meano11))]
Evento18 = pivoto42.loc[pivoto42['Count']>max(int(IRRo42*1.5),int(meano11))]
Evento19 = pivoto43.loc[pivoto43['Count']>max(int(IRRo43*1.5),int(meano13))]
Evento20 = pivoto44.loc[pivoto44['Count']>max(int(IRRo44*1.5),int(meano13))]
Evento21 = pivoto45.loc[pivoto45['Count']>max(int(IRRo45*1.5),int(meano14))]
Evento22 = pivoto46.loc[pivoto46['Count']>max(int(IRRo46*1.5),int(meano14))]
Evento23 = pivoto47.loc[pivoto47['Count']>max(int(IRRo47*1.5),int(meano15))]
Evento24 = pivoto48.loc[pivoto48['Count']>max(int(IRRo48*1.5),int(meano15))]
Evento25 = pivoto49.loc[pivoto49['Count']>max(int(IRRo49*1.5),int(meano17))]
Evento26 = pivoto50.loc[pivoto50['Count']>max(int(IRRo25*1.5),int(meano17))]
Evento27 = pivoto51.loc[pivoto51['Count']>max(int(IRRo25*1.5),int(meano18))]
Evento28 = pivoto52.loc[pivoto52['Count']>max(int(IRRo25*1.5),int(meano18))]
Evento29 = pivoto53.loc[pivoto53['Count']>max(int(IRRo25*1.5),int(meano19))]
Evento30 = pivoto54.loc[pivoto54['Count']>max(int(IRRo25*1.5),int(meano19))]
Evento31 = pivoto55.loc[pivoto55['Count']>max(int(IRRo25*1.5),int(meano20))]
Evento32 = pivoto56.loc[pivoto56['Count']>max(int(IRRo25*1.5),int(meano20))]
Evento33 = pivoto57.loc[pivoto57['Count']>max(int(IRRo25*1.5),int(meano21))]
Evento34 = pivoto58.loc[pivoto58['Count']>max(int(IRRo25*1.5),int(meano21))]
Evento35 = pivoto59.loc[pivoto59['Count']>max(int(IRRo25*1.5),int(meano23))]
Evento36 = pivoto60.loc[pivoto60['Count']>max(int(IRRo25*1.5),int(meano23))]


# In[91]:


# Let's Plot the Graph to visualize the results
pivoto25.plot(title='OutFlow on weekdays in peak hours in Jan', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto26.plot(title='OutFlow on weekdays in non peak hours in Jan', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto27.plot(title='OutFlow on weekends in peak hours in Jan', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivot28.plot(title='OutFlow on weekends in non peak hours in Jan', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto29.plot(title='OutFlow on weekdays in peak hours in Feb', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto30.plot(title='OutFlow on weekdays in non peak hours in Feb', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto31.plot(title='OutFlow on weekdays in peak hours in March', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto32.plot(title='OutFlow on weekdays in non peak hours in March', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto33.plot(title='OutFlow on weekdays in peak hours in April', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto34.plot(title='OutFlow on weekdays in non peak hours in April', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto35.plot(title='OutFlow on weekends in peak hours in April', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto36.plot(title='OutFlow on weekends in non peak hours in April', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto37.plot(title='OutFlow on weekdays in peak hours in May', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto38.plot(title='OutFlow on weekdays in non peak hours in May', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto39.plot(title='OutFlow on weekends in peak hours in May', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto40.plot(title='OutFlow on weekends in non peak hours in May', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto41.plot(title='OutFlow on weekdays in peak hours in June', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto42.plot(title='OutFlow on weekdays in non peak hours in June', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto43.plot(title='OutFlow on weekdays in peak hours in July', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto44.plot(title='OutFlow on weekdays in non peak hours in July', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto45.plot(title='OutFlow on weekends in peak hours in July', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto46.plot(title='OutFlow on weekends in non peak hours in July', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto47.plot(title='OutFlow on weekdays in peak hours in August', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto48.plot(title='OutFlow on weekdays in non peak hours in August', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto49.plot(title='OutFlow on weekdays in peak hours in Sept', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto50.plot(title='OutFlow on weekdays in non peak hours in Sept', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto51.plot(title='OutFlow on weekends in peak hours in Sept', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto52.plot(title='OutFlow on weekends in non peak hours in Sept', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto53.plot(title='OutFlow on weekdays in peak hours in Oct', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto54.plot(title='OutFlow on weekdays in non peak hours in Oct', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto55.plot(title='OutFlow on weekends in peak hours in Oct', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto56.plot(title='OutFlow on weekends in non peak hours in Oct', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto57.plot(title='OutFlow on weekdays in peak hours in Nov', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto58.plot(title='OutFlow on weekdays in non peak hours in Nov', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto59.plot(title='OutFlow on weekends in peak hours in Dec', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()

pivoto60.plot(title='OutFlow on weekends in non peak hours in Dec', color = {'green'},figsize = (20,5))
pyplot.tight_layout()
pyplot.show()


# In[92]:


# On the basis of the Analysis done above on the outflow data the following dates could be identified as dates with events
Eventoutflow = [Evento1, Evento2, Evento3, Evento4, Evento5,Evento6,Evento7,Evento8,Evento9,Evento10,Evento11, Evento12, Evento13,Evento14,Evento14, Evento15, Evento16, Evento17,Evento18,Evento19,Evento20,Evento21,Evento22,Evento23,Evento24,Evento25, Evento26, Evento27,Evento28,Evento29,Evento30,Evento31,Evento32,Evento33,Evento34,Evento35,Evento36]
Eventoutflow_df = pd.concat(Eventoutflow)


# In[93]:


Eventoutflow_df.head()


# In[94]:


Eventoutflow_df.describe()


# In[95]:


Eventoutflow_df.count()


# In[96]:



Eventoutflow_df.reset_index(inplace=True)


# In[97]:


Eventoutflow_df.head()


# In[98]:


EventDatesoutflow = Eventoutflow_df['datenew']


# In[99]:


Eventtimeoutflow = Eventoutflow_df['Time']


# In[100]:


Eventoutflow = pd.concat([EventDatesoutflow,Eventtimeoutflow],axis =1 )


# In[105]:



Event_df.reset_index(inplace=True)


# In[106]:



EventDatesinflow = Event_df['datenew']
Eventtimeinflow = Event_df['Time']


# In[107]:


Eventinflow = pd.concat([EventDatesinflow,Eventtimeinflow],axis =1)
Eventoutflow = pd.concat([EventDatesoutflow,Eventtimeoutflow],axis =1)


# In[108]:


j= []
for i in EventDatesinflow:
    r = i.strftime("%Y/%m/%d")
    j.append(r)


# In[109]:


q= []
for i in Eventtimeinflow :
    gr = i.strftime("%H.%M")
    a = float(gr)
    q.append(a)
     
        
        
    


# In[110]:


j =pd.DataFrame(j)
q =pd.DataFrame(q)


# In[111]:


ji= []
for io in EventDatesoutflow:
    ro = io.strftime("%Y/%m/%d")
    ji.append(ro)

qi= []
for iq in Eventtimeoutflow :
    gra = iq.strftime("%H.%M")
    ak = float(gra)
    qi.append(ak)


# In[112]:


ji = pd.DataFrame(ji)
qi = pd.DataFrame(qi)


# In[113]:


Eventinflowdata = pd.concat([j,q],axis =1)
Eventoutflowdata = pd.concat([ji,qi],axis =1)


# In[114]:


Eventinflowdata.columns = ['datenewin','Time']
Eventoutflowdata.columns = ['datenewin','Time']


# In[115]:


Eventoutflowdata.dropna()


# In[116]:



tym = df['Time']


# In[117]:


tym.dropna()


# In[118]:


# Dropping the Null Values/Missing Values
tym.drop([7985,9488],inplace = True)


# In[119]:



qqo= []
for im in tym :
    grq = im.strftime("%H.%M")
    aba = float(grq)
    qqo.append(aba)


# In[120]:


timenewvar = pd.DataFrame(qqo)


# In[121]:


timenewvar.columns = ['Timeneww']


# In[122]:



df = pd.concat([df, timenewvar ], axis=1)


# In[123]:


in_dfcopy3 = df.loc[df['flowid'] == 9]
in_dfcopy3.dropna(inplace = True)


# In[124]:


out_dfcopy3 = df.loc[df['flowid'] == 7]
out_dfcopy3.dropna(inplace = True)


# In[125]:


# Adding the Event Flag in the Inflow dataset
in_dfcopy3['EventFlag'] = np.where((in_dfcopy3['dateneww'].isin(Eventinflowdata['datenewin']) & in_dfcopy3['Timeneww'].isin(Eventinflowdata['Time'])), 1 , 0)


# In[126]:


in_dfcopy3['Timeneww']


# In[127]:


in_dfcopy3.describe()


# In[128]:




# Adding the Event Flag in the Inflow dataset
out_dfcopy3['EventFlag'] = np.where((out_dfcopy3['dateneww'].isin(Eventoutflowdata['datenewin']) & out_dfcopy3['Timeneww'].isin(Eventoutflowdata['Time'])), 1 , 0)


# In[129]:


out_dfcopy3.describe()


# In[130]:


train_data = pd.concat([in_dfcopy3,out_dfcopy3])


# In[131]:


train_data.drop('Time',axis = 1,inplace = True)


# In[132]:


train_data.head()


# In[133]:


train_data.describe()


# In[141]:


#Importing the libraries 
from itertools import chain
from sklearn.feature_selection import RFE
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import GridSearchCV, cross_val_score, learning_curve, train_test_split
from sklearn.metrics import precision_score, recall_score, confusion_matrix, roc_curve, precision_recall_curve, accuracy_score
import warnings


# In[134]:


# calculating the missing values
null_feat = pd.DataFrame(len(train_data['flowid']) - train_data.isnull().sum(), columns = ['Count'])


# In[135]:



null_feat.head()
# We can infer that our data doesn't have any missing values


# In[136]:



# 1 is for event and 0 is for no event
train_data['EventFlag'].value_counts()


# In[137]:


#Reassign target and drop useless features

# Drop useless variables
X = train_data.drop(['flowid','datenew','EventFlag','dateneww'],axis =1)


# In[138]:


y = train_data.EventFlag


# In[139]:


y.loc[y.isnull() == True]


# In[142]:


# Train_test split
random_state = 42
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.12, random_state = random_state)


# In[512]:


#Predictive model : Logistic Regression
#Logistic Regression and GridSearch CV to optimise hyperparameters (accuracy)


# In[143]:


# Find best hyperparameters (accuracy)
log_clf = LogisticRegression(random_state = random_state)
param_grid = {
            'penalty' : ['l2','l1'],  
            'C' : [0.001, 0.01, 0.1, 1, 10, 100, 1000]
            }

CV_log_clf = GridSearchCV(estimator = log_clf, param_grid = param_grid , scoring = 'accuracy', verbose = 1, n_jobs = -1)
CV_log_clf.fit(X_train, y_train)

best_parameters = CV_log_clf.best_params_
print('The best parameters for using this model is', best_parameters)


# In[144]:



from matplotlib import pyplot as plt
import itertools
def plot_confusion_matrix(cm, classes,
                          normalize = False,
                          title = 'Confusion matrix"',
                          cmap = plt.cm.Blues) :
    plt.imshow(cm, interpolation = 'nearest', cmap = cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation = 0)
    plt.yticks(tick_marks, classes)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])) :
        plt.text(j, i, cm[i, j],
                 horizontalalignment = 'center',
                 color = 'white' if cm[i, j] > thresh else 'black')

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    
# Show metrics 
def show_metrics():
    tp = cm[1,1]
    fn = cm[1,0]
    fp = cm[0,1]
    tn = cm[0,0]
    print('Accuracy  =     {:.3f}'.format((tp+tn)/(tp+tn+fp+fn)))
    print('Precision =     {:.3f}'.format(tp/(tp+fp)))
    print('Recall    =     {:.3f}'.format(tp/(tp+fn)))
    print('F1_score  =     {:.3f}'.format(2*(((tp/(tp+fp))*(tp/(tp+fn)))/
                                                 ((tp/(tp+fp))+(tp/(tp+fn))))))


# In[145]:


# Precision-recall curve
def plot_precision_recall():
    plt.step(recall, precision, color = 'b', alpha = 0.2,
             where = 'post')
    plt.fill_between(recall, precision, step ='post', alpha = 0.2,
                 color = 'b')

    plt.plot(recall, precision, linewidth=2)
    plt.xlim([0.0,1])
    plt.ylim([0.0,1.05])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision Recall Curve')
    plt.show();


# In[146]:


# ROC curve
def plot_roc():
    plt.plot(fpr, tpr, label = 'ROC curve', linewidth = 2)
    plt.plot([0,1],[0,1], 'k--', linewidth = 2)
   # plt.xlim([0.0,0.001])
   # plt.ylim([0.0,1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.show();


# In[147]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
#Log with best hyperparameters
CV_log_clf = LogisticRegression(C = best_parameters['C'], 
                                penalty = best_parameters['penalty'], 
                                random_state = random_state)

CV_log_clf.fit(X_train, y_train)
y_pred = CV_log_clf.predict(X_test)
y_score = CV_log_clf.decision_function(X_test)

# Confusion maxtrix & metrics
cm = confusion_matrix(y_test, y_pred)
class_names = [0,1]
plt.figure()
plot_confusion_matrix(cm, 
                      classes=class_names, 
                      title='Logistic Confusion matrix')
plt.savefig('6')
plt.show()

show_metrics()

# ROC curve
fpr, tpr, t = roc_curve(y_test, y_score)
plot_roc()


# In[148]:


#make prediction using the test set
Y_test = CV_log_clf.predict(X_test)


# In[149]:


CV_log_clf_score = CV_log_clf.score(X_test, y_test)
print("\nmean accuracy: %.2f" % CV_log_clf_score)


# In[150]:


from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score


# In[168]:



#create adaboost classification obj
ab_clf = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(), n_estimators=100, 
                            learning_rate=0.5, random_state=100)

#training via adaboost classficiation model
ab = ab_clf.fit(X_train, y_train)
print("training....\n")

#make prediction using the test set
ab_pred = ab_clf.predict(X_test)
print('prediction: \n', ab_pred)

print('\nparms: \n', ab_clf.get_params)


# In[152]:


#score
ab_clf_score = ab_clf.score(X_test, y_test)
print("\nmean accuracy: %.2f" % ab_clf.score(X_test, y_test))


# In[153]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Confusion maxtrix & metrics
cm = confusion_matrix(y_test, ab_pred)
class_names = [0,1]
plt.figure()
plot_confusion_matrix(cm, 
                      classes=class_names, 
                      title='Adaboost Confusion matrix')
plt.savefig('6')
plt.show()

show_metrics()

# ROC curve
fpr, tpr, t = roc_curve(y_test, y_score)
plot_roc()


# In[154]:


from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier


# In[155]:


bagging = BaggingClassifier(base_estimator= DecisionTreeClassifier(), max_samples = 0.5, max_features = 0.5, 
                            bootstrap = False, bootstrap_features = False)

bagging.fit(X_train, y_train)
bg_pred = bagging.predict(X_test)

bg_dt_score = bagging.score(X_test, y_test)
bagging.score(X_test, y_test)


# In[156]:


bagging = BaggingClassifier(base_estimator= KNeighborsClassifier(), max_samples = 0.5, max_features = 0.5, 
                            bootstrap = False, bootstrap_features = False)

bagging.fit(X_train, y_train)
bg_pred = bagging.predict(X_test)

bg_score = bagging.score(X_test, y_test)
bagging.score(X_test, y_test)


# In[157]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Confusion maxtrix & metrics
cm = confusion_matrix(y_test, bg_pred)
class_names = [0,1]
plt.figure()
plot_confusion_matrix(cm, 
                      classes=class_names, 
                      title='Bagging Confusion matrix')
plt.savefig('6')
plt.show()

show_metrics()

# ROC curve
fpr, tpr, t = roc_curve(y_test, y_score)
plot_roc()


# In[169]:


from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(1000, 300, 300), solver='adam', shuffle=False, tol = 0.0001)

model = mlp.fit(X_train, y_train)
mlp_pred = mlp.predict(X_test)

print("parameter: ", mlp.get_params())

mlp_score = mlp.score(X_test, y_test)
mlp.score(X_test, y_test)


# In[170]:


mlp_pred


# In[171]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Confusion maxtrix & metrics
cm = confusion_matrix(y_test, mlp_pred)
class_names = [0,1]
plt.figure()
plot_confusion_matrix(cm, 
                      classes=class_names, 
                      title='MLP Confusion matrix')
plt.savefig('6')
plt.show()

show_metrics()

# ROC curve
fpr, tpr, t = roc_curve(y_test, y_score)
plot_roc()


# In[172]:


d = {'Model': ['Logistic Regression', 'Adaboost', 'Bagging_decision tree based', 'Bagging_KNeighbors', 'MLP'],
     'accuracy' : [CV_log_clf_score, ab_clf_score, bg_dt_score, bg_score, mlp_score]}

result_df = pd.DataFrame(data = d)
result_df


# In[173]:


result_df.plot(x='Model', y='accuracy', kind='bar', figsize=(8, 8), title=' Prediction Accuracy', 
               sort_columns=True)


# In[174]:


import pickle
# Saving model to disk
pickle.dump(model, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))



# In[175]:


print(model.predict([[7,0,1,1,16]]))


# In[176]:


print(model.predict([[200,0,1,1,16]]))


# In[177]:


print(model.predict([[5,0,1,1,16]])
     )


# In[178]:


print(model.predict([[10,0,1,1,16]]))


# In[179]:


print(model.predict([[0,0,1,1,0]]))


# In[ ]:




