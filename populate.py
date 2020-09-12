import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bloodbank.settings')

import django
django.setup()


from bloodapp.models import User, Profile
from bloodrequestapp.models import UserGroup, Membership, BloodRequest




def populate():

    add_user_group()

def add_user_group():
    GROUP = {
        'Group A Positive': 'A+',
        'Group A Negative': 'A-',
        'Group B Positive': 'B+',
        'Group B Negative': 'B-',
        'Group AB Positive': 'AB+',
        'Group AB Negative': 'AB-',
        'Group O Positive': 'O+',
        'Group O Negative': 'O-'
    }

    for key, value in GROUP.items():
        obj, created = UserGroup.objects.get_or_create(group_name=key, group_code=value)
        print(f'{key} created')        

if __name__ == '__main__':
    print('start populating...')
    populate()
    print('Done...')
