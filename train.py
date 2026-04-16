import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

print("Training model...")

# Load data
df = pd.read_csv("dataset.csv")

X = df[["area", "bedrooms"]]
y = df["price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Training completed! Model saved as model.pkl")