import urllib.request
import json
import time
import datetime
import os


class WeaTherDate:
    def __init__(self):
        self.access_key = "iVy1CxcjAjAw8Cbsd%2BaBCmEAhd0Y2MqECSVJ3ziFK%2FZvuBBFNCgL0oyiBiuWLb4dnCZfBB00d4vkSoakGqYS4w%3D%3D"
        self.repo_base_name = "whether_bigdata"
        self.dir_delimeter = "/"
        self.depth_level2_name = "whether_info"
        self.file_limit = 3

        if not os.path.exists('.' + self.dir_delimeter + self.repo_base_name):
            self.make_base_dir()
        if not os.path.exists('.' + self.dir_delimeter + self.repo_base_name +
                              self.dir_delimeter + self.depth_level2_name + '1'):
            self.make_depth2_dir('1')

        self.json_weather_result = []
        self.yyyymmdd = time.strftime('%Y%m%d')
        self.day_time = time.strftime('%H%M')
        self.day_hour = time.strftime('%H')
        self.day_min = time.strftime('%M')
        self.day_sec = time.strftime('%S')
        self.x_cordinate = "89"
        self.y_cordinate = "91"
        self.get_Realtime_Weather_info()

    def make_base_dir(self):
        os.mkdir("." + self.dir_delimeter + self.repo_base_name)

    def make_depth2_dir(self, dir_num):
        os.mkdir("." + self.dir_delimeter + self.repo_base_name +
                 self.dir_delimeter + self.depth_level2_name + str(dir_num))

    def get_directory_num(self):
        dir_num = len(os.listdir('.' + self.dir_delimeter + self.repo_base_name))
        if len(os.listdir('.' + self.dir_delimeter + self.repo_base_name +
                          self.dir_delimeter + self.depth_level2_name + str(dir_num))) >= self.file_limit:
            dir_num += 1
            self.make_depth2_dir(dir_num)
        return dir_num

    def get_request_url(self, url):
        req = urllib.request.Request(url)

        try:
            response = urllib.request.urlopen(req)
            if response.getcode() == 200:
                print("[%s] URL Requset Success" % datetime.datetime.now())
                return response.read().decode('utf-8')
        except Exception as e:
            print(e)
            print("[%s] Error for URL : %s " % (datetime.datetime.now(), url))
            return None

    def get_weather_url(self, day_time):
        end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

        parameta = "?"
        parameta += "ServiceKey=" + self.access_key
        parameta += "&_type=" + "json"
        parameta += "&base_date=" + self.yyyymmdd
        parameta += "&base_time=" + day_time
        parameta += "&nx=" + self.x_cordinate
        parameta += "&ny=" + self.y_cordinate
        parameta += "&numOfRows=100"
        url = end_point + parameta

        url_data = self.get_request_url(url)
        print(url)
        if url_data is None:
            return None
        else:
            return json.loads(url_data)

    def make_whether_json(self, day_time):
        jsonData = self.get_weather_url(day_time)
        if jsonData['response']['header']['resultMsg'] == 'OK':
            for prn_data in jsonData['response']['body']['items']['item']:
                self.json_weather_result.append({'baseDate': prn_data.get('baseDate'),
                                                 'baseTime': prn_data.get('baseTime'),
                                                 'category': prn_data.get('category'),
                                                 'fcstDate': prn_data.get('fcstDate'),
                                                 'fcstTime': prn_data.get('fcstTime'),
                                                 'fcstValue': prn_data.get('fcstValue'),
                                                 'nx': prn_data.get('nx'),
                                                 'ny': prn_data.get('ny')})

        with open(".%s%s%s%s%s%s동구_신암동_초단기예보조회_%s%s%s" % (
                self.dir_delimeter, self.repo_base_name, self.dir_delimeter,
                self.depth_level2_name, self.get_directory_num(),
                self.dir_delimeter, self.yyyymmdd, self.day_time, self.day_sec),
                  'w', encoding='utf-8') as outfile:
            json.dump(self.json_weather_result, outfile, indent=4, sort_keys=True, ensure_ascii=False)

    def get_Realtime_Weather_info(self):
        day_min_int = int(self.day_min)
        if 30 < day_min_int < 59:
            day_time = time.strftime("%H%M", time.localtime(time.time()))
            print("\n<<실시간 기상정보 업데이트를 실시합니다!!>>\n".center(30))
            self.make_whether_json(day_time)
        elif 0 <= day_min_int <= 30:
            day_hour_int = int(self.day_hour)
            day_hour_int -= 1
            revised_min = 60 + (day_min_int - 30)
            day_time = "{0:0>2}".format(day_hour_int) + str(revised_min)
            print("\n<<실시간 기상정보 업데이트를 실시합니다!!>>\n".center(30))
            self.make_whether_json(day_time)

    def get_rain_value(self):
        rp = []
        for item in self.json_weather_result:
            if item['category'] == 'RN1':
                rp.append({'time': item['fcstTime'], 'value': item['fcstValue']})

        recent = 0
        temp = rp[0]['time']
        for item in rp:
            if temp >= item['time']:
                temp = item['time']
                recent = item['value']
        return int(recent)

    def get_humidity_value(self):
        hum = []
        for item in self.json_weather_result:
            if item['category'] == 'REH':
                hum.append({'time': item['fcstTime'], 'value': item['fcstValue']})
        recent = 0
        temp = hum[0]['time']
        for item in hum:
            if temp >= item['time']:
                temp = item['time']
                recent = item['value']
        return int(recent)

    def get_rain_humidity(self):
        rain = self.get_rain_value()
        humidity = self.get_humidity_value()

        return {'rain': rain, 'humidity': humidity}

