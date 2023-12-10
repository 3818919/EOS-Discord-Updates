# EOS Discord Updates
Provides discord status alerts for the Endless Online Server

Bot will first check status of server displayed on the endless-online.com website. If the server is displayed as online it will ping the server to make sure. If either of these steps returns false & the bot's last recorded status was online, the bot will send out the offline discord embed (json) to the webhook.

If both of these are true & the bot's last recorded status was offline, the bot will send out the online discord embed (json) to the webhook.

If the last recorded status of the server is the same as the latest status, nothing will happen. This is to not spam the server with online or offline alerts.

## Changing the role ping
Changing the role ping can be done in the `server_online.json` & `server_offline.json` files (specifically the `content` data which is currently displayed as @here). 
To use a custom role, follow the following steps:
  1. Copy the role ID of the role in discord
  2. replace the `@here` with `<@&ROLEID>`

An example of this is if the role ID is `123456789` you would replace the `@here` with `<@&123456789>`

## Scraping the endless online website
If you're interested in scraping game data from the endless-online.com website, check the `Endless Online > website.py` file as it contains several functions setup to do so. 
