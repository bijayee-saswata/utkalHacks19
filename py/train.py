'''
Date: 16th March 2019
Author: Swain Subrat Kumar
'''

#importing libraries
from pandas import read_csv
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

#load_dataset
data = read_csv("creditcard_sampledata_2.csv")

#Extraction of Features and Lables
X = data.iloc[:,0:30].values
y = data.iloc[:,-1].values

#train-test split
X_train,X_test,y_train,y_test = train_test_split(X, y , test_size=0.2, stratify = y)

#data oversampling
method = RandomOverSampler()
X_resampled, y_resampled = method.fit_sample(X_train, y_train)

#defining classifiers
clf1 = LogisticRegression(class_weight='balanced', random_state=1)
clf2 = RandomForestClassifier(class_weight='balanced', random_state=1)
clf3 = GaussianNB()
ensemble_model = VotingClassifier(estimators=[('lr', clf1), ('rf', clf2), ('gnb', clf3)], voting='hard')
ensemble_model.fit(X_resampled, y_resampled)

predicted = ensemble_model.predict(X_test)
f1_score_value = f1_score(y_test, predicted, average='weighted')
#print(f1_score_value)
from sklearn.metrics import classification_report, confusion_matrix
# Print classification report using predictions
print(classification_report(y_test, predicted))
# Print confusion matrix using predictions
print(confusion_matrix(y_test, predicted))
from sklearn.externals import joblib
filename = 'file.sav'
joblib.dump(ensemble_model, filename)