# EOS Discord Update Bot

This bot provides Discord status alerts for the Endless Online Server, ensuring real-time updates on server availability.

## Bot Functionality

The bot performs the following checks to determine the server status:

1. **Initial Check**: Verifies the server status on the endless-online.com website.
2. **Secondary Verification**: Pings the server directly for confirmation.
3. **Status Alert**:
   - If the server is offline and the last recorded status was online, the bot sends an offline alert.
   - If the server is online and the last recorded status was offline, the bot sends an online alert.
   - If there is no change in the server status, no alert is sent to avoid spamming.

## Customizing Role Pings

To change the role ping in the alerts, modify the `server_online.json` and `server_offline.json` files:

1. Replace the default `@here` in the `content` field with the custom role ID in the format `<@&ROLEID>`.
   - For example, if the role ID is `123456789`, replace `@here` with `<@&123456789>`.

## Scraping Data from Endless Online

For users interested in scraping game data from the Endless Online website:

- Refer to the `Endless Online > website.py` file. It contains pre-configured functions for effective data scraping.

**Note**: Ensure that your scraping activities comply with the terms and conditions of the Endless Online website.

## Private Server Status Alerts
For private server projects, check the [Private Server Status Bot](https://github.com/3818919/Server_Status) which comes with an easy config file.
