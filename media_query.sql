SELECT 
    users.name,
    posts.title,
    posts.content
FROM users
JOIN posts
    ON users.user_id = posts.user_id
WHERE users.grade = '2nd';