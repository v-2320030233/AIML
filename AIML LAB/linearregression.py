# Import necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generate random dataset (for example purposes)
np.random.seed(0)
X = 2 * np.random.rand(100, 1)  # 100 data points, 1 feature
y = 4 + 3 * X + np.random.randn(100, 1)  # Linear relation: y = 4 + 3x + noise

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Linear Regression model
lin_reg = LinearRegression()

# Train the model
lin_reg.fit(X_train, y_train)

# Make predictions on test data
y_pred = lin_reg.predict(X_test)

# Evaluate the model using Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)

# Print the model parameters and MSE
print(f"Intercept: {lin_reg.intercept_}")
print(f"Coefficient: {lin_reg.coef_}")
print(f"Mean Squared Error: {mse}")

# Predicting for a new input value
new_value = np.array([[1.5]])  # Input value for prediction
prediction = lin_reg.predict(new_value)
print(f"Prediction for {new_value[0][0]}: {prediction[0][0]}")
