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
names = ["Accuracy", "Average Processing Time", "Efficiency"]
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
    plt.show()

# %%
