# %%
import matplotlib.pyplot as plt
import numpy as np

# Data about techniques and models
techniques = [
    "COT_1",
    "COT_2",
    "IO_1",
    "IO_1 W/ CS-5",
    "COT_3",
    "3-SHOT COT_3",
    "3-SHOT COT_1",
    "3-SHOT COT_4",
]

models = [
    "DOLPHIN MISTRAL 2.0 7B",
    "MISTRAL INSTRUCT 0.2 7B",
    "MISTRAL OPENORCA 7B",
    "OPENHERMES MISTRAL 2.5 7B",
    "PHI 2 3B",
]

# Data for the correctness plot

correctness_values = [
    [0.89, 0.9, 0.88, 0.97, 0.54],
    [0.37, 0.74, 0.65, 0.44, 0.72],
    [0.53, 0.79, 0.16, 0.62, 0.55],
    [0.59, 0.76, 0.14, 0.67, 0.56],
    [0.84, 0.92, 0.89, 0.78, 0.13],
    [0.91, 0.91, 0.77, 0.88, 0.12],
    [0.84, 0.92, 0.82, 0.93, 0.2],
    [0.93, 0.89, 0.69, 0.91, 0.18],
]

# Data for the elapsed time plot

elapsed_time_values = [
    [773.32, 987.69, 871.17, 840.02, 569.82],
    [1081.82, 817.19, 861.69, 825.72, 437.53],
    [36.67, 36.08, 36.58, 36.42, 30.26],
    [144.64, 138.35, 142.22, 136.09, 131.97],
    [527.85, 728.00, 893.92, 1246.49, 1396.63],
    [503.23, 571.55, 721.96, 705.70, 1367.18],
    [712.41, 715.82, 752.36, 706.91, 835.86],
    [610.69, 730.60, 940.21, 840.78, 1032.30],
]

# Create a numpy array for the correctness values
correctness_array = np.array(correctness_values)

# Create a numpy array for average elapsed time values
average_elapsed_time_values_array = (np.array(elapsed_time_values) / 100).round(2)

# Create a numpy array for the efficiency values
efficiency_array = (correctness_array / average_elapsed_time_values_array).round(2)

# %%

arrays = [correctness_array, average_elapsed_time_values_array, efficiency_array]
names = ["Accuracy", "Processing Time", "Efficiency"]
color_palettes = ["YlGn", "YlOrRd", "YlGnBu"]

for array, name, palette in zip(arrays, names, color_palettes):
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    # NOTE: Logarithm is used for the efficiency plot only!
    im = ax.imshow(
        np.log(array) if name in ["Efficiency"] else array,
        cmap=palette,
    )

    # Set ticks and labels
    ax.set_xticks(np.arange(len(models)))
    ax.set_yticks(np.arange(len(techniques)))
    ax.set_xticklabels(models)
    ax.set_yticklabels(techniques)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(techniques)):
        for j in range(len(models)):
            text = ax.text(
                j,
                i,
                f"{array[i, j]:.2f}",
                ha="center",
                va="center",
                color="black",
            )

    ax.set_title(f"{name} Values for \nDifferent Techniques and Models")
    fig.tight_layout()
    # Save the plot as a svg file
    plt.savefig(f"{name}.svg", format="svg", bbox_inches="tight", transparent=True)
    # Save as pdf
    plt.savefig(f"{name}.pdf", format="pdf", bbox_inches="tight", transparent=True)
    plt.show()

# %%
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Calculate means
correctness_means = correctness_array.mean(axis=1)
elapsed_time_means = average_elapsed_time_values_array.mean(axis=1)
efficiency_means = efficiency_array.mean(axis=1)

# Define the number of groups and the number of bars per group
num_groups = len(techniques)
num_bars = 3

# Define the width of each bar and the positions of the bars
bar_width = 0.27
bar_positions = np.arange(num_groups)

