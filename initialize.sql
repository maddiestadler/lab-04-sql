CREATE TABLE users(
    user_id INT PRIMARY KEY, 
    name VARCHAR(100),
    major VARCHAR(100),
    grade VARCHAR(20));

CREATE TABLE posts(
    post_id INT PRIMARY KEY,
    user_id INT,
    title VARCHAR(100),
    content TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id));

INSERT INTO users (user_id, name, major, grade)
VALUES (1, 'Sally', 'political science', '1st');

INSERT INTO users (user_id, name, major, grade)
VALUES (2, 'John', 'data science', '4th');

INSERT INTO users (user_id, name, major, grade)
VALUES (3, 'Sarah', 'english', '2nd');

INSERT INTO users (user_id, name, major, grade)
VALUES (4, 'Mona', 'chemistry', '2nd');

INSERT INTO users (user_id, name, major, grade)
VALUES (5, 'Katie', 'computer science', '4th');

INSERT INTO users (user_id, name, major, grade)
VALUES (6, 'Tommy', 'spanish', '1st');

INSERT INTO users (user_id, name, major, grade)
VALUES (7, 'Lexie', 'statistics', '3rd');

INSERT INTO users (user_id, name, major, grade)
VALUES (8, 'Siena', 'data science', '3rd');

INSERT INTO users (user_id, name, major, grade)
VALUES (9, 'Phoebe', 'biology', '3rd');

INSERT INTO users (user_id, name, major, grade)
VALUES (10, 'Raegan', 'philosophy', '4th');

INSERT INTO posts (post_id, user_id, title, content)
VALUES (1, 1, 'Hobby', 'My favorite hobby is pickleball.');

INSERT INTO posts (post_id, user_id, title, content)
VALUES (2, 2, 'Pets', 'I have 3 dogs and 1 cat.');

INSERT INTO posts (post_id, user_id, title, content)
VALUES (3, 3, 'Family', 'I have a family of 5.');

INSERT INTO posts (post_id, user_id, title, content)
VALUES (4, 4, 'Birthday', 'My birthday is October 25th.');

INSERT INTO posts (post_id, user_id, title, content)
VALUES (5, 5, 'Zodiac sign', 'My zodiac sign is Gemini.');

INSERT INTO posts (post_id, user_id, title, content)
VALUES (6, 6, 'Season', 'My favorite season is fall, especially at UVA.');

INSERT INTO posts (post_id, user_id, title, content)
VALUES (7, 7, 'Dinner', 'I had chicken parmesan for dinner today.');

INSERT INTO posts (post_id, user_id, title, content)
VALUES (8, 8, 'Number', 'My lucky number is 13.');

INSERT INTO posts (post_id, user_id, title, content)
VALUES (9, 9, 'Concert', 'I have attended 16 concerts in my lifetime.');

INSERT INTO posts (post_id, user_id, title, content)
VALUES (10, 10, 'Talent', 'My secret talent is wiggling my ears.');

