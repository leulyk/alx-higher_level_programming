-- 0x0D. SQL introduction, task 17

-- convert database, first_table and name field to utf8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_general_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CHARACTER SET utf8 COLLATE utf8_general_ci;