# Create a grouped bar chart with a white background
fig, ax1 = plt.subplots(figsize=(7, 5))

# Add bars for correctness
rects1 = ax1.bar(
    bar_positions - bar_width,
    correctness_means,
    bar_width,
    label="Average Correctness",
    color="green",
    alpha=0.7,
)
ax1.set_ylabel("Average Correctness", color="green", weight="bold", fontsize=12)
ax1.tick_params(axis="y", labelcolor="green")

# Add average line for correctness
ax1.axhline(y=correctness_means.mean(), color="green", linestyle="--", linewidth=0.5)

# Create second y-axis for elapsed time
ax2 = ax1.twinx()
rects2 = ax2.bar(
    bar_positions,
    elapsed_time_means,
    bar_width,
    label="Average Elapsed Time",
    color="orange",
    alpha=0.7,
)
ax2.set_ylabel("Average Elapsed Time", color="orange", weight="bold", fontsize=12)
ax2.tick_params(axis="y", labelcolor="orange")

# Add average line for elapsed time
ax2.axhline(y=elapsed_time_means.mean(), color="orange", linestyle="--", linewidth=0.5)

# Create third y-axis for efficiency
ax3 = ax1.twinx()
rects3 = ax3.bar(
    bar_positions + bar_width,
    efficiency_means,
    bar_width,
    label="Average Efficiency",
    color="blue",
    alpha=0.7,
)
ax3.set_ylabel("Average Efficiency", color="blue", weight="bold", fontsize=12)
ax3.tick_params(axis="y", labelcolor="blue")

# Add average line for efficiency
ax3.axhline(y=efficiency_means.mean(), color="blue", linestyle="--", linewidth=0.5)

# Move the third y-axis to the left
ax3.spines["right"].set_position(("outward", 60))

# Remove the spines
ax1.spines["top"].set_visible(False)
ax2.spines["top"].set_visible(False)
ax3.spines["top"].set_visible(False)

# Add labels, title, and legend
ax1.set_xlabel("Technique", fontsize=12)
ax1.set_title(
    "Average Values by Technique",
    fontsize=12,
)
ax1.set_xticks(bar_positions)
ax1.set_xticklabels(techniques)
plt.setp(
    ax1.get_xticklabels(),
    rotation=45,
    horizontalalignment="right",
    weight="bold",
    fontsize=10,
)

# Remove the grid
ax1.grid(False)
ax2.grid(False)
ax3.grid(False)

# Add bars for correctness with shadows
ax1.bar(
    bar_positions - bar_width,
    correctness_means,
    bar_width,
    color="black",
    alpha=0.1,
    align="edge",
)
rects1 = ax1.bar(
    bar_positions - bar_width,
    correctness_means,
    bar_width,
    label="Average Correctness",
    color="green",
    alpha=0.7,
)

# Add bars for elapsed time with shadows
ax2.bar(
    bar_positions, elapsed_time_means, bar_width, color="black", alpha=0.1, align="edge"
)
rects2 = ax2.bar(
    bar_positions,
    elapsed_time_means,
    bar_width,
    label="Average Elapsed Time",
    color="orange",
    alpha=0.7,
)

# Add bars for efficiency with shadows
ax3.bar(
    bar_positions + bar_width,
    efficiency_means,
    bar_width,
    color="black",
    alpha=0.1,
    align="edge",
)
rects3 = ax3.bar(
    bar_positions + bar_width,
    efficiency_means,
    bar_width,
    label="Average Efficiency",
    color="blue",
    alpha=0.7,
)

# Show the plot
plt.tight_layout()

# Save the plot as a svg file
plt.savefig("Average Values by Technique.svg", format="svg", bbox_inches="tight")

# Save the plot as a png file
plt.savefig("Average Values by Technique.png", format="png", bbox_inches="tight")

# Save as pdf
plt.savefig("Average Values by Technique.pdf", format="pdf", bbox_inches="tight")

plt.show()
# %%
