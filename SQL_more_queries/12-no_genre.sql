-- show shows without genre
SELECT s.title, NULL AS genre_id FROM tv_shows AS s 
WHERE NOT EXISTS (SELECT 1 FROM tv_show_genres WHERE tv_show_genres.show_id = s.id ORDER BY s.title ASC);