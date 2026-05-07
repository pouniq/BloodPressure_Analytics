def Average_Melt(meltedList, name):
    
    for d, n in zip(meltedList,name):
        print('-'*24 , f'Average value for {n}', ''*25)
        print(d.groupby('time_of_day', observed=False )['measurement'].mean())
        print('-'*50)
        
        
        


def iqr_bounds(series, factor=1.5):
        q1 = series.quantile(0.25)
        q2 = series.quantile(0.75)
        iqr = q2 - q1
        lower_bound = q1 - factor * iqr
        upper_bound = q2 + factor * iqr

        return lower_bound, upper_bound, iqr