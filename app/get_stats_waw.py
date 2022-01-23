import json
from typing import Dict
import urllib.request as request
from datetime import datetime


def get_json(link: str) -> int:
    with request.urlopen(link) as url:
        data = json.loads(url.read().decode())
    return data


def assign_area_category(flat_area: int) -> str:
    if flat_area <= 20:
        category = '20_or_less'
    elif flat_area <= 30:
        category = '20_30' 
    elif flat_area <= 40:
        category = '30_40' 
    elif flat_area <= 50:
        category = '40_50' 
    elif flat_area <= 60:
        category = '50_60' 
    elif flat_area <= 70:
        category = '60_70' 
    elif flat_area <= 80:
        category = '70_80' 
    else:
        category = '80_or_more'
    return category


def get_month_num(date: str = None) -> str:
    str_date = datetime.strptime(date, '%Y-%m-%d')
    return str_date.strftime("%Y-%m")


def get_price_size_category(flat: Dict = None, link: str = None) -> int:
    data = get_json(link)
    price_m_loc_area_cat = data['price_m_loc_area_cat']

    flat_location = flat.location
    flat_area_category = assign_area_category(flat.area)
    flat_month_num = get_month_num(flat.date)

    for elem in price_m_loc_area_cat:
        if elem['location'] == flat_location:
            if elem['flat_area_category'] == flat_area_category:
                if elem['month_num'] == flat_month_num:
                    return elem['avg_price_per_m']


def get_price_history(ad_id: str = None) -> Dict:
    link_price_history = "https://raw.githubusercontent.com/mbalcerzak/warsaw_flats_api/raspberry-updates/json_dir/latest_changes.json"
    data = get_json(link_price_history)

    return data[ad_id]


if __name__ == "__main__":
    link_stat_prices = "https://raw.githubusercontent.com/mbalcerzak/warsaw_flats_api/raspberry-updates/json_dir/flats.json"

    flat = {"location": "Bemowo",
            "area": 27,
            "month_num": "2021-01",
            "avg_price_per_m": 11601,
            "num_flats": 2,
            "month": "January2021"}

    # TODO WTF
    """"
    File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 507, in open
    req.timeout = timeout
    AttributeError: 'dict' object has no attribute 'timeout'
    """

    # print(get_price_size_category(link_stat_prices, flat))

    # print(get_price_history("10010275453741012520720209"))