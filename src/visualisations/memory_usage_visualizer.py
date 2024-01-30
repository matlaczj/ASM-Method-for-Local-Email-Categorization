# %%
import matplotlib.pyplot as plt
import numpy as np

data = {
    "512 MB": {"Usage": 2.54, "Change": +0.16},
    "1 GB": {"Usage": 7.34, "Change": -0.03},
    "2 GB": {"Usage": 4.94, "Change": -0.15},
    "3 GB": {"Usage": 1.87, "Change": -0.06},
    "4 GB": {"Usage": 10.36, "Change": -0.45},
    "6 GB": {"Usage": 15.76, "Change": -0.57},
    "8 GB": {"Usage": 31.67, "Change": +0.44},
    "10 GB": {"Usage": 3.33, "Change": 0.00},
    "11 GB": {"Usage": 1.76, "Change": -0.06},
    "12 GB": {"Usage": 15.23, "Change": +0.92},
    "16 GB": {"Usage": 1.67, "Change": +0.12},
    "24 GB": {"Usage": 2.54, "Change": -0.04},
    "Other": {"Usage": 0.97, "Change": +0.46},
}

categories = list(data.keys())
usage = [item["Usage"] for item in data.values()]

fig, ax1 = plt.subplots(figsize=(4, 3))  # Smaller figure size

# Increase bar width for better visibility in a compact plot
ax1.bar(categories, usage, color="blue", alpha=0.7, label="Usage (%)", width=0.6)

# Increase font size for better visibility
ax1.set_xlabel("Memory Size", fontsize=12)
ax1.set_ylabel("Usage (%)", color="blue", fontsize=12)
ax1.tick_params("y", colors="blue", labelsize=10)

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45, ha="right")

# Create a secondary y-axis for the cumsum plot
ax2 = ax1.twinx()
ax2.plot(
    categories,
    np.cumsum(usage),
    color="dodgerblue",
    marker="o",
    label="Cumulative Usage (%)",
)
ax2.set_ylabel("Cumulative Usage (%)", color="dodgerblue", fontsize=12)
ax2.tick_params("y", colors="dodgerblue", labelsize=10)

fig.suptitle(
    "VRAM Memory Usage Distribution",
    fontsize=10,
)

plt.tight_layout()  # Adjust layout for better visibility

plt.savefig(
    "VRAM Memory Usage.svg",
    format="svg",
    bbox_inches="tight",
    transparent=True,
)
plt.show()  # %%

# %%
