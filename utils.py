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
    

def is_same_week(t):
    '''
    是否在同周
    '''
    tm = time.strptime(t, '%Y-%m-%d')
    dt = datetime.datetime(tm.tm_year, tm.tm_mon, tm.tm_mday)
    tm = time.localtime()
    dt_now = datetime.datetime(tm.tm_year, tm.tm_mon, tm.tm_mday)
    start_t = dt_now - datetime.timedelta(dt_now.isoweekday() - 1)
    step = 7 - dt_now.isoweekday() + 1
    end_t = dt_now + datetime.timedelta(step)
    if start_t <= dt < end_t:
        return True
    return False


def random_32():
    '''生成32位16进制随机数'''
    import random
    print ''.join(map(lambda x:'%04x'%random.randint(0,65535),range(8)))
    import os
    from binascii import hexlify
    print hexlify(os.urandom(16))


def sort_dict_by_val(d, reverse=False):
    '''字典排序--根据value'''
    from operator import itemgetter
    return sorted(d.iteritems(), key=itemgetter(1), reverse=reverse)


def sort_dict_by_key(d, reverse=False):
    '''字典排序--根据value'''
    from operator import itemgetter
    return sorted(d.iteritems(), key=itemgetter(0), reverse=reverse)
