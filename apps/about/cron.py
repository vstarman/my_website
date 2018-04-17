import os, datetime
from django_crontab import crontab


def test():
    path = os.path.abspath(__file__)[:-18]
    full_path = path + 'static/test.txt'
    # print(path)
    date_now = str(datetime.datetime.now())
    print('work time ----->' + str(date_now))
    with open(full_path, 'a+') as f:
        f.write('this is the test for crontab, ----->' + date_now + '\n')

if __name__ == '__main__':
    test()
