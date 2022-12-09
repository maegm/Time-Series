import pandas as pd
import seaborn as sns


if __name__ == '__main__':
    df = pd.read_csv(
        './utils/data/andes.csv',
        sep=';',
        parse_dates=['STARTDATE'],
        date_parser=lambda x: pd.to_datetime(x, format="%Y-%m-%d")
    )
    sns.pairplot(df)    # Scatter matrix
    pd.plotting.lag_plot(df['VOLUMEN'], lag=1)
