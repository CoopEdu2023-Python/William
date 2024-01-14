import requests
import pandas as pd

area = ('河北', '山西', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '海南', '四川', '贵州', '云南', '陕西', '甘肃', '青海', '台湾', '内蒙古', '广西', '西藏', '宁夏', '新疆', '北京', '天津', '上海', '重庆', '香港', '澳门', '中国台湾', '巴西', '意大利', '英国', '中国', '越南', '加拿大', '西班牙', '委内瑞拉', '中国澳门', '柬埔寨', '布隆迪', '新加坡', '塞浦路斯', '乌干达', '马来西亚', '澳大利亚', '日本', '爱尔兰', '莫桑比克', '缅甸', '塞尔维亚', '德国', '俄罗斯', '以色列', '波兰', '菲律宾', '韩国', '摩洛哥')
area_dict = dict()
for i in area:
    response = requests.get(url=f'http://api.tianditu.gov.cn/geocoder?ds={{"keyWord":"{i}"}}&tk=b170f9a6a9bcdcf2ae56f016ba8c3a50')
    area_dict[i] = (response.json()['location']['lon'], response.json()['location']['lat'])

lon = list()
lat = list()
area_name = list()
csv_file_path = "评论信息.csv"
data = pd.read_csv(csv_file_path)

# 提取某一列的全部内容
desired_column = 'ip地址'
column_values = data[desired_column]
# 打印提取的列内容
for ip in column_values:
    if ip in area:
        area_name.append(ip)
        lon.append(area_dict[ip][0])
        lat.append(area_dict[ip][1])

print(len(lat))
with open('位置信息/lat.txt', 'w', encoding='utf-8') as f:
    f.write(str(lat))
print(len(lon))
with open('位置信息/lon.txt', 'w', encoding='utf-8') as f:
    f.write(str(lon))
print(len(area_name))
with open('位置信息/area.txt', 'w', encoding='utf-8') as f:
    f.write(str(area_name))


with open('位置信息/lat.txt', 'r', encoding='utf-8') as f:
    lat = f.read()
with open('位置信息/lon.txt', 'r', encoding='utf-8') as f:
    lon = f.read()
with open('位置信息/area.txt', 'r', encoding='utf-8') as f:
    area_name = f.read()

lat = lat.replace('[', '').replace(']', '').split(', ')
lon = lon.replace('[', '').replace(']', '').split(', ')
area_name = area_name.replace('[', '').replace(']', '').split(', ')
float_lat = [float(x) for x in lat]
float_lon = [float(x) for x in lon]
location_lat_lon = list()
for i in range(len(float_lon)):
    location_lat_lon.append((area_name[i].strip("'"), float_lat[i], float_lon[i]))

location_lat_lon_size = dict()
location_list = list()
for i in location_lat_lon:
    if i in location_list:
        location_lat_lon_size[i] += 1
    else:
        location_lat_lon_size[i] = 0
        location_list.append(i)
print(location_lat_lon_size)

with open('位置信息/location.csv', 'w', encoding='utf-8') as f:
    f.write(f'地名,lat,lon,size,人数,\n')
for i in location_lat_lon_size.items():
    print(i)
    with open('位置信息/location.csv', 'a+', encoding='utf-8') as f:
        f.write(f"{i[0][0]},{i[0][1]},{i[0][2]},{i[1]*120+9000},{i[1]+1}\n")