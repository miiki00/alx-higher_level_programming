-- lists all shows contained in `hbtn_0d_tvshow`
-- that have atleast one genere linked.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
FULL OUT JOIN tv_show_genres
WHERE tv_shows.genre_id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
