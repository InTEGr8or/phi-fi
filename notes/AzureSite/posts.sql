SELECT min(post_date) as post_date, post_title 
FROM acsm_4ba41f6c770a6de.wp_posts 
GROUP BY post_title
order by min(post_date) desc;