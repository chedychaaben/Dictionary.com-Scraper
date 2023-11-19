import pandas as pd
from bs4 import BeautifulSoup
import os


htmls = os.listdir('Dictionary_text')

df = pd.read_csv("Dictionary.com-first.csv") 

emojies_and_data = []

for html in htmls:
    print("Working on ", html)
    with open (f'Dictionary_text/{html}', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        try:
            meaning             = ' '.join(sent.text.replace('\n','') for sent in soup.find('div', {'class':'article-word__definition'}).find_all('p')).replace('Related words:','')
        except:
            meaning=''
        
        try:
            where_it_comes_from = ' '.join(sent.text.replace('\n','') for sent in soup.find('div', {'class':'article-word__origin'}).find_all('p'))
        except:
            where_it_comes_from = ''

        try:
            who_uses_it = ' '.join(sent.text.replace('\n','') for sent in soup.find('div', {'class':'article-word__usage'}).find_all('p'))
        except:
            who_uses_it = ''
        emojies_and_data.append([html[:-5] ,meaning, where_it_comes_from, who_uses_it])

#print(emojies_and_data[0])


# Work and edit the dataframe !
row_counter = 0
for row in df.itertuples():
    for e in emojies_and_data:
        if e[0] == row[2]:
            df.at[row_counter,'Dict - Meaning']= e[1]
            df.at[row_counter,'Dict - Where Does It Come From?']= e[2]
            df.at[row_counter,'Dict - Who Uses It?']= e[3]
    row_counter += 1



df.to_csv("Dictionary.com.csv", index=False) 