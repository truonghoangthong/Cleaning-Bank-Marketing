import pandas as pd
import numpy as np

df = pd.read_csv("bank_marketing.csv")
df['month'] = pd.to_datetime(df['month'], format='%b').dt.month
client = df[['client_id','age','job','marital','education','credit_default','mortgage']]
client['credit_default'] = client['credit_default'].replace({'yes':1,'no':0,'unknown':0}).astype(bool)
client['mortgage'] = client['mortgage'].replace({'yes':1,'no':0,'unknown':0}).astype(bool)
client['job'] = client['job'].str.replace('.','_')
client['education'] =client['education'].str.replace('unknown','np.NaN')
client['education'] = client['education'].str.replace('.','_')
read = client.to_csv('client.csv',index=False)
print(client['education'])

campaign = df[['client_id','number_contacts','contact_duration','previous_campaign_contacts','previous_outcome','campaign_outcome']]
campaign['previous_outcome'] = campaign['previous_outcome'].replace({'success':1,'failure':0,'nonexistent':0}).astype(bool)
campaign['campaign_outcome'] = campaign['campaign_outcome'].replace({'yes':1,'no':0}).astype(bool)
campaign['last_contact_date'] = pd.to_datetime({'year': 2020, 'month': df['month'], 'day': df['day']})
read = campaign.to_csv('campaign.csv',index=False)

economics = df[['client_id','cons_price_idx','euribor_three_months']]
read = economics.to_csv('economics.csv',index=False)