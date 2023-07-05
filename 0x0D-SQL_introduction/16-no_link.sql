-- lists all records of the table second_table.
-- where name has value.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
