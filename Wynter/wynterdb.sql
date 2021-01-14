-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 14, 2021 at 08:44 PM
-- Server version: 10.3.25-MariaDB-0+deb10u1
-- PHP Version: 7.3.19-1~deb10u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `slyjenna`
--

-- --------------------------------------------------------

--
-- Table structure for table `blacklistedwords`
--

CREATE TABLE `blacklistedwords` (
  `word` varchar(255) NOT NULL COMMENT 'The blacklisted word',
  `id` int(11) NOT NULL COMMENT 'Auto Incrementing ID to make mssql stfu xD',
  `guildId` varchar(20) DEFAULT NULL COMMENT 'Guild ID'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `blacklistedwords`
--

INSERT INTO `blacklistedwords` (`word`, `id`, `guildId`) VALUES
('fuck', 1, NULL),
('shit', 2, NULL),
('cunt', 3, NULL),
('bastard', 4, NULL),
('bitch', 5, NULL),
('prick', 6, NULL),
('nigga', 7, NULL),
('nigger', 8, NULL),
('nignog', 9, NULL),
('n1gga', 10, NULL),
('n1gger', 11, NULL),
('nugger', 12, NULL),
('slut', 13, NULL),
('twat', 14, NULL),
('wanker', 15, NULL),
('faggot', 16, NULL),
('fag', 17, NULL),
('whore', 18, NULL),
('dickhead', 19, NULL),
('nibba', 20, NULL),
('f-u-c-k', 21, NULL),
('f-uck', 22, NULL),
('s-hit', 23, NULL),
('frick', 24, NULL),
('sh1t', 25, NULL),
('b1tch', 26, NULL),
('ni:b::b:a', 27, NULL),
('fück', 28, NULL),
('dick', 29, NULL),
('fruck', 30, NULL),
('niggggggaaaaaa', 31, NULL),
('cock', 32, NULL),
('cocksucker', 33, NULL),
('pussy', 34, NULL),
('nibber', 35, NULL),
('niqqer', 36, NULL),
('fuck', 37, NULL),
('shit', 38, NULL),
('cunt', 39, NULL),
('bastard', 40, NULL),
('bitch', 41, NULL),
('prick', 42, NULL),
('nigga', 43, NULL),
('nigger', 44, NULL),
('nignog', 45, NULL),
('n1gga', 46, NULL),
('n1gger', 47, NULL),
('nugger', 48, NULL),
('slut', 49, NULL),
('twat', 50, NULL),
('wanker', 51, NULL),
('faggot', 52, NULL),
('fag', 53, NULL),
('whore', 54, NULL),
('dickhead', 55, NULL),
('nibba', 56, NULL),
('f-u-c-k', 57, NULL),
('f-uck', 58, NULL),
('s-hit', 59, NULL),
('frick', 60, NULL),
('sh1t', 61, NULL),
('b1tch', 62, NULL),
('ni:b::b:a', 63, NULL),
('fück', 64, NULL),
('dick', 65, NULL),
('fruck', 66, NULL),
('niggggggaaaaaa', 67, NULL),
('cock', 68, NULL),
('cocksucker', 69, NULL),
('pussy', 70, NULL),
('nibber', 71, NULL),
('niqqer', 72, NULL),
('fuck', 73, NULL),
('shit', 74, NULL),
('cunt', 75, NULL),
('bastard', 76, NULL),
('bitch', 77, NULL),
('prick', 78, NULL),
('nigga', 79, NULL),
('nigger', 80, NULL),
('nignog', 81, NULL),
('n1gga', 82, NULL),
('n1gger', 83, NULL),
('nugger', 84, NULL),
('slut', 85, NULL),
('twat', 86, NULL),
('wanker', 87, NULL),
('faggot', 88, NULL),
('fag', 89, NULL),
('whore', 90, NULL),
('dickhead', 91, NULL),
('nibba', 92, NULL),
('f-u-c-k', 93, NULL),
('f-uck', 94, NULL),
('s-hit', 95, NULL),
('frick', 96, NULL),
('sh1t', 97, NULL),
('b1tch', 98, NULL),
('ni:b::b:a', 99, NULL),
('fück', 100, NULL),
('dick', 101, NULL),
('fruck', 102, NULL),
('niggggggaaaaaa', 103, NULL),
('cock', 104, NULL),
('cocksucker', 105, NULL),
('pussy', 106, NULL),
('nibber', 107, NULL),
('niqqer', 108, NULL),
('fuck', 109, NULL),
('shit', 110, NULL),
('cunt', 111, NULL),
('bastard', 112, NULL),
('bitch', 113, NULL),
('prick', 114, NULL),
('nigga', 115, NULL),
('nigger', 116, NULL),
('nignog', 117, NULL),
('n1gga', 118, NULL),
('n1gger', 119, NULL),
('nugger', 120, NULL),
('slut', 121, NULL),
('twat', 122, NULL),
('wanker', 123, NULL),
('faggot', 124, NULL),
('fag', 125, NULL),
('whore', 126, NULL),
('dickhead', 127, NULL),
('nibba', 128, NULL),
('f-u-c-k', 129, NULL),
('f-uck', 130, NULL),
('s-hit', 131, NULL),
('frick', 132, NULL),
('sh1t', 133, NULL),
('b1tch', 134, NULL),
('ni:b::b:a', 135, NULL),
('fück', 136, NULL),
('dick', 137, NULL),
('fruck', 138, NULL),
('niggggggaaaaaa', 139, NULL),
('cock', 140, NULL),
('cocksucker', 141, NULL),
('pussy', 142, NULL),
('nibber', 143, NULL),
('niqqer', 144, NULL),
('fuck', 145, '784883980733644832'),
('shit', 146, '784883980733644832'),
('cunt', 147, '784883980733644832'),
('bastard', 148, '784883980733644832'),
('bitch', 149, '784883980733644832'),
('prick', 150, '784883980733644832'),
('nigga', 151, '784883980733644832'),
('nigger', 152, '784883980733644832'),
('nignog', 153, '784883980733644832'),
('n1gga', 154, '784883980733644832'),
('n1gger', 155, '784883980733644832'),
('nugger', 156, '784883980733644832'),
('slut', 157, '784883980733644832'),
('twat', 158, '784883980733644832'),
('wanker', 159, '784883980733644832'),
('faggot', 160, '784883980733644832'),
('fag', 161, '784883980733644832'),
('whore', 162, '784883980733644832'),
('dickhead', 163, '784883980733644832'),
('nibba', 164, '784883980733644832'),
('f-u-c-k', 165, '784883980733644832'),
('f-uck', 166, '784883980733644832'),
('s-hit', 167, '784883980733644832'),
('frick', 168, '784883980733644832'),
('sh1t', 169, '784883980733644832'),
('b1tch', 170, '784883980733644832'),
('ni:b::b:a', 171, '784883980733644832'),
('fück', 172, '784883980733644832'),
('dick', 173, '784883980733644832'),
('fruck', 174, '784883980733644832'),
('niggggggaaaaaa', 175, '784883980733644832'),
('cock', 176, '784883980733644832'),
('cocksucker', 177, '784883980733644832'),
('pussy', 178, '784883980733644832'),
('nibber', 179, '784883980733644832'),
('niqqer', 180, '784883980733644832');

-- --------------------------------------------------------

--
-- Table structure for table `bypasschannels`
--

CREATE TABLE `bypasschannels` (
  `id` int(11) NOT NULL COMMENT 'Auto Incrementing ID to make mssql stfu xD',
  `channelid` varchar(255) NOT NULL COMMENT 'The Channel ID',
  `guildId` varchar(20) DEFAULT NULL COMMENT 'Guild ID'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `guilds`
--

CREATE TABLE `guilds` (
  `id` varchar(20) NOT NULL COMMENT 'Guild ID',
  `name` varchar(255) DEFAULT NULL COMMENT 'The Guild Name',
  `prefix` varchar(255) DEFAULT '!' COMMENT 'The Prefix',
  `deleteinvlinks` tinyint(4) DEFAULT 0 COMMENT 'Delete inv links or not',
  `enablefandx` tinyint(4) DEFAULT 0 COMMENT 'Enable F and X commands or not',
  `enfandximages` tinyint(4) NOT NULL COMMENT 'Enable / disable f and x command images.',
  `muterole` varchar(255) DEFAULT NULL COMMENT 'The guilds mute role'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `punishments`
--

CREATE TABLE `punishments` (
  `id` int(11) NOT NULL COMMENT 'Incremented ID',
  `servername` varchar(255) DEFAULT NULL COMMENT 'The Guild Name',
  `serverid` varchar(255) NOT NULL COMMENT 'The server ID',
  `offender` varchar(255) NOT NULL COMMENT 'The offender name',
  `offenderid` varchar(255) NOT NULL,
  `moderator` varchar(255) NOT NULL COMMENT 'The moderator name',
  `type` varchar(255) NOT NULL COMMENT 'Type of punishment',
  `reason` varchar(255) NOT NULL COMMENT 'Reason of punishment'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `twitter`
--

CREATE TABLE `twitter` (
  `id` varchar(255) NOT NULL,
  `secret` varchar(255) NOT NULL,
  `token` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blacklistedwords`
--
ALTER TABLE `blacklistedwords`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bypasschannels`
--
ALTER TABLE `bypasschannels`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `guilds`
--
ALTER TABLE `guilds`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `punishments`
--
ALTER TABLE `punishments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `twitter`
--
ALTER TABLE `twitter`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `IDX_ec8fddcdc5dec2ffd9693afe4f` (`secret`),
  ADD UNIQUE KEY `IDX_0bf7851ed0e904c61600482224` (`token`),
  ADD UNIQUE KEY `IDX_1ad06f173076d81d149d39d787` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blacklistedwords`
--
ALTER TABLE `blacklistedwords`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Auto Incrementing ID to make mssql stfu xD', AUTO_INCREMENT=181;
--
-- AUTO_INCREMENT for table `bypasschannels`
--
ALTER TABLE `bypasschannels`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Auto Incrementing ID to make mssql stfu xD';
--
-- AUTO_INCREMENT for table `punishments`
--
ALTER TABLE `punishments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Incremented ID';
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
