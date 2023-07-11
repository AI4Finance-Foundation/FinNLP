import requests
import parsel
from lxml import etree
from tqdm import tqdm
import time
import re

def check_china_ips(proxies_list):
    """检测ip的方法"""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}
    
    can_use = []
    for proxy in tqdm(proxies_list, desc = "Checking ips"):
        try:
            response = requests.get('http://www.baidu.com', headers=headers, proxies=proxy, timeout=1)  # 超时报错
            if response.status_code == 200:
                can_use.append(proxy)
        except Exception as error:
            # print(error)
            pass
    return can_use

def check_us_ips(proxies_list):
    """检测ip的方法"""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}

    can_use = []
    for proxy in tqdm(proxies_list, desc = "Checking ips"):
        try:
            response = requests.get('http://www.google.com', headers=headers, proxies=proxy, timeout=1)  # 超时报错
            if response.status_code == 200:
                can_use.append(proxy)
        except Exception as error:
            # print(error)
            pass
    return can_use

def get_china_free_proxy(pages = 10):
    proxies_list = []
    for page in tqdm(range(1, pages+1), desc = "Gathering free ips by pages..."):

        base_url = f'https://www.kuaidaili.com/free/inha/{page}'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}
        success = False
        while not success:
            try:
                response = requests.get(base_url, headers=headers)
                data = response.text
                res = etree.HTML(data)
                trs = res.xpath('//table/tbody/tr')
                if len(trs)!=0:
                    success = True
                    for tr in trs:
                        proxies_dict = {}
                        http_type = tr.xpath('./td[4]/text()')[0]
                        ip_num = tr.xpath('./td[1]/text()')[0]
                        port_num = tr.xpath('./td[2]/text()')[0]
                        proxies_dict[http_type] = ip_num + ':' + port_num
                        proxies_list.append(proxies_dict)
                else:
                    time.delay(0.01)
      
            except:
                pass

    can_use = check_china_ips(proxies_list)

    print(f'获取到的代理ip数量: {len(proxies_list)} 。Get proxy ips: {len(proxies_list)}.')
    print(f'能用的代理数量： {len(can_use)}。Usable proxy ips: {len(can_use)}.' )

    return can_use

def get_us_free_proxy(pages = 10):
    url = "https://openproxy.space/list/http"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Connection Error. Please make sure that your computer now have the access to Google.com")
    res = etree.HTML(response.text)
    http_type = "HTTP"
    proxies_list = []

    scripts = res.xpath("//script")
    content = scripts[3].xpath(".//text()")
    pattern = re.compile('LIST",data:(.+),added:')
    result_list = pattern.findall(content[0])
    result_list = result_list[0].strip("[{").strip("}]").split("},{")

    for result in result_list:
        pattern = re.compile('\[(.+)\]')
        result = pattern.findall(result)
        result = result[0].split(",")
        result = [r.strip("\"") for r in result]
        for ip in result:
            proxies_list.append(
                {http_type: ip}
            )
    total = pages* 15
    proxies_list = proxies_list[:total] 
    can_use = check_us_ips(proxies_list)
    print(f'Get proxy ips: {len(proxies_list)}.')
    print(f'Usable proxy ips: {len(can_use)}.' )

    return can_use

class Kuaidaili:
    def __init__(self, tunnel, username, password):
        self.tunnel = tunnel
        self.username = username
        self.password = password

    def get_kuaidaili_tunnel_proxy(self):
        proxies = {
            "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": self.username, "pwd": self.password, "proxy": self.tunnel},
            "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": self.username, "pwd": self.password, "proxy": self.tunnel}
        }
        return proxies