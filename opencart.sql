-- Удаляем старые таблицы если есть
DROP TABLE IF EXISTS `oc_category`, `oc_product`, `oc_product_description`, `oc_category_description`, `oc_product_to_category`;

-- Создаём категорию Devices
CREATE TABLE `oc_category` (
  `category_id` int NOT NULL,
  `parent_id` int NOT NULL,
  `top` tinyint(1) NOT NULL,
  `column` int NOT NULL,
  `sort_order` int NOT NULL,
  `status` tinyint(1) NOT NULL
);

CREATE TABLE `oc_category_description` (
  `category_id` int NOT NULL,
  `language_id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `meta_title` varchar(255) NOT NULL
);

INSERT INTO `oc_category` (`category_id`, `parent_id`, `top`, `column`, `sort_order`, `status`)
VALUES (999, 0, 1, 1, 1, 1);

INSERT INTO `oc_category_description` (`category_id`, `language_id`, `name`, `meta_title`)
VALUES (999, 1, 'Devices', 'Devices Meta');

-- Продукты
CREATE TABLE `oc_product` (
  `product_id` int NOT NULL,
  `model` varchar(64) NOT NULL,
  `price` decimal(15,4) NOT NULL,
  `quantity` int NOT NULL,
  `status` tinyint(1) NOT NULL
);

CREATE TABLE `oc_product_description` (
  `product_id` int NOT NULL,
  `language_id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` text,
  `meta_title` varchar(255) NOT NULL
);

CREATE TABLE `oc_product_to_category` (
  `product_id` int NOT NULL,
  `category_id` int NOT NULL
);

-- Вставим 4 продукта: 2 мыши, 2 клавиатуры
INSERT INTO `oc_product` (`product_id`, `model`, `price`, `quantity`, `status`) VALUES
(101, 'mouse-a', 10.00, 100, 1),
(102, 'mouse-b', 15.00, 50, 1),
(103, 'keyboard-a', 20.00, 100, 1),
(104, 'keyboard-b', 25.00, 100, 1);

INSERT INTO `oc_product_description` (`product_id`, `language_id`, `name`, `description`, `meta_title`) VALUES
(101, 1, 'Mouse A', 'Optical Mouse A', 'Mouse A Meta'),
(102, 1, 'Mouse B', 'Optical Mouse B', 'Mouse B Meta'),
(103, 1, 'Keyboard A', 'Mechanical Keyboard A', 'Keyboard A Meta'),
(104, 1, 'Keyboard B', 'Mechanical Keyboard B', 'Keyboard B Meta');

INSERT INTO `oc_product_to_category` (`product_id`, `category_id`) VALUES
(101, 999),
(102, 999),
(103, 999),
(104, 999);