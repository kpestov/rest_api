CREATE DATABASE test1;
use test1;

CREATE TABLE tree (
  id INT unsigned NOT NULL AUTO_INCREMENT,
  parent_id INT unsigned DEFAULT NULL,
  name VARCHAR(50) NOT NULL UNIQUE,
  slug VARCHAR(140) UNIQUE,
  body TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (parent_id) REFERENCES tree (id)
    ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO tree
  (parent_id, name, slug, body)

VALUES
  (NULL, 'Programming language', NULL, NULL),
  (1, 'Dynamically typed languages', NULL, NULL),
  (2, 'Python', 'Python', 'some text'),
  (2, 'JavaScript', 'JavaScript', 'some text');