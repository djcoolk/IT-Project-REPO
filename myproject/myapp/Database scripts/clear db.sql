-- Set the database context to your database
USE WellnessWhisperDB;  -- Change this to your database name if different

-- Disable foreign key constraints
EXEC sp_MSforeachtable "ALTER TABLE ? NOCHECK CONSTRAINT ALL";

-- Drop all tables
EXEC sp_MSforeachtable "DROP TABLE ?";

-- Optional: Drop any views, stored procedures, and functions if necessary
-- Uncomment these lines if needed
-- EXEC sp_MSforeachtable "DROP VIEW ?";
-- EXEC sp_MSforeachtable "DROP PROCEDURE ?";
-- EXEC sp_MSforeachtable "DROP FUNCTION ?";

-- Re-enable foreign key constraints
EXEC sp_MSforeachtable "ALTER TABLE ? CHECK CONSTRAINT ALL";
