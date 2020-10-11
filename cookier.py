import requests

class Cookier:
    
    def check(self, url):
        if url.startswith('http://'):
            target = url
        else:
            target ='http://' + url;

        req = requests.get(target)

        print(req.cookies)
        cookies = dict(admin=True)
        cookie_req = requests.get(target, cookies=cookies)

        for cookie in req.cookies:
                print("Name:", cookie.name)
                print("Value:", cookie.value)
                print("Domain:", cookie.domain)
                print("Path:", cookie.path)
                print("Secure", cookie.secure)
                print("HTTP", self.check_http_only(cookie))

    def check_http_only(self, xd):
        if 'http_only' in xd.__rest.keys():
            return True            
        else :
            return False

