-- Drop the database if it exists to refresh it
BEGIN
    DROP DATABASE WellnessWhisperDB;
END;
GO

-- Create the database
CREATE DATABASE WellnessWhisperDB;
GO

-- Use the newly created database
USE WellnessWhisperDB;
GO

-- 1. Roles Table
CREATE TABLE roles (
    role_id INT NOT NULL IDENTITY(1,1),
    description TEXT,
    role_name VARCHAR(255),
    permissions TEXT,
    PRIMARY KEY(role_id)
);
GO

-- 2. Users Table
CREATE TABLE users (
    user_id INT NOT NULL IDENTITY(1,1),
    role_id INT,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    profile_picture VARCHAR(255),
    bio TEXT,
    location VARCHAR(255),
    last_login DATETIME,
    is_verified BIT DEFAULT 0,
    PRIMARY KEY(user_id),
    FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE SET NULL
);
GO

-- 3. Sessions Table
CREATE TABLE sessions (
    session_id INT NOT NULL IDENTITY(1,1),
    user_id INT,
    start_time DATETIME,
    end_time DATETIME,
    status VARCHAR(50),
    PRIMARY KEY(session_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
GO

-- 4. Counsellor Profiles Table (moved before Bookings for FK reference)
CREATE TABLE counsellor_profiles (
    counsellor_id INT NOT NULL IDENTITY(1,1),
    user_id INT,
    specialization VARCHAR(255),
    experience_years INT,
    qualification VARCHAR(255),
    bio TEXT,
    PRIMARY KEY(counsellor_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
GO

-- 5. Bookings Table
CREATE TABLE bookings (
    booking_id INT NOT NULL IDENTITY(1,1),
    user_id INT,
    counsellor_id INT,
    session_id INT,
    booking_date DATETIME,
    status VARCHAR(50),
    PRIMARY KEY(booking_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY (counsellor_id) REFERENCES counsellor_profiles(counsellor_id) ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE SET NULL
);
GO

-- 6. Chat Logs Table
CREATE TABLE chat_logs (
    chat_id INT NOT NULL IDENTITY(1,1),
    session_id INT,
    sender_id INT,
    receiver_id INT,
    message TEXT,
    timestamp DATETIME,
    PRIMARY KEY(chat_id),
    FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE CASCADE,
    FOREIGN KEY (sender_id) REFERENCES users(user_id) ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY (receiver_id) REFERENCES users(user_id) ON DELETE NO ACTION ON UPDATE NO ACTION
);
GO

-- 7. Call Logs Table
CREATE TABLE call_logs (
    call_id INT NOT NULL IDENTITY(1,1),
    session_id INT,
    caller_id INT,
    callee_id INT,
    start_time DATETIME,
    end_time DATETIME,
    status VARCHAR(50),
    PRIMARY KEY(call_id),
    FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE CASCADE,
    FOREIGN KEY (caller_id) REFERENCES users(user_id) ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY (callee_id) REFERENCES users(user_id) ON DELETE NO ACTION ON UPDATE NO ACTION
);
GO

-- 8. Mood Tracking Table
CREATE TABLE mood_tracking (
    mood_entry_id INT NOT NULL IDENTITY(1,1),
    user_id INT,
    mood INT CHECK (mood >= 0 AND mood <= 5),
    entry_date DATETIME,
    comments TEXT,
    PRIMARY KEY(mood_entry_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
GO

-- 9. Counsellor Availability Table
CREATE TABLE counsellor_availabilities (
    availability_id INT NOT NULL IDENTITY(1,1),
    counsellor_id INT,
    day_of_week VARCHAR(20),
    start_time TIME,
    end_time TIME,
    PRIMARY KEY(availability_id),
    FOREIGN KEY (counsellor_id) REFERENCES counsellor_profiles(counsellor_id) ON DELETE CASCADE
);
GO

-- 10. Notifications Table
CREATE TABLE notifications (
    notification_id INT NOT NULL IDENTITY(1,1),
    user_id INT,
    message TEXT,
    timestamp DATETIME,
    status VARCHAR(50),
    PRIMARY KEY(notification_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
GO

-- 11. Chatbot Logs Table
CREATE TABLE chatbot_logs (
    chatbot_log_id INT NOT NULL IDENTITY(1,1),
    user_id INT,
    input_message TEXT,
    response_message TEXT,
    timestamp DATETIME,
    PRIMARY KEY(chatbot_log_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
GO