# 💰Anti-Money-Laundering💰

## Introduction

The purpose of this Anti-money laundering (AML) is to process of preventing and detecting the use of illicit funds for illegal activities. AML is a crucial 
challenge for financial institutions, as they face the risk of regulatory fines, reputational damage, and criminal prosecution if they fail to comply with 
the laws and regulations that aim to combat money laundering. AML also helps to protect the integrity and stability of the financial system, and to prevent 
the financing of terrorism, corruption, and other crimes.

## 🎯Project Aim

The aim of the project on anti-money laundering in data science is to develop advanced algorithms and models that can effectively detect and prevent money laundering activities within financial systems. The project aims to leverage machine learning and data analysis techniques to identify suspicious patterns, anomalies, and potential risks associated with financial transactions. Through this project, the goal is to enhance the efficiency and accuracy of anti-money laundering efforts, reduce false positives, and improve overall regulatory compliance. Ultimately, the aim is to protect the integrity of the financial system and mitigate the risks posed by money laundering activities.

## 📅Data Collection 

I collected the data from Kaggle, a popular online platform for sharing and discovering datasets. The dataset was obtained from Kaggle, and it consists of a comprehensive collection of information relevant to my project. By utilizing data from Kaggle, I can leverage the existing knowledge and resources shared by the data science community to enhance the accuracy and reliability of my analysis. The dataset from Kaggle provides a valuable foundation for my research, enabling me to explore patterns, trends, and insights in my field of interest.

## 🧷Feature Engineering

Handling Missing Values: The code uses a pipeline to impute missing values using the median strategy. It saves the imputation pipeline using joblib.dump(). This step ensures that missing values in numerical features are filled.

Outlier Treatment: The code applies Winsorization using the Winsorizer from the feature-engine library to handle outliers. It saves the Winsorizer model using joblib.dump(). Winsorization helps in reducing the impact of extreme values on the model.

Scaling Numerical Features: The code uses the MinMaxScaler to scale the numerical features in the dataset. It saves the scaling pipeline using joblib.dump(). Scaling ensures that all features have a similar range and prevents any particular feature from dominating the model.

Encoding Categorical Features: The code applies one-hot encoding using the OneHotEncoder to encode categorical features. It saves the encoding pipeline using joblib.dump(). One-hot encoding transforms categorical variables into binary vectors, allowing them to be used in machine learning algorithms.

Feature Concatenation: The code concatenates the scaled numerical features and the encoded categorical features into a single dataframe named clean_data. This step combines the processed features into a format suitable for model training.

## 📳Model Selection & Optimisation

After performing feature engineering on the dataset, the next step is to select and optimize the best model for the task at hand. I evaluated multiple classifiers to determine their performance and selected the best model based on various evaluation metrics.

The following classifiers were tested:

- KNeighborsClassifier
- DecisionTreeClassifier
- RandomForestClassifier
- GradientBoostingClassifier
- AdaBoostClassifier
- LogisticRegression
- GaussianNB
- LinearDiscriminantAnalysis
- QuadraticDiscriminantAnalysis
- SVC

For each classifier, I trained the model on the training data and evaluated its performance on the test data. The evaluation included metrics such as accuracy, confusion matrix, and classification report. This allowed me to assess how well each model performed in predicting the target variable.

Based on the evaluation results, the best performing model was determined. The model's accuracy, confusion matrix, and classification report were considered to make an informed decision.

Finally, I saved the selected model using the pickle library to be able to reuse it in the future without retraining.

It's worth noting that model selection and optimization is an iterative process, and different techniques like hyperparameter tuning or cross-validation can be employed to further enhance the performance of the chosen model. Additionally, the selection of the best model depends on the specific requirements and constraints of the project.

## ⚒️Tool Used
![image](https://github.com/Manoj-P-Kurdekar/Anti-Money-Laundering/assets/102578528/f8f27076-3893-4ddf-aa0c-96795b07152a)
- Jupyter and Spyder is used as an IDE.
- For visualization of the plots, Matplotlib and Seaborn are used.
- Streamlit Platform is used for deployment of the model.

## 🚀Result

The best performing Random Forest Classifier produced an accuracy score of 95.2% on the testing set, compared to a baseline score of 50%. In this case false negatives are an unwanted risk, so a high recall score is important, the best Random Forest produced a recall of 97% on the testing set.

## 😊Conclusion

The Random Forest Classifier demonstrated outstanding performance in the anti-money laundering project. It achieved an impressive accuracy score of 95.2% on the testing set, surpassing the baseline accuracy of 50%. With a focus on minimizing false negatives, the model exhibited a remarkable recall score of 97%. These results indicate the effectiveness of the Random Forest Classifier in accurately identifying potential money laundering activities. The high recall score suggests that the model successfully captured a significant portion of fraudulent transactions, minimizing the risk of missing suspicious transactions. Overall, the Random Forest Classifier is a reliable and valuable tool for enhancing anti-money laundering efforts and safeguarding financial systems against illicit activities.
