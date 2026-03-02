-- list all shows with at least one genre linked
USE hbtn_0d_tvshows;
SELECT s.title, sg.genre_id FROM tv_shows AS s 
INNER JOIN tv_show_genres AS sg ON s.id = sg.show_id 
ORDER BY s.title ASC, sg.genre_id ASC;