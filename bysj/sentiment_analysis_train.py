import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from nltk.tokenize import word_tokenize  # 分词器加载
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib


def clean(text):
    word_tokenize_clean = word_tokenize(text)
    # print(word_tokenize_clean)
    return word_tokenize_clean

github_standard_data = pd.read_excel("github_standard_clean.xlsx", header=None)
test_data = pd.DataFrame(github_standard_data)
comments_content_x = test_data[2::][3]
comments_sentiment_y = test_data[2::][4]  #将获取的polarity_number转成二维
comments_content_x_vec = list()
for i in range(2,len(comments_content_x)+2):
    if str(test_data[3][i]) == ' ':
        test_data[3][i] = "None"
        print("此为"+ test_data[3][i])
    comments_content_x_vec.append(str(test_data[3][i]))

# print(comments_content_x_vec)   #打印二维评论
# print(comments_sentiment_y)      #打印极向polarity_number
comments_sentiment_y_vec = list()
for i in comments_sentiment_y:
    comments_sentiment_y_vec.append([i])
# print(comments_sentiment_y_vec)
# print(len(comments_content_x_vec))
# print(len(comments_sentiment_y_vec))

# print(comments_content_x_vec)
comments_content_x_vec_ndarray = np.asarray(comments_content_x_vec,dtype=None)
comments_sentiment_y_vec_ndarray = np.asarray(comments_sentiment_y_vec,dtype='float64')
# print(comments_content_x_vec_ndarray)
# print(comments_sentiment_y_vec_ndarray)

X_train,X_test,y_train,y_test = train_test_split(comments_content_x_vec_ndarray,comments_sentiment_y_vec_ndarray, test_size=0.33, random_state=3)
X = X_train.tolist()
y= y_train.tolist()
print(X)

TFIDF_SVM_Sentiment_Model = Pipeline([
    ('TFIDF', TfidfVectorizer()),
    ('SVM', SVC(C=0.95, kernel='linear', probability=True))
])

TFIDF_SVM_Sentiment_Model.fit(X[:6000],np.ravel(y[:6000]))
svm_test_score = TFIDF_SVM_Sentiment_Model.score(X_test,y_test)
joblib.dump(TFIDF_SVM_Sentiment_Model,'tfidf_svm_sentiment.model')
print(svm_test_score)




# print(x_train)
# print(y_train)
# clf =SVC()
# clf.fit(x_train, y_train)
# clf.score(x_train,y_train)

