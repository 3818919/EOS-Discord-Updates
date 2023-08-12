import json
import requests
  
class webhook:
  # Define the information sent when the server goes from offline > online
  def online():
    with open('data/server_online.json', 'r') as f:
      webhook_embed = json.load(f)
    return webhook_embed

  # Define the information sent when the server goes from online > offline
  def offline():
    with open('data/server_offline.json', 'r') as f:
      webhook_embed = json.load(f)
    return webhook_embed

# Define discord server storage file
def get_list():
  with open('data/servers.json', 'r') as f:
    data = json.load(f)
  return list(data.values())
