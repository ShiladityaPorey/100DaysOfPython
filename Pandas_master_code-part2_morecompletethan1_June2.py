"""
=========================================================
                PANDAS CHEAT SHEET
        (For Cosmology / HEP Phenomenology)
=========================================================
"""

import pandas as pd
import numpy as np

# =======================================================
# Create a DataFrame
# =======================================================

A = pd.DataFrame({
    "n_s": [0.95549, 0.96623, 0.95749,
            0.95987, 0.96211, 0.96423],

    "r": [8.50E-11, 6.44E-11, 8.11E-11,
          7.66E-11, 7.23E-11, 6.83E-11],

    "phi_end": [39.47, 52.04, 41.34,
                43.79, 46.38, 49.13]
})


# =======================================================
# Basic information
# =======================================================

print(A.shape)          # (rows, columns)
print(A.dtypes)         # data type of each column
print(A.columns)        # column names
print(A.describe())     # summary statistics

print(A.head())         # first 5 rows
print(A.tail())         # last 5 rows


# =======================================================
# Select columns
# =======================================================

print(A["r"])                  # one column
print(A[["r", "phi_end"]])     # multiple columns


# =======================================================
# Select rows
# =======================================================

print(A.iloc[0:5:2])           # integer indexing

A.index = ["a","b","c","d","e","f"]
print(A.loc[["a","d"]])        # label indexing


# =======================================================
# Filtering
# =======================================================

print(A[A["r"] > 7.6E-11])

print(
    A[
        (A["n_s"] > 0.956) &
        (A["r"] < 7.7E-11)
    ]
)

# Cleaner syntax
print(
    A.query("0.956 < n_s < 0.965")
)


# =======================================================
# Sorting
# =======================================================

print(
    A.sort_values("r", ascending=False)
)

print(
    A.sort_values(
        ["n_s","r"],
        ascending=[True,False]
    )
)


# =======================================================
# Add new columns
# =======================================================

A["epsilon"] = A["r"]/16

A["sqrt_r"] = np.sqrt(A["r"])

print(A)


# =======================================================
# Statistics
# =======================================================

print(A["r"].min())
print(A["r"].max())
print(A["r"].mean())

print(A.corr())          # correlation matrix


# =======================================================
# Drop rows / columns
# =======================================================

print(
    A.drop(columns=["sqrt_r"])
)

print(
    A.drop(index=["d"])
)


# =======================================================
# Missing values
# =======================================================

print(A.isna())

A = A.fillna(0)

print(A.dropna())


# =======================================================
# Rename columns
# =======================================================

A = A.rename(
    columns={"phi_end":"phi_f"}
)


# =======================================================
# Select rows + columns together
# =======================================================

print(
    A.loc[
        A["r"] < 7E-11,
        ["n_s","phi_f"]
    ]
)


# =======================================================
# Apply a custom function
# =======================================================

def slow_roll(r):
    return r/16

A["eps_apply"] = A["r"].apply(slow_roll)


# =======================================================
# Concatenate DataFrames
# =======================================================

new_point = pd.DataFrame({

    "n_s":[0.97126],
    "r":[5.48E-11],
    "phi_f":[40.60],
    "epsilon":[5.48E-11/16],
    "eps_apply":[5.48E-11/16]

})

COMB = pd.concat(
    [A, new_point],
    ignore_index=True
)

print(COMB)


# =======================================================
# Reset index
# =======================================================

COMB = COMB.reset_index(drop=True)


# =======================================================
# Remove duplicates
# =======================================================

print(COMB.duplicated())

COMB = COMB.drop_duplicates()


# =======================================================
# Random sample
# =======================================================

print(COMB.sample(3))


# =======================================================
# Largest / Smallest values
# =======================================================

print(COMB.nlargest(2,"n_s"))

print(COMB.nsmallest(2,"r"))


# =======================================================
# Merge two tables
# =======================================================

# scan.csv
# id  n_s  r

# chi2.csv
# id  chi2

# scan = pd.read_csv("scan.csv")
# chi2 = pd.read_csv("chi2.csv")

# merged = pd.merge(scan, chi2, on="id")


# =======================================================
# Group by
# =======================================================

# A["model"] = [
#     "Starobinsky",
#     "Starobinsky",
#     "Alpha",
#     "Alpha",
#     "T-model",
#     "T-model"
# ]

# print(A.groupby("model").mean())


# =======================================================
# Read / Write files
# =======================================================

# CSV
# A.to_csv("scan.csv", index=False)

# Read CSV
# A = pd.read_csv("scan.csv")

# Read whitespace-separated file
# A = pd.read_csv(
#     "scan.dat",
#     sep=r"\s+"
# )

# Save with scientific notation
# A.to_csv(
#     "scan.csv",
#     float_format="%.15E",
#     index=False
# )


# =======================================================
# Useful one-liners
# =======================================================

# A.columns
# A.shape
# A.head()
# A.tail()
# A.info()
# A.describe()
# A.value_counts()
# A.reset_index(drop=True)
# A.sample(5)