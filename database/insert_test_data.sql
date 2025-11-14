/* ******************************************************
Insert test data into the skill_bootcamp database.
********************************************************/

-- Switch to the skill_bootcamp database.
USE skill_bootcamp;

-- Insert data into the cohorts table.
INSERT INTO cohorts (cohort_name, start_date, end_date) VALUES
('Fall 2025 Cohort', '2025-09-01', '2025-12-08'),
('Winter 2025 Cohort', '2025-12-15', '2026-03-20'),
('Spring 2026 Cohort', '2026-03-25', '2026-06-30'),
('Summer 2026 Cohort', '2026-07-01', '2026-09-15'),
('Data Science Cohort', '2025-10-01', '2026-01-15'),
('AI Bootcamp Cohort', '2025-11-05', '2026-02-10'),
('Cybersecurity Cohort', '2025-09-15', '2025-12-20'),
('Web Dev Cohort', '2025-10-10', '2026-01-25'),
('Cloud Cohort', '2025-08-15', '2025-11-30'),
('DevOps Cohort', '2025-09-20', '2025-12-25'),
('Networking Cohort', '2025-09-05', '2025-12-10'),
('ML Cohort', '2025-10-05', '2026-01-05'),
('Blockchain Cohort', '2025-09-25', '2025-12-28'),
('Frontend Cohort', '2025-09-10', '2025-12-15'),
('Backend Cohort', '2025-09-12', '2025-12-17'),
('Game Dev Cohort', '2025-10-20', '2026-01-25'),
('Mobile Dev Cohort', '2025-11-01', '2026-02-10'),
('Cloud Native Cohort', '2025-09-22', '2025-12-18'),
('System Admin Cohort', '2025-09-18', '2025-12-20'),
('Security Cohort', '2025-08-30', '2025-12-05');

-- Insert data into the students table.
INSERT INTO students (first_name, last_name, cohort_id) VALUES
('Ruba', 'Alhwaiti', 1),
('Michael', 'Johnson', 1),
('Jessica', 'Brown', 1),
('David', 'Miller', 2),
('Joshua', 'Davis', 2),
('Ashley', 'Wilson', 3),
('Christopher', 'Moore', 3),
('Amanda', 'Taylor', 4),
('Daniel', 'Anderson', 5),
('Sarah', 'Thomas', 5),
('Matthew', 'Jackson', 6),
('Jennifer', 'White', 7),
('Andrew', 'Harris', 7),
('Megan', 'Martin', 8),
('Ryan', 'Thompson', 9),
('Lauren', 'Garcia', 10),
('Brandon', 'Martinez', 11),
('Stephanie', 'Robinson', 12),
('Justin', 'Clark', 13),
('Nicole', 'Rodriguez', 14);

-- Insert data into the modules table.
INSERT INTO modules (module_name, description) VALUES
('Python Basics', 'Introduction to Python programming and syntax'),
('Database Design', 'Learn SQL, normalization, and schema design'),
('Web Fundamentals', 'HTML, CSS, and JavaScript essentials'),
('Networking Concepts', 'Introduction to computer networks and protocols'),
('Cybersecurity Basics', 'Principles of security and threat mitigation'),
('Data Science Intro', 'Learn data cleaning, analysis, and visualization'),
('Machine Learning', 'Intro to supervised and unsupervised learning'),
('Cloud Computing', 'AWS, Azure, and cloud deployment basics'),
('DevOps Foundations', 'CI/CD, Docker, and Kubernetes introduction'),
('Mobile App Dev', 'Android and iOS basics using Flutter'),
('Game Development', 'Unity and game logic fundamentals'),
('Frontend Development', 'Modern frontend frameworks and best practices'),
('Backend Development', 'APIs, Node.js, and database connections'),
('Blockchain Intro', 'Understand blockchain and smart contracts'),
('AI Fundamentals', 'Introduction to artificial intelligence concepts'),
('System Administration', 'Linux, shell scripting, and automation'),
('Ethical Hacking', 'Pen-testing and security best practices'),
('Cloud Native Apps', 'Containers, orchestration, and scaling'),
('Web Security', 'OWASP Top 10 and secure coding'),
('Data Structures', 'Essential algorithms and data handling');

-- Insert data into the student_module_xref table.
INSERT INTO student_module_xref (student_id, module_id, status) VALUES
(1, 1, 'Completed'),
(1, 2, 'In Progress'),
(2, 1, 'Completed'),
(2, 3, 'In Progress'),
(3, 4, 'In Progress'),
(4, 1, 'Completed'),
(4, 5, 'In Progress'),
(5, 2, 'Completed'),
(5, 3, 'Completed'),
(6, 6, 'In Progress'),
(7, 7, 'In Progress'),
(8, 4, 'Completed'),
(9, 5, 'In Progress'),
(10, 8, 'In Progress'),
(11, 9, 'Completed'),
(12, 10, 'Completed'),
(13, 11, 'In Progress'),
(14, 12, 'In Progress'),
(15, 13, 'Completed'),
(16, 14, 'In Progress'),
(17, 15, 'Completed'),
(18, 16, 'Completed'),
(19, 17, 'In Progress'),
(20, 18, 'In Progress');
