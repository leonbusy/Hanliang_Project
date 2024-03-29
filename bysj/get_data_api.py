from github import Github
from openpyxl import Workbook
import re
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
from github_rate_limit import rate_limited_github_instance
import re
import time

wb = Workbook()
sheet = wb.create_sheet('sheet1', index=0)
row = ["repo_name", "pr_number","pr_create_by", "pr_title", 'create_time', "comment", "is_merged","comment_author"]
sheet.append(row)

# github_token = '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'
# github_instance = Github()
# repositories = ["donnemartin/system-design-primer", "TheAlgorithms/Python", "vinta/awesome-python", "nvbn/thefuck", "huggingface/transformers"]
repositories = ["huggingface/transformers"]
# repositories = ["donnemartin/system-design-primer", "TheAlgorithms/Python", "vinta/awesome-python", "nvbn/thefuck"]
# repositories = ["donnemartin/system-design-primer"]


# Judge whether the character is Chinese
def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

count = 0
for repository_name in repositories:
    repo = rate_limited_github_instance().get_repo(repository_name)
    pull_requests = repo.get_pulls(state='closed', sort='newest')

    for pull_request in pull_requests:
        pr_number = pull_request.number
        # print(pr_number)
        pr_title = pull_request.title
        # print(pull_request.is_merged())

        # print(pull_request.get_issue_comments()[1])
        for comments in pull_request.get_issue_comments():
            list_comments = list()

            newest_time = "2022-01-01 0:00:00"
            if comments.body != None and time.strptime(newest_time,'%Y-%m-%d %H:%M:%S') > \
                    time.strptime(str(comments.created_at), '%Y-%m-%d %H:%M:%S') and (pull_request.user != comments.user) and \
                (is_Chinese(comments.body)==False):

                list_comments.append(ILLEGAL_CHARACTERS_RE.sub(r'', repository_name))
                list_comments.append(ILLEGAL_CHARACTERS_RE.sub(r'', str(pr_number)))
                pr_create_by_user = re.search(r'"(.+?)"', str(pull_request.user)).group().lstrip('''"''').rstrip('''"''')
                list_comments.append(ILLEGAL_CHARACTERS_RE.sub('r', str(pr_create_by_user)))
                list_comments.append(ILLEGAL_CHARACTERS_RE.sub(r'', pr_title))

                # print(str(comments.created_at))
                list_comments.append(ILLEGAL_CHARACTERS_RE.sub(r'', str(comments.created_at)))

                # list_comments.append(comments.body)  # 存入excel时有特殊符号报错
                list_comments.append(ILLEGAL_CHARACTERS_RE.sub(r'', comments.body))  # 存入excel时有特殊符号报错，需要用空格代替
                list_comments.append(ILLEGAL_CHARACTERS_RE.sub(r'', str(pull_request.is_merged())))
                search_str = re.search(r'"(.+?)"', str(comments.user)).group().lstrip('''"''').rstrip('''"''')
                list_comments.append(ILLEGAL_CHARACTERS_RE.sub(r'', str(search_str)))
                sheet.append(list_comments)
                print(list_comments)
            else:
                print("该Pull request的评论为空或PR不足六个月，不存入")
        # print(type(pull_request.get_issue_comments()))
        if pull_request.get_issue_comments() != '':
            count += 1
            print("收入第：" + str(count) + "条Pull requst")
        # break





wb.save('data_test' + '.xlsx')