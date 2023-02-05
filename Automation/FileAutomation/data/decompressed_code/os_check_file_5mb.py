import os

filenames = ['service_contract.hwp', 'christmas_report.pptx',
             'business_report.docx', 'accounting_report.pptx', 'account_book.pptx']

over_5mb_filenames = []

for file in filenames:
    if os.path.getsize("{}".format(file))>5000000:
        over_5mb_filenames.append(file)

print("5MB가 넘는 파일 리스트:")
print(over_5mb_filenames)