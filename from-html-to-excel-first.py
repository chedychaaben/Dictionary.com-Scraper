import pandas as pd
from bs4 import BeautifulSoup
import os

df = pd.DataFrame({
    'Number' : [],
    'CLDR' : [],
    'Emoji' : [],
    'Name' : [],
    'Dict - Meaning' : [],
    'Dict - Where Does It Come From?' : [],
    'Dict - Who Uses It?' : [],
    'Image' : [],
    'Url' : [],
})


emojies_soup = []

# From lists os collection page to Python list
with open (f'Scraped_data_manually.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')
    lists = soup.find_all('div', {'class':'list'})
    for l in lists:
        emojies = l.find_all('li')
        for emojie in emojies:
            emojies_soup.append(emojie)

counter = 1
for emoji_li in emojies_soup:
    try:
        a_tag = emoji_li.find('a')
        img_tag = a_tag.find('img')
        # Getting data
        url = a_tag['href']
        CLDR = a_tag['href'][35:-1]
        name = a_tag.text
        image_src = img_tag['src']
        emoji = img_tag['alt']
        if len(emoji)>1:
            raise ValueError("Double emojies")
        meaning = where_it_comes_from = who_uses_it = ''
        df.loc[counter] = [counter, CLDR, emoji, name, meaning, where_it_comes_from, who_uses_it, image_src, url]
        counter += 1
    except:
        pass # If i didn't work then there is a prob either Two emojis OR no emojie

df.to_csv("Dictionary.com-first.csv", index=False) 