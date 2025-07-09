import matplotlib.pyplot as plt

def plot_hist(df, col, bins=20):
    df[col].hist(bins=bins)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()
