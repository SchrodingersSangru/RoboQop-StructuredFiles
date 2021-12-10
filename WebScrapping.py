import pandas as pd
## This Program file is written to webscrap the tickers of specific indices. 
## Every Index has a specific class, in which methods are written to get the coreect tickers.
## also there are functions for extracting Sector_wise tickers, Industrials, IT, Automobile.


class SP500:
#for the S&P500 tickers 
    
    
    
    def SP500_tickers_sector_wise():
        # for extracting the tickers of some specific sectos
        import pandas as pd 
        Get_data=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
        df = Get_data[0]
        sector_df = df[df['GICS Sector'] == 'Information Technology'] 
        sector_Symbols = sector_df['Symbol'].values.tolist()
        names = sector_df['Security'].values.tolist()
        sector_dict = dict(zip(sector_Symbols, names))
        Sector_df= pd.DataFrame.from_dict(sector_dict, orient ='index')
        Sector_df.columns = ['comapny_name']
        Sector_df.index.name = 'tickers'
        Sector_df.reset_index(level=0, inplace=True)
        return Sector_df
        
        
        
class dow:
    
    #For extracting the data of dow indices. 
    #there are multiple dow indices, which are there in the market, so have to write method ofr each of that. 
    
    def dow_tickers():
        Get_data=pd.read_html('https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average')
        df = Get_data[1]
        sector_df = df[df['Industry'] == 'Information technology']
        sector_Symbols = sector_df['Symbol'].values.tolist()
        names = sector_df['Company'].values.tolist()
        sector_dict = dict(zip(sector_Symbols, names))
        Sector_df= pd.DataFrame.from_dict(sector_dict, orient ='index')
        Sector_df.columns = ['comapny_name']
        Sector_df.index.name = 'tickers'
        Sector_df.reset_index(level=0, inplace=True)
        return Sector_df


class Nifty50:
    
    #to get the data of tickers in the Nifty50 index.
    
    def Nifty50_tickers():
        Get_data=pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50')
        df = Get_data[1]
        #add the setor name here to get the data of specific sector. 
        sector_df = df[df['Sector'] == 'Automobile']
        sector_Symbols = sector_df['Symbol'].values.tolist()
        names = sector_df['Company Name'].values.tolist()
        sector_dict = dict(zip(sector_Symbols, names))
        Sector_df= pd.DataFrame.from_dict(sector_dict, orient ='index')
        Sector_df.columns = ['comapny_name']
        Sector_df.index.name = 'tickers'
        Sector_df.reset_index(level=0, inplace=True)
        return Sector_df
        
        
class BSE:
    #for extracting the BSE data. 

    
    def BSE_tickers():    
        Get_data=pd.read_html('https://en.wikipedia.org/wiki/List_of_BSE_SENSEX_companies')
        df = Get_data[0]
        #add the setor name here to get the data of specific sector. 
        sector_df = df[df['Sector'] == 'Automobile']
        sector_Symbols = sector_df['Symbol'].values.tolist()
        names = sector_df['Companies'].values.tolist()
        sector_dict = dict(zip(sector_Symbols, names))
        Sector_df= pd.DataFrame.from_dict(sector_dict, orient ='index')
        Sector_df.columns = ['comapny_name']
        Sector_df.index.name = 'tickers'
        Sector_df.reset_index(level=0, inplace=True)
        return Sector_df
