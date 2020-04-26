
# Reddit Flare Detection
This repository contains code for a machine learning model that detects the flair of the reddit post, given the url.

The repo is divided into the following structure:

1. Notebooks - Containing all the .pynb files related to the project.
2. Web App - containing all the files needed for running the web-app.
3. Model - containing the pickle file of the best performing model.

## How to run locally
Open terminal and perform the following steps.
1. Clone the repository
```
git clone
```
2. Install the required libraries
```
pip3 install -r requirements.txt
```
3. Navigate to the folder containing flask code
```
cd web_app
```
4. Export the following variables in your terminal
```
export FLASK_APP=app.py && export FLASK_ENV=development
```
5. Run the app
```
flask run
```
6. Go to the address as shown after running the command above.




## Results:

### Features : Titles+Comments+Body+Url
|                |Model used                          | Accuracy                         |
|----------------|-------------------------------|-----------------------------|
||`Random Forest Classifier`            | 68.983           |
||`naive_bayes`            |057.657            |
| |`linear_svm`|71.042|
||`logistic regression`            |70.656 |
| |`Bag Of Words`|64.092|


### Features : Titles+Comments+Body

|                |Model used                          | Accuracy                         |
|----------------|-------------------------------|-----------------------------|
||`Random Forest Classifier`            | 69.240           |
||`Naive Bayes`            |55.083            |
| |`Linear svm`|67.567|
||`Logistic Regression`            |69.112 |
| |`Bag Of Words`|65.122|

### Features : Title+Body

|                |Model used                          | Accuracy                         |
|----------------|-------------------------------|-----------------------------|
||`Random Forest Classifier`            | 65.637           |
||`Naive Bayes`            |60.875            |
| |`Linear svm`|66.795|
||`Logistic Regression`            | 66.410 |
| |`Bag Of Words`|64.052|


### Features : Title+Comments

|                |Model used                          | Accuracy                         |
|----------------|-------------------------------|-----------------------------|
||`Random Forest Classifier`            | 60.231|
||`Naive Bayes`            |50.454            |
| |`Linear svm`|63.191|
||`Logistic Regression`            |62.934 |
| |`Bag Of Words`|61.122|


### Features : Title

|                |Model used                          | Accuracy                         |
|----------------|-------------------------------|-----------------------------|
||`Random Forest Classifier`            | 54.697           |
||`Naive Bayes`            |53.796            |
| |`Linear svm`|53.925|
||`Logistic Regression`            |54.569 |
| |`Bag Of Words`|53.796|
