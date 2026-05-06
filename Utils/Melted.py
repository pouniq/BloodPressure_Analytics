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




class Make_dataframe:
    
    # ''''
    # In this class If you put any excel data,
    # You get the result of separated Right 
    # and Left Arms. with the blood pressure measurements

    # ''''
    import pandas as pd
    
    df = pd.read_excel('../Data/BP.xlsx')
    
    def __init__(self, df):
        df = df
        
        
    def Decompose(self):
        self.df['day'] = self.df['day'].ffill()
        self.df['hand'] = self.df['hand'].ffill()
        self.df['date'] = self.df['date'].ffill()
        
        
    def Filter_hand(self):
    
        hands = ['R','L']
        for hand in hands:
            if hand == 'R':
                df_R = self.df[self.df['hand'] == 'R']
                df_R = df_R.drop('hand' , axis=1)
                df_R_s = df_R[df_R['type'] == 'Systolic'] 
                df_R_d =  df_R[df_R['type'] == 'Diastolic'] 
                df_R_p =  df_R[df_R['type'] == 'Pulse']
            
            else:
                df_L = self.df[self.df['hand'] == 'L']
                df_L = df_L.drop('hand' , axis=1)
                df_L_s = df_L[df_L['type'] == 'Systolic'] 
                df_L_d =  df_L[df_L['type'] == 'Diastolic'] 
                df_L_p =  df_L[df_L['type'] == 'Pulse']
                
                
    def df_melt(self,dataset):
            
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
    
    
    def rename(self):
        pass
        
    
    def Change_format(self):
    
        df_L['day'] = pd.to_numeric(df_L['day'])
        df_L['date'] = pd.to_datetime(df_L['date'], format='%Y/%m/%d')

        
        df_R['day'] = pd.to_numeric(df_R['day'])
        df_R['date'] = pd.to_datetime(df_R['date'], format='%Y/%m/%d')