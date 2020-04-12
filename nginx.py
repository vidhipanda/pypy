# Author: Vidhi Panda <vidhimpanda@gmail.com>
# Parsing log files

import requests


def main():
    url = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
    x = requests.get(url)
    logsdata = x.text
    loglines = logsdata.split("\n")
    ips = []
    for logline in loglines:
        logarr = logline.split(' ')
        ips.append(logarr[0])
    unique_ips = list(set(ips))
    for ip in unique_ips:
        print(ip)


main()
