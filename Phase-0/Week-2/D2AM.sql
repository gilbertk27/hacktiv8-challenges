-- EXPLAIN ANALYZE INSERT INTO students(student_id, "student_name")
-- VALUES(1, 'asdad')

-- ALTER TABLE students
--     student_name VARCHAR(50);

-- TRUNCATE TABLE students;

-- DELETE FROM students
-- WHERE student_id > 3 or student_name = 'Yud';

-- UPDATE students
-- SET student_name = 'gigi'
-- WHERE student_id = 3;

-- INSERT INTO students("student_name")
-- VALUES ('budi');

-- ALTER TABLE students
-- DROP COLUMN IF EXISTS address CASCADE;

-- ALTER TABLE students
-- ADD COLUMN address text not null;

-- CREATE TABLE buddies(
--     buddy_id INT PRIMARY KEY,
--     buddy_name VARCHAR(50) NOT NULL,
-- 	student_id int,
-- 	FOREIGN KEY (student_id) REFERENCES students(student_id)
-- );

-- ALTER TABLE students(
--     student_id SERIAL PRIMARY KEY,
--     student_name VARCHAR(50) NOT NULL
-- );

-- DROP TABLE students;

