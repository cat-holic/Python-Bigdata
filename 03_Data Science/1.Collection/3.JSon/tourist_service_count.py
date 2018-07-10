import urllib.request
import datetime
import json

access_key = "XvG2mNKoiQICNgMNoafx4VMTUnqfoO5vgBzk%2Fmx2Q5Zmb9mVVtkve5dC527wO%2FeAOxyoTKGe4XnZrygEmj%2F9Sg%3D%3D"
nation_dic = {}


def get_request_url(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s" % (datetime.datetime.now(), url))
        return None


# [Code 1]
def getNatVistior(yyyymm, nat_cd, ed_cd):
    end_point = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList?"

    parameter = "_type=json&serviceKey=" + access_key
    parameter += "&YM=" + str(yyyymm)
    parameter += "&NAT_CD=" + nat_cd
    parameter += "&ED_CD=" + ed_cd

    url = end_point + parameter

    retData = get_request_url(url)

    if retData is None:
        return None
    else:
        return json.loads(retData)


def main():
    with open("national_code_selected.txt", 'r', encoding='utf-8-sig') as readfile:
        a = readfile.readlines()
        for i in a:
            i = i.replace('\n', '').replace(' ', '')
            nation_dic[i[4:]] = i[:3]
    nation_code_list = nation_dic.values()
    jsonResult = []

    # 중국 :112/ 일본:130 / 미국:275

    # national_code = "112"
    ed_cd = "E"

    nStartYear = 2017
    nEndYear = 2017
    for code in nation_code_list:
        for year in range(nStartYear, nEndYear + 1):
            for month in range(12, 13):
                yyyymm = "{0}{1:0>2}".format(year, month)
                jsonData = getNatVistior(yyyymm, code, ed_cd)

                if jsonData['response']['header']['resultMsg'] == 'OK':
                    krName = jsonData['response']['body']['items']['item']['natKorNm']
                    krName = krName.replace(' ', '')
                    iTotalvisit = jsonData['response']['body']['items']['item']['num']
                    print("%s_%s:%s" % (krName, yyyymm, iTotalvisit))
                    jsonResult.append([krName, iTotalvisit])

    sortResult = sorted(jsonResult, key=lambda a: a[1],reverse=True)
    print(sortResult)
    # jsonResult.append(
    #     {'nat_name': krName, 'nat_cd': national_code, 'yyyymm': yyyymm, 'visit_cnt': iTotalvisit})

    # cnVisit = []
    # VisitYM = []
    # index = []
    # i = 0
    # for item in jsonResult:
    #     index.append(i)
    #     cnVisit.append(item['visit_cnt'])
    #     VisitYM.append(item['yyyymm'])
    #     i += 1
    with open('%s해외방문색 순위.json' % nStartYear, 'w', encoding='utf-8') as outfile:
        json.dump(sortResult, outfile, indent=4, sort_keys=True, ensure_ascii=False)


if __name__ == "__main__":
    main()
