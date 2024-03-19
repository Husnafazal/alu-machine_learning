-- list all shows with at least one genre linked
-- display show title - genre_id
-- order by show title genre_id
-- use only one SELECT statement

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title, tv_show_genres.genre_id;