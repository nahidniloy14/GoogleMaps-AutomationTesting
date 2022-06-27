import requests
apikey='AIzaSyC_21djKfxgIhoPaUlWH7hZL6GpuI1etyI'
url="https://maps.googleapis.com/maps/api/distancematrix/json?"
BananiCode=destinations=23.795854785548258, 90.40038404967298
MoakhaliCode=origins=23.783956937286288, 90.39501722576492

response=requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?+BananiCode&MoakhaliCode&mode=walking&key=apikey')
print(response.status_code)
print(response.json())
