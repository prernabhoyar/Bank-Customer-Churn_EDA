import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Bank Customer Churn Analysis")

# Load dataset
df = pd.read_csv("Customer-Churn-Records.csv")

st.subheader("Dataset Preview")
st.write(df.head())

st.subheader("Dataset Shape")
st.write(df.shape)

# Drop unnecessary columns
df = df.drop(["RowNumber","CustomerId","Surname"], axis=1)

# Churn Distribution
st.subheader("Customer Churn Distribution")

fig1, ax1 = plt.subplots()
sns.countplot(x="Exited", data=df, ax=ax1)
st.pyplot(fig1)

# Churn by Gender
st.subheader("Churn by Gender")

fig2, ax2 = plt.subplots()
sns.countplot(x="Gender", hue="Exited", data=df, ax=ax2)
st.pyplot(fig2)

# Churn by Geography
st.subheader("Churn by Geography")

fig3, ax3 = plt.subplots()
sns.countplot(x="Geography", hue="Exited", data=df, ax=ax3)
st.pyplot(fig3)

# Age Distribution
st.subheader("Age Distribution")

fig4, ax4 = plt.subplots()
sns.histplot(df["Age"], bins=30, kde=True, ax=ax4)
st.pyplot(fig4)

# Correlation Heatmap
st.subheader("Correlation Heatmap")

fig5, ax5 = plt.subplots(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax5)
st.pyplot(fig5)