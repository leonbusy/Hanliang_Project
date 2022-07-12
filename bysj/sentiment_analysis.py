from sklearn.externals import joblib
import pandas as pd


get_data = pd.read_excel("data2.xlsx", header=None,keep_default_na=False)
for i in range(1,len(get_data[5])):
    data_read = get_data[5][i]
    # print(data_read)
    if data_read == '':
        data_read = "None"
        # print(data_read)
    model = joblib.load('tfidf_svm_sentiment.model')
    y_pre = model.predict([data_read])
    print(y_pre)
    proba = model.predict_proba([data_read])[0]
    print(proba)
    if y_pre[0] == -1:
        print(data_read,": Most likely negative in sentiment（Probability："+str(proba[0])+")")
    elif y_pre[0] == 0:
        print(data_read,": Most likely neutral in sentiment（Probability："+str(proba[1])+")")
    elif y_pre[0] == 1:
        print(data_read,": Most likely negative in sentiment（Probability："+str(proba[2])+")")
