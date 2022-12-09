import pandas as pd


if __name__ == '__main__':

    df = pd.read_csv(
        './utils/data/andes.csv',
        sep=';',
        parse_dates=['STARTDATE'],
        date_parser=lambda x: pd.to_datetime(x, format="%Y-%m-%d")
    )

    pd.plotting.autocorrelation_plot(df['VOLUMEN'])
