"""
定时任务模块
"""
import os, datetime
from django_crontab import crontab


def test():
    print('-'*100)
    # print(a, b)
    path = os.path.abspath(__file__)[:-18]
    full_path = path + 'static/test.txt'
    # print(path)
    date_now = str(datetime.datetime.now())
    print('work time ----->' + str(date_now))
    with open(full_path, 'a+') as f:
        f.write('this is the test for crontab, ----->' + date_now + '\n')


def test_has_params(a,b,c, **kwargs):
    print('-'*100)
    num = a+b+c
    print(a,b,c,num)
    path = os.path.abspath(__file__)[:-18]
    full_path = path + 'static/test.txt'
    # print(path)
    date_now = str(datetime.datetime.now())
    print('work time ----->' + str(date_now))
    with open(full_path, 'a+') as f:
        f.write('Crontab has param, %s ----->' % num + date_now + '\n')


if __name__ == '__main__':
    test_has_params(1,2,3)
