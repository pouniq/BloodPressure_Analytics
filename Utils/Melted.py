def df_melt(dataset):
    
    import pandas as pd
    
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





def Merge_df(df1, df2, df3):
    import pandas as pd
    
    df = pd.merge(df1, df2, how='right', on=['date', 'time_of_day','day'])
    df = pd.merge(df, df3, how='inner', on=['date', 'time_of_day','day'])

    df.rename(columns= {'measurement': 'Pulse', 'measurement_x':'Diastolic', 'measurement_y':'Systolic'}, inplace=True)
    df.drop(columns=['type_x', 'type_y', 'type'], inplace=True)
    
    return df



def correct_order_timeOfDay(df):
    
    import pandas as pd
    
    # Define the desired order of time_of_day
    time_order = ["morning", "noon", "night"]

    # Convert the "time_of_day" column to a categorical type with the specified order
    df["time_of_day"] = pd.Categorical(df["time_of_day"], categories=time_order, ordered=True)

    # Sort the DataFrame by "day" and then by the ordered "time_of_day"
    df = df.sort_values(by=["day", "time_of_day"])

    # Reset the index to have a clean sequential index
    df = df.reset_index(drop=True)

    # Display the sorted DataFrame
    return df
        

