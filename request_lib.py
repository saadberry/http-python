import requests

# payload = {'username':'saad', 'password': 'abc'}
# r = requests.post("https://httpbin.org/post", data=payload)

# print((r.text))
# print(r.status_code)
# print(r.json())
# print(r.url)

# setting json value to a variable
# r_dict = r.json()
# print(r_dict['form'])


##USING AUTHENTICATION
# credentials = {'username':'saad', 'password': 'abc'}
r = requests.get('https://httpbin.org/basic-auth/saad/abc',timeout=3)
# print(r.text)
print(r)

# with open('comic.png', 'wb') as f:
#     f.write(r.content)