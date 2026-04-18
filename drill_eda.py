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
    """حساب الإحصائيات الوصفية وحفظها في ملف CSV"""
    summary = df.describe()
    summary.loc['median'] = df.median(numeric_only=True)    
    summary = summary.loc[['count', 'mean', 'median', 'std', 'min', 'max']]
    summary.to_csv("output/summary.csv")
    return summary

def plot_distributions(df, columns, output_path):
    """رسم توزيع البيانات للأعمدة المحددة"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten() 
    for i, col in enumerate(columns):
        sns.histplot(df[col], kde=True, ax=axes[i])
        axes[i].set_title(f'Distribution of {col}')
    
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close() # لإغلاق الشكل وتوفير الذاكرة

def plot_correlation(df, output_path):
    """رسم خريطة الارتباط Heatmap"""
    numeric_df = df.select_dtypes(include=[np.number])
    corr_matrix = numeric_df.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def main():
    """Load data, compute summary, and generate all plots."""
    # التأكد من وجود مجلد output
    os.makedirs("output", exist_ok=True)

    # تحميل البيانات (تأكد أن الملف موجود في مجلد data)
    try:
        df = pd.read_csv("data/sample_sales.csv")
    except FileNotFoundError:
        print("Error: ملف data/sample_sales.csv غير موجود!")
        return

    # 1. تشغيل حساب الملخص
    compute_summary(df)
    print("Success: summary.csv is now in the output folder!")

    # 2. تشغيل رسم التوزيعات (هنا تم استدعاء الدالة)
    cols_to_plot = ['quantity', 'unit_price', 'quantity', 'unit_price']
    plot_distributions(df, cols_to_plot, "output/distributions.png")
    print("Success: distributions.png is now in the output folder!")

    # 3. تشغيل رسم الارتباط
    plot_correlation(df, "output/correlation.png")
    print("Success: correlation.png is now in the output folder!")
    
    print("\n--- All Tasks Complete! Check your 'output' folder ---")

if __name__ == "__main__":
    main()