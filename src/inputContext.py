# coding: UTF-8
import subprocess
from model import model

def simUsers(model):
    # 類似ユーザーを抽出し逐次的に返す
    threshold = 0.5

    for compUser in allUsers:
        if getAccuracy(compUser,model) > threshold:
            yield compUser

def matchContext(history, context):
    # 履歴のコンテキストが適合しているか判定
    if :
        return  

def addTransactionList(history):
    # コンテキストに適合した履歴を追加
    pass

def gentransactionList(simUsers,context):
    # 入力したコンテキストに一致する類似ユーザーの履歴集合を返す
    transactionList = list()

    for simUser in simUsers():
        for history in historyList:
            if matchContext(history, context):
                addTransactionList(history)
    return transactionList

def main():
    print "ユーザー名を入力 :"
    user = raw_input()
    userModel = model.genModel(user)

    print "コンテキスト情報を入力します"
    print "誰と出かけるか(一人/家族/同性/異性 : 0/1/2/3)を入力 :",
    context = input()

    print "あなたと類似したユーザーから抽出した履歴 :"
    print gentransactionList(simUsers,context)

if __name__ == '__main__':
    main()