import requests


session = requests.session()
res = session.get("https://nj.meituan.com/")
uuid = requests.utils.dict_from_cookiejar(res.cookies).get('uuid')
print(uuid)

# ids = "4213385"

# headers = {
# 	'Accept': 'application/json',
# 	'Accept-Encoding': 'gzip, deflate, br',
# 	'Accept-Language': 'zh-CN,zh;q=0.9',
# 	'Connection': 'keep-alive',
# 	'Host': 'www.meituan.com',
# 	'Referer': 'https://www.meituan.com/meishi/4213385/',
# 	'Sec-Fetch-Mode': 'cors',
# 	'Sec-Fetch-Site': 'same-origin',
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
# }

# page = 

# res = session.get(url=f"https://www.meituan.com/meishi/api/poi/getMerchantComment?uuid={uuid}&platform=1&partner=126&originUrl=https://www.meituan.com/meishi/{ids}/&riskLevel=1&optimusCode=10&id=4213385&userId=&offset=0&pageSize=10&sortType=1",headers=headers)

# print(res.json())

