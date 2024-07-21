# -How-to-use-Apollo-Save-Tool-AIO-Fake-account-for-Chaiki-
 How to use Apollo Save Tool AIO + Fake account for Chaiki 

# Fake account creation for Chiaki and misc   
1. Download and install [Apollo Save Tool](https://pkg-zone.com/details/APOL00004) to your PS4 guide on how here >[How to install FPKGS](https://github.com/DrYenyen/How-To-Install-PS4-FPKGS)     
2. Download and unpack/install chiaki for the platform you want > https://git.sr.ht/~thestr4ng3r/chiaki/refs/v2.2.0
2. Launch Apollo Save Tool then navigate to option 5 from left to righ **User Tools**
3. Select **Activate PS4 Accounts**
4. Select the account you want to activate and press **X**    
5. A string of letters and numbers will show up copy them **CORRECTLY** then press **R2** then **X** and then keep pressing **O** till you are asked if you want to exit to the XMB accept then restart the console   
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
0. Once you are ready to run the code paste the string of letters and numbers you copied earlier where the red line is shown below and run the scrip   
0. Copy the new string of numbers and letters it should end with ''=''
0. You can now open Chiaki and paste it in the **PSN Account-ID (base64):** field along with the pin you are getting from the remote play menu.    
10. Enjoy!

