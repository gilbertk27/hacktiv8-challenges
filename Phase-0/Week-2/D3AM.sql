-- Create the students table
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INTEGER,
    campus_id INTEGER,
    total_grade FLOAT,
	CONSTRAINT fk_campus
		FOREIGN KEY (campus_id)
		REFERENCES campus(id)
		ON DELETE CASCADE
);

DROP TABLE students

-- Insert data into the students table
INSERT INTO students (name, age, campus_id, total_grade)
VALUES
    ('Rafif Iman', 20, 1, 85.5),
    ('Hana Arisona', 21, 2, 90.2),
    ('Raka Purnomo', 19, 1, 78.9),
    ('Danu Irfansyah', 20, 3, 92.7),
    ('Rachman Ardhi', 22, 2, 88.1);

-- Create the campus table
CREATE TABLE campus (
    id SERIAL PRIMARY KEY,
    campus_name VARCHAR(50),
    batch VARCHAR(10),
    start_date DATE
);

-- Insert data into the campus table
INSERT INTO campus (campus_name, batch, start_date)
VALUES
    ('Remote', 'RMT-1', '2023-01-01'),
    ('Jakarta', 'HCK-2', '2023-02-01'),
    ('BSD', 'BSD-4', '2023-03-01'),
    ('Surabaya', 'SUB-1', '2023-04-01'),
    ('Singapore', 'SIN-1', '2023-05-01');
	
	
SELECT name,age FROM students
SELECT name as student_name, age FROM students

SELECT * FROM students
WHERE age > 20

SELECT * FROM students
WHERE age = 20

SELECT * FROM students
WHERE name = 'Rafif Iman'

SELECT * FROM students
WHERE name ILIKE '%ra%'

SELECT * FROM students
WHERE name ILIKE '%O%'

-- huruf bsr kecil ILIKE hurus bsr / kcl LIKE
SELECT * FROM students
WHERE name LIKE '__n%'

SELECT * FROM campus
WHERE start_date BETWEEN '2023-03-01' AND '2023-06-01'

SELECT * FROM campus
WHERE start_date < '2023-03-01'

SELECT * FROM students
WHERE total_grade BETWEEN 90 and 95

SELECT sum(total_grade), count(total_grade), 
		MIN(total_grade), MAX(total_grade)
FROM students

SELECT * FROM students
WHERE age >= 20

-- group by
SELECT campus_id, sum(total_grade), count(total_grade) 
FROM students
WHERE age >= 20
GROUP BY campus_id
HAVING SUM(total_grade) > 90

SELECT * FROM students
ORDER BY age DESC, name

-- Soal: tampilkan data murid beserta kampusnya
-- tabel pertama disebut LEFT
-- default inner join klo dideclare

SELECT * from students
RIGHT JOIN campus ON students.campus_id = campus.id

INSERT INTO students (name, total_grade)
VALUES ('budi',90)

SELECT * from students
LEFT JOIN campus ON students.campus_id = campus.id


