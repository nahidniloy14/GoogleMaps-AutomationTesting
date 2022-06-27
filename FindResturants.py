import requests
apikey='AIzaSyC_21djKfxgIhoPaUlWH7hZL6GpuI1etyI'

url='https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
locationBias='locationbias=circle%3A2000%4047.6918452%2C-122.2226413'

response=requests.get('https://maps.googleapis.com/maps/api/place/findplacefromtext/json?+input=Resturants&inputtype=textquery&locationBias&key=apikey')
print(response.status_code)
print(response.json())
