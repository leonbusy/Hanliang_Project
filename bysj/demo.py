import requests
import json
import xlwt
from openpyxl import Workbook

# 获取指定接口的数据：Request interface data
def fetchUrl(url):
    '''
    Function: visit the webpage of URL, get the webpage content and return
    parameters: URL of target webpage
    Return: HTML content of the target page
    '''

    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Authorization': 'token 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',
        'Content-Type': 'application/json',
        'method': 'GET',
        'Accept': 'application/json'
    }

    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    result = json.loads(r.text)  # json字符串转换成字典
    return result




if __name__ == '__main__':
    '''
    主函数：程序入口
    '''
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)

    col = ("repo_name","pr_title","comment", 'time', 'author_association','language')
    for i in range(0, len(col)):
        sheet.write(0, i, col[i])

    # agent = ['https://api.github.com/repos/bitcoin/bitcoin/pulls/comments']

    # agent = ['https://api.github.com/repos/bitcoin/bitcoin/pulls/comments'
    #     , 'https://api.github.com/repos/airbnb/javascript/pulls/comments']

    agent = ['https://api.github.com/repos/bitcoin/bitcoin/pulls'
        , 'https://api.github.com/repos/airbnb/javascript/pulls'
        , 'https://api.github.com/repos/TheAlgorithms/Python/pulls'
        , 'https://api.github.com/repos/twbs/bootstrap/pulls'
        , 'https://api.github.com/repos/geekcomputers/Python/pulls'
        ]


    datalist = list()
    for i in agent:
        query_url = i
        print("Writting " + str(agent.index(query_url) + 1) + " agent")
        for j in range(1,5):
            query_url = i+"?page="+str(j)+"&q=is%3Apr+is%3Aopen"
            fetch_result = fetchUrl(query_url)
            if fetch_result!=None:
            # print(len(fetch_result))
                for k in range(0,len(fetch_result)):
                    # dic=fetch_result[k]
                    datalist.append([fetch_result[k]['base']['repo']['full_name'],
                                     fetch_result[k]['title'],
                                     fetch_result[k]['body'],
                                     fetch_result[k]['created_at'],
                                     fetch_result[k]['author_association'],
                                     fetch_result[k]['base']['repo']['language']])
                # print(datalist)


    for i in range(0,len(datalist)):
        data=datalist[i]
        for j in range(0,len(col)):
            sheet.write(i+1,j,data[j])


    book.save('data' + '.xlsx')
    # for i in range(0,len(fetch_result)):
        # aa=fetch_result[i]
        # print(aa['body'],aa['created_at'],aa['author_association'])


