-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 30, 2023 at 07:26 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `auth_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `diabetes`
--

CREATE TABLE `diabetes` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `bs_fast` int(11) NOT NULL,
  `breakfast_time` time NOT NULL,
  `breakfast_menu` varchar(255) NOT NULL,
  `lunch_time` time NOT NULL,
  `lunch_menu` varchar(255) NOT NULL,
  `dinner_time` time NOT NULL,
  `dinner_menu` varchar(255) NOT NULL,
  `bs_dinner` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `diabetes`
--

INSERT INTO `diabetes` (`id`, `user_id`, `date`, `bs_fast`, `breakfast_time`, `breakfast_menu`, `lunch_time`, `lunch_menu`, `dinner_time`, `dinner_menu`, `bs_dinner`) VALUES
(1, 4, '2023-04-07', 45, '17:48:00', 'fdfd', '20:46:00', 'dfdf', '17:46:00', 'dfdf', 3434),
(2, 4, '2023-04-07', 45, '17:48:00', 'fdfd', '20:46:00', 'dfdf', '17:46:00', 'dfdf', 3434),
(3, 4, '2023-04-07', 45, '17:48:00', 'fdfd', '20:46:00', 'dfdf', '17:46:00', 'dfdf', 3434);

-- --------------------------------------------------------

--
-- Table structure for table `reset_password`
--

CREATE TABLE `reset_password` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `temp_password` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `reset_password`
--

INSERT INTO `reset_password` (`id`, `email`, `temp_password`, `created_at`) VALUES
(1, 'crosetsw09@gmail.com', '51b2da8e', '2023-04-29 14:11:01'),
(2, 'crosetsw09@gmail.com', '1604cf16', '2023-04-29 14:16:30'),
(3, 'crosetsw09@gmail.com', '16e04e49', '2023-04-29 14:18:15'),
(4, 'crosetsw09@gmail.com', '0ad22e95', '2023-04-29 14:20:11');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `fullname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `dob` date NOT NULL,
  `username` varchar(255) NOT NULL,
  `fpassword` varchar(255) NOT NULL,
  `question1` varchar(255) NOT NULL,
  `question1_answer` varchar(255) NOT NULL,
  `question2` varchar(255) NOT NULL,
  `question2_answer` varchar(255) NOT NULL,
  `question3` varchar(255) NOT NULL,
  `question3_answer` varchar(255) NOT NULL,
  `picture_pass` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `fullname`, `email`, `phone`, `dob`, `username`, `fpassword`, `question1`, `question1_answer`, `question2`, `question2_answer`, `question3`, `question3_answer`, `picture_pass`) VALUES
(4, 'joseph gitau', 'crosetsw09@gmail.com', '+254724772046', '2023-04-21', 'burt', 'Jose2509@@', 'college', 'gfhfh', 'field-trip', 'gfgf', 'driving-instructor', 'rerere', 'stefan-rodriguez-2AovfzYV3rc-unsplash.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `diabetes`
--
ALTER TABLE `diabetes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reset_password`
--
ALTER TABLE `reset_password`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `diabetes`
--
ALTER TABLE `diabetes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `reset_password`
--
ALTER TABLE `reset_password`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
