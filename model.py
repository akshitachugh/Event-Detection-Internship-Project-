import pandas as pd
from pandas import datetime
from datetime import date
from matplotlib import pyplot
import numpy as np

# read and parse data 
df = pd.read_excel('C:\\Users\\akshu\\Downloads\\Internship.xlsx', header=0, squeeze=True)

# Renaming the columns 
df.columns = ['flowid', 'date','Time','Count']


df.date

# Checking Missing Values in date column
df.date.isnull().sum()

df.date.loc[df.date.isnull() == True]

df.drop([7985,9488],inplace = True)

df.date.isnull().sum()

# Since the format of the date variable in not consistent let's make it consisitent
date = pd.to_datetime(df['date'])

# Concatenating the date variable with a consistent format with the df dataset.
df = pd.concat([df, date], axis=1)

df.head()

# Renaming the columns
df.columns = ['flowid', 'date','Time','Count','datenew']


# Creating a string varible dateneww for analysis
w = df['datenew']
w.tolist()
wt = []
for l in w:
    gr = l.strftime("%Y/%m/%d")
    wt.append(gr)

datenewww = pd.DataFrame(wt)
df = pd.concat([df,  datenewww], axis=1)

# Renaming the columns
df.columns = ['flowid', 'date','Time','Count','datenew','dateneww']

df['dateneww']

# Now we are doing the Exploratory Data Analysis to see if the inflow and outflow of people are dependent on the weekday 
# We are finding the weekday from the Date Variable

from datetime import datetime
data = []
for i in range(10081):
           data.append(df.datenew[i].weekday())
           

# Droping the column date with an inconsistent format
df.drop('date', axis=1, inplace=True)

# O means Monday 
# 1 means Tuesday
# 2 means Wednesday
# 3 means Thursday 
# 4 means Friday
# 5 means Saturday
# 6 means Sunday

data

# Converting the list to Pandas DataFrame
dayofweek = pd.DataFrame(data)

# Concatenating the column Dayofweek with df dataset
df = pd.concat([df, dayofweek], axis=1)
 

df.head()

# Naming the columns of the df dataset
df.columns = ['flowid', 'Time','Count','datenew','dateneww','dayofweek']

# Hence for our analysis lets divide our day of the week column into weekdays and weekends
# weekdays is denoted by True
# weekends is denoted by False

I = [0,1,2,3,4,5]

df['weekdayFlag'] = np.where(df['dayofweek'].isin(I), 1 , 0)


# For our analysis let's also parse month from the date variable since the inflow and outflow of people vary with the month
from datetime import datetime
data = []
for i in range(10081):
           data.append(df.datenew[i].month)

month = pd.DataFrame(data)

df = pd.concat([df, month], axis=1)

df.columns = ['flowid', 'Time','Count','datenew','dateneww','dayofweek','weekdayFlag','month']

df.head()

# From the df data separating the inflow and outflow data
# Output Data is defined as out_df
# Input Data is defined as in_df
out_df = df.loc[df['flowid'] == 7]

in_df = df.loc[df['flowid'] == 9]

# Let's find the peak hours flag for Inflow and Outflow Data on weekend and weekday
# Let's subset the data for weekdays and weekends for each month



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

# Drawing the pivot table for inflow data for each month
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







# Let's subset the data into peak and non-peak hours for month 1 
inflowdatamonth1weekdayPeak = inflowdatamonth1weekday.loc[inflowdatamonth1weekday['PeakFlag']== True]

inflowdatamonth1weekdayNonPeak = inflowdatamonth1weekday.loc[inflowdatamonth1weekday['PeakFlag']== False]

inflowdatamonth1weekendPeak = inflowdatamonth1weekend.loc[inflowdatamonth1weekend['PeakFlag']== True]

inflowdatamonth1weekendNonPeak = inflowdatamonth1weekend.loc[inflowdatamonth1weekend['PeakFlag']== False]



pivot25 = inflowdatamonth1weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot26 = inflowdatamonth1weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot27 = inflowdatamonth1weekendPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot28 = inflowdatamonth1weekendNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
mean25 = pivot25.mean()
mean26 = pivot26.mean()
mean27 = pivot27.mean()
mean28 = pivot28.mean()
Event1 = pivot25.loc[pivot25['Count']>int(mean25)]
Event2 = pivot26.loc[pivot26['Count']>int(mean26)]
Event3 = pivot27.loc[pivot27['Count']> int(mean27)]
Event4 = pivot28.loc[pivot28['Count']>  int(mean28)]

