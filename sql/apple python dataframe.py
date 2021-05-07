import pandas as pd
import numpy as np

a = pd.DataFrame([['Canada', 'BC'], ['Canada', 'TO'], ['USA', 'WA'], ['USA', 'IL']], columns = ['country', 'state'])
b = pd.DataFrame([['BC', 100], ['TO', 200], ['WA', 96], ['IL', 78]], columns = ['state', 'population'])

print([len(a.country.unique()), len(a.state.unique())])

df = pd.merge(a,b, on = 'state')
country_population = df.groupby('country').agg({
    'population':np.sum
    })

# df.groupby('country').agg({
#     'population': 'sum'
# })

country_population.rename(columns = {"population": "country_population"}, inplace = True)
res = pd.merge(df, country_population, on = 'country')
res['percentage'] = res['population']/res['country_population']*100
res = res.sort_values(['country', 'percentage'], ascending = False)
res

# res.groupby('country').head(1).reset_index(drop=True)