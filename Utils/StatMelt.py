def Average_Melt(df_cols, name):
    
    for d, n in zip(df_cols,name):
        print('-'*24 , f'Average value for {n}', ''*25)
        print(df.groupby('time_of_day', observed=False )[n].mean())
        print('-'*50)

            
        


def iqr_bounds(series, factor=1.5):
        q1 = series.quantile(0.25)
        q2 = series.quantile(0.75)
        iqr = q2 - q1
        lower_bound = q1 - factor * iqr
        upper_bound = q2 + factor * iqr

        return lower_bound, upper_bound, iqr