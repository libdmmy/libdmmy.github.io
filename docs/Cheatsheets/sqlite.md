# sqlite

## useful information
there's `vd` (`visidata`) utility to view sqlite databases in a nice TUI.

## basic stuff
create a new database and enter it in command line:
```bash
sqlite3 database.db
```

```sql
-- this is comment btw
-- you can write syntax in either lowercase or uppercase

-- start making changes
begin transaction;

-- without `if not exists` it'll throw an error if table already exists
create table if not exists users (
 -- <NAME> <TYPE> <OPTIONS>,
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age integer check (age >= 0),
    email text unique
);

-- insert data
-- please note, that strings are accepted only in single-quotes,
--   not " one;
INSERT INTO users (name, age) VALUES ('dummy', 16);

-- update data
UPDATE users SET age = 17 WHERE name = 'dummy';

-- delete data
DELETE FROM users WHERE id = 101;

-- save changes
commit;

-- view table's columns
pragma table_info(users);
-- 0|id|INTEGER|0||1
-- 1|name|TEXT|1||0
-- 2|age|INTEGER|0||0
-- 3|email|TEXT|0||0

begin transaction;

-- rename table
ALTER TABLE users RENAME TO customers;

-- select data
SELECT * FROM customers WHERE age > 25 ORDER BY name DESC LIMIT 5;

-- add column
ALTER TABLE customers ADD COLUMN phone TEXT;

-- drop column
ALTER TABLE customers DROP COLUMN phone;

-- delete table
DROP TABLE customers;

-- drop changes
rollback;
```
