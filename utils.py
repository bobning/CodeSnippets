#!/usr/bin/env python
#coding:utf8

def code_lines():
    '''统计各种语言的代码行数'''
    import os
    from collections import defaultdict
    d = defaultdict(int)
    for dirpath, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            ext = os.path.splitext(filename)[1]
            d[ext] += len(list(open(path)))
    for ext, n_lines in d.items():
        print ext, n_lines


def define_process_name():
    '''自定义python程序进程名'''
    procname = 'Hello'
    import os, sys
    if not os.environ.has_key('NEWPROCNAME'):
        os.execlpe(sys.executable, procname, __file__, {'NEWPROCNAME': procname})
    import dl
    libc = dl.open('/lib/libc.so.6')
    libc.call('prctl', 15, '%s\0' %procname, 0, 0, 0)


def time_convert():
    '''时间转换'''
    import time
    #str-->int
    print int(time.mktime(time.strptime('2010-07-30 02:10:11', '%Y-%m-%d %H:%M:%S')))
    #int->str
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def random_32():
    '''生成32位16进制随机数'''
    import random
    print ''.join(map(lambda x:'%04x'%random.randint(0,65535),range(8)))
