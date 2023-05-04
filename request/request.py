import requests

url = "https://github.com"
try:
	r = requests.get(url, timeout = 2)
	print(r.status_code) #https yerine http yazsaydık da bizi https e yönlendirecekti. Yönlendirme 
	#olmasın istiyorsak allow_redirects parametresini False a çekmeliyiz!
	print(r.text)
except Exception as e:
	print(e)	
