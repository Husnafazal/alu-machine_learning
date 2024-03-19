-- display the number of shows linked to:
-- each record should display genre_ - number_of_shows linked to genre
-- 1st column should be genre
-- 2nd column should be number of shows
-- don't display records with 0 shows
-- sort by number of shows linked to genre in descending order
-- use only one SELECT statement

SELECT tv_genres.name AS genre, 
       COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;