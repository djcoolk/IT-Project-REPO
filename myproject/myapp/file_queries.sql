-- Use the database
USE WellnessWhisperDB;
GO

-- Insert roles into the roles table
INSERT INTO roles (description, role_name, permissions) VALUES
('General user with basic access rights', 'general user', 'read, book, track mood'),
('Counsellor with permissions to manage sessions', 'counsellor', 'read, manage sessions, chat, call'),
('Administrator with full permissions', 'admin', 'read, write, delete, manage users');
GO

-- Insert users into the users table
-- Adding 3 general users for variety
INSERT INTO users (role_id, username, email, password_hash, full_name, profile_picture, bio, location, last_login, is_verified) VALUES
(1, 'user1', 'user1@example.com', 'password_hash_1', 'User One', 'profile_pic_1.jpg', 'This is user one bio.', 'Location One', GETDATE(), 1),
(1, 'user2', 'user2@example.com', 'password_hash_2', 'User Two', 'profile_pic_2.jpg', 'This is user two bio.', 'Location Two', GETDATE(), 0),
(1, 'user3', 'user3@example.com', 'password_hash_3', 'User Three', 'profile_pic_3.jpg', 'This is user three bio.', 'Location Three', GETDATE(), 1),
-- Adding 5 counsellors
(2, 'counsellor1', 'counsellor1@example.com', 'password_hash_4', 'Counsellor One', 'profile_pic_4.jpg', 'This is counsellor one bio.', 'Location Four', GETDATE(), 1),
(2, 'counsellor2', 'counsellor2@example.com', 'password_hash_5', 'Counsellor Two', 'profile_pic_5.jpg', 'This is counsellor two bio.', 'Location Five', GETDATE(), 1),
(2, 'counsellor3', 'counsellor3@example.com', 'password_hash_6', 'Counsellor Three', 'profile_pic_6.jpg', 'This is counsellor three bio.', 'Location Six', GETDATE(), 1),
(2, 'counsellor4', 'counsellor4@example.com', 'password_hash_7', 'Counsellor Four', 'profile_pic_7.jpg', 'This is counsellor four bio.', 'Location Seven', GETDATE(), 1),
(2, 'counsellor5', 'counsellor5@example.com', 'password_hash_8', 'Counsellor Five', 'profile_pic_8.jpg', 'This is counsellor five bio.', 'Location Eight', GETDATE(), 1),
-- Adding admin named Kwaku
(3, 'kwaku', 'kwaku@example.com', 'password_hash_9', 'Kwaku Admin', 'profile_pic_9.jpg', 'This is Kwaku the admin.', 'Location Nine', GETDATE(), 1);
GO

-- Insert counsellor profiles into the counsellor_profiles table
-- Align user IDs of counsellors to match user table insertion IDs
INSERT INTO counsellor_profiles (user_id, specialization, experience_years, qualification, bio) VALUES
(4, 'Mental Health', 10, 'PhD in Psychology', 'Counsellor One has extensive experience in mental health counseling.'),
(5, 'Career Counseling', 8, 'MSc in Career Counseling', 'Counsellor Two specializes in career advice and guidance.'),
(6, 'Relationship Counseling', 12, 'PhD in Human Relations', 'Counsellor Three focuses on relationship matters.'),
(7, 'Stress Management', 7, 'MSc in Health Psychology', 'Counsellor Four is an expert in managing and reducing stress.'),
(8, 'Substance Abuse Counseling', 15, 'PhD in Addiction Studies', 'Counsellor Five has extensive experience in substance abuse counseling.');
GO

-- Insert some sample data for other tables as needed
INSERT INTO sessions (user_id, start_time, end_time, status) VALUES
(1, GETDATE(), DATEADD(hour, 1, GETDATE()), 'scheduled'),
(2, GETDATE(), DATEADD(hour, 1, GETDATE()), 'completed');
GO

INSERT INTO bookings (user_id, counsellor_id, session_id, booking_date, status) VALUES
(1, 1, 1, GETDATE(), 'scheduled'),
(2, 1, 2, GETDATE(), 'completed');
GO

INSERT INTO mood_tracking (user_id, mood, entry_date, comments) VALUES
(1, 3, GETDATE(), 'Feeling neutral today'),
(2, 4, GETDATE(), 'Feeling good today');
GO

INSERT INTO counsellor_availabilities (counsellor_id, day_of_week, start_time, end_time) VALUES
(1, 'Monday', '09:00:00', '17:00:00'),
(2, 'Wednesday', '09:00:00', '17:00:00'),
(3, 'Tuesday', '09:00:00', '17:00:00'),
(4, 'Thursday', '09:00:00', '17:00:00'),
(5, 'Friday', '09:00:00', '17:00:00');
GO

INSERT INTO notifications (user_id, message, timestamp, status) VALUES
(1, 'Your booking is confirmed.', GETDATE(), 'unread'),
(2, 'Your session is completed.', GETDATE(), 'unread');
GO

INSERT INTO chatbot_logs (user_id, input_message, response_message, timestamp) VALUES
(1, 'Hello, I am feeling stressed.', 'I am here to help you. Can you describe what is causing you stress?', GETDATE()),
(2, 'How can I book a session?', 'You can book a session through the Bookings page on our platform.', GETDATE());
GO