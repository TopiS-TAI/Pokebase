-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: 20.05.2024 klo 20:54
-- Palvelimen versio: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pokemon`
--

-- --------------------------------------------------------

--
-- Rakenne taululle `mons`
--

CREATE TABLE `mons` (
  `id` int(11) NOT NULL,
  `name` varchar(64) NOT NULL,
  `hp` int(11) NOT NULL,
  `attack` int(11) NOT NULL,
  `defense` int(11) NOT NULL,
  `s_attack` int(11) NOT NULL,
  `s_defense` int(11) NOT NULL,
  `speed` int(11) NOT NULL,
  `type1` int(11) NOT NULL,
  `type2` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Vedos taulusta `mons`
--

INSERT INTO `mons` (`id`, `name`, `hp`, `attack`, `defense`, `s_attack`, `s_defense`, `speed`, `type1`, `type2`) VALUES
(1, 'Bulbasaur', 45, 45, 49, 65, 65, 45, 5, 8),
(2, 'Charmander', 39, 52, 43, 60, 50, 65, 2, NULL);

-- --------------------------------------------------------

--
-- Rakenne taululle `types`
--

CREATE TABLE `types` (
  `id` int(11) NOT NULL,
  `name` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Vedos taulusta `types`
--

INSERT INTO `types` (`id`, `name`) VALUES
(1, 'normal'),
(2, 'fire'),
(3, 'water'),
(4, 'electric'),
(5, 'grass'),
(6, 'ice'),
(7, 'fighting'),
(8, 'poison'),
(9, 'ground'),
(10, 'flying'),
(11, 'psychic'),
(12, 'bug'),
(13, 'rock'),
(14, 'ghost'),
(15, 'dragon'),
(16, 'dark'),
(17, 'steel'),
(18, 'fairy');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mons`
--
ALTER TABLE `mons`
  ADD PRIMARY KEY (`id`),
  ADD KEY `type1` (`type1`,`type2`),
  ADD KEY `type2` (`type2`);

--
-- Indexes for table `types`
--
ALTER TABLE `types`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `mons`
--
ALTER TABLE `mons`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `types`
--
ALTER TABLE `types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- Rajoitteet vedostauluille
--

--
-- Rajoitteet taululle `mons`
--
ALTER TABLE `mons`
  ADD CONSTRAINT `mons_ibfk_1` FOREIGN KEY (`type1`) REFERENCES `types` (`id`),
  ADD CONSTRAINT `mons_ibfk_2` FOREIGN KEY (`type2`) REFERENCES `types` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
