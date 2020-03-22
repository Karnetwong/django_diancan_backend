/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80015
Source Host           : localhost:3306
Source Database       : sell

Target Server Type    : MYSQL
Target Server Version : 80015
File Encoding         : 65001

Date: 2020-02-04 15:46:31
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '评论者姓名',
  `openid` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '评论者姓名',
  `content` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '评论内容',
  `avatar_url` text COLLATE utf8mb4_unicode_ci COMMENT '评论者的头像',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '评论时间',
  PRIMARY KEY (`comment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='评论信息表';

-- ----------------------------
-- Records of comment
-- ----------------------------
INSERT INTO `comment` VALUES ('1', '.', 'ob3yX5HMjRbZ1LFDPFlVjOjR5H8k', '好吃', 'https://wx.qlogo.cn/mmopen/vi_32/HWmbzHIO9wGVVAGVrEgZricxGiaHQfhnoRNq7AxHI3nqOb8vfgG0BsT7hic3iaKd6Y8icDXwp03hL6HZR5qb89VS3Eg/132', '2020-01-19 16:32:36');
INSERT INTO `comment` VALUES ('2', 'wangzx', 'ob3yX5HMjRbZ1LFDPFlVjOjR5H8k', '好吃', 'https://wx.qlogo.cn/mmopen/vi_32/HWmbzHIO9wGVVAGVrEgZricxGiaHQfhnoRNq7AxHI3nqOb8vfgG0BsT7hic3iaKd6Y8icDXwp03hL6HZR5qb89VS3Eg/132', '2020-01-29 17:34:23');
INSERT INTO `comment` VALUES ('3', 'wangzx', 'ob3yX5HMjRbZ1LFDPFlVjOjR5H8k', '超好吃', 'https://wx.qlogo.cn/mmopen/vi_32/HWmbzHIO9wGVVAGVrEgZricxGiaHQfhnoRNq7AxHI3nqOb8vfgG0BsT7hic3iaKd6Y8icDXwp03hL6HZR5qb89VS3Eg/132', '2020-01-29 17:34:40');
INSERT INTO `comment` VALUES ('4', 'wangzx', 'ob3yX5HMjRbZ1LFDPFlVjOjR5H8k', '超级好吃', 'https://wx.qlogo.cn/mmopen/vi_32/HWmbzHIO9wGVVAGVrEgZricxGiaHQfhnoRNq7AxHI3nqOb8vfgG0BsT7hic3iaKd6Y8icDXwp03hL6HZR5qb89VS3Eg/132', '2020-01-29 17:34:57');

-- ----------------------------
-- Table structure for order_detail
-- ----------------------------
DROP TABLE IF EXISTS `order_detail`;
CREATE TABLE `order_detail` (
  `detail_id` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `order_id` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `product_id` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `product_name` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '商品名称',
  `product_price` decimal(8,2) NOT NULL COMMENT '当前价格,单位分',
  `product_quantity` int(11) NOT NULL COMMENT '数量',
  `product_icon` varchar(512) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '小图',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`detail_id`),
  KEY `idx_order_id` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='订单商品';

-- ----------------------------
-- Records of order_detail
-- ----------------------------
INSERT INTO `order_detail` VALUES ('1579421709624490060', '1579421709611529406', '1579417739335639116', '皮蛋瘦肉粥', '12.00', '2', 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1148526283,1948675981&fm=26&gp=0.jpg', '2020-01-19 16:15:09', '2020-01-19 16:15:09');
INSERT INTO `order_detail` VALUES ('1579422671175732227', '1579422671173893314', '1579417739335639116', '皮蛋瘦肉粥', '12.00', '1', 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1148526283,1948675981&fm=26&gp=0.jpg', '2020-01-19 16:31:11', '2020-01-19 16:31:11');
INSERT INTO `order_detail` VALUES ('1579424340536697425', '1579424340531485345', '1579417739335639116', '皮蛋瘦肉粥', '12.00', '1', 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1148526283,1948675981&fm=26&gp=0.jpg', '2020-01-19 16:59:00', '2020-01-19 16:59:00');
INSERT INTO `order_detail` VALUES ('1579429210972207428', '1579429210970873738', '1579417739335639116', '皮蛋瘦肉粥', '12.00', '1', 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1148526283,1948675981&fm=26&gp=0.jpg', '2020-01-19 18:20:10', '2020-01-19 18:20:10');
INSERT INTO `order_detail` VALUES ('1579429210974468599', '1579429210970873738', '1579417844455664459', '叉烧包', '3.00', '2', 'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=356732141,1696248304&fm=26&gp=0.jpg', '2020-01-19 18:20:11', '2020-01-19 18:20:11');
INSERT INTO `order_detail` VALUES ('1579598943074998217', '1579598943068159557', '1579417739335639116', '皮蛋瘦肉粥', '12.00', '1', 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1148526283,1948675981&fm=26&gp=0.jpg', '2020-01-21 17:29:03', '2020-01-21 17:29:03');
INSERT INTO `order_detail` VALUES ('1579603911872239669', '1579603911869248285', '1579417844455664459', '叉烧包', '3.00', '1', 'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=356732141,1696248304&fm=26&gp=0.jpg', '2020-01-21 18:51:51', '2020-01-21 18:51:51');
INSERT INTO `order_detail` VALUES ('1579603911884736267', '1579603911869248285', '1579417739335639116', '皮蛋瘦肉粥', '12.00', '1', 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1148526283,1948675981&fm=26&gp=0.jpg', '2020-01-21 18:51:51', '2020-01-21 18:51:51');
INSERT INTO `order_detail` VALUES ('1580290417212869653', '1580290417208905904', '1579417844455664459', '叉烧包', '3.00', '1', 'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=356732141,1696248304&fm=26&gp=0.jpg', '2020-01-29 17:33:37', '2020-01-29 17:33:37');
INSERT INTO `order_detail` VALUES ('1580292380695640555', '1580292380694172447', '1579417739335639116', '皮蛋瘦肉粥', '12.00', '2', 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1148526283,1948675981&fm=26&gp=0.jpg', '2020-01-29 18:06:20', '2020-01-29 18:06:20');
INSERT INTO `order_detail` VALUES ('1580528552400215687', '1580528552366254427', '1579417739335639116', '皮蛋瘦肉粥', '12.00', '2', 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1148526283,1948675981&fm=26&gp=0.jpg', '2020-02-01 11:42:32', '2020-02-01 11:42:32');
INSERT INTO `order_detail` VALUES ('1580528598889561206', '1580528598887799245', '1579417739335639116', '皮蛋瘦肉粥', '12.00', '1', 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1148526283,1948675981&fm=26&gp=0.jpg', '2020-02-01 11:43:18', '2020-02-01 11:43:18');

-- ----------------------------
-- Table structure for order_master
-- ----------------------------
DROP TABLE IF EXISTS `order_master`;
CREATE TABLE `order_master` (
  `order_id` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `buyer_name` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '买家名字',
  `buyer_phone` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '买家电话',
  `buyer_address` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '买家桌号',
  `buyer_openid` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '买家微信openid',
  `order_amount` decimal(8,2) NOT NULL COMMENT '订单总金额',
  `order_status` tinyint(3) NOT NULL DEFAULT '0' COMMENT '订单状态, 默认为新下单',
  `pay_status` tinyint(3) NOT NULL DEFAULT '0' COMMENT '支付状态, 默认未支付',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`order_id`),
  KEY `idx_buyer_openid` (`buyer_openid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='订单表';

-- ----------------------------
-- Records of order_master
-- ----------------------------
INSERT INTO `order_master` VALUES ('1579421709611529406', '.', '15805849785', '1号桌', 'null', '24.00', '3', '0', '2020-01-19 16:15:09', '2020-01-19 16:32:01');
INSERT INTO `order_master` VALUES ('1579422671173893314', '.', '15805849785', '1号桌', 'ob3yX5HMjRbZ1LFDPFlVjOjR5H8k', '12.00', '4', '0', '2020-01-19 16:31:11', '2020-01-19 16:32:36');
INSERT INTO `order_master` VALUES ('1579424340531485345', '.', '15805849785', '1号桌', 'ob3yX5HMjRbZ1LFDPFlVjOjR5H8k', '12.00', '4', '0', '2020-01-19 16:59:00', '2020-01-29 17:34:23');
INSERT INTO `order_master` VALUES ('1579429210970873738', '.', '15805849785', '1号桌', 'ob3yX5HMjRbZ1LFDPFlVjOjR5H8k', '18.00', '4', '0', '2020-01-19 18:20:11', '2020-01-29 17:34:41');
INSERT INTO `order_master` VALUES ('1579598943068159557', 'wangzx', '15805849785', '1号桌', 'ob3yX5HMjRbZ1LFDPFlVjOjR5H8k', '12.00', '4', '0', '2020-01-21 17:29:03', '2020-01-29 17:34:57');
INSERT INTO `order_master` VALUES ('1579603911869248285', 'wangzx', '15805849785', '1号桌', 'ob3yX5HMjRbZ1LFDPFlVjOjR5H8k', '15.00', '3', '0', '2020-01-21 18:51:51', '2020-01-28 18:09:02');
INSERT INTO `order_master` VALUES ('1580290417208905904', 'wangzx', '15918259517', '1号桌', 'ob3yX5HMjRbZ1LFDPFlVjOjR5H8k', '3.00', '3', '0', '2020-01-29 17:33:37', '2020-01-29 17:33:58');
INSERT INTO `order_master` VALUES ('1580292380694172447', 'wangzx', '15918259517', '1号桌', 'ob3yX5HMjRbZ1LFDPFlVjOjR5H8k', '24.00', '1', '0', '2020-01-29 18:06:20', '2020-01-29 18:06:20');
INSERT INTO `order_master` VALUES ('1580528552366254427', 'wangzx', '15918259517', '1号桌', 'ob3yX5HMjRbZ1LFDPFlVjOjR5H8k', '24.00', '1', '0', '2020-02-01 11:42:32', '2020-02-01 11:42:32');
INSERT INTO `order_master` VALUES ('1580528598887799245', 'wangzx', '15918259517', '1号桌', 'ob3yX5HMjRbZ1LFDPFlVjOjR5H8k', '12.00', '1', '0', '2020-02-01 11:43:18', '2020-02-01 11:43:18');

-- ----------------------------
-- Table structure for picture
-- ----------------------------
DROP TABLE IF EXISTS `picture`;
CREATE TABLE `picture` (
  `pic_id` int(11) NOT NULL AUTO_INCREMENT,
  `pic_url` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `pic_message` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`pic_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='轮播图表';

-- ----------------------------
-- Records of picture
-- ----------------------------
INSERT INTO `picture` VALUES ('1', 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1579433625016&di=e6c70596fea47e971bec41301a6f92e8&imgtype=0&src=http%3A%2F%2Fyouimg1.c-ctrip.com%2Ftarget%2F1004070000002q96w061C_R_1024_10000_Q90.jpg', '1', '2020-01-19 16:45:59', '2020-01-19 16:45:59');
INSERT INTO `picture` VALUES ('2', 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1580558658619&di=14d9d6d2a866f1f50f481f59baf3a013&imgtype=0&src=http%3A%2F%2Fimgsa.baidu.com%2Fforum%2Fpic%2Fitem%2F8ae6b01ea8d3fd1f416e1df23c4e251f94ca5f7b.jpg', '2', '2020-02-01 17:17:10', '2020-02-01 17:17:10');

-- ----------------------------
-- Table structure for product_category
-- ----------------------------
DROP TABLE IF EXISTS `product_category`;
CREATE TABLE `product_category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '类目名字',
  `category_type` int(11) NOT NULL COMMENT '类目编号',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='类目表';

-- ----------------------------
-- Records of product_category
-- ----------------------------
INSERT INTO `product_category` VALUES ('1', '粥品', '1', '2020-01-19 15:07:14', '2020-01-19 15:07:14');
INSERT INTO `product_category` VALUES ('2', '包子', '2', '2020-01-19 15:10:06', '2020-01-19 15:10:06');

-- ----------------------------
-- Table structure for product_info
-- ----------------------------
DROP TABLE IF EXISTS `product_info`;
CREATE TABLE `product_info` (
  `product_id` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `product_name` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '商品名称',
  `product_price` decimal(8,2) NOT NULL COMMENT '单价',
  `product_stock` int(11) NOT NULL COMMENT '库存',
  `product_description` varchar(64) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '描述',
  `product_icon` varchar(512) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '小图',
  `product_status` tinyint(3) DEFAULT '0' COMMENT '商品状态,0正常1下架',
  `category_type` int(11) NOT NULL COMMENT '类目编号',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='商品表';

-- ----------------------------
-- Records of product_info
-- ----------------------------
INSERT INTO `product_info` VALUES ('1579417739335639116', '皮蛋瘦肉粥', '12.00', '88', '好吃美味', 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1148526283,1948675981&fm=26&gp=0.jpg', '0', '1', '2020-01-19 15:08:59', '2020-02-01 11:43:18');
INSERT INTO `product_info` VALUES ('1579417844455664459', '叉烧包', '3.00', '996', '新鲜叉烧', 'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=356732141,1696248304&fm=26&gp=0.jpg', '0', '2', '2020-01-19 15:10:44', '2020-01-29 17:33:37');

-- ----------------------------
-- Table structure for seller_info
-- ----------------------------
DROP TABLE IF EXISTS `seller_info`;
CREATE TABLE `seller_info` (
  `seller_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '用户手机号',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`seller_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='卖家信息表';

-- ----------------------------
-- Records of seller_info
-- ----------------------------
INSERT INTO `seller_info` VALUES ('1', 'Karnetwong', '123456', '12345678', '2020-01-19 14:59:10', '2020-02-01 17:14:44');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `openid` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '微信openid',
  `zhuohao` varchar(64) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '桌号',
  `renshu` varchar(64) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '就餐人数',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='用户信息表';

-- ----------------------------
-- Records of user
-- ----------------------------
