import requests
import json
import jsonpath
import fontTools

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Referer': 'https://h5.waimai.meituan.com/waimai/mindex/home',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://h5.waimai.meituan.com',
    'Connection': 'keep-alive',
}
cookies = {
    '_lx_utm': 'utm_source%3DBaidu%26utm_medium%3Dorganic',
    '_lxsdk_cuid': '16c2302ab6dc8-0a3d0f563d6c22-14367940-1aeaa0-16c2302ab6ec8',
    '_lxsdk': '16c2302ab6dc8-0a3d0f563d6c22-14367940-1aeaa0-16c2302ab6ec8',
    'wm_order_channel': 'default',
    'utm_source': '',
    'terminal': 'i',
    'w_utmz': 'utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)',
    'openh5_uuid': '16c2302ab6dc8-0a3d0f563d6c22-14367940-1aeaa0-16c2302ab6ec8',
    'w_latlng': '36657209,117055413',
    'w_actual_lat': '0',
    'w_actual_lng': '0',
    'cssVersion': '9968de10',
    'au_trace_key_net': 'default',
    '_lxsdk_s': '16c2c23ca54-8d5-31a-b59%7C%7C55',
    'uuid': '16c2302ab6dc8-0a3d0f563d6c22-14367940-1aeaa0-16c2302ab6ec8',
    'igateApp': 'custom',
    'w_uuid': '16c2302ab6dc8-0a3d0f563d6c22-14367940-1aeaa0-16c2302ab6ec8',
    'mtsi-real-ip': '60.208.74.98',
    'mtsi-cur-time': '2019-07-26 11:02:55',
    'w_visitid': '0a2aadc8-ed0a-419d-b086-8546a9a5e0c0',
}


params = (
    ('_', '1564110538926'),
    ('X-FOR-WITH', '4CH20e1RM5tFPC3ysgcEMB2eNihocq70OCgAZlOxM6ErimvsViyCQWHTX3s9O5sr5notM0IjX2yiTvX5yQOTNeumO+bn/AmDSF4ilrVVhVYYnuC+CUNIhWdAeJSq7u4Rz2GwjLsUrxG6B4u8Y0P7lw=='),
)
data = {
  'startIndex': '4',
  'sortId': '0',
  'multiFilterIds': '',
  'sliderSelectCode': '',
  'sliderSelectMin': '',
  'sliderSelectMax': '',
  'geoType': '2',
  'rankTraceId': 'E7BE070C8CAF616576DFC1828EAACE84',
  'uuid': '16c2302ab6dc8-0a3d0f563d6c22-14367940-1aeaa0-16c2302ab6ec8',
  'platform': '3',
  'partner': '4',
  'originUrl': 'https://h5.waimai.meituan.com/waimai/mindex/home',
  'riskLevel': '71',
  'optimusCode': '10',
  'wm_latitude': '36657209',
  'wm_longitude': '117055413',
  'wm_actual_latitude': '0',
  'wm_actual_longitude': '0',
  'openh5_uuid': '16c2302ab6dc8-0a3d0f563d6c22-14367940-1aeaa0-16c2302ab6ec8',
  '_token': 'eJxVj9uOokAQht+FW43dICdN5gJBAcEDIqhM5gKksRlsQGgRney7b092NptNKvmrvvorVfXFNXbKTXnIK5Afch1quCnHj+BI5oYcbVlHkkWeh9JYkBVpyJ3/Y+pEYCxpQoObvo9ZX5aVj2+wY/U/8M7LKhyyHfBjKIgsvj02s3CY0rqdAoCl0SPOSZyPCMrpPS5H54qAPwiQvExRD3BFEDuKY8Nkz4aZFj8a/yj9W6/YF8zb5peSZWj5vBYrenu8NG+XqVd9AH1/rNj7Yu7y4+ACHTlu2nVAWi9HGEcJdUAj1brvdtQvdfFzJU/y51YeI2TbeSqsr4uO2sWJksrvbVBhUoEXXy17EiI4e6F75K6LwsGyY+U4qMSj4jzF7UGu562pL3V06PG1UKV5glCtPqpFpXpWlu7v7u7S9wbeGHwhhE77ijUqR6FlmWnvoLqbVKv+VgPdN1IxN/3FHEMziAzPM17SKYg0TWk817bMZrdQwaTxyTHd8KYqiWG2KfdnFHebMqH3e1JcvEkZKb0mCpUZkVWIMYKxvgoVmklacM/EmaBnFw9CFOwNa5m4IIWlC0qE28lztj8r622X2vPn6Yi8wWCTAv/gHPMbWW/5RSo+P9cHeCvqg+uK2lHIE/h4e+N+/QYm5b9y'
}

response = requests.post('https://i.waimai.meituan.com/openh5/homepage/poilist', headers=headers, params=params, cookies=cookies, data=data)

js = json.loads(response.text)
print(js)





