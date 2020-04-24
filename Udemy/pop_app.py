import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Udemy.settings')

import django
django.setup()

import random
from first_app.models import accessRecord, webPage, topics
from faker import Faker

fakegen = Faker()
top = ['Search', 'Social', 'News', 'Games']

def add_topic():
    t = topics.objects.get_or_create(top_name=random.choice(top))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        wbpg = webPage.objects.get_or_create(topic=top, url=fake_url, name = fake_name)[0]

        acc_rec = accessRecord.objects.get_or_create(name=wbpg, date=fake_date)[0]
if __name__ == '__main__':
    print ('populating script')
    populate(20)
    print('population complete')
