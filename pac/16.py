from urllib import  request

def youdao(key):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data={

    "i": "girl",
    "from":"AUTO",
    "to":"AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "15615389555401",
    "sign": "3cf046757e17e109f19d1a76e0ccbdfe",
    "ts": "1561538955540",
    "bv": "6463522ba46bac94c96fd37965fadc8d",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTION"
    }

    data = parse.urlencode(data).encode()



    headers = {
    Accept: application / json, text / javascript, * / *; q = 0.01
    Accept - Encoding: gzip, deflate
    Accept - Language: zh - CN, zh;
    q = 0.9
    Cache - Control: no - cache
    Connection: keep - alive
    Content - Length: 241
    Content - Type: application / x - www - form - urlencoded;
    charset = UTF - 8
    Cookie: _ntes_nnid = f9837d06198a5cf4d842ae8170498a6e, 1493109488781;
    OUTFOX_SEARCH_USER_ID = -947028734 @ 123.58
    .182
    .242;
    OUTFOX_SEARCH_USER_ID_NCOO = 1080109820.8104465;
    JSESSIONID = aaavW7riVkdr5cze_9sUw;
    ___rl__test__cookies = 1561538955539
    Host: fanyi.youdao.com
    Origin: http: // fanyi.youdao.com
    Pragma: no - cache
    Referer: http: // fanyi.youdao.com /
                      User - Agent: Mozilla / 5.0(Windows
    NT
    6.1;
    Win64;
    x64) AppleWebKit / 537.36(KHTML, like
    Gecko) Chrome / 75.0
    .3770
    .100
    Safari / 537.36
    X - Requested - With: XMLHttpRequest
    }



