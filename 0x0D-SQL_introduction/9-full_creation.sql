-- creates a table called second_table with attributes id, name, score.
-- and create 4 records.
CREATE TABLE IF NOT EXISTS `second_table` (
	id INT,
	name VARCHAR(256),
	score INT
);
INSERT INTO `second_table`
VALUES
(1, 'Jhon', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