pivot25.plot(title='InFlow on weekdays in peak hours in Jan', color = {'green'})
pyplot.tight_layout()
pyplot.show()


pivot26.plot(title='InFlow on weekdays in nonpeak hours in Jan', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivot27.head()

pivot28.head()

# Let's subset the data into peak and non-peak hours for month 2
inflowdatamonth2weekdayPeak = inflowdatamonth2weekday.loc[inflowdatamonth2weekday['PeakFlag']== True]

inflowdatamonth2weekdayNonPeak = inflowdatamonth2weekday.loc[inflowdatamonth2weekday['PeakFlag']== False]



pivot29 = inflowdatamonth2weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot30 = inflowdatamonth2weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
mean29 = pivot29.mean()
mean30 = pivot30.mean()

Event5 = pivot29.loc[pivot29['Count']>int(mean29)]
Event6 = pivot30.loc[pivot30['Count']>int(mean30)]


pivot29.plot(title='InFlow on weekdays in peak hours in Feb', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivot30.plot(title='InFlow on weekdays in non peak hours in Feb', color = {'green'})
pyplot.tight_layout()
pyplot.show()

# Let's subset the data into peak and non-peak hours for month 3
inflowdatamonth3weekdayPeak = inflowdatamonth3weekday.loc[inflowdatamonth3weekday['PeakFlag']== True]

inflowdatamonth3weekdayNonPeak = inflowdatamonth3weekday.loc[inflowdatamonth3weekday['PeakFlag']== False]

pivot31 = inflowdatamonth3weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot32 = inflowdatamonth3weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
mean31 = pivot31.mean()
mean32 = pivot32.mean()


Event7 = pivot31.loc[pivot31['Count']>int(mean31)]
Event8 = pivot32.loc[pivot32['Count']>int(mean32)]

pivot31.plot(title='InFlow on weekdays in peak hours in March', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivot32.plot(title='InFlow on weekdays in non-peak hours in March', color = {'green'})
pyplot.tight_layout()
pyplot.show()


# Let's subset the data into peak and non-peak hours for month 4
inflowdatamonth4weekdayPeak = inflowdatamonth4weekday.loc[inflowdatamonth4weekday['PeakFlag']== True]

inflowdatamonth4weekdayNonPeak = inflowdatamonth4weekday.loc[inflowdatamonth4weekday['PeakFlag']== False]

inflowdatamonth4weekendPeak = inflowdatamonth4weekend.loc[inflowdatamonth4weekend['PeakFlag']== True]

inflowdatamonth4weekendNonPeak = inflowdatamonth4weekend.loc[inflowdatamonth4weekend['PeakFlag']== False]

pivot33 = inflowdatamonth4weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot34 = inflowdatamonth4weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot35 = inflowdatamonth4weekendPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot36 = inflowdatamonth4weekendNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
mean33 = pivot33.mean()
mean34 = pivot34.mean()
mean35 = pivot35.mean()
mean36 = pivot36.mean()
Event9 = pivot33.loc[pivot33['Count']>int(mean33)]
Event10 = pivot34.loc[pivot34['Count']>int(mean34)]
Event11 = pivot35.loc[pivot35['Count']>int(mean35)]
Event12 = pivot36.loc[pivot36['Count']>int(mean36)]


pivot33.plot(title='InFlow on weekdays in peak hours in April', color = {'green'})
pyplot.tight_layout()
pyplot.show()
pivot34.plot(title='InFlow on weekdays in non- peak hours in April', color = {'green'})
pyplot.tight_layout()
pyplot.show()




# Let's subset the data into peak and non-peak hours for month 5
inflowdatamonth5weekdayPeak = inflowdatamonth5weekday.loc[inflowdatamonth5weekday['PeakFlag']== True]

inflowdatamonth5weekdayNonPeak = inflowdatamonth5weekday.loc[inflowdatamonth5weekday['PeakFlag']== False]

inflowdatamonth5weekendPeak = inflowdatamonth5weekend.loc[inflowdatamonth5weekend['PeakFlag']== True]

inflowdatamonth5weekendNonPeak = inflowdatamonth5weekend.loc[inflowdatamonth5weekend['PeakFlag']== False]

pivot37 = inflowdatamonth5weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot38 = inflowdatamonth5weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot39 = inflowdatamonth5weekendPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot40 = inflowdatamonth5weekendNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
mean37 = pivot37.mean()
mean38 = pivot38.mean()
mean39 = pivot39.mean()
mean40 = pivot40.mean()
Event13 = pivot37.loc[pivot37['Count']>int(mean37)]
Event14 = pivot38.loc[pivot38['Count']>int(mean38)]
Event15 = pivot39.loc[pivot39['Count']>int(mean39)]
Event16 = pivot40.loc[pivot40['Count']>int(mean40)]

pivot37.plot(title='InFlow on weekdays in peak hours in May', color = {'green'})
pyplot.tight_layout()
pyplot.show()
pivot38.plot(title='InFlow on weekdays in non peak hours in May', color = {'green'})
pyplot.tight_layout()
pyplot.show()


# Let's subset the data into peak and non-peak hours for month 6
inflowdatamonth6weekdayPeak = inflowdatamonth6weekday.loc[inflowdatamonth6weekday['PeakFlag']== True]

inflowdatamonth6weekdayNonPeak = inflowdatamonth6weekday.loc[inflowdatamonth6weekday['PeakFlag']== False]




pivot41 = inflowdatamonth6weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot42 = inflowdatamonth6weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
mean41 = pivot41.mean()
mean42 = pivot42.mean()
Event17 = pivot41.loc[pivot41['Count']>int(mean41)]
Event18 = pivot42.loc[pivot42['Count']>int(mean42)]


pivot41.plot(title='InFlow on weekdays in peak hours in June', color = {'green'})
pyplot.tight_layout()
pyplot.show()
pivot42.plot(title='InFlow on weekdays in non peak hours in June', color = {'green'})
pyplot.tight_layout()
pyplot.show()

# Let's subset the data into peak and non-peak hours for month 7
inflowdatamonth7weekdayNonPeak = inflowdatamonth7weekday.loc[inflowdatamonth7weekday['PeakFlag']== False]

inflowdatamonth7weekendPeak = inflowdatamonth7weekend.loc[inflowdatamonth7weekend['PeakFlag']== True]

inflowdatamonth7weekendNonPeak = inflowdatamonth7weekend.loc[inflowdatamonth7weekend['PeakFlag']== False]

pivot44 = inflowdatamonth7weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot45 = inflowdatamonth7weekendPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot46 = inflowdatamonth7weekendNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')

mean44 = pivot44.mean()
mean45 = pivot45.mean()
mean46 = pivot46.mean()


Event19 = pivot44.loc[pivot44['Count']>int(mean44)]
Event20 = pivot45.loc[pivot45['Count']>int(mean45)]
Event21 = pivot46.loc[pivot46['Count']>int(mean46)]

pivot44.plot(title='InFlow on weekdays in nonpeak hours in July', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivot45.plot(title='InFlow on weekends in peak hours in July', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivot46.plot(title='InFlow on weekends in non peak hours in July', color = {'green'})
pyplot.tight_layout()
pyplot.show()

inflowdatamonth8weekdayPeak = inflowdatamonth8weekday.loc[inflowdatamonth8weekday['PeakFlag']== True]
inflowdatamonth8weekdayNonPeak = inflowdatamonth8weekday.loc[inflowdatamonth8weekday['PeakFlag']== False]
inflowdatamonth8weekendPeak = inflowdatamonth8weekend.loc[inflowdatamonth8weekend['PeakFlag']== True]
inflowdatamonth8weekendNonPeak = inflowdatamonth8weekend.loc[inflowdatamonth8weekend['PeakFlag']== False]
pivot47 = inflowdatamonth8weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot48 = inflowdatamonth8weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot49 = inflowdatamonth8weekendPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot50 = inflowdatamonth8weekendNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')

mean47 = pivot47.mean()
mean48 = pivot48.mean()
mean49 = pivot49.mean()
mean50 = pivot50.mean()

Event19 = pivot47.loc[pivot47['Count']>int(mean47)]
Event20 = pivot48.loc[pivot48['Count']>int(mean48)]
Event21 = pivot49.loc[pivot49['Count']>int(mean49)]
Event22 = pivot50.loc[pivot50['Count']>int(mean50)]


inflowdatamonth9weekdayPeak = inflowdatamonth9weekday.loc[inflowdatamonth9weekday['PeakFlag']== True]
inflowdatamonth9weekdayNonPeak = inflowdatamonth9weekday.loc[inflowdatamonth9weekday['PeakFlag']== False]
inflowdatamonth9weekendPeak = inflowdatamonth9weekend.loc[inflowdatamonth9weekend['PeakFlag']== True]
inflowdatamonth9weekendNonPeak = inflowdatamonth9weekend.loc[inflowdatamonth9weekend['PeakFlag']== False]
pivot51 = inflowdatamonth9weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot52 = inflowdatamonth9weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot53 = inflowdatamonth9weekendPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot54 = inflowdatamonth9weekendNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')

mean51 = pivot51.mean()
mean52 = pivot52.mean()
mean53 = pivot53.mean()
mean54 = pivot54.mean()

Event23 = pivot51.loc[pivot51['Count']>int(mean51)]
Event24 = pivot52.loc[pivot52['Count']>int(mean52)]
Event25 = pivot53.loc[pivot53['Count']>int(mean53)]
Event26 = pivot54.loc[pivot54['Count']>int(mean54)]

inflowdatamonth10weekdayPeak = inflowdatamonth10weekday.loc[inflowdatamonth10weekday['PeakFlag']== True]
inflowdatamonth10weekdayNonPeak = inflowdatamonth10weekday.loc[inflowdatamonth10weekday['PeakFlag']== False]
inflowdatamonth10weekendPeak = inflowdatamonth10weekend.loc[inflowdatamonth10weekend['PeakFlag']== True]
inflowdatamonth10weekendNonPeak = inflowdatamonth10weekend.loc[inflowdatamonth10weekend['PeakFlag']== False]
pivot55 = inflowdatamonth10weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot56 = inflowdatamonth10weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot57 = inflowdatamonth10weekendPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot58 = inflowdatamonth10weekendNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')

mean55 = pivot55.mean()
mean56 = pivot56.mean()
mean57 = pivot57.mean()
mean58 = pivot58.mean()

Event27 = pivot55.loc[pivot55['Count']>int(mean55)]
Event28 = pivot56.loc[pivot56['Count']>int(mean56)]
Event29 = pivot57.loc[pivot57['Count']>int(mean57)]
Event30 = pivot58.loc[pivot58['Count']>int(mean58)]

inflowdatamonth11weekdayPeak = inflowdatamonth11weekday.loc[inflowdatamonth11weekday['PeakFlag']== True]
inflowdatamonth11weekdayNonPeak = inflowdatamonth11weekday.loc[inflowdatamonth11weekday['PeakFlag']== False]
#inflowdatamonth11weekendPeak = inflowdatamonth11weekend.loc[inflowdatamonth11weekend['PeakFlag']== True]
#inflowdatamonth11weekendNonPeak = inflowdatamonth11weekend.loc[inflowdatamonth11weekend['PeakFlag']== False]
pivot59 = inflowdatamonth11weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot60 = inflowdatamonth11weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
#pivot61 = inflowdatamonth11weekendPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
#pivot62 = inflowdatamonth11weekendNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')

mean59 = pivot59.mean()
mean60 = pivot60.mean()
#mean61 = pivot61.mean()
#mean62 = pivot62.mean()



Event31 = pivot59.loc[pivot59['Count']>int(mean59)]
Event32 = pivot60.loc[pivot60['Count']>int(mean60)]
#Event36 = pivot61.loc[pivot61['Count']>int(mean61)]
#Event37 = pivot62.loc[pivot62['Count']>int(mean62)]

pivot47.plot(title='InFlow on weekdays in peak hours in Aug', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivot48.plot(title='InFlow on weekdays in non peak hours in Aug', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivot49.plot(title='InFlow on weekends in peak hours in Aug', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivot50.plot(title='InFlow on weekends in non peak hours in Aug', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivot51.plot(title='InFlow on weekdays in peak hours in Sept', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivot52.plot(title='InFlow on weekdays in non peak hours in Sept', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivot53.plot(title='InFlow on weekends in peak hours in Sept', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivot54.plot(title='InFlow on weekends in non peak hours in Sept', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivot55.plot(title='InFlow on weekdays in peak hours in Oct', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivot56.plot(title='InFlow on weekdays in non peak hours in Oct', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivot57.plot(title='InFlow on weekends in peak hours in Oct', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivot58.plot(title='InFlow on weekends in non peak hours in Oct', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivot59.plot(title='InFlow on weekdays in peak hours in Nov', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivot60.plot(title='InFlow on weekdays in non peak hours in Nov', color = {'green'})
pyplot.tight_layout()
pyplot.show()



inflowdatamonth12weekdayPeak = inflowdatamonth12weekday.loc[inflowdatamonth12weekday['PeakFlag']== True]
inflowdatamonth12weekdayNonPeak = inflowdatamonth12weekday.loc[inflowdatamonth12weekday['PeakFlag']== False]
#inflowdatamonth12weekendPeak = inflowdatamonth12weekend.loc[inflowdatamonth12weekend['PeakFlag']== True]
#inflowdatamonth12weekendNonPeak = inflowdatamonth12weekend.loc[inflowdatamonth12weekend['PeakFlag']== False]
pivot61 = inflowdatamonth12weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivot62 = inflowdatamonth12weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
#pivot63 = inflowdatamonth12weekendPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
#pivot64 = inflowdatamonth12weekendNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')

mean61 = pivot61.mean()
mean62 = pivot62.mean()
#mean63 = pivot63.mean()
#mean64 = pivot64.mean()

pivot61.plot(title='InFlow on weekdays in peak hours in Dec', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivot62.plot(title='InFlow on weekdays in non peak hours in Dec', color = {'green'})
pyplot.tight_layout()
pyplot.show()

#pivot63.plot(title='InFlow on weekdays in peak hours in Dec', color = {'green'})
#pyplot.tight_layout()
#pyplot.show()

#pivot64.plot(title='InFlow on weekdays in non peak hours in Dec', color = {'green'})
#pyplot.tight_layout()
#pyplot.show()

# On the basis of the Analysis done above on the inflow data the following dates could be identified as dates with events
Event = [Event1, Event2, Event3, Event4, Event5,Event6,Event7,Event8,Event9,Event10,Event11, Event12, Event13,Event14,Event15, Event16, Event17, Event18,Event19,Event20,Event21,Event22,Event23,Event24,Event25,Event26,Event27, Event28, Event29,Event30,Event31,Event32]
Event_df = pd.concat(Event)

Event_df.count()

Event_df.head()

#Outflow Data
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

# Drawing the pivot table for inflow data for each month
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

# Pivot Table for month 1 
pivoto25 = outflowdatamonth1weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto26 = outflowdatamonth1weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto27 = outflowdatamonth1weekendPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto28 = outflowdatamonth1weekendNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')

meano25 = pivoto25.mean()
meano26 = pivoto26.mean()
meano27 = pivoto27.mean()
meano28 = pivoto28.mean()

# Pivot Table for month 2 
pivoto29 = outflowdatamonth2weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto30 = outflowdatamonth2weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')

meano29 = pivoto29.mean()
meano30 = pivoto30.mean()

# Pivot Table for month 3 
pivoto31 = outflowdatamonth3weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto32 = outflowdatamonth3weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')

meano31 = pivoto31.mean()
meano32 = pivoto32.mean()

# Pivot Table for month 4 
pivoto33 = outflowdatamonth4weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto34 = outflowdatamonth4weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto35 = outflowdatamonth4weekendPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto36 = outflowdatamonth4weekendNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')

meano33 = pivoto33.mean()
meano34 = pivoto34.mean()
meano35 = pivoto35.mean()
meano36 = pivoto36.mean()

# Pivot Table for month 5 
pivoto37 = outflowdatamonth5weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto38 = outflowdatamonth5weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto39 = outflowdatamonth5weekendPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto40 = outflowdatamonth5weekendNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')

meano37 = pivoto37.mean()
meano38 = pivoto38.mean()
meano39 = pivoto39.mean()
meano40 = pivoto40.mean()

# Pivot Table for month 6
pivoto41 = outflowdatamonth6weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto42 = outflowdatamonth6weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')


meano41 = pivoto41.mean()
meano42 = pivoto42.mean()

# Pivot Table for month 7

pivoto43 = outflowdatamonth7weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto44 = outflowdatamonth7weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto45 = outflowdatamonth7weekendPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto46 = outflowdatamonth7weekendNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')

meano43 = pivoto43.mean()
meano44 = pivoto44.mean()
meano45 = pivoto45.mean()
meano46 = pivoto46.mean()


# Pivot Table for month 8

pivoto47 = outflowdatamonth8weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto48 = outflowdatamonth8weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
meano47 = pivoto47.mean()
meano48 = pivoto48.mean()

# Pivot Table for month 9

pivoto49 = outflowdatamonth9weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto50 = outflowdatamonth9weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto51 = outflowdatamonth9weekendPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto52 = outflowdatamonth9weekendNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
meano49 = pivoto49.mean()
meano50 = pivoto50.mean()
meano51 = pivoto51.mean()
meano52 = pivoto52.mean()

# Pivot Table for month 10

pivoto53 = outflowdatamonth10weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto54 = outflowdatamonth10weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')

pivoto55 = outflowdatamonth10weekendPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto56 = outflowdatamonth10weekendNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
meano53 = pivoto53.mean()
meano54 = pivoto54.mean()
meano55 = pivoto55.mean()
meano56 = pivoto56.mean()


# Let's subset the data into peak and non-peak hours for month 11
pivoto57 = outflowdatamonth11weekdayPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
pivoto58 = outflowdatamonth11weekdayNonPeak.pivot_table(index='datenew', values=['Count'], aggfunc='sum')
meano57 = pivoto57.mean()
meano58 = pivoto58.mean()

# Let's subset the data into peak and non-peak hours for month 12
pivoto59 = outflowdatamonth12weekdayPeak.pivot_table(index=['datenew'], values=['Count'], aggfunc='sum')
pivoto60 = outflowdatamonth12weekdayNonPeak.pivot_table(index=['datenew'], values=['Count'], aggfunc='sum')
meano59 = pivoto59.mean()
meano60 = pivoto60.mean()


# Let's Plot the Graph to visualize the results
pivoto25.plot(title='OutFlow on weekdays in peak hours in Jan', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto26.plot(title='OutFlow on weekdays in non peak hours in Jan', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto27.plot(title='OutFlow on weekends in peak hours in Jan', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivot28.plot(title='OutFlow on weekends in non peak hours in Jan', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto29.plot(title='OutFlow on weekdays in peak hours in Feb', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto30.plot(title='OutFlow on weekdays in non peak hours in Feb', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto31.plot(title='OutFlow on weekdays in peak hours in March', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto32.plot(title='OutFlow on weekdays in non peak hours in March', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto33.plot(title='OutFlow on weekdays in peak hours in April', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto34.plot(title='OutFlow on weekdays in non peak hours in April', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto35.plot(title='OutFlow on weekends in peak hours in April', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto36.plot(title='OutFlow on weekends in non peak hours in April', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto37.plot(title='OutFlow on weekdays in peak hours in May', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto38.plot(title='OutFlow on weekdays in non peak hours in May', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto39.plot(title='OutFlow on weekends in peak hours in May', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto40.plot(title='OutFlow on weekends in non peak hours in May', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto41.plot(title='OutFlow on weekdays in peak hours in June', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto42.plot(title='OutFlow on weekdays in non peak hours in June', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto43.plot(title='OutFlow on weekdays in peak hours in July', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto44.plot(title='OutFlow on weekdays in non peak hours in July', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto45.plot(title='OutFlow on weekends in peak hours in July', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto46.plot(title='OutFlow on weekends in non peak hours in July', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto47.plot(title='OutFlow on weekdays in peak hours in August', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto48.plot(title='OutFlow on weekdays in non peak hours in August', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto49.plot(title='OutFlow on weekdays in peak hours in Sept', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto50.plot(title='OutFlow on weekdays in non peak hours in Sept', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto51.plot(title='OutFlow on weekends in peak hours in Sept', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto52.plot(title='OutFlow on weekends in non peak hours in Sept', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto53.plot(title='OutFlow on weekdays in peak hours in Oct', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto54.plot(title='OutFlow on weekdays in non peak hours in Oct', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto55.plot(title='OutFlow on weekends in peak hours in Oct', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto56.plot(title='OutFlow on weekends in non peak hours in Oct', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto57.plot(title='OutFlow on weekdays in peak hours in Nov', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto58.plot(title='OutFlow on weekdays in non peak hours in Nov', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto59.plot(title='OutFlow on weekends in peak hours in Dec', color = {'green'})
pyplot.tight_layout()
pyplot.show()

pivoto60.plot(title='OutFlow on weekends in non peak hours in Dec', color = {'green'})
pyplot.tight_layout()
pyplot.show()

# Let's Define Event on the basis of the outflow data
Event25 = pivot25.loc[pivot25['Count']>int(meano25)]
Event26 = pivot26.loc[pivot26['Count']>int(meano26)]
Event27 = pivot27.loc[pivot27['Count']>int(meano27)]
Event28 = pivot28.loc[pivot28['Count']>int(meano28)]
Event29 = pivot29.loc[pivot29['Count']>int(meano29)]
Event30 = pivot30.loc[pivot30['Count']>int(meano30)]
Event31 = pivot31.loc[pivot31['Count']>int(meano31)]
Event32 = pivot32.loc[pivot32['Count']>int(meano32)]
Event33 = pivot33.loc[pivot33['Count']>int(meano33)]
Event34 = pivot34.loc[pivot34['Count']>int(meano34)]
Event35 = pivot35.loc[pivot35['Count']>int(meano35)]
Event36 = pivot36.loc[pivot36['Count']>int(meano36)]
Event37 = pivot37.loc[pivot37['Count']>int(meano37)]
Event38 = pivot38.loc[pivot38['Count']>int(meano38)]
Event39 = pivot39.loc[pivot39['Count']>int(meano39)]
Event40 = pivot40.loc[pivot40['Count']>int(meano40)]
Event41 = pivot41.loc[pivot41['Count']>int(meano41)]
Event42 = pivot42.loc[pivot42['Count']>int(meano42)]
#Event43 = pivot43.loc[pivot43['Count']>int(meano43)]
Event44 = pivot44.loc[pivot44['Count']>int(meano44)]
Event45 = pivot45.loc[pivot45['Count']>int(meano45)]
Event46 = pivot46.loc[pivot46['Count']>int(meano46)]
Event47 = pivot47.loc[pivot47['Count']>int(meano47)]
Event48 = pivot48.loc[pivot48['Count']>int(meano48)]
Event49 = pivot49.loc[pivot49['Count']>int(meano49)]
Event50 = pivot50.loc[pivot50['Count']>int(meano50)]
Event51 = pivot51.loc[pivot51['Count']>int(meano51)]
Event52 = pivot52.loc[pivot52['Count']>int(meano52)]
Event53 = pivot53.loc[pivot53['Count']>int(meano53)]
Event54 = pivot54.loc[pivot54['Count']>int(meano54)]
Event55 = pivot55.loc[pivot55['Count']>int(meano55)]
Event56 = pivot56.loc[pivot56['Count']>int(meano56)]
Event57 = pivot57.loc[pivot57['Count']>int(meano57)]
Event58 = pivot58.loc[pivot58['Count']>int(meano58)]
Event59 = pivot59.loc[pivot59['Count']>int(meano59)]
Event60 = pivot60.loc[pivot60['Count']>int(meano60)]




# On the basis of the Analysis done above on the outflow data the following dates could be identified as dates with events
Eventoutflow = [Event25, Event26, Event27, Event28, Event29,Event30,Event31,Event32,Event33,Event34,Event35, Event36, Event37,Event38,Event39, Event40, Event41, Event42,Event44,Event45,Event46,Event47,Event48,Event49,Event50,Event51, Event52, Event53,Event54,Event55,Event56,Event57,Event58,Event59,Event60]
Eventoutflow_df = pd.concat(Eventoutflow)

Eventoutflow_df.head()

Eventoutflow_df.count()

EventDatesoutflow = Eventoutflow_df.index

EventDatesinflow = Event_df.index

j= []
for i in EventDatesinflow:
    r = i.strftime("%Y/%m/%d")
    j.append(r)


q= []
for m in EventDatesoutflow:
    p = m.strftime("%Y/%m/%d")
    q.append(p)

j = pd.DataFrame(j)
q = pd.DataFrame(q)

j.columns = ['datenewin']
q.columns = ['datenewout']

in_dfcopy3 = df.loc[df['flowid'] == 9]
in_dfcopy3.dropna(inplace = True)

out_dfcopy3 = df.loc[df['flowid'] == 7]
out_dfcopy3.dropna(inplace = True)


# Adding the Event Flag in the Inflow dataset
in_dfcopy3['EventFlag'] = np.where(in_dfcopy3['dateneww'].isin(j['datenewin']), 1 , 0)

in_dfcopy3.describe()

# Adding the Event Flag in the Outflow dataset
out_dfcopy3['EventFlag'] = np.where(out_dfcopy3['dateneww'].isin(q['datenewout']), 1 , 0)

out_dfcopy3.describe()

train_data = pd.concat([in_dfcopy3,out_dfcopy3])


# Creating a float variable time for analysis
w = train_data['Time']
w.tolist()
wt = []
for l in w:
    gr = l.strftime("%H.%M")
    a = float(gr)
    wt.append(a)


Time = pd.DataFrame(wt)
train_data= pd.concat([train_data,  Time], axis=1)

train_data.columns = ['flowid','Time','Count','datenew','dateneww','dayofweek','weekdayFlag','month','EventFlag','Timenew']

train_data.head()

train_data.describe()

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

train_data.drop('Time',axis = 1,inplace = True)

# calculating the missing values
null_feat = pd.DataFrame(len(train_data['flowid']) - train_data.isnull().sum(), columns = ['Count'])


null_feat.head()
# We can infer that our data doesn't have any missing values


# 1 is for event and 0 is for no event
train_data['EventFlag'].value_counts()


#Reassign target and drop useless features

# Drop useless variables
X = train_data.drop(['flowid','datenew','dateneww','EventFlag'],axis =1)



X.head()

X.Timenew.loc[X.Timenew.isnull() == True]

X.drop([10077,10078],inplace = True)


X.month.loc[X.month.isnull() == True]

X.drop([7985,9488],inplace = True)

y = train_data.EventFlag

y.loc[y.isnull() == True]

y.drop([7985,9488],inplace = True)

y.drop([10077,10078],inplace = True)


# Train_test split
random_state = 42
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.12, random_state = random_state)

#Predictive model : Logistic Regression
#Logistic Regression and GridSearch CV to optimise hyperparameters (accuracy)

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

import matplotlib.pyplot as plt

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


#make prediction using the test set
Y_test = CV_log_clf.predict(X_test)

CV_log_clf_score = CV_log_clf.score(X_test, y_test)
print("\nmean accuracy: %.2f" % CV_log_clf_score)

from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score


#create adaboost classification obj
ab_clf = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(), n_estimators=100, 
                            learning_rate=0.5, random_state=100)

#training via adaboost classficiation model
model = ab_clf.fit(X_train, y_train)
print("training....\n")

#make prediction using the test set
ab_pred_diabetes = ab_clf.predict(X_test)
print('prediction: \n', ab_pred_diabetes)

print('\nparms: \n', ab_clf.get_params)

#score
ab_clf_score = ab_clf.score(X_test, y_test)
print("\nmean accuracy: %.2f" % ab_clf.score(X_test, y_test))

import matplotlib.pyplot as plt


# Confusion maxtrix & metrics
cm = confusion_matrix(y_test, ab_pred_diabetes)
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


from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier

bagging = BaggingClassifier(base_estimator= DecisionTreeClassifier(), max_samples = 0.5, max_features = 0.5, 
                            bootstrap = False, bootstrap_features = False)

bagging.fit(X_train, y_train)
bg_pred_diabetes = bagging.predict(X_test)

bg_dt_score = bagging.score(X_test, y_test)
bagging.score(X_test, y_test)

bagging = BaggingClassifier(base_estimator= KNeighborsClassifier(), max_samples = 0.5, max_features = 0.5, 
                            bootstrap = False, bootstrap_features = False)

bagging.fit(X_train, y_train)
bg_pred_diabetes = bagging.predict(X_test)

bg_score = bagging.score(X_test, y_test)
bagging.score(X_test, y_test)

import matplotlib.pyplot as plt


# Confusion maxtrix & metrics
cm = confusion_matrix(y_test, bg_pred_diabetes)
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


from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(1000, 300, 300), solver='adam', shuffle=False, tol = 0.0001)

mlp.fit(X_train, y_train)
mlp_pred_diabetes = mlp.predict(X_test)

print("parameter: ", mlp.get_params())

mlp_score = mlp.score(X_test, y_test)
mlp.score(X_test, y_test)

mlp_pred_diabetes

d = {'Model': ['Logistic Regression', 'Adaboost', 'Bagging_decision tree based', 'Bagging_KNeighbors', 'MLP'],
     'accuracy' : [CV_log_clf_score, ab_clf_score, bg_dt_score, bg_score, mlp_score]}

result_df = pd.DataFrame(data = d)
result_df

result_df.plot(x='Model', y='accuracy', kind='bar', figsize=(8, 8), title='Diabetes Prediction Accuracy', 
               sort_columns=True)


# Saving model to disk
pickle.dump(model, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))





