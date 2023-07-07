-- lists shows that are on the Comedy genre.
SELECT DISTINCT `tv_shows`.`title`
FROM `tv_genres`
RIGHT JOIN `tv_show_genres`
ON `tv_genres`.`id` = `tv_show_genres`.`genre_id`
LEFT JOIN `tv_shows`
ON `tv_show_genres`.`show_id` = `tv_shows`.`id`
WHERE `tv_genres`.`name` = 'Comedy'
ORDER BY `tv_shows`.`title`;
