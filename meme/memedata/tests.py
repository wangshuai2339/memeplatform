from django.test import TestCase
from memedata import models
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meme.settings")# project_name 项目名称
django.setup()
import pymongo

myclient = pymongo.MongoClient(host="192.168.31.229", port=26000)
mydb = myclient["xy"]["user_identity_auth"]
myc1 = mydb.find_one()
print(myc1)
