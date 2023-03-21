import pandas as pd
from urllib.request import Request, urlopen

url = 'https://economia.uol.com.br/cotacoes/'

request = Request(url)
request.add_header('user-agent',
                   'Mozilla/5.0 (Windows NT 10.0; rv:91.0) \
                    Gecko/20100101 Firefox/91.0')

page = urlopen(request)

html = page.read()

tabelas = pd.read_html(html)

for idx, tabela in enumerate(tabelas):
    tabela.to_excel(f'tabela-{idx}.xlsx', index=False)