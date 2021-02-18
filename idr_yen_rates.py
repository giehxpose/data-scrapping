import requests

rates = requests.get('http://www.floatrates.com/daily/idr.json')
usd_yen = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":7.1551272159193e-5,"date":"Mon, 15 Feb 2021 00:00:02 GMT","inverseRate":13975.991898161},"jpy":{"code":"JPY","alphaCode":"JPY","numericCode":"392","name":"Japanese Yen","rate":0.0075103182959881,"date":"Mon, 15 Feb 2021 00:00:02 GMT","inverseRate":133.15014898026}}

for rate in usd_yen.values():
    print(rate)