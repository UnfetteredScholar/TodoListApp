-- create a table
CREATE TABLE todos(
  id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  name TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'Pending'
);

-- add test data
INSERT INTO todos (name, status)
  VALUES ('Buy new shows', 'Complete'),
  ('Buy new shirt', 'Pending');