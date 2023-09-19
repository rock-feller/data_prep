df = pd.DataFrame(np.random.randint(145,457, size=(30,27)))
df.columns = ['Day']+Cols1 +Cols2
df['Day'] = pd.to_datetime(date_range)
df.head()
