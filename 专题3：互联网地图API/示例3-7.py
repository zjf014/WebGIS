# 导入库
import requests
import json
import shapefile


def get_single_line(mykey, city_name, line_name):

    url = "https://restapi.amap.com/v3/bus/linename?s=rsv3&extensions=all&key={}&output=json&" \
          "city={}&offset=1&keywords={}&platform=JS".format(mykey, city_name, line_name)

    try:
        response = requests.get(url) 
        response = json.loads(response.text)       
        if response["buslines"]:
            mn = response["buslines"][0]

            nodes = mn["polyline"].split(";")
            polyline = []
            
            for i in range(len(nodes)):
                node = nodes[i]
                lng = float(node.split(",")[0])
                lat = float(node.split(",")[1])
                polyline.append([lng,lat])

            # 转化为shp文件
            w = shapefile.Writer(r"./{}/line.shp".format(city_name))
            w.field("line_name", "C")
            w.field("start_time", "C")
            w.field("end_time", "C")
            w.field("start_stop", "C")
            w.field("end_stop", "C")
            w.field("distance", "C")

            w.line([polyline])
            w.record(mn["name"], mn["start_time"], mn["end_time"], mn["start_stop"],
                    mn["end_stop"], mn["distance"], encode="gbk")
            w.close()
               
    except Exception as ex:
        print(ex,"{}数据爬取失败".format(line_name))



if __name__ == "__main__":

    # 将下面的key替换为自己申请的key
    key = "4d21cc2460446089d808875fb7cd9598"
    # 将城市名称改为自己需要获取的城市的名称，如北京市，只要填写北京，如果填写北京市可能会报错
    city_name = "大连"
    # 将线路名称改为你需要的线路名称
    line_name = '101路'
    get_single_line(key, city_name, line_name)
