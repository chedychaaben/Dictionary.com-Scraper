import requests
from bs4 import BeautifulSoup
import pandas as pd

# import list of CLDRS 
df = pd.read_csv('Dictionary.com.csv')
cldrs = df["CLDR"].tolist()

errors = []
for cldr in cldrs:
    url = f'https://www.dictionary.com/e/emoji/{cldr}/'
    r = requests.get(url)
    if r.status_code == 200:
        with open(f'Dictionary_text/{cldr}.html', 'w', encoding='utf8') as fp:
            soup = BeautifulSoup(r.text, 'html.parser')
            article = soup.find('article', {'class':'article-word'})
            fp.write(str(article))
    else:
        errors.append(url)

# Save Errors to txt 
with open('errors.txt', 'w', encoding='utf-8') as f:
    for e in errors:
        f.write(e + '\n')