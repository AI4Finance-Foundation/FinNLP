from finnlp.utils.get_proxy import get_china_free_proxy, get_us_free_proxy, Kuaidaili
import requests

class FinNLP_Downloader:
    def __init__(self, args = {}):
        self.use_proxy = True if "use_proxy" in args.keys() else False
        if self.use_proxy:
            self.country = args["use_proxy"]
        else:
            self.country = None
        self.max_retry = args["max_retry"] if "max_retry" in args.keys() else 1
        self.proxy_pages = args["proxy_pages"] if "proxy_pages" in args.keys() else 5
        if self.use_proxy:
            if "kuaidaili" in self.country:
                # tunnel, username, password
                assert "tunnel" in args.keys(), "Please make sure \'tunnel\' in your keys"
                assert "username" in args.keys(), "Please make sure \'username\' in your keys"
                assert "password" in args.keys(), "Please make sure \'password\' in your keys"
                self.proxy_list = Kuaidaili(args["tunnel"], args["username"], args["password"])
            else:
                self.proxy_id = 0
                self.proxy_list = self._update_proxy()
        else:
            self.proxy_list = []   
        
    def _get_proxy(self):
        if self.use_proxy:
            if "kuaidaili" in self.country:
                proxy = self.proxy_list.get_kuaidaili_tunnel_proxy()
                return proxy
            elif len(self.proxy_list) >0:
                proxy = self.proxy_list[self.proxy_id]
                self.proxy_id += 1
                if self.proxy_id == len(self.proxy_list):
                    self.proxy_id = 0 
                return proxy
        else:
            return None

    def _update_proxy(self):
        if "china" in self.country or "China" in self.country:
            return get_china_free_proxy(self.proxy_pages)
        else:
            return get_us_free_proxy(self.proxy_pages)

    def _request_get(self, url, headers = None, verify = None, params = None):
        if headers is None:
            headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0"
            }
        max_retry = self.max_retry
        proxies = self._get_proxy()
        for _ in range(max_retry):
            try:
                response = requests.get(url = url, proxies = proxies, headers = headers, verify = verify, params = params)
                if response.status_code == 200:
                    break
            except:
                response = None

        if response is not None and response.status_code != 200:
            response = None

        return response
    
    def _request_post(self, url, headers, json):
        max_retry = self.max_retry
        proxies = self._get_proxy()
        for _ in range(max_retry):
            try:
                response = requests.post(url = url, headers = headers, json = json, proxies = proxies)
                if response.status_code == 200:
                    break
            except:
                response = None

        if response is not None and response.status_code != 200:
            response = None

        return response
