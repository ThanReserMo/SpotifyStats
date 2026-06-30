import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('dark_background')

#https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023/data
st.title('Spotify Statistics 2023!')

#https://www.kaggle.com/code/sethegolfcu/unique-songs
stats=pd.read_csv('spotify-2023.csv',encoding='ISO-8859-1')

#streams where strings
#https://stackoverflow.com/questions/42719749/pandas-convert-string-to-int
stats.streams=pd.to_numeric(stats.streams,errors='coerce')




#https://stackoverflow.com/questions/70087538/expand-a-string-from-a-column-into-different-separate-columns-in-pandas
stats=stats.join(stats['artist(s)_name'].str.split(',',expand=True).add_prefix('artist_number_'))


st.header('Who is the artist with the most songs in the top 1000?')
#https://stackoverflow.com/questions/48590268/pandas-get-the-most-frequent-values-of-a-column
most_popular_artist=stats['artist_number_0'].value_counts()[:1].index

st.header(most_popular_artist[0])

st.header('Which artists appeared the most in the top 1000?')
top_n_artists=stats['artist_number_0'].value_counts()[:10].index
top_n_artists=top_n_artists.values

top_n_stats=stats[stats['artist_number_0'].isin(top_n_artists)]

countplot=sns.countplot(data=top_n_stats,x='artist_number_0')
plt.xticks(rotation=45)
fig=countplot.figure
st.pyplot(fig)

#most_popular_songs=stats['track_name'].value_counts()[:100].index
#top_100_songs=most_popular_songs.values

most_popular_stats=stats.nlargest(10,'streams')

plt.figure()

st.header('What are the 10 most popular songs?')
barplot=sns.barplot(most_popular_stats,x='track_name',y='streams',hue='artist_number_0')
#https://stackoverflow.com/questions/30490740/move-legend-outside-figure-in-seaborn-tsplot
sns.move_legend(barplot,'upper left',bbox_to_anchor=(1,1))
plt.xticks(rotation=90)
fig_bar=barplot.figure
st.pyplot(fig_bar)

st.header('Which artists were featured the most in the top 1000?')
top_n_feats=stats['artist_number_1'].value_counts()[:10].index
top_n_feats=top_n_feats.values

top_n_feat_stats=stats[stats['artist_number_1'].isin(top_n_feats)]

plt.figure()
countplot_feats=sns.countplot(data=top_n_feat_stats,x='artist_number_1')
plt.xticks(rotation=45)
fig_feats=countplot_feats.figure
st.pyplot(fig_feats)


st.title('Dataframe after modifications')
st.dataframe(stats)
#st.dataframe(artists_seperated)

