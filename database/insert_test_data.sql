USE skill_bootcamp;

INSERT INTO students (first_name, last_name)
VALUES
 ('Ruba','Oudah'),('Sara','Mohamed'),('Norah','alotaibi');

INSERT INTO modules (module_name, description)
VALUES
 ('Python Basics','Intro to Python'),
 ('Database Design','SQL & schema design');

INSERT INTO cohorts (cohort_name, start_date, end_date)
VALUES ('Fall 2025 Cohort','2025-09-01','2025-12-08');

INSERT INTO student_module_xref (student_id, module_id, status)
VALUES (1,1,'In Progress'), (2,2,'Completed');
