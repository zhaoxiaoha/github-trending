import datetime
import codecs
import requests
from pyquery import PyQuery as pq

def create_md(date, filename):
  with open(filename, 'w') as f:
     f.write("## " + date + "\n")

def scrape_hn(filename):

  for page in range(1, 4):

    url = 'https://news.ycombinator.com/?p=' + str(page)
    print(url)
    r = requests.get(url)

    d = pq(r.content)
    
    github_items = d('tr.athing:contains("github")')

    with codecs.open(filename, "a", "utf-8") as f:
      f.write('\n--- Page {} ---'.format(page))

      for item in github_items:
        i = pq(item)
        title = i('a.storylink').text()
        url = i('a.storylink').attr('href')
        score = i('.subtext span.score').text()

        f.write("\n* [{}]({}): {}".format(title, url, score))

def main():
  today = datetime.datetime.now().strftime('%Y-%m-%d')
  filename = '{}_hn.md'.format(today)

  create_md(today, filename)
  scrape_hn(filename)

if __name__ == '__main__':
  main()
