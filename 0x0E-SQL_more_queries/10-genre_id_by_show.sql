-- lists all shows contained in `hbtn_0d_tvshow`
-- that have atleast one genere linked.
SELECT `tv_shows`.`title`, `tv_show_genres`.`genre_id`
FROM `tv_show_genres`
INNER JOIN `tv_shows`
WHERE `tv_show_genres`.`show_id` = `tv_shows`.`id`
ORDER BY `tv_shows`.`title`, `tv_show_genres`.`genre_id`;
