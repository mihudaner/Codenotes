- 

ubuntu root密码应该是666666

wangkai 没有密码

window root密码root



# 网址资源

[下载网址](https://downloads.mysql.com/archives/community/)
[步骤](https://www.cnblogs.com/itcui/p/15511683.html)
[b站](https://www.bilibili.com/video/BV1Kr4y1i7ru?p=21&spm_id_from=pageDriver&vd_source=eef102f4fb053709a57c96d0c876628a)
[鱼皮闯关](http://sqlmother.yupi.icu/#/learn)
```
E:\soft\mysql-8.0.31-winx64\bin>mysqld --initialize --console
2023-08-24T08:25:21.049083Z 0 [System] [MY-013169] [Server] E:\soft\mysql-8.0.31-winx64\bin\mysqld.exe (mysqld 8.0.31) initializing of server in progress as process 32308
2023-08-24T08:25:21.085823Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
2023-08-24T08:25:21.538274Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
2023-08-24T08:25:22.243997Z 6 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: 8:grt)412Ymm

E:\soft\mysql-8.0.31-winx64\bin>
```

alter user 'root'@'localhost' identified by 'root';



# 命令
|  命令   |     解释     |
|:-----:|:----------:|
|  系统   |    400M    | 
 net start mysql|
net stop mysql|
 mysql -uroot -proot|登陆 
 show databases;|查看数据库 
use test; |使用 
create database xxxxxx;|创建  
select database();|当前选择  
drop database xxxxxx;|删除  
show tables;|查看当前数据库的表 
desc xxxx|查看表结构



### 表来存储数据

每一列的字段：字段名，数据类型，约束

# 基础篇代码
```sql
show databases;

show tables;

use test;

desc table_test;


CREATE TABLE person (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  sex  VARCHAR(10) UNIQUE,
  age INT,
  idcard   VARCHAR(100) UNIQUE,
  birthday VARCHAR(100)
);

ALTER TABLE frame AUTO_INCREMENT = 3;



-- --------------------------------------------- 插入-- ---------------------------------------------
INSERT INTO table_test values(18);
INSERT INTO person(name, gender, age, idcard, entrydate) values("王岐山","男", 28,"2202457451398","2000-07-26");

-- --------------------------------------------- 选择-- ---------------------------------------------
select * from table_test;

-- --------------------------------------------- 切换数据库-- ---------------------------------------------
use wksql;

-- ---------------------------------------------插入-- ---------------------------------------------
INSERT INTO person values
(1,"张无忌", "男", 28, "2201123545732", "2000-7-26"),
(2,"阿斯顿", "女", 2, "2201123545732", "2007-1-26"),
(3,"士大夫", "男", 78, "870201123545732", "2006-7-26"),
(4,"胜多少", "女", 38, "122045754745732", "2002-7-26"),
(5,"张收到", "男", 21, "220457545732", "2000-2-20"),
(6,"张无忌", "男", 28, "34612412011235732", "2000-7-26"),
(7,"深度", "男", 23, "805481242141732", "2023-5-21");
INSERT INTO person VALUES
(8, "王小明", "男", 28, "3201123545732", "1995-08-12"),
(9, "李小红", "女", 22, "4201123545732", "1999-03-25"),
(10, "张志华", "男", 39, "5201123545732", "1982-11-07"),
(11, "刘梦雨", "女", 30, "6201123545732", "1991-06-18"),
(12, "陈文静", "女", 27, "7201123545732", "1994-09-20"),
(13, "杨磊", "男", 25, "8201123545732", "1996-12-03"),
(14, "黄晨", "女", 32, "9201123545732", "1989-05-16"),
(15, "林阳", "男", 35, "10201123545732", "1986-08-27"),
(16, "周雪", "女", 28, "11201123545732", "1993-01-11"),
(17, "郑光", "男", 46, "12201123545732", "1975-04-02"),
(18, "王明明", "女", 24, "13201123545732", "1997-10-14"),
(19, "李涛", "男", 31, "14201123545732", "1990-07-29"),
(20, "张霞", "女", 33, "15201123545732", "1988-06-09"),
(21, "赵超", "男", 29, "16201123545732", "1992-09-30"),
(22, "孙芳", "女", 27, "17201123545732", "1994-02-15"),
(23, "李雄", "男", 38, "18201123545732", "1983-11-26"),
(24, "刘晨", "女", 23, "19201123545732", "1998-07-04"),
(25, "王建国", "男", 42, "20201123545732", "1979-12-08"),
(26, "张玉兰", "女", 29, "21201123545732", "1992-03-21"),
(27, "杨浩", "男", 34, "22201123545732", "1987-06-27"),
(28, "陈莉莉", "女", 25, "23201123545732", "1996-09-10"),
(29, "刘洋", "男", 31, "24201123545732", "1990-05-22"),
(30, "黄婷婷", "女", 28, "25201123545732", "1993-08-30"),
(31, "周瑞", "男", 37, "26201123545732", "1984-04-14"),
(32, "郑兵", "男", 44, "27201123545732", "1977-09-16"),
(33, "王莹莹", "女", 26, "28201123545732", "1995-12-28"),
(34, "李昊", "男", 30, "29201123545732", "1991-03-11"),
(35, "赵琳", "女", 29, "30201123545732", "1992-02-09"),
(36, "孙洪", "男", 35, "31201123545732", "1986-07-03"),
(37, "刘雯雯", "女", 24, "32201123545732", "1997-11-17"),
(38, "陈飞", "男", 36, "33201123545732", "1985-08-05"),
(39, "黄欣欣", "女", 23, "34201123545732", "1998-09-01"),
(40, "王峰", "男", 28, "35201123545732", "1993-05-29"),
(41, "李瑞瑞", "女", 31, "36201123545732", "1990-04-20"),
(42, "张明", "男", 40, "37201123545732", "1981-01-18"),
(43, "赵晴晴", "女", 26, "38201123545732", "1995-07-12"),
(44, "孙亮", "男", 33, "39201123545732", "1988-06-21"),
(45, "刘军", "男", 39, "40201123545732", "1982-12-04"),
(46, "陈秀兰", "女", 29, "41201123545732", "1992-10-15"),
(47, "黄敏", "男", 36, "42201123545732", "1985-04-27"),
(48, "王杰", "男", 31, "43201123545732", "1990-05-30"),
(49, "李小敏", "女", 27, "44201123545732", "1994-09-11"),
(50, "张平", "男", 28, "45201123545732", "1993-08-23");

-- --------------------------------------------- 修改-- ---------------------------------------------
update person set age = 10 where age < 10;


-- --------------------------------------------- 删除-- ---------------------------------------------
-- ## 删除表中多余的重复记录，重复记录是根据单个字段（Id）来判断，只留有age最小的记录
DELETE from person where name = "深度";

-- 方法一： (删除id重复的，并且不等于最小age的)https://blog.csdn.net/m0_51397290/article/details/127785228
select * from person;

# 创建临时表
CREATE TEMPORARY TABLE temp_table AS
SELECT * from person;
CREATE TEMPORARY TABLE temp_table2 AS
SELECT * from person;

# id重复 且 不在最小年龄删除
(SELECT MIN(age),id FROM temp_table GROUP BY id HAVING COUNT(*) > 1);
(SELECT id FROM temp_table2 GROUP BY id HAVING COUNT(id) > 1);

DELETE from person WHERE (id) IN
    (SELECT id FROM temp_table GROUP BY id HAVING COUNT(id) > 1)
    AND age NOT IN (SELECT MIN(age) FROM temp_table2 GROUP BY id HAVING COUNT(*) > 1);

DROP TEMPORARY TABLE temp_table;
DROP TEMPORARY TABLE temp_table2;

-- 方法二： (删除id重复的，并且不等于最小age的)
delete
    p1
from
    Person p1,
    Person p2
where
    (p1.id = p2.id) and (p1.age > p2.age);

########### 要删除在数据库表中所有字段完全相同的重复数据，只保留一份，您可以使用以下步骤

-- 创建临时表
CREATE TEMPORARY TABLE temp_table AS
SELECT DISTINCT *
FROM person;

-- 删除原始表中的所有数据
DELETE FROM Person;

-- 将临时表中的数据插入回原始表中
INSERT INTO Person
SELECT * FROM temp_table;

-- 删除临时表
DROP TEMPORARY TABLE temp_table;

############################################################################

-- --------------------------------------------- 查询-- ---------------------------------------------
select DISTINCT name,age from person;
select DISTINCT age from person;
select DISTINCT id from person;
select age as "年龄" from person;
select * from person;

update person set age = 10 where idcard="34612412011235732";
update person set idcard="5713075098240" where id = 6;
-- --------------------------------------------- 条件列表-- ---------------------------------------------
--  between.. and..  ,  in(..)  ,like , is null , and or not
select *from person where name like "__";

select *from person where name like "%光";

-- ---------------------------------------------聚合函数 avg  max-- ---------------------------------------------
select count(*) from person;

select max(name) from person;

-- ---------------------------------------------分组查询-- ---------------------------------------------
select count(*),gender,age from person group by gender,age;

select count(*),age from person where age>10  group by age having count(*)>=3;

-- ---------------------------------------------排序-- ---------------------------------------------
select * from person order by age desc;
select * from person order by id ;
select * from person order by age,entrydate desc;

-- --------------------------------------------- 分页查询-- ---------------------------------------------
select * from person order by age limit 10,10;

select * from person where age between 20 and 40 order by age,entrydate limit 5;

-- --------------------------------------------- 添加用户和权限操作 root密码root-- ---------------------------------------------
use mysql;
--  %所有主机而不是localhost
create user "wangkai"@"%" identified by "666666";
select * from user;

show GRANTS for "wangkai"@"%";
GRANT USAGE ON wksql.person TO `wangkai`@`%`;
GRANT all ON wksql.person TO `wangkai`@`%`;
revoke all ON wksql.person from `wangkai`@`%`;


-- --------------------------------------------- 字符串函数-- ---------------------------------------------
select concat('hello', 'col');
select substr(entrydate,1, 4)from person;
-- --------------------------------------------- 数值函数-- ---------------------------------------------
select ROUND(RAND(),4);
select CURDATE();
select NOW();
select MONTH(NOW());
-- --------------------------------------------- 日期函数-- ---------------------------------------------
select date_add(entrydate,INTERVAL 5000 DAY )from person;
select DATEDIFF(NOW(),entrydate),entrydate from person;

-- --------------------------------------------- 流程函数-- ---------------------------------------------
select name,if(age>10,age,null)from person;
select name,ifnull(age,0)from person;

--  case 和 when之间不加公式就是判断true和false，否则判断值
select
       case when YEAR(entrydate)<1990 THEN "老员工" when YEAR(entrydate)<2000 then "员工" else "新员工" end
from person;

select
    case YEAR(entrydate) WHEN 2000 THEN "世纪员工" else null end
from person;


-- --------------------------------------------- 约束(column约束)-- ---------------------------------------------
INSERT INTO restrain VALUES (2, "王明",  110, 1);
select * from restrain;
desc restrain;

-- ---------------------------------------------外键约束（外键关联）-- ---------------------------------------------
--  一对一
INSERT INTO part values
(1,"销售部"),
(2,"产品部"),
(3,"技术部");
select * from part order by id;
select * from person;

ALTER TABLE person add CONSTRAINT fk_part_id foreign key (part_id) references part(id);
--  默认有子表关联的数据，父表是删不掉的，报错
ALTER TABLE person drop CONSTRAINT fk_part_id;
ALTER TABLE person add CONSTRAINT fk_part_id foreign key (part_id) references part(id) on update cascade on delete set null;
-- 级联删除父表部门，对应子表所有的数据都会被删除


# 多对多 中间表实现，一个学生可以有多个课程，一个课程也有多个学生

# 一对一 表拆分

-- ------------------------------------> 多表查询 <--------------------------------------------
-- 准备数据
create table dept(
    id   int auto_increment comment 'ID' primary key,
    name varchar(50) not null comment '部门名称'
)comment '部门表';

create table emp(
    id  int auto_increment comment 'ID' primary key,
    name varchar(50) not null comment '姓名',
    age  int comment '年龄',
    job varchar(20) comment '职位',
    salary int comment '薪资',
    entrydate date comment '入职时间',
    managerid int comment '直属领导ID',
    dept_id int comment '部门ID'
)comment '员工表';

-- 添加外键
alter table emp add constraint fk_emp_dept_id foreign key (dept_id) references dept(id);

INSERT INTO dept (id, name) VALUES (1, '研发部'), (2, '市场部'),(3, '财务部'), (4, '销售部'), (5, '总经办'), (6, '人事部');
INSERT INTO emp (id, name, age, job,salary, entrydate, managerid, dept_id) VALUES
            (1, '金庸', 66, '总裁',20000, '2000-01-01', null,5),

            (2, '张无忌', 20, '项目经理',12500, '2005-12-05', 1,1),
            (3, '杨逍', 33, '开发', 8400,'2000-11-03', 2,1),
            (4, '韦一笑', 48, '开发',11000, '2002-02-05', 2,1),
            (5, '常遇春', 43, '开发',10500, '2004-09-07', 3,1),
            (6, '小昭', 19, '程序员鼓励师',6600, '2004-10-12', 2,1),

            (7, '灭绝', 60, '财务总监',8500, '2002-09-12', 1,3),
            (8, '周芷若', 19, '会计',48000, '2006-06-02', 7,3),
            (9, '丁敏君', 23, '出纳',5250, '2009-05-13', 7,3),

            (10, '赵敏', 20, '市场部总监',12500, '2004-10-12', 1,2),
            (11, '鹿杖客', 56, '职员',3750, '2006-10-03', 10,2),
            (12, '鹤笔翁', 19, '职员',3750, '2007-05-09', 10,2),
            (13, '方东白', 19, '职员',5500, '2009-02-12', 10,2),

            (14, '张三丰', 88, '销售总监',14000, '2004-10-12', 1,4),
            (15, '俞莲舟', 38, '销售',4600, '2004-10-12', 14,4),
            (16, '宋远桥', 40, '销售',4600, '2004-10-12', 14,4),
            (17, '陈友谅', 42, null,2000, '2011-10-12', 1,null);

-- 外连接
select * from person, part where person.part_id=part.id;
select p.name, p2.name from person p inner join part p2 on p.part_id = p2.id;
-- 左外连接
select p2.name, p.name from person p right outer join part p2 on p.part_id = p2.id;

-- 自连接
-- 1. 查询员工 及其 所属领导的名字
-- 表结构: emp
select * from emp;
select a.name , b.name from emp a , emp b where a.managerid = b.id;

select a.name , b.name from emp a left outer join emp b on a.managerid = b.id;

-- ------------------------------------> union all , union-- ------------------------------------>
select * from emp where salary < 5000 or age >50;
select * from emp where salary < 5000 union select * from emp where age >50;


-- ------------------------------------> 子查询，嵌套-- ------------------------------------>
-- 标量子查询     如果子查询只有一个结果称为
-- 列子查询   in, not in, any, some, all   根据销售部部门ID, 查询员工信息
select * from emp where dept_id in (select id from dept where name in ('销售部','研发部'));

select * from emp where salary > all ( select salary from emp where dept_id = (select id from dept where name = '财务部') );
select * from emp where salary > any ( select salary from emp where dept_id = (select id from dept where name = '研发部') );

-- 行子查询
select * from emp where (salary,managerid) = (select  salary,managerid from emp where name='张无忌');

-- 表子查询
-- 1. 查询与 "鹿杖客" , "宋远桥" 的职位和薪资相同的员工信息
select * from emp where (job,salary) in ( select job, salary from emp where name = '鹿杖客' or name = '宋远桥' );


-- 2. 查询入职日期是 "2006-01-01" 之后的员工信息 , 及其部门信息
select e.*, d.* from (select * from emp where entrydate > '2006-01-01') e left join dept d on e.dept_id = d.id ;


-- ------------------------------------> 事务-- ------------------------------------>
-- 数据准备
create table account(
    id int auto_increment primary key comment '主键ID',
    name varchar(10) comment '姓名',
    money int comment '余额'
) comment '账户表';
insert into account(id, name, money) VALUES (null,'张三',2000),(null,'李四',2000);


-- 恢复数据
update account set money = 2000 where name = '张三' or name = '李四';


select @@autocommit;

-- 转账操作 (张三给李四转账1000)
start transaction ;

-- 1. 查询张三账户余额
select * from account ;

-- 2. 将张三账户余额-1000
update account set money = money - 1000 where name = '张三';

程序执行报错 ...

-- 3. 将李四账户余额+1000
update account set money = money + 1000 where name = '李四';


-- 提交事务(需要重新打开start transaction ;)
commit;

-- 回滚事务(需要重新打开start transaction ;)
rollback;

-- ------------------------------------> 事务特性ACID-- ------------------------------------>
-- 原子性
-- 一致性
-- 隔离性
-- 持久性

-- 数据隔离级别(幻读解决是通过加锁的)
select @@transaction_isolation;
set session transaction isolation level repeatable read ;
```

# python链接mysql

https://www.bilibili.com/video/BV1Fx411d7Eb?p=4&vd_source=eef102f4fb053709a57c96d0c876628a

https://github.com/wmh02240/MySQL-Notes/tree/master/MySQL%E5%9F%BA%E7%A1%80/2.%E6%95%B0%E6%8D%AE%E5%BA%93%E7%9A%84%E6%93%8D%E4%BD%9C

```
 sudo apt-get install mysql-server
 sudo apt-get install mysql-client
 sudo service mysql start
 
 (py37) wangkai@wangkai-Legion-Y9000P-IAH7H:~$ ps ajx|grep mysql

  1   12585   12584   12584 ?             -1 Sl     131   0:01 /usr/sbin/mysqld --daemonize --pid-file=/run/mysqld/mysqld.pid

```



## 修改root密码

[在 Ubuntu 上安装和配置 MySQL 保姆级教程](https://zhuanlan.zhihu.com/p/610793026)



## 创建用户

[Ubuntu 安装和使用MySQL](https://blog.csdn.net/hwx865/article/details/90287715)

```mysql
mysql> CREATE USER 'wangkai'@'%';
Query OK, 0 rows affected (0.01 sec)

mysql> GRANT ALL PRIVILEGES ON *.* TO 'wangkai'@'%' WITH GRANT OPTION;
Query OK, 0 rows affected (0.00 sec)

SELECT user,authentication_string,plugin,host FROM mysql.user;

mysql> CREATE DATABASE python;
Query OK, 1 row affected (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| python             |
| sys                |
+--------------------+
5 rows in set (0.00 sec)

```

## [nvigat安装](https://blog.csdn.net/qq_39125445/article/details/80367952?spm=1001.2101.3001.6650.4&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-4-80367952-blog-96662514.235%5Ev40%5Epc_relevant_anti_t3_base&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-4-80367952-blog-96662514.235%5Ev40%5Epc_relevant_anti_t3_base&utm_relevant_index=9)

[nvigat破解](https://blog.csdn.net/qq_39125445/article/details/80367952?spm=1001.2101.3001.6650.4&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-4-80367952-blog-96662514.235%5Ev40%5Epc_relevant_anti_t3_base&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-4-80367952-blog-96662514.235%5Ev40%5Epc_relevant_anti_t3_base&utm_relevant_index=9)

[乱码](https://www.cnblogs.com/tanrong/p/10173109.html)

## 插入中文

> 出现上面问题主要是编码的问题
>
> 首先查看数据库的编码情况，命令如下：
>
> show  variables  like '%char%';
> 查看如下两个字段，如果不是utf-8，把它们设置成utf-8，命令如下：
>
> set character_set_server=utf8
> set character_set_database=utf8
>
>
> 根据本人实践情况，如果执行上面步骤后插入中文还是报错，则继续操作：
>
> 使用命令查看相关表是否是utf-8编码
>
> show create table 表名
> 结果如下：
>
> 一般出现插入中文出错，大概率表中的charset不是utf-8，使用命令更改相关表即可：
>
> alter table sys_task convert to charset utf8;
> ————————————————
> 版权声明：本文为CSDN博主「夜雨星光~」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
> 原文链接：https://blog.csdn.net/weixin_46567616/article/details/131953166

## [常用语法](https://blog.csdn.net/liulanba/article/details/130139105)

```mysql
CREATE TABLE `python`.`Untitled`  (
  `id` int(11) NOT NULL,
  `rgb_path` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `point_path` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `timestemp` datetime(0) DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  `frame_rate` float(255, 0) DEFAULT NULL,
  `exposure` float(255, 0) DEFAULT NULL,
  `gain` float(255, 0) DEFAULT NULL,
  `rgb_h` int(255) DEFAULT NULL,
  `rgb_w` int(255) DEFAULT NULL,
  `points_num` int(255) DEFAULT NULL,
  `defect_num` int(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
);



  INSERT INTO frame 
  (data_path , timestemp, exposure, gain, rgb_h, rgb_w, points_num, defect_num,  n0x,n0y, n0z)
                VALUES('/path/to/your/rgb/image.jpg', '2024-01-18 17:42:54', 0.5, 1.0, 1080, 1920, 10000, 5, 1.0, 1080.0, 1920.0);
                
                INSERT INTO frame(data_path , timestemp, exposure, gain, rgb_h, rgb_w, points_num, defect_num, n0x,n0y, n0z)
                VALUES ('./data/', '2024-01-18 20:39:04', 0, 0, 800, 800, 2304000, 8, -6.5, 7.5, 28.68);
                
                 
```

