Drop DATABASE cerveweb;
CREATE DATABASE  IF NOT EXISTS `cerveweb` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `cerveweb`;
-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: cerveweb
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cabecera_detalle`
--

DROP TABLE IF EXISTS `cabecera_detalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cabecera_detalle` (
  `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
  `importe_total` double DEFAULT '0',
  `pedido` int(9) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_cabecera_detalle_1_idx` (`pedido`),
  CONSTRAINT `fk_cabecera_detalle_1` FOREIGN KEY (`pedido`) REFERENCES `pedido` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cabecera_detalle`
--

LOCK TABLES `cabecera_detalle` WRITE;
/*!40000 ALTER TABLE `cabecera_detalle` DISABLE KEYS */;
/*!40000 ALTER TABLE `cabecera_detalle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historial_stock`
--

DROP TABLE IF EXISTS `historial_stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `historial_stock` (
  `id` int(15) unsigned NOT NULL AUTO_INCREMENT,
  `fecha_hora_movimiento` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cantidad` double NOT NULL DEFAULT '0',
  `unidad` int(9) unsigned NOT NULL,
  `signo` int(1) NOT NULL DEFAULT '0',
  `linea_detalle` int(9) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historial_stock`
--

LOCK TABLES `historial_stock` WRITE;
/*!40000 ALTER TABLE `historial_stock` DISABLE KEYS */;
/*!40000 ALTER TABLE `historial_stock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingrediente`
--

DROP TABLE IF EXISTS `ingrediente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ingrediente` (
  `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(120) DEFAULT NULL,
  `cantidad` double NOT NULL,
  `unidad` int(9) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_ingrediente_uni_idx` (`unidad`),
  CONSTRAINT `fk_ingrediente_uni` FOREIGN KEY (`unidad`) REFERENCES `unidad` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingrediente`
--

LOCK TABLES `ingrediente` WRITE;
/*!40000 ALTER TABLE `ingrediente` DISABLE KEYS */;
/*!40000 ALTER TABLE `ingrediente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `linea_detalle`
--

DROP TABLE IF EXISTS `linea_detalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `linea_detalle` (
  `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
  `cabecera` int(9) unsigned NOT NULL,
  `producto` int(9) unsigned NOT NULL,
  `cantidad` double DEFAULT NULL,
  `subtotal` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_linea_detalle_cabecera_idx` (`cabecera`),
  KEY `fk_linea_detalle_producto_idx` (`producto`),
  CONSTRAINT `fk_linea_detalle_cabecera` FOREIGN KEY (`cabecera`) REFERENCES `cabecera_detalle` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_linea_detalle_producto` FOREIGN KEY (`producto`) REFERENCES `producto` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `linea_detalle`
--

LOCK TABLES `linea_detalle` WRITE;
/*!40000 ALTER TABLE `linea_detalle` DISABLE KEYS */;
/*!40000 ALTER TABLE `linea_detalle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedido`
--

DROP TABLE IF EXISTS `pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pedido` (
  `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
  `nro_pedido` int(15) unsigned NOT NULL,
  `estado` varchar(45) DEFAULT NULL,
  `fecha_hora_entrega` timestamp NULL DEFAULT NULL,
  `orden_fabricacion` int(9) DEFAULT NULL,
  `solicitante` int(9) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_pedido_usuario_idx` (`solicitante`),
  CONSTRAINT `fk_pedido_usuario` FOREIGN KEY (`solicitante`) REFERENCES `usuario` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedido`
--

LOCK TABLES `pedido` WRITE;
/*!40000 ALTER TABLE `pedido` DISABLE KEYS */;
/*!40000 ALTER TABLE `pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `producto` (
  `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(256) DEFAULT NULL,
  `importe_unitario` double NOT NULL,
  `unidad` int(9) unsigned NOT NULL,
  `ingrediente` int(9) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_producto_unidad_idx` (`unidad`),
  KEY `fk_producto_ingrediente_idx` (`ingrediente`),
  CONSTRAINT `fk_producto_ingrediente` FOREIGN KEY (`ingrediente`) REFERENCES `ingrediente` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_producto_unidad` FOREIGN KEY (`unidad`) REFERENCES `unidad` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_usuario`
--

DROP TABLE IF EXISTS `tipo_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_usuario` (
  `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_usuario`
--

LOCK TABLES `tipo_usuario` WRITE;
/*!40000 ALTER TABLE `tipo_usuario` DISABLE KEYS */;
INSERT INTO `tipo_usuario` VALUES (1,'Cliente');
/*!40000 ALTER TABLE `tipo_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unidad`
--

DROP TABLE IF EXISTS `unidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unidad` (
  `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
  `abreviacion` varchar(10) NOT NULL,
  `descripcion` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unidad`
--

LOCK TABLES `unidad` WRITE;
/*!40000 ALTER TABLE `unidad` DISABLE KEYS */;
/*!40000 ALTER TABLE `unidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuario` (
  `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `email` varchar(120) NOT NULL,
  `nombre` varchar(120) DEFAULT NULL,
  `apellido` varchar(120) DEFAULT NULL,
  `cuit` varchar(45) NOT NULL,
  `es_usuario` int(1) DEFAULT NULL,
  `dni` varchar(45) NOT NULL,
  `razon_social` varchar(120) DEFAULT NULL,
  `tipo_usuario` int(9) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `cuit_UNIQUE` (`cuit`),
  UNIQUE KEY `dni_UNIQUE` (`dni`),
  KEY `fk_usuario_tipo_idx` (`tipo_usuario`),
  CONSTRAINT `fk_usuario_tipo` FOREIGN KEY (`tipo_usuario`) REFERENCES `tipo_usuario` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-18 21:04:35
