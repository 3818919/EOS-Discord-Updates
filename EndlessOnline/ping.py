import socket
import json
import config
import pytz
from EndlessOnline import website as EL

SERVER_IP = "game.endless-online.com"
SERVER_PORT = 8078
STATUS_FILE = 'data/status_switch/status.json'

### Main Server Check Function ###
def check_server():
  last_status = check_server_status(STATUS_FILE, 'last_status')
  state = get_state()
  if last_status != state:
    update_last_status(STATUS_FILE, state)
    if state:  # Server came online
      with open('data/server_online.json', 'r') as f:
        webhook_embed = json.load(f)
      webhook_embed['embeds'][0]['description'] = webhook_embed['embeds'][0]['description'].format(EL.version())
    else:  # Server went offline
      with open('data/server_offline.json', 'r') as f:
        webhook_embed = json.load(f)
      uptime = EL.uptime()
      webhook_embed['embeds'][0]['description'] = webhook_embed['embeds'][0]['description'].format(uptime)
    return webhook_embed
  return None


### Get Current Server State ###
def get_state():
    ping = ping_server(SERVER_IP, SERVER_PORT)
    website = EL.server_status()
    if website == 'Online' or website == 'Online!':
      if ping == True:
        update_new_status(STATUS_FILE, True)
        return True
      else:
        update_new_status(STATUS_FILE, False)
        return False
    else:
      update_new_status(STATUS_FILE, False)
      return False
      

### Send Ping To Server ###
def ping_server(ip, port):
    for _ in range(3):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((ip, port))
            return True
        except:
            pass
        finally:
            s.close()
    return False


### Data File Logic ###
def check_server_status(status_file, status_key):
    with open(status_file, 'r') as f:
        data = json.load(f)
    return data[status_key]


def update_new_status(status_file, new_status):
    with open(status_file, 'r') as f:
        data = json.load(f)
    data['new_status'] = new_status
    with open(status_file, 'w') as f:
        json.dump(data, f)


def update_last_status(status_file, new_status):
    with open(status_file, 'r') as f:
        data = json.load(f)
    data['last_status'] = new_status
    with open(status_file, 'w') as f:
        json.dump(data, f)