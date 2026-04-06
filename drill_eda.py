"""Core Skills Drill — Descriptive Analytics

Compute summary statistics, plot distributions, and create a correlation
heatmap for the sample sales dataset.

Usage:
    python drill_eda.py
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def compute_summary(df):
    summary = df.describe()
    summary.loc['median'] = df.median(numeric_only=True)    
    summary = summary.loc[['count', 'mean', 'median', 'std', 'min', 'max']]
    summary.to_csv("output/summary.csv")
    return summary
  


def plot_distributions(df, columns, output_path):
   
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten() 
    for i, col in enumerate(columns):
        sns.histplot(df[col], kde=True, ax=axes[i])
        axes[i].set_title(f'Distribution of {col}')
    
    plt.tight_layout()
    plt.savefig(output_path)


def plot_correlation(df, output_path):
   numeric_df = df.select_dtypes(include=[np.number])
   corr_matrix = numeric_df.corr()
   plt.figure(figsize=(8, 6))
   sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
   plt.title('Correlation Heatmap')
   plt.tight_layout()
   plt.savefig(output_path)


def main():
    """Load data, compute summary, and generate all plots."""
    os.makedirs("output", exist_ok=True)

    df = pd.read_csv("data/sample_sales.csv")   
    compute_summary(df)
    print("Success: summary.csv is now in the output folder!")


    cols_to_plot = ['quantity', 'unit_price', 'quantity', 'unit_price']
    print("Success: distributions.png is now in the output folder!")


    plot_correlation(df, "output/correlation.png")
    
    print("All Tasks Complete! Success: correlation.png is in the output folder.")
    # TODO: Call plot_correlation


if __name__ == "__main__":
    main()