#Naive Bayes classifier using iris
#Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

#Load the Iris Dataset
iris = load_iris()
X = iris.data
y = iris.target

#Split the dataset into training andd testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

#Initialize the Gaussian Naive Bayes classifier
gnb = GaussianNB()

#Train the classifier
gnb.fit(X_train, y_train)

#Make predictions on the test set
y_pred = gnb.predict(X_test)

#Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)   
print(f"Accuracy: {accuracy * 100:.2f}%")

#Predict the class for a new sample
new_sample = [[5.1, 3.5, 1.4, 0.2]]
predicted_class = gnb.predict(new_sample)
print(f"Predicted class for the new sample: {predicted_class[0]}")