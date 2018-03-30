# MySQL-Front 5.1  (Build 4.13)

/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE */;
/*!40101 SET SQL_MODE='' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES */;
/*!40103 SET SQL_NOTES='ON' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;


# Host: 127.0.0.1    Database: jcgame
# ------------------------------------------------------
# Server version 5.0.45-community-nt

DROP DATABASE IF EXISTS `jcgame`;
CREATE DATABASE `jcgame` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `jcgame`;

#
# Source for table django_migrations
#

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL auto_increment,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Dumping data for table django_migrations
#

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table news
#

DROP TABLE IF EXISTS `news`;
CREATE TABLE `news` (
  `Id` int(11) NOT NULL auto_increment,
  `tittle` varchar(255) default NULL,
  `contact` text,
  `picture` varchar(255) default NULL,
  `time` datetime default NULL,
  PRIMARY KEY  (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

#
# Dumping data for table news
#

LOCK TABLES `news` WRITE;
/*!40000 ALTER TABLE `news` DISABLE KEYS */;
INSERT INTO `news` VALUES (1,'铭记过去，展望未来','<p>我年青时以为金钱至上，而今年事已高，发现果真如此。</p>\n\n<p>人們總是會選擇性的遺忘一些災難，當災難再次降臨時，才會想起似曾相識 </p>\n\n<p>不要忘記傷痛<p>\n\n<p>因為它們會我們成為更好的自己<p>','/static/assets/pic/blog_main.gif','2018-03-30');
/*!40000 ALTER TABLE `news` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table rightbox
#

DROP TABLE IF EXISTS `rightbox`;
CREATE TABLE `rightbox` (
  `Id` int(11) NOT NULL auto_increment,
  `liked_news` varchar(255) default NULL,
  `news_name` varchar(255) default NULL,
  PRIMARY KEY  (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

#
# Dumping data for table rightbox
#

LOCK TABLES `rightbox` WRITE;
/*!40000 ALTER TABLE `rightbox` DISABLE KEYS */;
INSERT INTO `rightbox` VALUES (1,'http://www.wolaifan.cn/wiki/fiddler_doc','我來翻-文檔翻譯平台');
/*!40000 ALTER TABLE `rightbox` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table users_car
#

DROP TABLE IF EXISTS `users_car`;
CREATE TABLE `users_car` (
  `Id` int(11) NOT NULL auto_increment,
  `ip` varchar(255) default NULL,
  `isvisit` int(11) default NULL COMMENT '1访问过 0没访问过',
  `car_counts` int(11) default NULL,
  `multiple` int(5) default NULL,
  `visittime` varchar(50) default NULL,
  PRIMARY KEY  (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

#
# Dumping data for table users_car
#

LOCK TABLES `users_car` WRITE;
/*!40000 ALTER TABLE `users_car` DISABLE KEYS */;
INSERT INTO `users_car` VALUES (1,'127.1.0.1',0,NULL,NULL,NULL);
INSERT INTO `users_car` VALUES (2,'127.0.0.1',1,130,5,'1522425960');
INSERT INTO `users_car` VALUES (3,'192.168.1.101',1,426,6,'1521828763');
/*!40000 ALTER TABLE `users_car` ENABLE KEYS */;
UNLOCK TABLES;

/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
