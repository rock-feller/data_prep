
billboard = pd.read_csv('data/billboard_2000.csv')
pd.melt(billboard,
        id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
        value_name='rank', var_name='week')
