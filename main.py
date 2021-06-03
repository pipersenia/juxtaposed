from newspaper import Article, Config

def download_and_parse(url: str):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    config = Config()
    config.browser_user_agent = user_agent
    article = Article(url, config=config)
    try:
        article.download()
    except ArticleException:
        pass
    article.parse()
    print(article.authors)
    article.nlp()
    print(article.keywords)
    print(article.summary)

def main():
    urls = []
    urls.append('https://www.foxnews.com/politics/george-p-bush-texas-ag-candidacy')
    urls.append('https://www.cnn.com/2021/06/02/politics/george-p-bush-texas-attorney-general/index.html')
    for url in urls:
        download_and_parse(url)
        print("------------------------------")


if __name__ == '__main__':
    main()