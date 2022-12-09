import pandas as pd
import matplotlib.pyplot as plt


def lag_plots(s: pd.Series, n_lag: int):
    """
    Based on https://www.folkstalk.com/2022/09/dynamic-subplots-matplotlib-with-code-examples.html
    :param s: time series
    :return:
    """
    total = n_lag
    cols = 3

    # Compute Rows required
    rows = total // cols
    rows += total % cols

    # Create a Position index
    position = range(1, total + 1)

    # Create main figure
    fig = plt.figure(1)
    for k in range(total):
        # add every single subplot to the figure with a for loop

        ax = fig.add_subplot(rows, cols, position[k])
        pd.plotting.lag_plot(s, lag=k)
    plt.show()


if __name__ == '__main__':

    df = pd.read_csv(
        './utils/data/andes.csv',
        sep=';',
        parse_dates=['STARTDATE'],
        date_parser=lambda x: pd.to_datetime(x, format="%Y-%m-%d")
    )

    lag_plots(df['VOLUMEN'], n_lag=10)
