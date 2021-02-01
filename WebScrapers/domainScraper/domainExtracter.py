import tldextract

ext = tldextract.extract('http://forums.news.cnn.com/')
result = ext.domain + '.'+ ext.suffix
print(result)