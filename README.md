# -How-to-use-Apollo-Save-Tool-AIO-Fake-account-for-Chaiki-
 How to use Apollo Save Tool AIO + Fake account for Chaiki 

# Fake account creation for Chiaki and misc   
1. Download and install [Apollo Save Tool](https://pkg-zone.com/details/APOL00004) to your PS4 guide on how here >[How to install FPKGS](https://github.com/DrYenyen/How-To-Install-PS4-FPKGS)     
2. Download the **main.py** from here >    or copy and paste the code below into a website that is able to run python scripts    
```
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
```  
3. Websites it can run on or is already loaded on    
copy and paste into > https://www.online-python.com/ 
copy and paste into > https://www.programiz.com/python-programming/online-compiler/
Already loaded here > https://trinket.io/embed/python3/ba2ff26973
4. Alternatively run on your own PC offline

