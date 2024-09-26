#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# On a jailbroken PS4, install Apollo Save Tool, and activate a fake account in "User tools"
# https://github.com/bucanero/apollo-ps4
# Close then relaunch Apollo and write down your account ID ( it's the hex string between parenthesis after your user name)
# E.G : > Activate Offline Account YourUserName (1a2b3c4d5e6f7a8b)
# Replace the content of the "user_id" string with your actual hex string, then run the script to generate the base64
# encoded version of your account ID.

import base64


# PUT YOUR HEXADECIMAL ID BETWEEN THE ""
user_id = "" 

if len(user_id):
  user_id_int = int( user_id, 16 )
  user_id_base64 = base64.b64encode(user_id_int.to_bytes(8, "little")).decode()
  print( "Your 8 bytes, base64 encoded account ID is : " + str(user_id_base64))
else:
  print("Change the content of 'user_id' to match the string you found in Apollo.")