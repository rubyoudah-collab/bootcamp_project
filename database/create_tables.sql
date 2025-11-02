USE skill_bootcamp;

DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(25) NOT NULL,
  last_name  VARCHAR(25) NOT NULL,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS modules;
CREATE TABLE modules (
  id INT NOT NULL AUTO_INCREMENT,
  module_name VARCHAR(100) NOT NULL,
  description VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS cohorts;
CREATE TABLE cohorts (
  id INT NOT NULL AUTO_INCREMENT,
  cohort_name VARCHAR(100) NOT NULL,
  start_date VARCHAR(25) NOT NULL,
  end_date   VARCHAR(25) NOT NULL,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS student_module_xref;
CREATE TABLE student_module_xref (
  student_id INT NOT NULL,
  module_id  INT NOT NULL,
  status     VARCHAR(25) NOT NULL,
  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (module_id)  REFERENCES modules(id)  ON DELETE CASCADE ON UPDATE CASCADE
);
