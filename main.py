import os, requests, re

headers = {
    "authority": "www.tiktok.com",
    "method": "GET",
    "path": "/@yogchill/video/7314834173980757294",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "referer": "https://www.tiktok.com/logout?redirect_url=https%3A%2F%2Fwww.tiktok.com%2F%40yogchill%2Fvideo%2F7314834173980757294",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9156 Chrome/124.0.6367.243 Electron/30.2.0 Safari/537.36",
    'cookie': '_ttp=2dPRamoNAZWcoE1Heo3IaeyFhOI; s_v_web_id=verify_lura7jf2_nVWBwA20_4pQJ_4BN5_9XyA_jSMDS3YTJ7lN; tt_csrf_token=kZf4Dw7U-nq1v3QGWMbddj9gYjBqOjMVmukw; tt_chain_token=Ef5dzsREMXkQFpQyr/X8BQ==; tiktok_webapp_theme_auto_dark_ab=1; store-country-code=ua; store-country-code-src=uid; csrf_session_id=71307740677ada600742556f61d959fb; delay_guest_mode_vid=0; cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22hubspot%22:true%2C%22version%22:%22v10%22}; ak_bmsc=80D8D33A7B3D700336672AC1036FA9FB~000000000000000000000000000000~YAAQ2gNJFywiCSuRAQAAsmv2OxicDfVlrJmlBdRRAn8qeGNhsJfwCI4fZpqpYwjPhcAffmIVQfhRI/qPq78oo19SDRFXpYELwC0L+4veCqdokP5tz2xVE3rAHiS+Jk+EFpfElklTjM950NsyLFJobPtnVUCPYeBA/N9qClDJgmGzPb/LLHt1ioVVKz3YRFVusL5NWfuiaZFi6cGGDjWa2ImPsJasZXcJuQfzwSshaKgaDhl6QokCPq513AHGRlXK4BEYdGLexa0P/oyavzpX3hswWDbNahdlpSFDm32pwZQY1IqtsE7jHHfQJSncMca3GaL4R30u9G/XJWcYOXAbfGunhVAfZ6Z30apS3NnYbWoi8z2/kDJdKFBZGEG5LjsWPfCRMAfsZ2G4ow==; passport_csrf_token=31d03e3c38cef3d581c7ee7b5a532c8e; passport_csrf_token_default=31d03e3c38cef3d581c7ee7b5a532c8e; odin_tt=4773cd8e2ecd89230bd19fefb77d106cbec93bad67cd027795b6ed749c141340; sid_guard=59cf9b05d137e777f89dfd38e6e25096%7C1723289366%7C21600%7CSat%2C+10-Aug-2024+17%3A29%3A26+GMT; uid_tt=ca6f99b26085c9c7b4ffad12ce7916e7; uid_tt_ss=ca6f99b26085c9c7b4ffad12ce7916e7; sid_tt=59cf9b05d137e777f89dfd38e6e25096; sessionid=59cf9b05d137e777f89dfd38e6e25096; sessionid_ss=59cf9b05d137e777f89dfd38e6e25096; sid_ucp_v1=1.0.0-KDI3ZGJhYmI1ZWJjZTE5N2ViZTlmYWUyNjU3OTk3MDFhZGZlMjcxZDQKCRCWnt21BhizCxADGgZtYWxpdmEiIDU5Y2Y5YjA1ZDEzN2U3NzdmODlkZmQzOGU2ZTI1MDk2; ssid_ucp_v1=1.0.0-KDI3ZGJhYmI1ZWJjZTE5N2ViZTlmYWUyNjU3OTk3MDFhZGZlMjcxZDQKCRCWnt21BhizCxADGgZtYWxpdmEiIDU5Y2Y5YjA1ZDEzN2U3NzdmODlkZmQzOGU2ZTI1MDk2; tiktok_webapp_theme_source=system; tiktok_webapp_theme=dark; ttwid=1%7CM3e0PcCzYXfvvr8CTzxrYOIWuxBDVu_vu4dc1aGo0b4%7C1723289369%7Cbd1ad28c2d509492f8d18742ade8c5522cebcd3310b7b92a265d320d125d4588; msToken=ZDJm-Po5T2LPbz06dG2SukGAdojO1snIPBlpsXgGx81j9u_xRQ6H6H7MW11Epqh-Q15UQuEuSS8wPJH-hRAKOOFq77n2HkOZPdYFW1em_X54Vc2tmSt-j5RSuJ-pcZZmsbt9tVUi36UB-5tJa82Hdk7rrg==; msToken=Wv6IfS9lhhrxDP_UagcO9Vd1sWT-pmvxntFsEgIKB-fnCfJs9JIF0X575VAQMBXw4H2dWxTRUHGlXbinG9xVSAfUz9Z9I8pm1kGcgGHw2b8dimlZEIWUAtMQrYO_MIyIVOwPKf11tCQ8CCe6O9CZkx9Rkw==; bm_sv=BD40DE16049E89A3D130607F0AC6774B~YAAQ4ANJF5SH2jWRAQAARnYNPBgJUjPMY96lEbETgw1eA9mJdYSV7UDVPyy7uXDPGUxIBW86OuCjif0oWQ9h7qTbDyXSkvEW0LEp2RwT+weps3pDPCS1X6Lg+506T9XG0RHCbsfo+6/4eYNsJP5dG0BEaxYbMcks12f8Uc8vQcw17Kncs2b17LfOk1h4sYSbvR2983c/nGtOWVYpA91Sx8V75jn9+h1gjhb5SvWlSdW8FbDXeErnOKkj/mPeNnzKzw==~1'
}

need = input('video url (example: https://www.tiktok.com/@yogchill/video/7310732289497910574):\t').replace(' ', '')
#need = 'https://www.tiktok.com/@yogchill/video/7310732289497910574'
r = requests.get(need, headers=headers)
desc = re.search('"desc":"(.*?)","createTime"', r.text, re.DOTALL).group(1)
print(desc)
url = re.search('"playAddr":"(.*?)","downloadAddr"', r.text, re.DOTALL).group(1)
url = url.replace(r'\u002F', '/')
r = requests.get(url, headers=headers)
with open('video.mp4', 'wb') as f:f.write(r.content)
print('saved video as video.mp4')
