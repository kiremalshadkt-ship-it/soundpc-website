import os
import sys
sys.path.append(r'c:\Users\user\Desktop\soundpc-website-main')
os.environ['DJANGO_SETTINGS_MODULE'] = 'soundpc_website.settings'
import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
print('User count:', User.objects.count())
for u in User.objects.all():
    print('user:', u.username, 'is_active', u.is_active)
