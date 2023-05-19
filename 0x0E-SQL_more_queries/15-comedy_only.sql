-- A script that lists all Comedy shows in the database hbtn_0d_tvshows
-- The tv_genres table contains only one record where name = Comedy.
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
-- Note:Joined all tables with same key relationship(foreign keys)
SELECT tv_shows.title
FROM tv_genres
JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title;
