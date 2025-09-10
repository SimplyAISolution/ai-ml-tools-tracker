---
title: "Exploratory Data Analysis Assistant"
category: "data_science"
tags: ["eda", "statistics", "visualization", "pandas", "analysis"]
model_compatibility: ["gpt-4", "claude-3", "codellama", "gemini-pro"]
difficulty: "intermediate"
created_by: "AI Tools Tracker" 
created_at: "2024-01-01"
version: "1.0"
---

# Exploratory Data Analysis Assistant

## Description
Generates comprehensive Python code for exploratory data analysis including statistical summaries, visualizations, and insights for datasets.

## Prompt
```
I need to perform exploratory data analysis on a dataset. Please provide a comprehensive EDA script based on the following information:

**Dataset Description**: {dataset_description}
**File Format**: {file_format} (CSV, JSON, Excel, etc.)
**Key Columns**: {column_info}
**Analysis Goals**: {analysis_objectives}
**Specific Questions**: {research_questions}

Please generate Python code that includes:

### 1. Data Loading and Initial Inspection
- Load the dataset with appropriate libraries
- Display basic information (shape, dtypes, memory usage)
- Show first few rows and basic statistics

### 2. Data Quality Assessment
- Check for missing values and duplicates
- Identify data types and potential conversion needs
- Flag potential outliers or anomalies

### 3. Statistical Analysis
- Descriptive statistics for numerical columns
- Frequency distributions for categorical columns
- Correlation analysis between variables
- Distribution analysis (normality tests if relevant)

### 4. Visualizations
- Distribution plots for key variables
- Correlation heatmaps
- Box plots for outlier detection
- Categorical variable analysis
- Time series plots (if time data exists)

### 5. Key Insights and Recommendations
- Summary of findings
- Data quality issues to address
- Recommendations for further analysis
- Potential modeling considerations

Include proper imports, comments, and explanations for each step.
```

## Example Usage
```
Input:
- Dataset Description: E-commerce customer transaction data
- File Format: CSV
- Key Columns: customer_id, purchase_date, product_category, amount, age, gender
- Analysis Goals: Understand customer behavior and purchasing patterns
- Specific Questions: What drives higher spending? Are there seasonal trends?

Output:
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set plotting style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# 1. DATA LOADING AND INITIAL INSPECTION
print("=== DATA LOADING AND INITIAL INSPECTION ===")
df = pd.read_csv('ecommerce_transactions.csv')

print(f"Dataset shape: {df.shape}")
print(f"\nColumn types:\n{df.dtypes}")
print(f"\nMemory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
print(f"\nFirst 5 rows:\n{df.head()}")

# 2. DATA QUALITY ASSESSMENT
print("\n=== DATA QUALITY ASSESSMENT ===")
print(f"Missing values:\n{df.isnull().sum()}")
print(f"\nDuplicate rows: {df.duplicated().sum()}")

# Convert date column if needed
df['purchase_date'] = pd.to_datetime(df['purchase_date'])

# 3. STATISTICAL ANALYSIS
print("\n=== STATISTICAL ANALYSIS ===")
print("Numerical columns summary:")
print(df.describe())

print("\nCategorical columns frequency:")
for col in df.select_dtypes(include=['object']).columns:
    print(f"\n{col} distribution:")
    print(df[col].value_counts().head())

# Correlation analysis
numeric_cols = df.select_dtypes(include=[np.number]).columns
correlation_matrix = df[numeric_cols].corr()

# 4. VISUALIZATIONS
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Amount distribution
axes[0,0].hist(df['amount'], bins=50, alpha=0.7)
axes[0,0].set_title('Purchase Amount Distribution')
axes[0,0].set_xlabel('Amount')

# Age distribution
axes[0,1].hist(df['age'], bins=30, alpha=0.7)
axes[0,1].set_title('Customer Age Distribution')
axes[0,1].set_xlabel('Age')

# Category analysis
df['product_category'].value_counts().plot(kind='bar', ax=axes[0,2])
axes[0,2].set_title('Product Category Distribution')
axes[0,2].tick_params(axis='x', rotation=45)

# Correlation heatmap
sns.heatmap(correlation_matrix, annot=True, ax=axes[1,0], cmap='coolwarm')
axes[1,0].set_title('Correlation Matrix')

# Box plot for amounts by gender
df.boxplot(column='amount', by='gender', ax=axes[1,1])
axes[1,1].set_title('Purchase Amount by Gender')

# Monthly trends
monthly_sales = df.groupby(df['purchase_date'].dt.to_period('M'))['amount'].sum()
monthly_sales.plot(ax=axes[1,2])
axes[1,2].set_title('Monthly Sales Trends')

plt.tight_layout()
plt.show()

# 5. KEY INSIGHTS
print("\n=== KEY INSIGHTS ===")
print(f"Average purchase amount: ${df['amount'].mean():.2f}")
print(f"Most popular category: {df['product_category'].mode()[0]}")
print(f"Age range: {df['age'].min()} - {df['age'].max()} years")
print(f"Gender split: {df['gender'].value_counts(normalize=True)}")

# Statistical tests
male_amounts = df[df['gender'] == 'Male']['amount']
female_amounts = df[df['gender'] == 'Female']['amount']
t_stat, p_value = stats.ttest_ind(male_amounts, female_amounts)
print(f"\nGender spending difference (t-test p-value): {p_value:.4f}")

print("\n=== RECOMMENDATIONS ===")
print("1. Further investigate high-value customer segments")
print("2. Analyze seasonal patterns in more detail")
print("3. Consider customer lifetime value analysis")
print("4. Investigate product category preferences by demographics")
```
```

## Tips
- Adapt the code structure based on dataset size and complexity
- Include data validation steps for production environments
- Consider memory efficiency for large datasets
- Add interactive plots using plotly for better exploration
- Include feature engineering suggestions based on findings
- Provide actionable business insights, not just statistical summaries