
# loading the data  and observe
import pandas as pd
tb_hindura =  pd.read_csv('data/bindura_tb_patients.csv')
tb_hindura.head()

# slice the dataframe into male_dataframe and female dataframe
male_hindura_df = tb_hindura.iloc[:,[i for i in range(21)]]
female_hindura_df = tb_hindura.iloc[:,[0]+[i for i in range(21,41)]]

# tidy the male dataframe

male_tidy_hindura_df = pd.melt(frame = male_hindura_df , id_vars='days', 
                               var_name='sex_label', value_name='Fatigue Level')
# tidy the female dataframe
female_tidy_hindura_df = pd.melt(frame = female_hindura_df , id_vars='days', 
                               var_name='sex_label', value_name='Fatigue Level')

#merge them into one big dataframe (you just learned how to use pd.concat method)
all_tidy_hindura_df = pd.concat([female_tidy_hindura_df,male_tidy_hindura_df] , axis=0)
