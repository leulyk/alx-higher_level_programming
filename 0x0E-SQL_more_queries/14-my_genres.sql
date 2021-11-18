-- list the genres of the show 'Dexter'
SELECT name FROM tv_genres
INNER JOIN tv_show_genres
ON id = genre_id
WHERE show_id=8;
