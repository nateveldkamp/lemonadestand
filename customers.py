#%% imports
from faker import Faker
fake = Faker()

#%%
class Customer:
    def __init__(self):
        profile = fake.simple_profile()
        self.name = profile['name']
        self.gender = profile['sex']
        self.address = profile['address']
        self.email = profile['mail']
        self.dob = profile['birthdate']
        self.username = profile['username']
        self.job = fake.job()

#%%
def create_n_customers(n):
    return [ Customer() for i in range(0,n) ]

# %%
customers = create_n_customers(10)
print([i.name for i in customers])
