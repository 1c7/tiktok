#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Description:TikTok.py
@Date       :2023/02/11 13:06:23
@Author     :imgyh
@version    :1.0
@Github     :https://github.com/imgyh
@Mail       :admin@imgyh.com
-------------------------------------------------
Change Log  :
-------------------------------------------------
'''
import TikTokUtils
from TikTok import TikTok

def getAwemeInfo():
    share_link_video = "3.56 uSy:/ 复制打开抖音，看看【小透明的作品】没有女朋友就用我的吧哈哈哈哈 # 表情包锁屏  https://v.douyin.com/BugmVVD/"
    share_link_pic = "8.20 MJI:/ 复制打开抖音，看看【舍溪的图文作品】我又来放图集啦～还有你们要的小可爱大图也放啦～# ... https://v.douyin.com/BugrFTN/"
    tk = TikTok()

    url = tk.getShareLink(share_link_pic)
    key_type, key = tk.getKey(url)
    datanew, dataraw = tk.getAwemeInfo(key)
    print(datanew)

def getUserInfo():
    share_link_post = "1- 长按复制此条消息，打开抖音搜索，查看TA的更多作品。 https://v.douyin.com/BupCppt/"
    share_link_like = "2- 长按复制此条消息，打开抖音搜索，查看TA的更多作品。 https://v.douyin.com/BusJrfr/"
    tk = TikTok()

    url = tk.getShareLink(share_link_like)
    key_type, key = tk.getKey(url)
    awemeList = tk.getUserInfo(key, mode="like", count=35)
    print(awemeList)

def getLiveInfo():
    live_link = "https://live.douyin.com/40768897856"
    tk = TikTok()

    url = tk.getShareLink(live_link)
    key_type, key = tk.getKey(url)
    live_json = tk.getLiveInfo(key)
    print(live_json)

def getMixInfo():
    mix_link = 'https://v.douyin.com/B3J63Le/'
    tk = TikTok()

    url = tk.getShareLink(mix_link)
    key_type, key = tk.getKey(url)
    awemeList = tk.getMixInfo(key, count=35)
    print(len(awemeList))

def getUserAllMixInfo():
    user_all_mix_link = 'https://v.douyin.com/B38oovu/'
    tk = TikTok()

    url = tk.getShareLink(user_all_mix_link)
    key_type, key = tk.getKey(url)
    mixIdNameDict = tk.getUserAllMixInfo(key, count=35)
    print(mixIdNameDict)

def getMusicInfo():
    music_link = 'https://v.douyin.com/S6YMNXs/'
    tk = TikTok()

    url = tk.getShareLink(music_link)
    key_type, key = tk.getKey(url)
    awemeList = tk.getMusicInfo(key,count=35)
    print(len(awemeList))

def test():
    utils=TikTokUtils.Utils()
    user_all_mix_link = 'https://www.douyin.com/aweme/v1/web/aweme/post/?'+\
                        utils.getXbogus(url='device_platform=webapp&aid=6383&os_version=10&version_name=17.4.0&sec_user_id=MS4wLjABAAAA7G3S983y0b0m_7bcTSK7UzY-3hFJdHvMv-aVbbz0kIg&max_cursor=1626149119000&count=10')
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'referer': 'https://www.douyin.com/',
        'Cookie': 'passport_csrf_token=f61602fc63757ae0e4fd9d6bdcee4810; ttwid=1|S3B70hT91P08fJIZJfOQETOCRyfySRp95cXKBpdd2KA|1677745253|be2b0a6c96f4400315e013b22e949756d3028d25434bd028f415b50f2fc9d98d; msToken=58OWeEpSkfMK4IAYaYYLEGdsYU8ZZONYG4Y1iUTayG1P6s0PxSoQsfhT5qn0vTem7kSyk6U-M4a0P0o2ttjY_N2TaID0AcPCQEuTcucnWEkKUQe7MABFmaP9WLGpnA==;'    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'referer': 'https://www.douyin.com/',
        'Cookie': 'ttwid=1|sGp2L-Krm46cXHcK7BsKghavVeVQIIOYtQInA1LV0-w|1676899557|3e483426230c481bd34f4d6529d6252372c154b75be7d4a2baec8edbfd0a742c; __ac_signature=_02B4Z6wo00f01CEKaogAAIDBqkHxaCCYIyghKm4AAGu9c3; s_v_web_id=verify_ledo1j1t_0NwhDQFJ_nLca_42o5_8tAA_T8CWm5E2M6LF; msToken=%s;odin_tt=324fb4ea4a89c0c05827e18a1ed9cf9bf8a17f7705fcc793fec935b637867e2a5a9b8168c885554d029919117a18ba69;' % utils.generate_random_str(
            107)
    }
    import requests

    res = requests.get(user_all_mix_link,headers=headers1)
    print(res.text)

if __name__ == "__main__":
    # test()
    # getMusicInfo()
    # getUserAllMixInfo()
    # getMixInfo()
    # getAwemeInfo()
    # getUserInfo()
    # getLiveInfo()
    pass

