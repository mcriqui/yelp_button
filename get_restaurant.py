import requests

url = 'https://api.yelp.com/v3'
payload = {'some': 'data'}
headers = {'Authorization': 'Bearer <ZQW4OUEmZLNms1q8gHMdt67uYf3t_XchM4uMcsx_r0m0l5IhqPSa_Wrjw6KI9aE5VaKxigJLC7oTB69MZQ9RjvfWGGfiNi9YSgqd9gkLuR7saQDexvYhG8VheXA1W3Yx>'}

r = requests.get(url, headers=headers)

restaurants = requests.get('https://api.yelp.com/v3/businesses/restaurants')

print restaurants
