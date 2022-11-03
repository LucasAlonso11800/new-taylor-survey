CREATE DATABASE IF NOT EXISTS taylor_survey;

CREATE TABLE IF NOT EXISTS `questions_set` (
  `question_set_id` int unsigned NOT NULL AUTO_INCREMENT,
  `question_set_title` varchar(45) NOT NULL,
  `question_set_order` int NOT NULL,
  PRIMARY KEY (`question_set_id`),
  UNIQUE KEY `question_set_order_UNIQUE` (`question_set_order`),
  UNIQUE KEY `questions_set_title_UNIQUE` (`question_set_title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `questions` (
  `question_id` int unsigned NOT NULL AUTO_INCREMENT,
  `question_text` varchar(100) NOT NULL,
  `question_set_id` int unsigned NOT NULL,
  PRIMARY KEY (`question_id`),
  UNIQUE KEY `question_id_UNIQUE` (`question_id`),
  KEY `question_set_id_idx` (`question_set_id`),
  CONSTRAINT `question_set_id` FOREIGN KEY (`question_set_id`) REFERENCES `questions_set` (`question_set_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `options` (
  `option_id` int unsigned NOT NULL AUTO_INCREMENT,
  `option_text` varchar(100) NOT NULL,
  `question_id` int unsigned NOT NULL,
  PRIMARY KEY (`option_id`),
  UNIQUE KEY `option_text_idx` (`option_text`,`question_id`),
  KEY `question_id_idx` (`question_id`),
  CONSTRAINT `question_id` FOREIGN KEY (`question_id`) REFERENCES `questions` (`question_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `answers` (
  `answer_id` int unsigned NOT NULL AUTO_INCREMENT,
  `option_id` int unsigned NOT NULL,
  PRIMARY KEY (`answer_id`),
  UNIQUE KEY `answer_id_UNIQUE` (`answer_id`),
  KEY `option_id_idx` (`option_id`),
  CONSTRAINT `option_id` FOREIGN KEY (`option_id`) REFERENCES `options` (`option_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
