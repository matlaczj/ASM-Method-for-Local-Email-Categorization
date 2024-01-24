# %%
import pandas as pd
import random

# %%
df = pd.read_csv(
    r"C:\Users\username\Documents\Repozytoria\LM-Based-Email-Categorization-for-User-Defined-Labels\data\dataset.csv"
)


# %%
def add_possible_categories(df, max_categories_to_sample=10):
    unique_categories = list(df["actual_category"].unique())
    min_categories_to_sample = 5

    df["possible_categories"] = df["actual_category"].apply(
        lambda x: random.sample(
            unique_categories,
            random.randint(min_categories_to_sample, max_categories_to_sample),
        )
    )
    df["possible_categories"] = df.apply(
        lambda x: x["possible_categories"] + [x["actual_category"]], axis=1
    )
    df["possible_categories"] = df["possible_categories"].apply(lambda x: list(set(x)))

    df["possible_categories"] = df["possible_categories"].apply(
        lambda x: random.sample(x, len(x))
    )
    return df


# %%
dfex = add_possible_categories(df)

# %%
dfex.to_csv(
    r"C:\Users\username\Documents\Repozytoria\LM-Based-Email-Categorization-for-User-Defined-Labels\data\dataset_with_possible_categories.csv"
)
# %%
