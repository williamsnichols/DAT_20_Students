__author__ = 'asilver'

#%matplotlib inline

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#tell pandas to display wide tables as pretty HTML tables
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)

def remove_border(axes=None, top=False, right=False, left=True, bottom=True):
    """
    Minimize chartjunk by stripping out unnecesasry plot borders and axis ticks

    The top/right/left/bottom keywords toggle whether the corresponding plot border is drawn
    """
    ax = axes or plt.gca()
    ax.spines['top'].set_visible(top)
    ax.spines['right'].set_visible(right)
    ax.spines['left'].set_visible(left)
    ax.spines['bottom'].set_visible(bottom)

    #turn off all ticks
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')

    #now re-enable visibles
    if top:
        ax.xaxis.tick_top()
    if bottom:
        ax.xaxis.tick_bottom()
    if left:
        ax.yaxis.tick_left()
    if right:
        ax.yaxis.tick_right()
#-------------------------------
names = ['imdbID', 'title', 'year', 'score', 'votes', 'runtime', 'genres']
data = pd.read_csv('https://raw.githubusercontent.com/cs109/content/master/imdb_top_10000.txt', delimiter='\t', names=names).dropna()
print "Number of rows: %i" % data.shape[0]
#print data.head()  # print the first 5 rows
#-------------------------------

#LOOK THIS UP SEPARATELY - split function -
"""
dirty = '142 mins.'
number, text = dirty.split(' ')
clean = int(number)
print number
"""
#-------------------------------
clean_runtime = [float(r.split(' ')[0]) for r in data.runtime]
data['runtime'] = clean_runtime
#print data.head()
#-------------------------------
#determine the unique genres
genres = set()
for m in data.genres:
    genres.update(g for g in m.split('|'))
genres = sorted(genres)

#make a column for each genre
for genre in genres:
    data[genre] = [genre in movie.split('|') for movie in data.genres]

#print data.head()

#determine the unique genres
genres = set()
for m in data.genres:
    genres.update(g for g in m.split('|'))
genres = sorted(genres)

#make a column for each genre
for genre in genres:
    data[genre] = [genre in movie.split('|') for movie in data.genres]

#print data.head()
#-------------------------------

data['title'] = [t[0:-7] for t in data.title]
#print data.head()

#-------------------------------
#print data[['score', 'runtime', 'year', 'votes']].describe()
#-------------------------------
#hmmm, a runtime of 0 looks suspicious. How many movies have that?
#print len(data[data.runtime == 0])

#probably best to flag those bad data as NAN
#**this looks like a where for data frames
data.runtime[data.runtime==0] = np.nan
#-------------------------------
data.runtime.describe()
#-------------------------------
# more movies in recent years, but not *very* recent movies (they haven't had time to receive lots of votes yet?)
"""
plt.hist(data.year, bins=np.arange(1950, 2013), color='#cccccc')
plt.xlabel("Release Year")
remove_border()



plt.hist(data.score, bins=20, color='#cccccc')
plt.xlabel("IMDB rating")
remove_border()
plt.show()
#print data[data.score > 10]


plt.hist(data.runtime.dropna(), bins=50, color='#cccccc')
plt.xlabel("Runtime distribution")
remove_border()
plt.show()


#hmm, more bad, recent movies. Real, or a selection bias?

plt.scatter(data.year, data.score, lw=0, alpha=.08, color='k')
plt.xlabel("Year")
plt.ylabel("IMDB Rating")
remove_border()
plt.show()



plt.scatter(data.votes, data.score, lw=0, alpha=.2, color='k')
plt.xlabel("Number of Votes")
plt.ylabel("IMDB Rating")
plt.xscale('log')
remove_border()
plt.show()


#-------------------------------
# low-score movies with lots of votes
data[(data.votes > 9e4) & (data.score < 5)][['title', 'year', 'score', 'votes', 'genres']]
# The lowest rated movies
data[data.score == data.score.min()][['title', 'year', 'score', 'votes', 'genres']]
# The highest rated movies
data[data.score == data.score.max()][['title', 'year', 'score', 'votes', 'genres']]
#-------------------------------
#sum sums over rows by default
genre_count = np.sort(data[genres].sum())[::-1]
print pd.DataFrame({'Genre Count': genre_count})
#-------------------------------
#axis=1 sums over columns instead
genre_count = data[genres].sum(axis=1)
print "Average movie has %0.2f genres" % genre_count.mean()
genre_count.describe()
#-------------------------------
decade =  (data.year // 10) * 10

tyd = data[['title', 'year']]
tyd['decade'] = decade

tyd.head()
#-------------------------------
#mean score for all movies in each decade
decade_mean = data.groupby(decade).score.mean()
decade_mean.name = 'Decade Mean'
#print decade_mean

plt.plot(decade_mean.index, decade_mean.values, 'o-',
        color='r', lw=3, label='Decade Average')
plt.scatter(data.year, data.score, alpha=.04, lw=0, color='k')
plt.xlabel("Year")
plt.ylabel("Score")
plt.legend(frameon=False)
remove_border()
plt.show()

#-------------------------------
grouped_scores = data.groupby(decade).score

mean = grouped_scores.mean()
std = grouped_scores.std()

plt.plot(decade_mean.index, decade_mean.values, 'o-',
        color='r', lw=3, label='Decade Average')
plt.fill_between(decade_mean.index, (decade_mean + std).values,
                 (decade_mean - std).values, color='r', alpha=.2)
plt.scatter(data.year, data.score, alpha=.04, lw=0, color='k')
plt.xlabel("Year")
plt.ylabel("Score")
plt.legend(frameon=False)
remove_border()
"""
"""Excluded for HW
#-------------------------------
for decade, subset in data.groupby('decade'):
    print decade, subset[subset.score == subset.score.max()].title.values

#create a 4x6 grid of plots.
fig, axes = plt.subplots(nrows=4, ncols=6, figsize=(12, 8),
                         tight_layout=True)

bins = np.arange(1950, 2013, 3)
for ax, genre in zip(axes.ravel(), genres):
    ax.hist(data[data[genre] == 1].year,
            bins=bins, histtype='stepfilled', normed=True, color='r', alpha=.3, ec='none')
    ax.hist(data.year, bins=bins, histtype='stepfilled', ec='None', normed=True, zorder=0, color='#cccccc')

    ax.annotate(genre, xy=(1955, 3e-2), fontsize=14)
    ax.xaxis.set_ticks(np.arange(1950, 2013, 30))
    ax.set_yticks([])
    remove_border(ax, left=False)
    ax.set_xlabel('Year')
    """
#-------------------------------
#-------------------------------
#New Insights

#there is not a single Film-Noir movie that has a rating lower than 6.7. If I were a film maker seeking awards, I would pursue Film-Noir.
data_score_grp = data.groupby('score')
print data_score_grp.mean()

#The most controversial movies are Independence day, Terminator 3 and Bruce Almighty
print data[(data.score == data.score.median())&(data.votes > 9e4)][['title', 'year', 'score', 'votes', 'genres']]


#-------------------------------
print data.head()
plt.scatter(data.year, data.score, alpha=.5, color='k')
plt.xlabel("Year")
plt.ylabel("IMDB Rating")
plt.show()
#older movies receive better, more concentrated ratings

#-------------------------------
print data.head()
plt.scatter(data.year, data.votes, alpha=.5, color='k')
plt.xlabel("Year")
plt.ylabel("Votes")
plt.show()
#Older movies receive fewer ratings than newer movies



