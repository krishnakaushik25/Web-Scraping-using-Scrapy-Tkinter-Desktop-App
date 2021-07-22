from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode
import json

URL = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22usersSearchTerm%22%3A%22Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.751515256591%2C%22east%22%3A-79.84706574340896%2C%22south%22%3A25.342946787484824%2C%22north%22%3A26.108254806045707%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12700%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%2C%22sortSelection%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D&wants={%22cat1%22:[%22listResults%22],%22cat2%22:[%22total%22]}&requestId=11'


def cookie_parser():
    cookie_string = 'zguid=23|%248ea9631d-f8f7-4dd0-9746-51c02a98e61c; zgsession=1|c72532f3-a7a7-40e9-b23a-4fd8b51d1671; _ga=GA1.2.1086360466.1626967975; _gid=GA1.2.16559926.1626967975; zjs_user_id=null; zjs_anonymous_id=%228ea9631d-f8f7-4dd0-9746-51c02a98e61c%22; _gcl_au=1.1.702683907.1626967979; KruxPixel=true; DoubleClickSession=true; _pxvid=18ae2df2-eb02-11eb-a977-0242ac120007; __pdst=a34aebe7ed5842b88107aacc881f12c6; KruxAddition=true; _fbp=fb.1.1626967989823.2053436736; utag_main=v_id:017aced94df50009b457c27dcded03073001706b00978$_sn:1$_se:1$_ss:1$_st:1626969785656$ses_id:1626967985656%3Bexp-session$_pn:1%3Bexp-session$dcsyncran:1%3Bexp-session$tdsyncran:1%3Bexp-session$dc_visit:1$dc_event:1%3Bexp-session$dc_region:ap-east-1%3Bexp-session; _pin_unauth=dWlkPU1XSTBObVF6WXprdE5qRmpNaTAwTjJabUxXRmpPVGd0WXpoaE5XVmpNemM1T0RrMQ; JSESSIONID=B797493464E827F8EB20D732ABB21472; _px3=0101e03b5ba315fb0e2653b371d7f4f8832d356f655ff3bb9d52d51c836118e7:5urLd+SsV/GaY50cB/bDmHN9bc4yv7cxrW5cZyDDvi39klps2sxP4jNc0F85ZLWBUMxj1BQn8Xp5x2nAPstV/A==:1000:326OXYvJNAHDygU9GJO5mSUQ+TDNaE3h92vxKRuWyd3Xu1Bb2Lq3A6qud/26f2DtH745atO90g1kr6u/pafwRq+DOhu9brdRSgb2eSp1spGoC3ag/nra0SCZds0Ictok4VfZp3+ZpR6QXB22MjM0FnQxs7vtY2UQ94Eiliby1KrEB5YgAV/Wpa7CjZKrdetCJOB5y+ew5eoIEWV8f3jP8Q==; _uetsid=18806b80eb0211ebb61c15ac38472f06; _uetvid=1880c930eb0211eb8ae2bf7b53b75858; AWSALB=iQfjgD8+UczFRozvXBJt3S12ddqnY1rgLmoXi0TzvbFV4q5OCu0z2cuOO9v3bD501+W3KAErKxLVjZ2kxbc2Bw/y+BG7kEjmsTxbN2uBaM9jrDS3RFRmItA8DNDj; AWSALBCORS=iQfjgD8+UczFRozvXBJt3S12ddqnY1rgLmoXi0TzvbFV4q5OCu0z2cuOO9v3bD501+W3KAErKxLVjZ2kxbc2Bw/y+BG7kEjmsTxbN2uBaM9jrDS3RFRmItA8DNDj; search=6|1629560227094%7Crect%3D26.108254806045707%252C-79.84706574340896%252C25.342946787484824%252C-80.751515256591%26rid%3D12700%26disp%3Dmap%26mdm%3Dauto%26p%3D2%26z%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%09%0912700%09%09%09%09%09%09; _gat=1'
    cookie = SimpleCookie()
    cookie.load(cookie_string)

    cookies = {}

    for key, morsel in cookie.items():
        cookies[key] = morsel.value

    return cookies


def parse_new_url(url, page_number):
    url_parsed = urlparse(url)
    query_string = parse_qs(url_parsed.query)
    search_query_state = json.loads(query_string.get('searchQueryState')[0])
    search_query_state['pagination'] = {"currentPage": page_number}
    query_string.get('searchQueryState')[0] = search_query_state
    encoded_qs = urlencode(query_string, doseq=1)
    new_url = f"https://www.zillow.com/search/GetSearchPageState.htm?{encoded_qs}"
    return new_url
