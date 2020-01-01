#%%
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from main import get_ls_results

#%%
df = pd.read_csv('data/lem_stand_results.csv')
df.head()

#%%
filtered = df[ df['GlassesSold'] > df['GlassesMade'] ]
filtered.head()

# %%
plt.scatter(filtered['GlassesSold'], filtered['PricePerGlass'])

# %%
X = df[['PricePerGlass']].values
y = df['GlassesSold'].values
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
print(X)
print(y)
# print(X_train)
# print(y_train)

# %%
regressor = LinearRegression()  
regressor.fit(X, y)
# regressor.fit(X_train, y_train)

print(regressor.coef_)

# %%
