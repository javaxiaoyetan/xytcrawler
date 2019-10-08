# -*- coding: utf-8 -*-
"""
  获取现在时间
"""
def get_now():
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))