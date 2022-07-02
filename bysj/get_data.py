import requests
import json
import xlwt


# 获取指定接口的数据
def fetchUrl(url):
    '''
    功能：访问 url 的网页，获取网页内容并返回
    参数：目标网页的 url
    返回：目标网页的 html 内容
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
    col = ("comment", 'time', 'author_association')
    for i in range(0, len(col)):
        sheet.write(0, i, col[i])

    # agent = ['https://api.github.com/repos/bitcoin/bitcoin/pulls/comments']

    agent = ['https://api.github.com/repos/bitcoin/bitcoin/pulls/comments'
        , 'https://api.github.com/repos/airbnb/javascript/pulls/comments']

    datalist = list()
    for i in agent:
        query_url = i
        fetch_result = fetchUrl(query_url)
        # print(len(fetch_result))
        for i in range(0,len(fetch_result)):
            datalist.append([fetch_result[i]['body'],fetch_result[i]['created_at'],fetch_result[i]['author_association']])
        # print(datalist)
        print("Has written "+str(agent.index(query_url)+1)+" agent")

    for i in range(0,len(datalist)):
        data=datalist[i]
        for j in range(0,len(col)):
            sheet.write(i+1,j,data[j])

    book.save('data' + '.xls')
    # for i in range(0,len(fetch_result)):
        # aa=fetch_result[i]
        # print(aa['body'],aa['created_at'],aa['author_association'])




