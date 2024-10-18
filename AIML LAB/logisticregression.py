# Import necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Generate synthetic dataset (for example purposes)
# Two features, and a binary target (0 or 1)
np.random.seed(0)
X = np.random.randn(100, 2)  # 100 samples, 2 features
y = (X[:, 0] + X[:, 1] > 0).astype(int)  # Binary labels based on a linear separation

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Logistic Regression model
log_reg = LogisticRegression()

# Train the model
log_reg.fit(X_train, y_train)

# Make predictions on the test data
y_pred = log_reg.predict(X_test)

# Evaluate the model using accuracy score
accuracy = accuracy_score(y_test, y_pred)

# Print the model parameters and accuracy
print(f"Intercept: {log_reg.intercept_}")
print(f"Coefficients: {log_reg.coef_}")
print(f"Accuracy: {accuracy * 100:.2f}%")

# Predicting the probability of a new input value
new_value = np.array([[0.5, -0.5]])  # Input value for prediction
probability = log_reg.predict_proba(new_value)
print(f"Probability for {new_value}: {probability}")
