select * from campus;

BEGIN;

UPDATE students
SET total_grade = 90.1
WHERE id = 1;

UPDATE students
SET total_grade = 85.3
WHERE id = 2;

SELECT * from students;

ROLLBACK;
SELECT * from  students
ORDER BY id DESC;

BEGIN;
CREATE USER user1 WITH PASSWORD '1234';
CREATE USER user2 WITH PASSWORD '1234';
COMMIT;

GRANT SELECT ON students TO user1;
GRANT SELECT ON ALL TABLE IN SCHEMA public TO user1;

REVOKE SELECT ON students FROM user1;