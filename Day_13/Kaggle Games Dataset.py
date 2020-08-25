#!/usr/bin/env python
# coding: utf-8

# # Pandas Lab Exercise
# 
# 
# ## Part - 1
# We shall now test your skills in using Pandas package. We will be using the [games Dataset](https://www.kaggle.com/gutsyrobot/games-data/data) from Kaggle. 
# 
# Answer each question asked below wrt the games dataset.

# ** Import pandas as pd.**

# In[1]:


import pandas as pd


# ** Read games.csv as a dataframe called games.**

# In[2]:


games = pd.read_csv("games.csv")


# ** Check the head of the DataFrame. **

# In[3]:


games.head()


# ** Use .info() method to find out total number of entries in dataset**

# In[4]:


games.info()


# **What is the mean playin time for all games put together ?**

# In[6]:


games['playingtime'].mean()


# ** What is the highest number of comments received for a game? **

# In[7]:


games['total_comments'].max()


# ** What is the name of the game with id 1500?  **

# In[8]:


games[games['id']==1500]['name']


# ** And which year was it published? **

# In[9]:


games[games['id']==1500]['yearpublished']


# ** Which game has received highest number of comments? **

# In[10]:


games[games['total_comments']==games['total_comments'].max()]


# ** Which games have received least number of comments? **

# In[11]:


games[games['total_comments']==games['total_comments'].min()]


# ** What was the average minage of all games per game "type"? (boardgame & boardgameexpansion)**

# In[13]:


games.groupby('type').mean()['minage']


# ** How many unique games are there in the dataset? **

# In[14]:


games['id'].nunique()


# ** How many boardgames and boardgameexpansions are there in the dataset?  **

# In[15]:


games['type'].value_counts()


# ** Is there a correlation between playing time and total comments for the games? - Use the .corr() function **

# In[18]:


games[['playingtime','total_comments']].corr()


# In[ ]:




