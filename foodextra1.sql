-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 13, 2022 at 10:57 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `foodextra1`
--

-- --------------------------------------------------------

--
-- Table structure for table `app_tbl_beneficiar`
--

CREATE TABLE `app_tbl_beneficiar` (
  `beneficiar_id` varchar(90) NOT NULL,
  `name` varchar(90) NOT NULL,
  `description` varchar(90) NOT NULL,
  `location` varchar(90) NOT NULL,
  `address` varchar(90) NOT NULL,
  `contact_person` varchar(90) NOT NULL,
  `phone` varchar(90) NOT NULL,
  `email` varchar(90) NOT NULL,
  `status` varchar(90) NOT NULL,
  `pincode` varchar(90) NOT NULL,
  `proof` varchar(90) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_tbl_beneficiar`
--

INSERT INTO `app_tbl_beneficiar` (`beneficiar_id`, `name`, `description`, `location`, `address`, `contact_person`, `phone`, `email`, `status`, `pincode`, `proof`) VALUES
('BID_001', 'LUDIAD MUHAMED', 'iam jiuts not rich', 'kallai', 'SAJITHA HOUSE ,SPARK NO-71,PARAPPIL,\r\nFRANCIS ROAD, KALLAI PO', '8726262222', '7594066757', 'muhammedlud@gmail.com', 'verified', '', '/media/Screenshot%20(3).png');

-- --------------------------------------------------------

--
-- Table structure for table `app_tbl_donor`
--

CREATE TABLE `app_tbl_donor` (
  `donor_id` varchar(90) NOT NULL,
  `organization_name` varchar(90) NOT NULL,
  `person_in_charge_name` varchar(90) NOT NULL,
  `address` varchar(90) NOT NULL,
  `phone` varchar(90) NOT NULL,
  `alternative_phone` varchar(90) NOT NULL,
  `pincode` varchar(90) NOT NULL,
  `email` varchar(90) NOT NULL,
  `description` varchar(90) NOT NULL,
  `status` varchar(90) NOT NULL,
  `proof` varchar(90) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_tbl_donor`
--

INSERT INTO `app_tbl_donor` (`donor_id`, `organization_name`, `person_in_charge_name`, `address`, `phone`, `alternative_phone`, `pincode`, `email`, `description`, `status`, `proof`) VALUES
('DID_001', 'kfc hub', 'kfc', 'calicut', '6752728282', '9827272772', '675111', 'foodextra.in@gmail.com', '', 'verified', '/media/Annotation%202021-07-31%20214114_4fGByxi.png');

-- --------------------------------------------------------

--
-- Table structure for table `app_tbl_idgen`
--

CREATE TABLE `app_tbl_idgen` (
  `id` bigint(20) NOT NULL,
  `vid` int(11) NOT NULL,
  `did` int(11) NOT NULL,
  `bid` int(11) NOT NULL,
  `fid` int(11) NOT NULL,
  `prid` int(11) NOT NULL,
  `rid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `brid` int(11) NOT NULL,
  `alid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_tbl_idgen`
--

INSERT INTO `app_tbl_idgen` (`id`, `vid`, `did`, `bid`, `fid`, `prid`, `rid`, `cid`, `brid`, `alid`) VALUES
(1, 0, 2, 1, 2, 0, 0, 0, 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `app_tbl_login`
--

CREATE TABLE `app_tbl_login` (
  `id` bigint(20) NOT NULL,
  `username` varchar(90) NOT NULL,
  `password` varchar(90) NOT NULL,
  `catagory` varchar(90) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_tbl_login`
--

INSERT INTO `app_tbl_login` (`id`, `username`, `password`, `catagory`) VALUES
(1, 'admin', 'admin', 'admin'),
(2, 'DID_001', '6752728282', 'donor'),
(5, 'DID_002', '4567892929', 'donor'),
(6, 'foodextra.in@gmail.com', '6752728282', 'donor'),
(7, 'muhammedlud@gmail.com', '7594066757', 'beneficiar');

-- --------------------------------------------------------

--
-- Table structure for table `app_tbl_volunteers`
--

CREATE TABLE `app_tbl_volunteers` (
  `volunteer_id` varchar(90) NOT NULL,
  `name` varchar(90) NOT NULL,
  `age` varchar(90) NOT NULL,
  `gender` varchar(90) NOT NULL,
  `location` varchar(90) NOT NULL,
  `natureofjob` varchar(90) NOT NULL,
  `photo` varchar(90) NOT NULL,
  `email` varchar(90) NOT NULL,
  `phone` varchar(90) NOT NULL,
  `status` varchar(90) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add tbl_donor', 7, 'add_tbl_donor'),
(26, 'Can change tbl_donor', 7, 'change_tbl_donor'),
(27, 'Can delete tbl_donor', 7, 'delete_tbl_donor'),
(28, 'Can view tbl_donor', 7, 'view_tbl_donor'),
(29, 'Can add tbl_volunteers', 8, 'add_tbl_volunteers'),
(30, 'Can change tbl_volunteers', 8, 'change_tbl_volunteers'),
(31, 'Can delete tbl_volunteers', 8, 'delete_tbl_volunteers'),
(32, 'Can view tbl_volunteers', 8, 'view_tbl_volunteers'),
(33, 'Can add tbl_idgen', 9, 'add_tbl_idgen'),
(34, 'Can change tbl_idgen', 9, 'change_tbl_idgen'),
(35, 'Can delete tbl_idgen', 9, 'delete_tbl_idgen'),
(36, 'Can view tbl_idgen', 9, 'view_tbl_idgen'),
(37, 'Can add tbl_beneficiar', 10, 'add_tbl_beneficiar'),
(38, 'Can change tbl_beneficiar', 10, 'change_tbl_beneficiar'),
(39, 'Can delete tbl_beneficiar', 10, 'delete_tbl_beneficiar'),
(40, 'Can view tbl_beneficiar', 10, 'view_tbl_beneficiar'),
(41, 'Can add tbl_login', 11, 'add_tbl_login'),
(42, 'Can change tbl_login', 11, 'change_tbl_login'),
(43, 'Can delete tbl_login', 11, 'delete_tbl_login'),
(44, 'Can view tbl_login', 11, 'view_tbl_login'),
(45, 'Can add tbl_fooddonation', 12, 'add_tbl_fooddonation'),
(46, 'Can change tbl_fooddonation', 12, 'change_tbl_fooddonation'),
(47, 'Can delete tbl_fooddonation', 12, 'delete_tbl_fooddonation'),
(48, 'Can view tbl_fooddonation', 12, 'view_tbl_fooddonation'),
(49, 'Can add tbl_publicrequest', 13, 'add_tbl_publicrequest'),
(50, 'Can change tbl_publicrequest', 13, 'change_tbl_publicrequest'),
(51, 'Can delete tbl_publicrequest', 13, 'delete_tbl_publicrequest'),
(52, 'Can view tbl_publicrequest', 13, 'view_tbl_publicrequest'),
(53, 'Can add tbl_review', 14, 'add_tbl_review'),
(54, 'Can change tbl_review', 14, 'change_tbl_review'),
(55, 'Can delete tbl_review', 14, 'delete_tbl_review'),
(56, 'Can view tbl_review', 14, 'view_tbl_review'),
(57, 'Can add tbl_complaint', 15, 'add_tbl_complaint'),
(58, 'Can change tbl_complaint', 15, 'change_tbl_complaint'),
(59, 'Can delete tbl_complaint', 15, 'delete_tbl_complaint'),
(60, 'Can view tbl_complaint', 15, 'view_tbl_complaint'),
(61, 'Can add tbl_benefeciarrequest', 16, 'add_tbl_benefeciarrequest'),
(62, 'Can change tbl_benefeciarrequest', 16, 'change_tbl_benefeciarrequest'),
(63, 'Can delete tbl_benefeciarrequest', 16, 'delete_tbl_benefeciarrequest'),
(64, 'Can view tbl_benefeciarrequest', 16, 'view_tbl_benefeciarrequest'),
(65, 'Can add tbl_beneficiarfoodallot', 17, 'add_tbl_beneficiarfoodallot'),
(66, 'Can change tbl_beneficiarfoodallot', 17, 'change_tbl_beneficiarfoodallot'),
(67, 'Can delete tbl_beneficiarfoodallot', 17, 'delete_tbl_beneficiarfoodallot'),
(68, 'Can view tbl_beneficiarfoodallot', 17, 'view_tbl_beneficiarfoodallot');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(16, 'app', 'tbl_benefeciarrequest'),
(10, 'app', 'tbl_beneficiar'),
(17, 'app', 'tbl_beneficiarfoodallot'),
(15, 'app', 'tbl_complaint'),
(7, 'app', 'tbl_donor'),
(12, 'app', 'tbl_fooddonation'),
(9, 'app', 'tbl_idgen'),
(11, 'app', 'tbl_login'),
(13, 'app', 'tbl_publicrequest'),
(14, 'app', 'tbl_review'),
(8, 'app', 'tbl_volunteers'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-10-01 07:49:41.305854'),
(2, 'auth', '0001_initial', '2022-10-01 07:49:41.686172'),
(3, 'admin', '0001_initial', '2022-10-01 07:49:41.778017'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-10-01 07:49:41.786007'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-10-01 07:49:41.797990'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-10-01 07:49:41.849953'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-10-01 07:49:41.893893'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-10-01 07:49:41.906001'),
(9, 'auth', '0004_alter_user_username_opts', '2022-10-01 07:49:41.913869'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-10-01 07:49:41.945792'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-10-01 07:49:41.949787'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-10-01 07:49:41.957777'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-10-01 07:49:41.973791'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-10-01 07:49:41.989737'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-10-01 07:49:42.005749'),
(16, 'auth', '0011_update_proxy_permissions', '2022-10-01 07:49:42.021723'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-10-01 07:49:42.033707'),
(18, 'sessions', '0001_initial', '2022-10-01 07:49:42.061638'),
(19, 'app', '0001_initial', '2022-10-01 07:50:45.207801'),
(20, 'app', '0002_tbl_fooddonation_name', '2022-10-01 09:06:38.768843'),
(21, 'app', '0003_tbl_benefeciarrequest_donor_id', '2022-10-07 10:02:54.676685');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('8b8q3tbko403yfeufdfabga1gzz6ls3f', '.eJyrVkrJTFGyUnLxdIk3MDBU0lFKA_GNdZSSQLQhkM4DK3CCK0gqykwxBIoEuQaGugaHIIkC1dcCAGYcFWY:1ogkPm:0sLbU32vlc35hZSsS2CCduWFQTMzQjzPqOEQfYffZik', '2022-10-21 10:17:10.071350'),
('zdt2u3ku2g3fjqtilqqapdmlgsv6dkk6', 'eyJzMSI6ImZvb2RleHRyYS5pbkBnbWFpbC5jb20ifQ:1oeY5D:wWiZ0BZgLdda2Aeyz_b8-fFb0NEw-YyGOuTOXNIBll8', '2022-10-15 08:42:51.834679');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_benefeciarrequest`
--

CREATE TABLE `tbl_benefeciarrequest` (
  `request_id` varchar(90) NOT NULL,
  `required_date` varchar(90) NOT NULL,
  `required_time` varchar(90) NOT NULL,
  `required_quatity` varchar(90) NOT NULL,
  `remark` varchar(90) NOT NULL,
  `status` varchar(90) NOT NULL,
  `beneficiar_id_id` varchar(90) NOT NULL,
  `donation_id_id` varchar(90) NOT NULL,
  `donor_id_id` varchar(90) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_benefeciarrequest`
--

INSERT INTO `tbl_benefeciarrequest` (`request_id`, `required_date`, `required_time`, `required_quatity`, `remark`, `status`, `beneficiar_id_id`, `donation_id_id`, `donor_id_id`) VALUES
('REQUEST_001', '2022-10-07', '15:45:54', '', '', 'accepted', 'BID_001', 'FDID_002', 'DID_001');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_beneficiarfoodallot`
--

CREATE TABLE `tbl_beneficiarfoodallot` (
  `allotment_id` varchar(90) NOT NULL,
  `request_quatity` varchar(90) NOT NULL,
  `allotment_quatity` varchar(90) NOT NULL,
  `remark` varchar(90) NOT NULL,
  `allotment_date` varchar(90) NOT NULL,
  `allotment_time` varchar(90) NOT NULL,
  `status` varchar(90) NOT NULL,
  `donation_id_id` varchar(90) NOT NULL,
  `request_id_id` varchar(90) NOT NULL,
  `volunteer_id_id` varchar(90) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_complaint`
--

CREATE TABLE `tbl_complaint` (
  `complaint_id` varchar(90) NOT NULL,
  `complaint` varchar(90) NOT NULL,
  `date` varchar(90) NOT NULL,
  `status` varchar(90) NOT NULL,
  `beneficiar_id_id` varchar(90) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_fooddonation`
--

CREATE TABLE `tbl_fooddonation` (
  `donation_id` varchar(90) NOT NULL,
  `foodcatagory` varchar(90) NOT NULL,
  `quantity` varchar(90) NOT NULL,
  `photo` varchar(90) NOT NULL,
  `preparation_time` varchar(90) NOT NULL,
  `date` varchar(90) NOT NULL,
  `required_time` varchar(90) NOT NULL,
  `remark` varchar(90) NOT NULL,
  `status` varchar(90) NOT NULL,
  `donor_id_id` varchar(90) NOT NULL,
  `name` varchar(90) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_fooddonation`
--

INSERT INTO `tbl_fooddonation` (`donation_id`, `foodcatagory`, `quantity`, `photo`, `preparation_time`, `date`, `required_time`, `remark`, `status`, `donor_id_id`, `name`) VALUES
('FDID_001', 'nonveg', '25', '/media/Annotation%202021-07-31%20214114_pTPkxD0.png', '14:34', '2022-10-01', '19:34', 'asd', 'verified', 'DID_001', 'ff'),
('FDID_002', 'veg', '5', '/media/7b64bbf5_HO96KbZ.jpg', '14:19', '2022-10-07', '02:19', 'new one', 'pending', 'DID_001', 'sreeshma house1');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_publicrequest`
--

CREATE TABLE `tbl_publicrequest` (
  `request_id` varchar(90) NOT NULL,
  `location` varchar(90) NOT NULL,
  `phone` varchar(90) NOT NULL,
  `contact_person` varchar(90) NOT NULL,
  `email` varchar(90) NOT NULL,
  `request_food` varchar(90) NOT NULL,
  `remark` varchar(90) NOT NULL,
  `status` varchar(90) NOT NULL,
  `quantity` varchar(30) NOT NULL,
  `donation_id_id` varchar(90) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_review`
--

CREATE TABLE `tbl_review` (
  `review_id` varchar(90) NOT NULL,
  `name` varchar(90) NOT NULL,
  `review` varchar(90) NOT NULL,
  `date` varchar(90) NOT NULL,
  `address` varchar(90) NOT NULL,
  `beneficiar_id_id` varchar(90) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `app_tbl_beneficiar`
--
ALTER TABLE `app_tbl_beneficiar`
  ADD PRIMARY KEY (`beneficiar_id`);

--
-- Indexes for table `app_tbl_donor`
--
ALTER TABLE `app_tbl_donor`
  ADD PRIMARY KEY (`donor_id`);

--
-- Indexes for table `app_tbl_idgen`
--
ALTER TABLE `app_tbl_idgen`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `app_tbl_login`
--
ALTER TABLE `app_tbl_login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `app_tbl_volunteers`
--
ALTER TABLE `app_tbl_volunteers`
  ADD PRIMARY KEY (`volunteer_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `tbl_benefeciarrequest`
--
ALTER TABLE `tbl_benefeciarrequest`
  ADD PRIMARY KEY (`request_id`),
  ADD KEY `tbl_benefeciarreques_beneficiar_id_id_564f6b02_fk_app_tbl_b` (`beneficiar_id_id`),
  ADD KEY `tbl_benefeciarreques_donation_id_id_701c94b1_fk_tbl_foodd` (`donation_id_id`),
  ADD KEY `tbl_benefeciarreques_donor_id_id_ce47da89_fk_app_tbl_d` (`donor_id_id`);

--
-- Indexes for table `tbl_beneficiarfoodallot`
--
ALTER TABLE `tbl_beneficiarfoodallot`
  ADD PRIMARY KEY (`allotment_id`),
  ADD KEY `tbl_beneficiarfoodal_donation_id_id_91ec4db3_fk_tbl_foodd` (`donation_id_id`),
  ADD KEY `tbl_beneficiarfoodal_request_id_id_c5aa7e4c_fk_tbl_benef` (`request_id_id`),
  ADD KEY `tbl_beneficiarfoodal_volunteer_id_id_b2a51084_fk_app_tbl_v` (`volunteer_id_id`);

--
-- Indexes for table `tbl_complaint`
--
ALTER TABLE `tbl_complaint`
  ADD PRIMARY KEY (`complaint_id`),
  ADD KEY `tbl_complaint_beneficiar_id_id_3e773434_fk_app_tbl_b` (`beneficiar_id_id`);

--
-- Indexes for table `tbl_fooddonation`
--
ALTER TABLE `tbl_fooddonation`
  ADD PRIMARY KEY (`donation_id`),
  ADD KEY `tbl_fooddonation_donor_id_id_b7a75643_fk_app_tbl_donor_donor_id` (`donor_id_id`);

--
-- Indexes for table `tbl_publicrequest`
--
ALTER TABLE `tbl_publicrequest`
  ADD PRIMARY KEY (`request_id`),
  ADD KEY `tbl_publicrequest_donation_id_id_6f7e06eb_fk_tbl_foodd` (`donation_id_id`);

--
-- Indexes for table `tbl_review`
--
ALTER TABLE `tbl_review`
  ADD PRIMARY KEY (`review_id`),
  ADD KEY `tbl_review_beneficiar_id_id_2eb2c0ee_fk_app_tbl_b` (`beneficiar_id_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `app_tbl_idgen`
--
ALTER TABLE `app_tbl_idgen`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `app_tbl_login`
--
ALTER TABLE `app_tbl_login`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `tbl_benefeciarrequest`
--
ALTER TABLE `tbl_benefeciarrequest`
  ADD CONSTRAINT `tbl_benefeciarreques_beneficiar_id_id_564f6b02_fk_app_tbl_b` FOREIGN KEY (`beneficiar_id_id`) REFERENCES `app_tbl_beneficiar` (`beneficiar_id`),
  ADD CONSTRAINT `tbl_benefeciarreques_donation_id_id_701c94b1_fk_tbl_foodd` FOREIGN KEY (`donation_id_id`) REFERENCES `tbl_fooddonation` (`donation_id`),
  ADD CONSTRAINT `tbl_benefeciarreques_donor_id_id_ce47da89_fk_app_tbl_d` FOREIGN KEY (`donor_id_id`) REFERENCES `app_tbl_donor` (`donor_id`);

--
-- Constraints for table `tbl_beneficiarfoodallot`
--
ALTER TABLE `tbl_beneficiarfoodallot`
  ADD CONSTRAINT `tbl_beneficiarfoodal_donation_id_id_91ec4db3_fk_tbl_foodd` FOREIGN KEY (`donation_id_id`) REFERENCES `tbl_fooddonation` (`donation_id`),
  ADD CONSTRAINT `tbl_beneficiarfoodal_request_id_id_c5aa7e4c_fk_tbl_benef` FOREIGN KEY (`request_id_id`) REFERENCES `tbl_benefeciarrequest` (`request_id`),
  ADD CONSTRAINT `tbl_beneficiarfoodal_volunteer_id_id_b2a51084_fk_app_tbl_v` FOREIGN KEY (`volunteer_id_id`) REFERENCES `app_tbl_volunteers` (`volunteer_id`);

--
-- Constraints for table `tbl_complaint`
--
ALTER TABLE `tbl_complaint`
  ADD CONSTRAINT `tbl_complaint_beneficiar_id_id_3e773434_fk_app_tbl_b` FOREIGN KEY (`beneficiar_id_id`) REFERENCES `app_tbl_beneficiar` (`beneficiar_id`);

--
-- Constraints for table `tbl_fooddonation`
--
ALTER TABLE `tbl_fooddonation`
  ADD CONSTRAINT `tbl_fooddonation_donor_id_id_b7a75643_fk_app_tbl_donor_donor_id` FOREIGN KEY (`donor_id_id`) REFERENCES `app_tbl_donor` (`donor_id`);

--
-- Constraints for table `tbl_publicrequest`
--
ALTER TABLE `tbl_publicrequest`
  ADD CONSTRAINT `tbl_publicrequest_donation_id_id_6f7e06eb_fk_tbl_foodd` FOREIGN KEY (`donation_id_id`) REFERENCES `tbl_fooddonation` (`donation_id`);

--
-- Constraints for table `tbl_review`
--
ALTER TABLE `tbl_review`
  ADD CONSTRAINT `tbl_review_beneficiar_id_id_2eb2c0ee_fk_app_tbl_b` FOREIGN KEY (`beneficiar_id_id`) REFERENCES `app_tbl_beneficiar` (`beneficiar_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
