import zlib
import base64
import requests
import datetime
from pyquery import PyQuery as pq


class Meituan(object):
	"""docstring for Meituan"""
	def __init__(self, areas, foods):

		super(Meituan, self).__init__()
		self.areas = areas
		self.session = requests.session()
		self.objectlisturl = self.getobjecturl(areas, foods)

	def getobjecturl(self, areas, foods):
		
		cityurl = "https://www.meituan.com/changecity/"

		headers = {
			'Host': 'www.meituan.com',
			'Referer': 'https://su.meituan.com/',
			'Sec-Fetch-Mode': 'navigate',
			'Sec-Fetch-Site': 'same-site',
			'Sec-Fetch-User': '?1',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
		}
		
		res = self.session.get(url=cityurl, headers=headers).text
		
		doc = pq(res)
		infos = doc("div .alphabet-city-area .cities").find('a').items()

		
		for info in infos:
			
			_href = info.attr('href').split('.')[0].lstrip('/')
			_area = info.text()
			if areas == _area:
				self.areaid = _href
				break

		foodurl = f"https://{self.areaid}.meituan.com/meishi/c17"
		return foodurl
		
	def getobjectid(self):
		
		headers = {
			'Accept': 'application/json',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'zh-CN,zh;q=0.9',
			'Connection': 'keep-alive',
			'Host': 'nj.meituan.com',
			'Referer': 'https://nj.meituan.com/meishi/c17/',
			'Sec-Fetch-Mode': 'cors',
			'Sec-Fetch-Site': 'same-origin',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

		}

		uuid = self.getobjectuid()
		token = self.encode_token()
		
		res = self.session.get(f"https://{self.areaid}.meituan.com/meishi/api/poi/getPoiList?cityName={self.areas}&cateId=17&areaId=0&sort=&dinnerCountAttrId=&page=2&userId=248564712&uuid={uuid}&platform=1&partner=126&originUrl=https%3A%2F%2Fnj.meituan.com%2Fmeishi%2Fc17%2F&riskLevel=1&optimusCode=10&_token="+str(token),headers=headers).json()
		if res.get('status') == 0:

			totalCounts = res.get('data')#.get('totalCounts')
			print(totalCounts)
			# if totalCounts > 15:
			# 	pages = int(totalCounts/15)
		# for page in pages:

		# 	res = self.session.get(f"https://{self.areaid}.meituan.com/meishi/api/poi/getPoiList?cityName={self.areas}&cateId=17&areaId=0&sort=&dinnerCountAttrId=&page={str(page)}&userId=248564712&uuid={uuid}&platform=1&partner=126&originUrl=https%3A%2F%2Fnj.meituan.com%2Fmeishi%2Fc17%2F&riskLevel=1&optimusCode=10&_token="+str(token),headers=headers)

	def getobjectuid(self):
		
		res = requests.get(f"https://{self.areaid}.meituan.com/")
		uuid = requests.utils.dict_from_cookiejar(res.cookies).get('uuid')
		return uuid


	def encode_token(self):

		ts = int(datetime.datetime.now().timestamp() * 1000)
		token_dict = {
		'rId': 100900,
		'ver': '1.0.6',
		'ts': ts,
		'cts': ts + 100,
		'brVD': [1366, 663],
		'brR': [[1366, 768], [1366, 768], 24, 24],
		'bI': [f'https://{self.areaid}.meituan.com/meishi/c17/', ''],
		'mT': [],
		'kT': [],
		'aT': [],
		'tT': [],
		'aM': '',
		'sign': 'eJwVjbttwzAURXdx8Ur+9KEUgEXgyoCRzgMQ4pPNRCQF8tGAh0jtJTJB5kn2CFPdg4v7OdiM9uSMgMUSNpAaFk+PNxvQ/H4+f76/wPkYMR9TjfRKlFsI0k4+1HJMDo0UkLK/+njJm7kR7eWF8/jOAnqqNrIlBd643DxfpOaw22srNcnUZo1UI+ybpTXl0Ozsy8cZ77g1LimTgVrw/1P10zD2Wiqo1TuD0+r0quZJiLUfOjtPY8fkoJUcZ9VJJplg4vAHW3FKiw=='
		}
		encode = str(token_dict).encode()
		compress = zlib.compress(encode)
		b_encode = base64.b64encode(compress)
		token = str(b_encode, encoding='utf-8')
		return token.replace('/', '%2F').replace('+', '%2B').replace('=', '%3D').replace(':', '%3A')

	

m = Meituan("南京","火锅")
m.getobjectid()