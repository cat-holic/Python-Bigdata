import urllib.request
import datetime
import json
import math

access_key = "XvG2mNKoiQICNgMNoafx4VMTUnqfoO5vgBzk%2Fmx2Q5Zmb9mVVtkve5dC527wO%2FeAOxyoTKGe4XnZrygEmj%2F9Sg%3D%3D"


def get_request_url(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] URL Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:%s" % (datetime.datetime.now(), url))
        return None


# [Code 1]
def getTourPointVisitor(yyyymm, sido, gungu, nPagenum, nItems):
    end_point = "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&YM=" + yyyymm
    parameters += "&SIDO=" + urllib.parse.q                                                                                                                                                                                                                                                                                                        uote(sido)
    parameters += "&GUNGU=" + urllib.parse.quote(gungu)
    parameters += "&RES_NM=&pageNo=" + str(nPagenum)
    parameters += "&numOfRows=" + str(nItems)
    url = end_point + parameters

    retData = get_request_url(url)
    if retData is None:
        return None
    else:
        return json.loads(retData)


# [Code 2]
def getTourPointData(item, yyyymm, jsonResult):
    addrcd = 0 if 'addrCd' not in item.keys() else item['addrCd']
    gungu = '' if 'gungu' not in item.keys() else item['gungu']
    sido = '' if 'sido' not in item.keys() else item['sido']
    resNm = '' if 'resNm' not in item.keys() else item['resNm']
    rnum = 0 if 'rnum' not in item.keys() else item['rnum']
    ForNum = 0 if 'csForCnt' not in item.keys() else item['csForCnt']
    NatNum = 0 if 'csNatCnt' not in item.keys() else item['csNatCnt']

    jsonResult.append({'yyyymm': yyyymm, 'addrCd': addrcd, 'gungu': gungu, 'sido': sido, 'resNm': resNm,
                       'rnum': rnum, 'ForNum': ForNum, 'NatNum': NatNum})


def main():
    jsonResult = []

    sido = "서울특별시"
    gungu = ""
    nPagenum = 1
    nTotal = 0
    nItems = 100

    nStartYear = 2001
    nEndYear = 2017

    for year in range(nStartYear, nEndYear):
        for month in range(1, 13):
            yyyymm = "{0}{1:0>2}".format(str(year), str(month))
            nPagenum = 1

            # [CODE 3.Homenetwork]
            while True:
                jsonData = getTourPointVisitor(yyyymm, sido, gungu, nPagenum, nItems)

                if jsonData['response']['header']['resultMsg'] == 'OK':
                    nTotal = jsonData['response']['body']['totalCount']

                    if nTotal == 0:
                        break
                    for item in jsonData['response']['body']['items']['item']:
                        getTourPointData(item, yyyymm, jsonResult)
                    nPage = math.ceil(nTotal / 100)

                    if nPagenum == nPage:
                        break

                    nPagenum += 1
                else:
                    break
    with open('%s_광광지입장정보_%d_%d.json' % (sido, nStartYear, nEndYear - 1), 'w', encoding='utf-8') as outfile:
        retJson = json.dump(jsonResult, outfile, indent=4, sort_keys=True, ensure_ascii=False)
    print('%s_관광지 입장정보_%d_%d.json Saved' % (sido, nStartYear, nEndYear - 1))


if __name__ == '__main__':
    main()
