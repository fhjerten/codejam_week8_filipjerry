import random
import pandas as pd

# Make random golf round data
def simulate_golf_rounds(n_rounds=30, par=72, seed=42):
    """Generate fake golf round data with random scores."""

# Set random seed for repeatable results
    random.seed(seed)

# Make random scores around par
    scores = [par + random.randint(-3, 6) for _ in range(n_rounds)]

# Make strokes gained values
    strokes_gained = []
    sg = 0.0
    for _ in range(n_rounds):
        sg += random.uniform(-1.0, 1.0)
        strokes_gained.append(sg)

# Return data as a dataframe
    return pd.DataFrame({
        "round": range(1, n_rounds + 1),
        "score": scores,
        "strokes_gained": strokes_gained
    })
