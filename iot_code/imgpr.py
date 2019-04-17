########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
import simplejson as json
import os

headers = {
    # Request headers
    #'Content-Type': 'application/json',
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '1dd4a62c4e9c4146bff1321119f85a49',
}

params = urllib.parse.urlencode({
    # Request parameters
    'language': 'unk',
    'detectOrientation ': 'true',
})

try:
    conn = http.client.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
    body = open('/home/pi/piproject/images/car.jpg', 'rb').read()
    #body = json.dumps({"url" : "https://cdni.autocarindia.com/Utils/ImageResizer.ashx?n=http%3a%2f%2fcdni.autocarindia.com%2fExtraImages%2f20180402113123_NumberPlate_Swift.jpg&h=578&w=872&c=0"})
    conn.request("POST", "/vision/v1.0/ocr?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    dictio = json.loads(data)
    plate_text = dictio['regions'][0]['lines'][0]['words']
    str = ""
    for x in plate_text:
        str = str + x['text']
        # print(x)
    print ("Number Plate : ", str)
    with open('/home/pi/piproject/plate.txt', 'w') as f:
        f.write(str)
    f.close()
    # print(dictio['regions'][0]['lines'][0]['words'][0]['text'])
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
