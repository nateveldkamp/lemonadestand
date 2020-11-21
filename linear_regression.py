#%%
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.model_selection import train_test_split 
# from sklearn.linear_model import LinearRegression

#%%
df = pd.read_csv('data/ls_results.csv')
df.head()

#%%
filtered = df[ df['GlassesSold'] < df['GlassesMade'] ]
filtered = filtered[ filtered['StreetCrewWorking'] == False]
filtered = filtered[ filtered['SignsMade'] == 0]
filtered = filtered[ filtered['Weather'] == 'Sunny']
filtered = filtered[['GlassesSold','PricePerGlass','Weather']]
filtered.head()

#%%
filtered = filtered.drop_duplicates()
filtered.count()

# %%
sns.scatterplot(x='PricePerGlass', y='GlassesSold', hue="Weather", data=filtered)

# %%
X = filtered[['PricePerGlass']].values
y = filtered['GlassesSold'].values
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# print(X)
# print(y)
# print(X_train)
# print(y_train)

# %%
regressor = LinearRegression()  
regressor.fit(X, y)
# regressor.fit(X_train, y_train)
coefficient = round(regressor.coef_[0],2)
intercept = round(regressor.intercept_,2)
print(f'y={coefficient}x+{intercept}')

# %%
plt.scatter(X, y)
plt.plot(X, regressor.predict(X),color='k')
plt.show()

# %%
# regressor.predict(filtered[['PricePerGlass']])
filtered['Prediction'] = regressor.predict(filtered[['PricePerGlass']])
filtered

# %%
sns.scatterplot(x='PricePerGlass', y='GlassesSold', hue="Weather", data=filtered)
sns.lineplot(x='PricePerGlass', y='Prediction', data=filtered)
