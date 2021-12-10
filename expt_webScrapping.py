import pandas as pd 
Get_data=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
table = Get_data[0]
df =table 
#show unique economy sectors
sectors = df['GICS Sector'].values.tolist()
sectors = set(sectors)
sector_df = df[df['GICS Sector'] == 'Information technology']
sector_Symbols = sector_df['Symbol'].values.tolist()
names = sector_df['Security'].values.tolist()
sector_dict = dict(zip(sector_Symbols, names))
Company_names = sector_dict.keys()
company_ticker = sector_dict.values()
print(sector_dict, Company_names, company_ticker)