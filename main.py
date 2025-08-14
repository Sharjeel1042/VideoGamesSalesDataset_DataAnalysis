import numpy as np
import pandas as pd

def clean_df(df):
    df.columns = df.columns.str.strip().str.lower()

    df['name'] = df['name'].fillna('Unknown')
    df['platform'] = df['platform'].fillna('Unknown')
    df['publisher'] = df['publisher'].fillna('Unknown')
    df['na_sales'] = df['na_sales'].fillna(0)
    df['eu_sales'] = df['eu_sales'].fillna(0)
    df['jp_sales'] = df['jp_sales'].fillna(0)
    df['other_sales'] = df['other_sales'].fillna(0)
    df['global_sales'] = df['global_sales'].fillna(0)
    df['critic_score'] = df['critic_score'].fillna(0)
    df['critic_count'] = df['critic_count'].fillna(0)
    df['user_score'] = df['user_score'].fillna(0)
    df['user_count'] = df['user_count'].fillna(0)
    df['developer'] = df['developer'].fillna('N/A')
    df['rating'] = df['rating'].fillna('N/A')

    df['year_of_release'] = pd.to_numeric(df['year_of_release'], errors='coerce').astype('Int64')
    return df

if __name__ == "__main__":
    df = pd.read_csv('Video_Games_Sales.csv')
    df = clean_df(df)
    dfNonTime = df.dropna(subset=['genre'])
    df.to_csv('Non-TimeAnalysis.csv', index=False)
    dfTime = df.dropna(subset=['year_of_release'])
    dfTime.to_csv('Time-BasedAnalysis.csv', index=False)

dfNonTime = clean_df(pd.read_csv('Non-TimeAnalysis.csv'))
dfTime = clean_df(pd.read_csv('Time-BasedAnalysis.csv'))