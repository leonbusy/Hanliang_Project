from github import Github
from openpyxl import Workbook
import re
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
from github_rate_limit import rate_limited_github_instance


wb = Workbook()
sheet = wb.create_sheet('sheet1', index=0)
row = ["repo_name", "repo_number", "pr_title", 'create_time', "comment", "is_merged"]
sheet.append(row)

# github_token = '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'
# github_instance = Github()
repositories = ["kubernetes-client/python", "faif/python-patterns", "aimacode/aima-python", "gto76/python-cheatsheet", "google/python-fire"]

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
            if comments.body != None:

                list_comments.append(repository_name)
                list_comments.append(pr_number)
                list_comments.append(pr_title)


                # print(str(comments.created_at))
                list_comments.append(str(comments.created_at))

                # list_comments.append(comments.body)  # 存入excel时有特殊符号报错
                list_comments.append(ILLEGAL_CHARACTERS_RE.sub(r'', comments.body))  # 存入excel时有特殊符号报错，需要用空格代替
                list_comments.append(pull_request.is_merged())
                sheet.append(list_comments)
                print(list_comments)
            else:
                print("该Pull request的评论为空，不存入")
        # print(type(pull_request.get_issue_comments()))
        if pull_request.get_issue_comments() != '':
            count += 1
            print("收入第：" + str(count) + "条Pull requst")
        # break

# wb.save('data' + '.xlsx')