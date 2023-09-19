# load the data  and observe
covid_EA =  pd.read_csv('data/covid_eastafr.csv')
covid_EA.head()

# slice the dataframe into cases_dataframe and deaths dataframe
cases_covid_EA = covid_EA.iloc[:,[i for i in range(14)]]
deaths_covid_EA= covid_EA.iloc[:,[0]+[i for i in range(14,27)]]


# tidy the cases dataframe

cases_tidy_covid_EA = pd.melt(frame = cases_covid_EA , id_vars='Day', 
                               var_name='status_country', value_name='count')
# tidy the deaths dataframe
deaths_tidy_covid_EA = pd.melt(frame = deaths_covid_EA , id_vars='Day', 
                               var_name='status_country', value_name='count')

#merge them into one big dataframe (you just learned how to use pd.concat method)
all_tidy_covid_EA = pd.concat([cases_tidy_covid_EA,deaths_tidy_covid_EA] , axis=0)
