import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(
    page_title="Student Result Analysis",
    page_icon="📊",
    layout="wide"
)

# Load dataset
df = pd.read_csv("Expanded_data_with_more_features.csv")

# Remove unnecessary column if it exists
if "Unnamed: 0" in df.columns:
    df = df.drop("Unnamed: 0", axis=1)

# Clean weekly study hours
if "WklyStudyHours" in df.columns:
    df["WklyStudyHours"] = df["WklyStudyHours"].str.strip()

# Title
st.title("📊 Student Result Analysis")
st.write(
    "An interactive analysis of student academic performance "
    "using Python, Pandas, Matplotlib and Seaborn."
)

# Dataset overview
st.header("Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Students", len(df))

with col2:
    st.metric("Total Columns", len(df.columns))

with col3:
    st.metric(
        "Average Math Score",
        round(df["MathScore"].mean(), 2)
    )

# Show dataset
st.subheader("Student Dataset")
st.dataframe(df)

# Gender Distribution
st.header("Gender Distribution")

fig, ax = plt.subplots(figsize=(6, 4))

sns.countplot(data=df, x="Gender", ax=ax)

for container in ax.containers:
    ax.bar_label(container)

ax.set_title("Gender Distribution")

st.pyplot(fig)

# Parent Education Analysis
st.header("Parent Education vs Student Scores")

gb = df.groupby("ParentEduc").agg({
    "MathScore": "mean",
    "ReadingScore": "mean",
    "WritingScore": "mean"
})

st.dataframe(gb)

fig, ax = plt.subplots(figsize=(8, 5))

sns.heatmap(gb, annot=True, fmt=".2f", ax=ax)

ax.set_title("Parent Education vs Student Scores")

st.pyplot(fig)

# Test Preparation Analysis
if "TestPrep" in df.columns:

    st.header("Test Preparation vs Student Scores")

    test_prep = df.groupby("TestPrep").agg({
        "MathScore": "mean",
        "ReadingScore": "mean",
        "WritingScore": "mean"
    })

    st.dataframe(test_prep)

    fig, ax = plt.subplots(figsize=(8, 5))

    sns.heatmap(test_prep, annot=True, fmt=".2f", ax=ax)

    ax.set_title("Test Preparation vs Student Scores")

    st.pyplot(fig)

# Score Distribution
st.header("Score Distribution")

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

sns.boxplot(data=df, x="MathScore", ax=axes[0])
axes[0].set_title("Math Score")

sns.boxplot(data=df, x="ReadingScore", ax=axes[1])
axes[1].set_title("Reading Score")

sns.boxplot(data=df, x="WritingScore", ax=axes[2])
axes[2].set_title("Writing Score")

st.pyplot(fig)

# Ethnic Group Distribution
if "EthnicGroup" in df.columns:

    st.header("Ethnic Group Distribution")

    ethnic_counts = df["EthnicGroup"].value_counts()

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.pie(
        ethnic_counts,
        labels=ethnic_counts.index,
        autopct="%1.1f%%"
    )

    ax.set_title("Distribution of Ethnic Groups")

    st.pyplot(fig)

# Conclusion
st.header("Conclusion")

st.write(
    "This analysis explores student academic performance and examines "
    "different factors such as gender, parental education, test "
    "preparation and ethnic group. The project demonstrates how "
    "Python-based data analysis and visualization can be used to "
    "identify patterns in educational data."
)