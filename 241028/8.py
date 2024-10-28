company = [['삼성전자','삼성생명','삼성화재'], ['LG전자', 'LG화학'],['SKT', 'SK바이오사이언스'],['셀트리온']]
company[3].append('종근당')

for i in range(len(company)):
    company[i].pop()
