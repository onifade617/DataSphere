import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

st.set_page_config(page_title="Boston Housing Price Prediction", layout="wide")

st.title("🏠 Boston Housing Price Prediction App")
st.write("Explore the dataset, train a Linear Regression model, and make predictions interactively.")

# Step 1: Load Data
st.header("📂 Step 1: Load Dataset")
df = pd.read_csv(r"boston.csv")
st.dataframe(df.head())
st.write(f"**Dataset Shape:** {df.shape}")

# Step 2: Correlation Heatmap
st.header("📊 Step 2: Correlation Heatmap")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(df.corr(), annot=False, cmap="coolwarm", ax=ax)
plt.title("Correlation Heatmap of Boston Dataset")
st.pyplot(fig)

# Step 3: Features and Labels
x = df.drop(['medv'], axis=1)
y = df['medv']  # convert to Series for simplicity

st.subheader("🔎 Features and Labels")
with st.expander("Show first 5 rows of features"):
    st.dataframe(x.head())
with st.expander("Show first 5 rows of labels"):
    st.dataframe(y.head())

# Step 4: Train-Test Split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Step 5: Train Model
h_pred = LinearRegression()
h_pred.fit(x_train, y_train)
y_pred = h_pred.predict(x_test)

st.header("🤖 Model Performance")
st.write(f"**Mean Absolute Error (MAE):** {mean_absolute_error(y_test, y_pred):.2f}")
st.write(f"**Mean Squared Error (MSE):** {mean_squared_error(y_test, y_pred):.2f}")

# Step 6: Comparison Table
st.subheader("📋 Actual vs Predicted Values")
comp_df = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred})
st.dataframe(comp_df.head(10))

# Step 7: Make Predictions for Specific Row
st.header("🔮 Make a Prediction")
row_index = st.slider("Select a row index from test set", 0, len(x_test)-1, 1)
sample_features = x_test.iloc[row_index].values.reshape(1, -1)
predicted_value = h_pred.predict(sample_features)

st.write(f"**Selected Row Index:** {row_index}")
st.write(f"**Predicted MEDV:** {predicted_value[0]:.2f}")
st.write(f"**Actual MEDV:** {y_test.iloc[row_index]}")

st.success("✅ Model trained and predictions generated successfully!")
