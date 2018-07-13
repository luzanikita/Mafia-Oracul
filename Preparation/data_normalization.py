import pandas as pd

def to_normal(series):
    min_ = series.min()
    max_ = series.max()
    series = (series - min_) / (max_ - min_)
    
    return series

def main():
    players_stats = pd.read_csv('../Data/stats.csv')

    normal_stats = players_stats\
        .iloc[:,2:]\
        .transform(to_normal)  
    
    players_stats = pd.concat(
        [players_stats['Name'], normal_stats],
        axis=1)

    players_stats.to_csv('Data/normal_stats.csv')

if __name__ == '__main__':
    main()