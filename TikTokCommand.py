#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Description:TikTok.py
@Date       :2023/01/27 19:36:18
@Author     :imgyh
@version    :1.0
@Github     :https://github.com/imgyh
@Mail       :admin@imgyh.com
-------------------------------------------------
Change Log  :
-------------------------------------------------
'''

import argparse
import os
import json
from TikTok import TikTok
from TikTokUtils import Utils


def argument():
    parser = argparse.ArgumentParser(description='抖音批量下载工具 使用帮助')
    parser.add_argument("--link", "-l",
                        help="作品(视频或图集)、直播、合集、音乐集合、个人主页抖音分享链接(删除文案, 保证只有URL, https://v.douyin.com/kcvMpuN/)",
                        type=str, required=True)
    parser.add_argument("--path", "-p", help="下载保存位置",
                        type=str, required=True)
    parser.add_argument("--music", "-m", help="是否下载视频中的音乐(True/False), 默认为True",
                        type=Utils().str2bool, required=False, default=True)
    parser.add_argument("--cover", "-c", help="是否下载视频的封面(True/False), 默认为True, 当下载视频时有效",
                        type=Utils().str2bool, required=False, default=True)
    parser.add_argument("--avatar", "-a", help="是否下载作者的头像(True/False), 默认为True",
                        type=Utils().str2bool, required=False, default=True)
    parser.add_argument("--mode", "-M", help="link是个人主页时, 设置下载发布的作品(post)或喜欢的作品(like)或者用户所有合集(mix), 默认为post",
                        type=str, required=False, default="post")
    parser.add_argument("--number", "-n",
                        help="1.当下载单个合集、音乐集合、主页作品(post模式)和喜欢(like模式)时, 可设置下载前n个作品, 默认为0全部下载\r\n" +
                             "2.当下载主页下所有合集(mix模式)时, 设置下载前n个合集下所有作品, 默认为0全部下载",
                        type=int, required=False, default=0)
    parser.add_argument("--thread", "-t",
                        help="设置线程数, 默认5个线程",
                        type=int, required=False, default=5)
    args = parser.parse_args()

    return args


def main():
    utils = Utils()
    args = argument()
    tk = TikTok()
    url = tk.getShareLink(args.link)
    key_type, key = tk.getKey(url)
    if args.thread <= 0:
        args.thread = 5
    if key is None or key_type is None:
        return
    elif key_type == "user" and args.mode != 'mix':
        datalist = tk.getUserInfo(key, args.mode, 35, args.number)
        tk.userDownload(awemeList=datalist, music=args.music, cover=args.cover, avatar=args.avatar,
                        savePath=args.path, thread=args.thread)
    elif key_type == "user" and args.mode == 'mix':
        if not os.path.exists(args.path):
            os.mkdir(args.path)
        mixIdNameDict = tk.getUserAllMixInfo(key, 35, args.number)

        for mix_id in mixIdNameDict:
            print(f'[  提示  ]:正在下载合集 [{mixIdNameDict[mix_id]}] 中的作品\r\n')
            mix_file_name = utils.replaceStr(mixIdNameDict[mix_id])
            datalist = tk.getMixInfo(mix_id, 35)
            tk.userDownload(awemeList=datalist, music=args.music, cover=args.cover, avatar=args.avatar,
                        savePath=os.path.join(args.path, mix_file_name), thread=args.thread)
            print(f'[  提示  ]:合集 [{mixIdNameDict[mix_id]}] 中的作品下载完成\r\n')
    elif key_type == "mix":
        datalist = tk.getMixInfo(key,35, args.number)
        tk.userDownload(awemeList=datalist, music=args.music, cover=args.cover, avatar=args.avatar,
                        savePath=args.path, thread=args.thread)
    elif key_type == "music":
        datalist = tk.getMusicInfo(key,35, args.number)
        tk.userDownload(awemeList=datalist, music=args.music, cover=args.cover, avatar=args.avatar,
                        savePath=args.path, thread=args.thread)
    elif key_type == "aweme":
        datanew, dataraw = tk.getAwemeInfo(key)
        tk.awemeDownload(awemeDict=datanew, music=args.music, cover=args.cover, avatar=args.avatar,
                         savePath=args.path, usingThread=False)
    elif key_type == "live":
        live_json = tk.getLiveInfo(key)
        if not os.path.exists(args.path):
            os.mkdir(args.path)

        # 保存获取到json
        print("[  提示  ]:正在保存获取到的信息到result.json\r\n")
        with open(os.path.join(args.path, "result.json"), "w", encoding='utf-8') as f:
            f.write(json.dumps(live_json, ensure_ascii=False, indent=2))
            f.close()


if __name__ == "__main__":
    main()
