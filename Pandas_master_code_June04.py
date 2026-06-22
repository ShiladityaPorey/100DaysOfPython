# ============================================================
#                 PANDAS FOR COSMOLOGY RESEARCH
# ============================================================
#
# June 04, 2026
# Learn:
#   DataFrame
#   Series
#   Column selection
#   Row selection (loc / iloc)
#   Filtering
#   Sorting
#   Statistics
#   Creating new columns
#   GroupBy
#   Missing values
#   CSV I/O
#   Concatenation
#
# Dataset resembles a typical inflation/reheating scan.
#
# ============================================================

import numpy as np
import pandas as pd

# ============================================================
# CREATE DATAFRAME
# ============================================================

df = pd.DataFrame({
    "ns"   : [0.964, 0.968, 0.971, 0.966, 0.963],
    "r"    : [8e-4, 4e-4, 2e-3, 7e-4, 1e-4],
    "Nreh" : [5, 5, 10, 15, 15],
    "mChi" : [1e10, 2e10, 5e9, 3e10, 8e9],
    "yChi" : [1e-8, 1e-10, 1e-12, 1e-9, 1e-11]
})

print("\nOriginal DataFrame")
print(df)

# ============================================================
# BASIC INFORMATION
# ============================================================


# DataFrame Structure
#
#                 columns
#                    ↓
#        +----------------------------+
#        | Name | Age | Salary | City |
# +------+----------------------------+
# |  0   |                           |
# |  1   |                           |
# |  2   |                           |
# |  3   |                           |
# |  4   |                           |
# +------+----------------------------+
#    ↑
#  index


print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nData types")
print(df.dtypes)

print("\nSummary statistics")
print(df.describe())
# DataFrame.describe() does not require the data to be sorted

# ============================================================
# COLUMN SELECTION
# ============================================================

print("\nColumn: ns")

ns_series = df["ns"]

print(ns_series)
print(type(ns_series))   # Series

print("\nTwo columns")

print(df[["ns", "r"]])

# ============================================================
# ROW SELECTION USING iloc
# ============================================================

print("\nFirst row")

print(df.iloc[0])

print("\nRows 0-2")

print(df.iloc[0:3])

print("\nElement [row=0, col=1]")

print(df.iloc[0, 1])

# ============================================================
# ROW SELECTION USING loc
# ============================================================

df.index = ["A", "B", "C", "D", "E"]

print("\nCustom index")

print(df)

print("\nRow A")

print(df.loc["A"])

print("\nRows A and D")

print(df.loc[["A", "D"]])

# ============================================================
# FILTERING
# ============================================================

print("\nr < 0.001")

print(df[df["r"] < 0.001])

print("\nPlanck-like region")

print(
    df[
        (df["ns"] > 0.962)
        &
        (df["ns"] < 0.970)
    ]
)

print("\nNreh = 15")

print(df[df["Nreh"] == 15])

# ============================================================
# SORTING
# ============================================================

print("\nSort by r")

print(df.sort_values("r"))

print("\nSort by mChi (largest first)")

print(
    df.sort_values(
        "mChi",
        ascending=False
    )
)

# ============================================================
# CREATE NEW COLUMNS
# ============================================================

print("\nCreate derived quantities")

df["log10_mChi"] = np.log10(df["mChi"])

df["log10_yChi"] = np.log10(df["yChi"])

print(df)

# ============================================================
# SIMPLE STATISTICS
# ============================================================

print("\nMean r")

print(df["r"].mean())

print("\nMaximum mChi")

print(df["mChi"].max())

print("\nMinimum mChi")

print(df["mChi"].min())

# ============================================================
# UNIQUE VALUES
# ============================================================

print("\nUnique reheating e-folds")

print(df["Nreh"].unique())

# ============================================================
# GROUPBY
# ============================================================

print("\nAverage mChi for each Nreh")

print(
    df.groupby("Nreh")["mChi"].mean()
)

print("\nNumber of points for each Nreh")

print(
    df.groupby("Nreh")["ns"].count()
)

# ============================================================
# MISSING VALUES
# ============================================================

print("\nInsert missing value")

df.loc["B", "mChi"] = np.nan

print(df)

print("\nMissing value count")

print(df.isna().sum())

print("\nFill missing values")

df["mChi"] = df["mChi"].fillna(0)

print(df)

# ============================================================
# DROP COLUMN
# ============================================================

print("\nDrop column")

print(
    df.drop(columns=["log10_yChi"])
)

# ============================================================
# DROP ROW
# ============================================================

print("\nDrop row")

print(
    df.drop(index=["C"])
)

# ============================================================
# CONCATENATE DATAFRAMES
# ============================================================

print("\nConcatenate")

extra = pd.DataFrame({
    "ns"   : [0.967],
    "r"    : [3e-4],
    "Nreh" : [20],
    "mChi" : [9e10],
    "yChi" : [1e-13],
    "log10_mChi" : [np.log10(9e10)],
    "log10_yChi" : [np.log10(1e-13)]
})

combined = pd.concat([df, extra], ignore_index=True)

print(combined)

# ============================================================
# SAVE TO CSV
# ============================================================

combined.to_csv(
    "scan_results.csv",
    index=False
)

print("\nSaved: scan_results.csv")

# ============================================================
# READ CSV
# ============================================================

loaded = pd.read_csv(
    "scan_results.csv"
)

print("\nLoaded from CSV")

print(loaded.head())

# ============================================================
# MOST COMMON RESEARCH WORKFLOW
# ============================================================

print("\nViable parameter space")

viable = loaded[
    (loaded["r"] < 0.001)
    &
    (loaded["ns"] > 0.962)
    &
    (loaded["ns"] < 0.970)
]

print(viable)

print("\nNumber of viable points")

print(len(viable))

# ============================================================
# END
# ============================================================