#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Scripts update last name of Telegram user every 10 seconds
#
# By @CodyDoby 
# Telegram Group: https://t.me/google_dive
# Blog: https://gfan.loan/
#

from telethon import TelegramClient, sync
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.errors import SessionPasswordNeededError
import time, sys
import os.path
from time import gmtime, strftime
from random import random

api_auth_file = 'api_auth'
if not os.path.exists(api_auth_file):
    api_id = input('api_id: ')
    api_hash = input('api_hash: ')
else 
    api_id = 123456
    api_hash = '00000000000000000000000000000000'

client = TelegramClient(api_auth_file, api_id, api_hash)
client.start()

#print('My infomation')
#me = client.get_me()
#print(me.stringify())

# change localtime：ln -sf /usr/share/zoneinfo/Asia/Chongqing /etc/localtime
# https://stackoverflow.com/questions/4788533/python-strftime-gmtime-not-respecting-timezone
while True:
    try:
        #time_cur = strftime("%H:%M:%S:%p:%a", time.localtime())
        time_cur = strftime("%y:%m:%d:%H:%M:%S:%p:%a", time.localtime())
        y, m, d, hour, minu, seco, p, abbwn = time_cur.split(':')

        # Update every 10 seconds 
        if int(seco) % 10 == 0:
            for_fun = random()
            # with a prob
            if for_fun < 0.33:
                last_name = '%s时:%s分' % (hour, minu)
            elif for_fun < 0.66:
                last_name = '%s:%s %s %s' % (hour, minu, p, abbwn)
            else:
                last_name = '%s年%s月%s日 %s时:%s分' % (y, m, d, hour, minu)
                
            client(UpdateProfileRequest(last_name=last_name))
        # CPU sleep 
        time.sleep(1)

    except KeyboardInterrupt:
        print('\nUsername resetting...\n')
        client(UpdateProfileRequest(last_name=''))
        sys.exit()
