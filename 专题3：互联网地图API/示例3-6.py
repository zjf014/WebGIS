
import json
import requests


def getPOI():
    url = 'https://api.map.baidu.com/place/v2/search?query=%E5%B0%8F%E5%AD%A6&tag=%E5%B0%8F%E5%AD%A6&region=%E5%A4%A7%E8%BF%9E&ret_coordtype=gcj02ll&output=json&ak=DVemu7RUOx6XTjUDBSmxBIMtbPugRKwD&page_size=20'
    req = requests.get(url)
    json_data = json.loads(req.text)

    count=0  # 序号

    f = open("poi.csv", 'w+', encoding='gbk') 

    if json_data['status'] == 0:
        total = json_data['total']

        for i in range(total//20+1):
            url_page = url + '&page_num={}'.format(i)
            # print(url_page)
            req = requests.get(url_page)
            json_data = json.loads(req.text)
            for locs in json_data['results']:
                count+=1
                print(count,locs['name'],locs['location']['lng'],locs['location']['lat'],locs['address'],sep=',',file=f)

    f.close()


if __name__ == '__main__':
    getPOI()
