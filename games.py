import csv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import tz
from os import walk
import matplotlib.dates as mdates


names, years, games = [], [], []

def printout(title): #template_file = str, old_vals, new_vals = L
  with open(title, 'r') as f:
    print("Reading file {}".format(title))
    reader = csv.reader(f)
    csv_list = list(reader)
    for entry in csv_list:
      name = entry[0]
      year = float(entry[1])
      game_num = int(entry[2])
      print(year)
      names.append(name)
      years.append(year)
      games.append(game_num)
      """
      #time.append(entry[2])
      words = string.split(' ')
      #print(words)
      timex= datetime.utcfromtimestamp(int(float(words[2]))-21600)#.strftime('%d %H:%M')
      dates.append(timex)
      time.append(float(words[2])/3600-433394+18)
      temp.append(float(words[12]))"""

filename = 'game_data.txt'
printout(filename)


plt.xkcd()
#Creating a figure with some fig size
fig, ax = plt.subplots(figsize = (4,2))
ax.bar(years,games,width=0.4)
#plt.xticks(names,rotation=60)
plt.title("Number of Games Produced for Different Gaming Consoles, Per Wikipedia")
#ax.set_xticks(names)
#Now the trick is here.
#plt.text() , you need to give (x,y) location , where you want to put the numbers,
#So here index will give you x pos and data+1 will provide a little gap in y axis.
#for index,data in enumerate(games):
#    plt.text(names[index] , y =data+50 , s=f"{int(data)}")
plt.show()
