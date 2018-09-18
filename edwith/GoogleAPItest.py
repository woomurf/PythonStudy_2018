import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address':address})
    # address = address 이다. ?address=지역+어쩌구&저쩌구 -> 변환 과정은 encode가 해준다.

    print('Retrieving: ', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved: ',len(data),'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js,indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat',lat, 'lng',lng)
    location = js['results'][0]['formatted_address']
    print(location)
