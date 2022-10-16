
# import pandas as pd
# df = pd.read_csv('data/King_County_House_prices_dataset.csv')
# focus on the lower 50% percentile, excluded two zip code
# defind lowest n mean value of houses, 68 zip code when p = 50
def find_cheaper_area(df, n): # p low percentile of the market price, n number of zip code of lower price mean
    df_price50 = df[df.price<df.price.describe()['50%']]    
    df_chp_area = df_price50[df_price50.zipcode.isin(zip_chp)]
    return df_chp_area