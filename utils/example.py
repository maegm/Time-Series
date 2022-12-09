# Credit to
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def trend(time, slope=0):
    return slope * time


def seasonal_pattern(season_time):
    """Just an arbitrary pattern, you can change it if you wish"""
    return np.where(season_time < 0.4,
                    np.cos(season_time * 2 * np.pi),
                    1 / np.exp(3 * season_time))


def seasonality(time, period, amplitude=1, phase=0):
    """Repeats the same pattern at each period"""
    season_time = ((time + phase) % period) / period
    return amplitude * seasonal_pattern(season_time)


def white_noise(time, noise_level=1, seed=None):
    rnd = np.random.RandomState(seed)
    return rnd.randn(len(time)) * noise_level


def generate_time_series(days: int, slope: float, baseline: float, noise_level: int, amplitude: int):
    time = np.arange(days)
    series = baseline + trend(time, slope) + seasonality(time, period=365, amplitude=amplitude)
    noise = white_noise(time, noise_level)

    series += noise
    df = pd.DataFrame(data={'TIME': time, 'TIME_SERIES': series})
    return df


def plot_series(time, series, format="-", start=0, end=None, label=None):
    plt.figure(figsize=(10, 6))
    plt.plot(time[start:end], series[start:end], format, label=label)
    plt.xlabel("Time")
    plt.ylabel("Value")
    if label:
        plt.legend(fontsize=14)
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    days = 365*4 + 1
    slope = 0.05
    baseline = 10
    noise_level = 5
    amplitude = 40
    df = generate_time_series(days, slope, baseline, noise_level, amplitude)
    plot_series(df['TIME'], df['TIME_SERIES'])

    df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv', parse_dates=['date'])
    plot_series(df['date'], df['value'])