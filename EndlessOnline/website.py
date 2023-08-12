import pandas as pd
import lxml
import requests
from bs4 import BeautifulSoup
import re

#############################################################
# This file is for the website scraping of Endless-Online.com
# The data has been formatted specifically for discord usage
#############################################################

class url:
  server = 'https://game.endless-online.com/server.html'
  online = 'https://game.endless-online.com/playerlist.html'
  top_players = 'https://game.endless-online.com/top100.html'
  top_guilds = 'https://game.endless-online.com/guilds.html'

def table_lookup(url):
  soup = BeautifulSoup(requests.get(url).text, 'html.parser')
  return soup.find_all('table')

# string
def time_of_day():
  images = table_lookup(url.server)[1].find_all('img')
  for image in images:
    match image['src']:
      case 'daypart_0.jpg':
        return "Daytime"
      case 'daypart_1.jpg':
        return "Morning"
      case 'daypart_2.jpg':
        return "Nighttime"
      case 'daypart_3.jpg':
        return "Evening"

# string
def version():
  return pd.read_html(url.server)[2].iloc[0, 1]

# string
def server_status():
  return pd.read_html(url.server)[2].iloc[1, 1]

# string
def mail_gateway():
  return pd.read_html(url.server)[2].iloc[2, 1]

# string
def uptime():
  uptime_ = pd.read_html(url.server)[3].iloc[0, 1]
  return uptime_

# integer's of combined & singular minutes
def day_cycle():
  daytime = [int(num) for num in re.findall('\d+', pd.read_html(url.server)[5].iloc[0, 1])]
  shadow = [int(num) for num in re.findall('\d+', pd.read_html(url.server)[5].iloc[1, 1])]
  night = [int(num) for num in re.findall('\d+', pd.read_html(url.server)[5].iloc[2, 1])]
  return sum(daytime + shadow + shadow + night), daytime, shadow, night

# integer
def online_count():
  return int(pd.read_html(url.server)[4].iloc[1, 1].split('/')[0].strip())

# integer
def accounts_created():
  return int(pd.read_html(url.server)[6].iloc[0, 1])

# integer
def characters_created():
  return int(pd.read_html(url.server)[6].iloc[1, 1])

# integer
def guilds_created():
  return int(pd.read_html(url.server)[6].iloc[2, 1])

# String of names, titles, exp, genders in descending order
def online():
  names = '\n'.join(pd.read_html(url.online)[2][0])
  titles = '\n'.join(pd.read_html(url.online)[2][1])
  exp = '\n'.join(pd.read_html(url.online)[2][2])
  genders = '\n'.join(pd.read_html(url.online)[2][3])
  return names, titles, exp, genders

# String of names, titles, levels, exp, genders in descending order
def top_players():
  names = '\n'.join(pd.read_html(url.top_players)[2][0])
  titles = '\n'.join(pd.read_html(url.top_players)[2][1])
  levels = '\n'.join(pd.read_html(url.top_players)[2][2])
  exp = '\n'.join(pd.read_html(url.top_players)[2][3])
  genders = '\n'.join(pd.read_html(url.top_players)[2][4])
  return names, titles, levels, exp, genders

# String of names, tags, member count, exp in descending order
def top_guilds():
  names = '\n'.join(pd.read_html(url.top_guilds)[2][0])
  tags = '\n'.join(pd.read_html(url.top_guilds)[2][1])
  members = '\n'.join(pd.read_html(url.top_guilds)[2][2])
  exp = '\n'.join(pd.read_html(url.top_guilds)[2][3])
  return names, tags, members, exp