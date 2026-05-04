import sys, os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# import the RTL module

# !*pip install openpyxl
df = pd.read_csv('Data/BP.csv')
# df = pd.read_excel('BP.xlsx')

df_half = df.loc[0:29].copy()
df_half['day'] = df_half['day'].ffill()
df_half['hand'] = df_half['hand'].ffill()
df_half['date'] = df_half['date'].ffill()

df_half = df_half.dropna()
col_num = ['morning', 'noon', 'night']
col_cat = ['hand', 'type']



# filtering the right hand
df_half_R = df_half[df_half['hand'] == 'R']
df_half_R = df_half_R.drop('hand' , axis=1)
df_half_R_s = df_half_R[df_half_R['type'] == 'Systolic'] 
df_half_R_d =  df_half_R[df_half_R['type'] == 'Diastolic'] 
df_half_R_p =  df_half_R[df_half_R['type'] == 'Pulse']




# filtering the left hand
df_half_L = df_half[df_half['hand'] == 'L']
df_half_L = df_half_L.drop('hand' , axis=1)
df_half_L_s = df_half_L[df_half_L['type'] == 'Systolic'] 
df_half_L_d =  df_half_L[df_half_L['type'] == 'Diastolic'] 
df_half_L_p =  df_half_L[df_half_L['type'] == 'Pulse']
                         

def df_melt(dataset):
    df_long = dataset.melt(
        id_vars=['day', 'date', 'type'], 
        value_vars=['morning', 'noon', 'night'],
        var_name='time_of_day', 
        value_name='measurement'
    )
    time_order = ['morning', 'noon', 'night']
    df_long['time_of_day'] = pd.Categorical(df_long['time_of_day'], categories=time_order, ordered=True)

    df_long = df_long.sort_values(by=['date', 'time_of_day']).reset_index(drop=True)
    print(df_long)

    return pd.DataFrame(df_long)




# left hand

fig, ax = plt.subplots(3,1,figsize=(10,7))

ax[0].plot(df_half_L_p['morning'], color = 'red')
ax[0].set_title('Morning, Left Hand Pulse')

ax[1].plot(df_half_L_p['noon'])
ax[1].set_title('Noon, Left Hand Pulse')

ax[2].plot(df_half_L_p['night'])
ax[2].set_title('Night, Left Hand Pulse')
plt.tight_layout()
plt.show()


datasets = [df_half_L_p , df_half_L_d , df_half_L_s]
names = ['Pulse' , 'Diastolic', 'Systolic']
for data, name in  zip(datasets, names):
    fig, ax = plt.subplots(3,1,figsize=(10,7))

    ax[0].plot(data['morning'], color = 'red')
    ax[0].set_title(f'Morning, Left Hand {name}')

    ax[1].plot(data['noon'])
    ax[1].set_title(f'Noon, Left Hand {name}')

    ax[2].plot(data['night'])
    ax[2].set_title(f'Night, Left Hand {name}')
    plt.tight_layout()
    plt.show()
          
    
# melt the dataset.
df_p = df_melt(df_half_L_p)
df_s = df_melt(df_half_L_s)
df_d = df_melt(df_half_L_d)


melted_list = [df_p , df_s , df_d]
name = ['pulse', 'Systolic', 'Diastolic']
for d, n in zip(melted_list,name):
    print('-'*24 , f'Average value for {n}', ''*25)
    print(d.groupby('time_of_day', observed=False )['measurement'].mean())
    print('-'*50)


# this is were you develope T-Test to comapare if 
# getting BP with Right or Left hand would differ 
# in any case.





# Analysis of Left hand








