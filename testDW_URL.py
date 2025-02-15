from fake_useragent import UserAgent
import requests
   
ua = UserAgent()
print(ua.chrome)
header = {'User-Agent':str(ua.chrome)}
print(header)
url = "https://www.youtube.com/watch?v=tZT2MCYu6Zw"
htmlContent = requests.get(url, headers=header)
print(htmlContent)
