def Average_Melt(meltedList, name):
    
    for d, n in zip(meltedList,name):
        print('-'*24 , f'Average value for {n}', ''*25)
        print(d.groupby('time_of_day', observed=False )['measurement'].mean())
        print('-'*50)