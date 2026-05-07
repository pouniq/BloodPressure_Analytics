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




# class Make_dataframe:
    
#     # ''''
#     # In this class If you put any excel data,
#     # You get the result of separated Right 
#     # and Left Arms. with the blood pressure measurements

#     # ''''
#     import pandas as pd
    
    
#     def __init__(self, df):
#         self.df = df
        
        
#     def Decompose(self):
#         self.df['day'] = self.df['day'].ffill()
#         self.df['hand'] = self.df['hand'].ffill()
#         self.df['date'] = self.df['date'].ffill()
        
        
#     def Filter_hand(self):
    
#         hands = ['R','L']
#         for hand in hands:
#             if hand == 'R':
#                 self.df_R = self.df[self.df['hand'] == 'R']
#                 self.df_R = df_R.drop('hand' , axis=1)
#                 self.df_R_s = df_R[df_R['type'] == 'Systolic'] 
#                 self.df_R_d =  df_R[df_R['type'] == 'Diastolic'] 
#                 self.df_R_p =  df_R[df_R['type'] == 'Pulse']
            
#             else:
#                 self.df_L = self.df[self.df['hand'] == 'L']
#                 self.df_L = df_L.drop('hand' , axis=1)
#                 self.df_L_s = df_L[df_L['type'] == 'Systolic'] 
#                 self.df_L_d =  df_L[df_L['type'] == 'Diastolic'] 
#                 self.df_L_p =  df_L[df_L['type'] == 'Pulse']
                
                
#     def df_melt(self,dataset):
            
#         df_long = dataset.melt(
#             id_vars=['day', 'date', 'type'], 
#             value_vars=['morning', 'noon', 'night'],
#             var_name='time_of_day', 
#             value_name='measurement'
#         )
        
#         time_order = ['morning', 'noon', 'night']
#         df_long['time_of_day'] = pd.Categorical(df_long['time_of_day'], categories=time_order, ordered=True)

#         df_long = df_long.sort_values(by=['date', 'time_of_day']).reset_index(drop=True)
#         print(df_long)

#         return pd.DataFrame(df_long)   
    
    
#     def rename(self):
#         self.df_L_dt.rename(columns={'measurement': 'Diastolic'}, inplace)
#         self.df_L_st.rename(columns={'measurement': 'Systolic'})
#         sefl.df_L_pt.rename(columns={'measurement': 'Pulse'})



#     def merge(self):
#         dataframes = [df_L_st, df_L_pt]

#         df_L = pd.merge(df_L_dt, df_L_st, how='right', on=['date', 'time_of_day','day'])
#         df_L = pd.merge(df_L, df_L_pt, how='inner', on=['date', 'time_of_day','day'])
#         df_L.rename(columns= {'measurement': 'Pulse', 'measurement_x':'Diastolic', 'measurement_y':'Systolic'}, inplace=True)
#         df_L.drop(columns=['type_x', 'type_y', 'type'], inplace=True)
#         df_L = df_L.sort_values(by='date', ascending=False)
#         df_L
 
#     def Change_format(self):
    
#         df_L['day'] = pd.to_numeric(df_L['day'])
#         df_L['date'] = pd.to_datetime(df_L['date'], format='%Y/%m/%d')

        
#         df_R['day'] = pd.to_numeric(df_R['day'])
#         df_R['date'] = pd.to_datetime(df_R['date'], format='%Y/%m/%d')
        
        
        
        
        
        
        
        
# GAP gpt    
# import pandas as pd

# class Make_dataframe:
#     """
#     This class takes BP excel data and separates Right and Left arm
#     blood pressure measurements.
#     """

#     def __init__(self, df):
#         self.df = df.copy()
#         self.df_R = None
#         self.df_L = None

#     def decompose(self):
#         self.df['day'] = self.df['day'].ffill()
#         self.df['hand'] = self.df['hand'].ffill()
#         self.df['date'] = self.df['date'].ffill()
#         return self.df

#     def filter_hand(self):
#         self.df_R = self.df[self.df['hand'] == 'R'].drop(columns=['hand']).copy()
#         self.df_L = self.df[self.df['hand'] == 'L'].drop(columns=['hand']).copy()
#         return self.df_R, self.df_L

#     def df_melt(self, dataset):
#         df_long = dataset.melt(
#             id_vars=['day', 'date', 'type'],
#             value_vars=['morning', 'noon', 'night'],
#             var_name='time_of_day',
#             value_name='measurement'
#         )

#         time_order = ['morning', 'noon', 'night']
#         df_long['time_of_day'] = pd.Categorical(
#             df_long['time_of_day'],
#             categories=time_order,
#             ordered=True
#         )

#         df_long = df_long.sort_values(by=['date', 'time_of_day']).reset_index(drop=True)
#         return df_long

#     def prepare_side(self, side_df):
#         """
#         Converts one side dataframe into a combined table with:
#         day, date, time_of_day, Diastolic, Systolic, Pulse
#         """
#         long_df = self.df_melt(side_df)

#         # Split by type
#         df_d = long_df[long_df['type'] == 'Diastolic'].rename(columns={'measurement': 'Diastolic'})
#         df_s = long_df[long_df['type'] == 'Systolic'].rename(columns={'measurement': 'Systolic'})
#         df_p = long_df[long_df['type'] == 'Pulse'].rename(columns={'measurement': 'Pulse'})

#         # Keep only needed columns
#         base_cols = ['day', 'date', 'time_of_day']

#         df_final = df_d[base_cols + ['Diastolic']].merge(
#             df_s[base_cols + ['Systolic']],
#             on=base_cols,
#             how='outer'
#         ).merge(
#             df_p[base_cols + ['Pulse']],
#             on=base_cols,
#             how='outer'
#         )

#         df_final['day'] = pd.to_numeric(df_final['day'], errors='coerce')
#         df_final['date'] = pd.to_datetime(df_final['date'], errors='coerce')

#         df_final = df_final.sort_values(by=['date', 'time_of_day']).reset_index(drop=True)
#         return df_final

#     def process(self):
#         self.decompose()
#         self.filter_hand()

#         result_R = self.prepare_side(self.df_R)
#         result_L = self.prepare_side(self.df_L)

#         return result_R, result_L
