/* *************************************************************
Drop and Create the tables for the skill_bootcamp database.
*************************************************************** */

-- Switch to the skill_bootcamp database.
USE skill_bootcamp;

-- Drop the cohorts table if it exists
DROP TABLE IF EXISTS cohorts;

-- Create the cohorts table
CREATE TABLE cohorts (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  cohort_name VARCHAR(100) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL
);

-- Drop the students table if it exists
DROP TABLE IF EXISTS students;

-- Create the students table
CREATE TABLE students (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(25) NOT NULL,
  last_name  VARCHAR(25) NOT NULL,
  cohort_id INT
);

-- Add foreign key constraint to link cohort_id to cohorts table
ALTER TABLE `students` ADD CONSTRAINT `student_cohort_ibfk_1` FOREIGN KEY (`cohort_id`) REFERENCES `cohorts`(`id`) ON DELETE SET NULL ON UPDATE CASCADE;

-- Drop the modules table if it exists
DROP TABLE IF EXISTS modules;

-- Create the modules table
CREATE TABLE modules (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  module_name VARCHAR(100) NOT NULL,
  description VARCHAR(255) NOT NULL
);

-- Drop the student_module_xref table if it exists
DROP TABLE IF EXISTS student_module_xref;

-- Create the student_module_xref table
CREATE TABLE student_module_xref (
  student_id INT NOT NULL,
  module_id  INT NOT NULL,
  status VARCHAR(25) DEFAULT 'in-progress'
);

-- Designate the composite primary key
ALTER TABLE `student_module_xref` ADD PRIMARY KEY (`student_id`, `module_id`);

-- Add foreign key constraint to link student_id to students table
ALTER TABLE `student_module_xref` ADD CONSTRAINT `xref_student_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students`(`id`) ON DELETE CASCADE ON UPDATE CASCADE; 

-- Add foreign key constraint to link module_id to modules table
ALTER TABLE `student_module_xref` ADD CONSTRAINT `xref_module_ibfk_2` FOREIGN KEY (`module_id`) REFERENCES `modules`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
