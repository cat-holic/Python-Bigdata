from sklearn import model_selection, svm, metrics


def load_csv(fname):
    labels = []
    images = []
    with open(fname, "r") as f:
        for line in f:
            cols = line.split(",")
            if len(cols) < 2: continue
            labels.append(int(cols.pop(0)))
            vals = list(map(lambda n: int(n) / 256, cols))
            images.append(vals)
    return {"labels": labels, "images": images}


data = load_csv("./01.mnist/train.csv")
test = load_csv("./01.mnist/t10k.csv")
# 학습하기
clf = svm.SVC()
clf.fit(data["images"], data["labels"])

# 예측하기 --- 3.Homenetwork
predict = clf.predict(test["images"])

# 결과 확인하기
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("정답률 = %0.2f" % (ac_score * 100))
print("리포트 =")
print(cl_report)
