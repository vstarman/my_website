'''
本地环境配置
'''
import os

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gjxq_talentsys',
        'USER': 'root',
        'PASSWORD': 'mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
print("local 环境")

