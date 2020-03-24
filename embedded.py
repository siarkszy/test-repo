import urllib, urllib2, cookielib

username = 'admin'
password = 'mypassword'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'username' : username, 'j_password' : password})
opener.open('http://tieto.com/supersecret/login.php', login_data)
print resp.read()
