import matplotlib.pyplot as plt

# To make line chart for golf scores
def line_scores(df):
    plt.figure()
    plt.plot(df["round"], df["score"], marker="o")
    plt.title("Golf Round Scores")
    plt.xlabel("Round #")
    plt.ylabel("Score")
    plt.tight_layout()
    plt.savefig("data/processed/scores_line.png", dpi=200)

# Scatter chart for wind vs score
def scatter_wind_vs_score(df):
    plt.figure()
    plt.scatter(df["windmax"], df["score"])
    plt.title("Wind Speed vs Score")
    plt.xlabel("Max Wind (m/s)")
    plt.ylabel("Score")
    plt.tight_layout()
    plt.savefig("data/processed/wind_vs_score.png", dpi=200)
