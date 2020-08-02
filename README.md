# IoT Mask

      _________ _______ _________   _______  _______  _______  _        
      \__   __/(  ___  )\__   __/  (       )(  ___  )(  ____ \| \    /\
         ) (   | (   ) |   ) (     | () () || (   ) || (    \/|  \  / /
         | |   | |   | |   | |     | || || || (___) || (_____ |  (_/ / 
         | |   | |   | |   | |     | |(_)| ||  ___  |(_____  )|   _ (  
         | |   | |   | |   | |     | |   | || (   ) |      ) ||  ( \ \ 
      ___) (___| (___) |   | |     | )   ( || )   ( |/\____) ||  /  \ \
      \_______/(_______)   )_(     |/     \||/     \|\_______)|_/    \/
   
                             
Senior Capstone project by Alden King, Patrick Schofield & Brian Beals -

software designed to block specific domains/ip to protect home networks and specifically IoT devices via ebtables

SETUP:

1.) under sudo, run global_rules.py - this sets the global rules that all connected devices must follow

2.) under sudo, run web_app.py - this allows you to connect to the device via the localhost

3.) under sudo, run bandwidth_monitor.py - this allows the device to start monitoring bandwidth and outputting to results.txt

4.) under sudo, run ebtable_count.py - this allows the device to monitor the number of packets passed through the rules list

KNOWN BUGS:

- There is a chance that the images in static do not self-delete as intended, this results in severe resource-hogging and could lead to the device freezing

- There is a chance that the images are deleted faster than the scripts have time to generate new ones, this results in the data not being displayed on the page until new graphs are rendered to the static folder. A broken image icon is put in its place until an image can be served
