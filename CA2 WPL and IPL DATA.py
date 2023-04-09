#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
web=requests.get("https://www.espn.in/cricket/standings/series/1348825/women's-premier-league")
soup=BeautifulSoup(web.text,'html.parser')
#sleep(2)
table=soup.find('div',class_='responsive-table-wrap')

teamName=[]
print('\033[1m'+"Women Premier League".center(100)+'\033[0m',"\n\n")
print("Participating Team Names\n")
for info in table.find_all('span',class_='team-names'):
    name=info.text
    print(name)
    teamName.append(name)
print('\n\n')
print("Team name with other details\n")
i=0
OtherInfo=[]*5

for info2 in table.find_all('tbody'):
    for row in info2.find_all('tr',class_='standings-row'):
        print(i+1,". ",teamName[i])
        info3=[]
        for space in row.find_all('td',class_=''):
            details=space.text
            print("\t",details)
            info3.append(details)
        OtherInfo.append(info3)
        i=i+1
        print()
    
        
    #teamName.append(team)
print('\n\n\n\n')
for element in OtherInfo:
    if element == '':
        OtherInfo.remove(element)

print(str(OtherInfo))
M,W,L,T,NR,PT,NRR,FOR,AGAINST=[],[],[],[],[],[],[],[],[]
for m in OtherInfo:
    M.append(m[0])
    W.append(m[1])
    L.append(m[2])
    T.append(m[3])
    NR.append(m[4])
    PT.append(m[5])
    NRR.append(m[6])
    FOR.append(m[7])
    AGAINST.append(m[8])


dict={
    'Team':teamName,
    'M':M,
    'W':W,
    'L':L,
    'T': T,
    'N/R':NR,
    'PT':PT,
    'NRR':NRR,
    'FOR':FOR,
    'AGAINST':AGAINST
}
data=pd.DataFrame(dict)
data.to_csv("Women Premier League.csv",index=False)



# In[14]:


#Indian Premier League for Men
import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import*

web=requests.get("https://www.espncricinfo.com/series/indian-premier-league-2023-1345038/points-table-standings")
sleep(2)
soup=BeautifulSoup(web.content,'html.parser')
#sleep(2)

tbody=soup.find('tbody',class_="ds-text-center")
print('\033[1m'+"Indian Premier League for Men".center(80)+'\033[0m',"\n\n")
print("Participating Teams\n")
i=0

Details=[]
i=0
Names=[]
Points=[]
for row in tbody.find_all('tr',class_='ds-text-tight-s'):
    name=row.find('span',class_="ds-text-tight-s ds-font-bold ds-uppercase ds-text-left")
    print(i+1,".",name.text)
    Names.append(name.text)
    info4=[]
    for space in row.find_all('td',class_="ds-w-0 ds-whitespace-nowrap ds-min-w-max"):
        details=space.text
        print("\t",details) 
        info4.append(details)
    points=row.find('td',class_="ds-w-0 ds-whitespace-nowrap ds-min-w-max ds-font-bold").text
    print("\t",points)
    Points.append(points)
    Details.append(info4)
    i=i+1
    print()


M,W,L,T,NR,NRR,FOR,AGAINST=[],[],[],[],[],[],[],[]
for m in Details:
    M.append(m[0])
    W.append(m[1])
    L.append(m[2])
    T.append(m[3])
    NR.append(m[4])
    NRR.append(m[5])
    FOR.append(m[6])
    AGAINST.append(m[7])


dict2={
    'Team':Names,
    'M':M,
    'W':W,
    'L':L,
    'T': T,
    'N/R':NR,
    'NRR':NRR,
    'Points':Points,
    'FOR':FOR,
    'AGAINST':AGAINST
}
data=pd.DataFrame(dict2)
data.to_csv("Indian Premier League3.csv",index=False)





# In[7]:


print('\033[1m'+"Women Premier League".center(80)+'\033[0m')
ipl=pd.read_csv('Women Premier League.csv')
ipl.head()


# In[15]:


print('\033[1m'+"Indian Premier League for Men".center(70)+'\033[0m')
ipl2=pd.read_csv('Indian Premier League3.csv')
ipl2


# In[75]:


#Women Premier League
from time import*
import matplotlib.pyplot as plt
print('\033[1m'+"WPL Histogram".center(100)+'\033[0m')
plt.barh(range(len(ipl['PT'])),ipl['PT'], align='center')

# Add title and axis labels
plt.title('Points Histogram')
plt.ylabel('Teams')
plt.xlabel('Points')

# Set y-axis tick labels
plt.yticks(range(len(ipl['PT'])),ipl['Team'])
plt.xlim(0,15)
# Show the histogram graph
plt.show()

plt.barh(range(len(ipl['W'])),ipl['W'], align='center')

# Add title and axis labels
plt.title('Win Histogram')
plt.ylabel('Teams')
plt.xlabel('Wins')

# Set y-axis tick labels
plt.yticks(range(len(ipl['W'])),ipl['Team'])
plt.xlim(0,8)
# Show the histogram graph
plt.show()

plt.barh(range(len(ipl['NRR'])),ipl['NRR'], align='center')

# Add title and axis labels
plt.title('Net Run Rate Histogram')
plt.ylabel('Teams')
plt.xlabel('Net Run Rate')

# Set y-axis tick labels
plt.yticks(range(len(ipl['NRR'])),ipl['Team'])
plt.xlim(-4,3)

# Show the histogram graph
plt.show()


# In[77]:


print('\033[1m'+"IPL Histogram".center(100)+'\033[0m')
plt.barh(range(len(ipl2['Points'])),ipl2['Points'], align='center')

# Add title and axis labels
plt.title('Points Histogram')
plt.ylabel('Teams')
plt.xlabel('Points')

# Set y-axis tick labels
plt.yticks(range(len(ipl2['Points'])),ipl2['Team'])
plt.xlim(0,5)
# Show the histogram graph
plt.show()
plt.barh(range(len(ipl2['W'])),ipl2['W'], align='center')

# Add title and axis labels
plt.title('Win Histogram')
plt.ylabel('Teams')
plt.xlabel('Wins')

# Set y-axis tick labels
plt.yticks(range(len(ipl2['W'])),ipl2['Team'])
plt.xlim(0,5)
# Show the histogram graph
plt.show()
plt.barh(range(len(ipl2['NRR'])),ipl2['NRR'], align='center')

# Add title and axis labels
plt.title('Net Run Rate Histogram')
plt.ylabel('Teams')
plt.xlabel('Net Run Rate')

# Set y-axis tick labels
plt.yticks(range(len(ipl2['NRR'])),ipl2['Team'])
plt.xlim(-4,4)

# Show the histogram graph
plt.show()


# In[ ]:




