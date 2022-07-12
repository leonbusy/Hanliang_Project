from github import Github
from openpyxl import Workbook
import re
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE


wb = Workbook()
sheet = wb.create_sheet('sheet1', index=0)
row = ["repo_name", "repo_number", "pr_title", 'create_time', "comment"]
sheet.append(row)

token = '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'
github_instance = Github(token)
repositories = ["airbnb/javascript", "bitcoin/bitcoin", "TheAlgorithms/Python", "twbs/bootstrap", "geekcomputers/Python"]


for repository_name in repositories:
    repo = github_instance.get_repo(repository_name)
    pull_requests = repo.get_pulls(state='open', sort='newest')

    for pull_request in pull_requests:
        pr_number = pull_request.number
        # print(pr_number)
        pr_title = pull_request.title


            # print(pull_request.get_issue_comments()[1])
        for comments in pull_request.get_issue_comments():
            list_comments = list()
            list_comments.append(repository_name)
            list_comments.append(pr_number)
            list_comments.append(pr_title)


            # print(str(comments.created_at))
            list_comments.append(str(comments.created_at))

            # list_comments.append(comments.body)  # 存入excel时有特殊符号报错
            list_comments.append(ILLEGAL_CHARACTERS_RE.sub(r'', comments.body))  # 存入excel时有特殊符号报错，需要用空格代替

            sheet.append(list_comments)
            print(list_comments)
        # break

wb.save('data' + '.xlsx')