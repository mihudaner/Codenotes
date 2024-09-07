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

## 表来存储数据

每一列的字段：字段名，数据类型，约束



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



# 笔试



## 声明参数类型声明

![image-20240529165104526](E:\codenotes\JOB\四大件\MYSQL\img\image-20240529165104526.png)

##  增量备份

![image-20240529165144381](E:\codenotes\JOB\四大件\MYSQL\img\image-20240529165144381.png)

## select

![image-20240527231358019](E:\codenotes\JOB\四大件\MYSQL\img\image-20240527231358019.png)

```
LEFT(str,length); 
str是要提取子字符串的字符串。length是一个正整数，指定将从左边返回的字符数。
```

![image-20240527231539041](E:\codenotes\JOB\四大件\MYSQL\img\image-20240527231539041.png)



## 乐观锁和悲观锁的区别

> 美团2024年春招第一场笔试【技术】

### 乐观锁和悲观锁

>
> ​     乐观锁：认为别人不会同时修改数据，因此乐观锁默认是不会上锁的，只有在执行更新的时候才会去判断在此期间别人是否修改了数据，如果别人修改了数据则放弃操作，否则执行操作。
>
> ​     悲观锁：认为别人一定会同时修改数据，因此悲观锁在操作数据时是直接把数据上锁，直到操作完成之后才会释放锁，在上锁期间其他人不能操作数据。
>
> 
>
> ==读取频繁使用乐观锁，写入频繁使用悲观锁==

> 
>
> ### 悲观锁（Pessimistic Locking）
>
> #### 特点
>
> - **锁定策略**：悲观锁假定数据在并发环境下会发生冲突，因此在读写数据之前，都会锁定数据。
> - **锁定范围**：通常包括行锁、表锁，甚至数据库级别的锁。
> - **加锁时间**：在读取数据时就加锁，直到事务结束才释放锁。
>
> #### 优点
>
> - **数据一致性高**：通过加锁保证了在并发操作下的数据一致性和完整性。
> - **适用于高冲突场景**：在高冲突的场景下，能够有效防止数据的并发修改问题。
>
> #### 缺点
>
> - **性能开销大**：由于频繁加锁、解锁，系统的性能开销较大，容易导致死锁问题。
> - **并发性低**：由于锁的存在，会导致较低的并发性能，其他事务需要等待锁释放。
>
> #### 适用场景
>
> - **高冲突场景**：数据冲突较多的场景，如银行转账系统。
> - **关键数据更新**：数据一致性要求极高的场景。
>
> #### 示例
>
> 在关系型数据库中，使用悲观锁可以通过SQL语句实现：
>
> ```
> sql复制代码-- 悲观锁示例，使用SELECT ... FOR UPDATE语句
> BEGIN;
> SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
> -- 对数据进行更新操作
> UPDATE accounts SET balance = balance - 100 WHERE id = 1;
> COMMIT;
> ```
>
> ### 乐观锁（Optimistic Locking）
>
> #### 特点
>
> - **锁定策略**：乐观锁假定数据在并发环境下不会发生冲突，因此在读写数据之前不会加锁，只在提交数据时进行冲突检测。
> - **冲突检测**：通常通过版本号或时间戳来检测数据是否发生变化。
> - **加锁时间**：仅在提交数据时检测并发冲突，如果检测到冲突则回滚事务。
>
> #### 优点
>
> - **性能开销低**：因为不需要频繁加锁和解锁，系统的性能开销较低。
> - **并发性高**：允许更多的事务并发执行，提高系统的并发性能。
>
> #### 缺点
>
> - **数据一致性较低**：在高冲突场景下，可能会频繁回滚事务，导致性能下降。
> - **重试机制复杂**：事务冲突时需要进行重试，增加了实现的复杂度。
>
> #### 适用场景
>
> - **低冲突场景**：数据冲突较少的场景，如用户个人信息更新。
> - **读多写少**：读操作多于写操作的场景。
>
> #### 示例
>
> 在关系型数据库中，使用乐观锁可以通过版本号实现：
>
> ```
> sql复制代码-- 乐观锁示例，使用版本号机制
> -- 假设accounts表中有一个version列
> BEGIN;
> -- 读取数据及其版本号
> SELECT id, balance, version FROM accounts WHERE id = 1;
> -- 更新操作时，检查版本号是否一致
> UPDATE accounts SET balance = balance - 100, version = version + 1 
> WHERE id = 1 AND version = <old_version>;
> COMMIT;
> ```
>
> 



# 事务

![image-20240906120631681](E:\codenotes\JOB\四大件\MYSQL\img\image-20240906120631681.png)

## 事务的特征

> #### 1. 原子性（Atomicity）
>
> 事务必须是一个不可分割的工作单位，其中的所有操作要么全部完成，要么全部不完成。如果事务在进行中遇到错误或其他情况需要中止，那么已经执行的所有操作必须撤销，即回滚。
>
> #### 2. 一致性（Consistency）
>
> 事务必须使数据库从一个一致性状态转变到另一个一致性状态。回滚确保在事务失败时，数据库不会处于不一致的状态。
>
> #### 3. 隔离性（Isolation）
>
> 事务的执行是隔离的，一个事务的操作对其他事务是不可见的，直到事务提交为止。如果在提交前检测到并发冲突，回滚确保不会将未完成的、不一致的数据暴露给其他事务。
>
> #### 4. 持久性（Durability）
>
> 一旦事务提交，修改就会永久保存到数据库中，不会因为系统崩溃或其他原因丢失。回滚操作在事务提交前进行，不影响已经提交的持久化数据。

## 事务回滚

在数据库管理系统中，事务（Transaction）是指一组逻辑操作单元，这些操作要么全部成功，要么全部失败。

> ### 事务回滚的工作机制
>
> 1. **事务开始**：事务开始时，数据库系统记录当前状态，通常使用日志来记录事务的各项操作。
>2. **操作执行**：事务执行过程中，所有操作的修改不会立即写入持久存储，而是暂时保存在缓存中。
> 3. **冲突检测**：在事务提交前，系统会检测是否存在并发冲突（如版本号不一致）。
>4. **回滚操作**：如果检测到冲突或遇到其他错误，系统将利用日志中记录的原始状态信息，撤销事务中已执行的操作，将数据恢复到事务开始前的状态。
> 5. **事务结束**：如果事务没有遇到冲突且成功执行所有操作，则进行提交操作，将所有修改永久写入数据库。
>
> ### 事务回滚的示例
>
> 假设有两个用户同时尝试更新同一个银行账户的余额：
>
> ```
>sql复制代码-- 事务1
> BEGIN;
>SELECT balance FROM accounts WHERE id = 1;
> -- balance = 100
>UPDATE accounts SET balance = balance - 50 WHERE id = 1;
> -- 修改还未提交
>
> -- 事务2
>BEGIN;
> SELECT balance FROM accounts WHERE id = 1;
> -- balance = 100
> UPDATE accounts SET balance = balance - 30 WHERE id = 1;
> -- 修改还未提交
> 
>-- 事务1提交
> COMMIT;
>-- 提交成功，账户余额更新为50
> 
>-- 事务2提交
> -- 检测到并发冲突，因为事务2读取的balance是旧值100而非最新值50
> -- 事务2回滚，撤销更新操作，账户余额恢复到提交前的状态50
> ROLLBACK;
> ```
> 
> ==重点在 COMMIT  ROLLBACK==
> 
> 



### COMMIT ROLLBACK

```
set autocommit=0; set autocommit=OFF;
```

**MySQL**：在默认的自动提交模式下，`UPDATE`后会立即提交。如果事务已开始（通过`START TRANSACTION`），你需要显式地调用`COMMIT`来保存更改。



###  FOR UPDATE;加不加的区别

> 在SQL中，`FOR UPDATE` 子句用于在执行查询时锁定所选记录，==防止其他事务修改==这些记录。这种锁定机制对于实现==悲观锁==非常重要。
>
> 
>
> #### 不加 `FOR UPDATE`
>
> ```
> sql
> 复制代码
> SELECT * FROM accounts WHERE id = 1;
> ```
>
> - **读操作**：直接读取数据，不会对数据进行任何锁定。
> - **并发性**：多个事务可以同时读取相同的数据，不会相互阻塞。
> - **数据一致性**：不能保证在读取数据到更新数据之间，数据不会被其他事务修改。可能会导致“不可重复读”或“幻读”等并发问题。
>
> #### 加 `FOR UPDATE`
>
> ```
> sql
> 复制代码
> SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
> ```
>
> - **读操作**：读取数据并加锁（通常是行锁）。
> - **并发性**：其他事务在试图读取相同的数据时，如果也使用`FOR UPDATE`，将被阻塞，直到当前事务释放锁。
> - **数据一致性**：保证在读取到更新数据之间，数据不会被其他事务修改，避免了“不可重复读”和“幻读”问题。
>
> ### 具体应用场景与示例
>
> #### 不加 `FOR UPDATE` 的场景
>
> 1. **只读操作**：当你只需要读取数据，不进行任何修改时，不需要加锁。例如，生成报表或统计数据。
> 2. **低并发要求**：在不需要严格控制并发的应用中，可以避免加锁带来的性能开销。
>
> ```
> sql复制代码-- 只读查询
> SELECT balance FROM accounts WHERE id = 1;
> -- 可以多个事务并发执行，无锁定开销
> ```
>
> #### 加 `FOR UPDATE` 的场景
>
> 1. **事务完整性**：需要在读取后进行更新操作，并确保数据在读取到更新之间不被其他事务修改时。
> 2. **高并发控制**：在多用户高并发的环境中，需要严格控制数据一致性。
>
> ```
> sql复制代码-- 事务开始
> BEGIN;
> 
> -- 读取数据并加锁
> SELECT balance FROM accounts WHERE id = 1 FOR UPDATE;
> 
> -- 执行更新操作
> UPDATE accounts SET balance = balance - 50 WHERE id = 1;
> 
> -- 提交事务
> COMMIT;
> ```
>
> ### 例子解释
>
> 假设有两个事务，事务A和事务B，都尝试读取和更新同一账户的余额。
>
> #### 不加 `FOR UPDATE` 的情况
>
> ```
> sql复制代码-- 事务A
> BEGIN;
> SELECT balance FROM accounts WHERE id = 1;
> -- 读取到的balance为100
> -- 假设此时事务B也开始执行
> 
> -- 事务B
> BEGIN;
> SELECT balance FROM accounts WHERE id = 1;
> -- 读取到的balance也是100
> UPDATE accounts SET balance = balance - 30 WHERE id = 1;
> COMMIT;
> 
> -- 事务A继续
> UPDATE accounts SET balance = balance - 50 WHERE id = 1;
> COMMIT;
> -- 最终余额为50，但事务A和事务B都基于初始余额100进行了更新，导致数据不一致。
> ```
>
> #### 加 `FOR UPDATE` 的情况
>
> ```
> sql复制代码-- 事务A
> BEGIN;
> SELECT balance FROM accounts WHERE id = 1 FOR UPDATE;
> -- 读取到的balance为100，锁定记录
> 
> -- 事务B
> BEGIN;
> SELECT balance FROM accounts WHERE id = 1 FOR UPDATE;
> -- 此时事务A已经锁定记录，事务B将被阻塞，直到事务A完成
> 
> -- 事务A继续
> UPDATE accounts SET balance = balance - 50 WHERE id = 1;
> COMMIT;
> -- 事务A提交，释放锁
> 
> -- 事务B继续
> SELECT balance FROM accounts WHERE id = 1 FOR UPDATE;
> -- 读取到的balance为50
> UPDATE accounts SET balance = balance - 30 WHERE id = 1;
> COMMIT;
> -- 最终余额为20，数据一致。
> ```
>
> ### 总结
>
> - **不加 `FOR UPDATE`**：适用于只读操作或低并发要求的场景，不会加锁，允许多个事务并发读取数据，但不能保证数据一致性。
> - **加 `FOR UPDATE`**：适用于需要确保数据一致性的场景，通过加锁防止数据在读取到更新之间被其他事务修改，适用于高并发环境，确保事务的完整性和数据的一致性。
>
> 根据具体应用场景的需求选择是否使用`FOR UPDATE`，以平衡性能和数据一致性。



# 介绍

![查询语句执行流程](https://cdn.xiaolincoding.com/gh/xiaolincoder/mysql/sql%E6%89%A7%E8%A1%8C%E8%BF%87%E7%A8%8B/mysql%E6%9F%A5%E8%AF%A2%E6%B5%81%E7%A8%8B.png)

**Server 层负责建立连接、分析和执行 SQL**

**存储引擎层负责数据的存储和提取**

## 流程



> ### 第一步连接器
>
> - 连接的过程需要先经过 TCP 三次握手，因为 MySQL 是基于 TCP 协议进行传输的，如果 MySQL 服务 并没有启动
>
> - 如果一个用户已经建立了连接，即使管理员中途修改了该用户的权限，也不会影响已经存在连接的 权限。
> - MySQL 服务支持的最大连接数由 max_connections 参数控制，比如我的 MySQL 服务默认是 151 个, 超过这个值，系统就会拒绝接下来的连接请求

> ### 第一步连接器
>
> - 连接的过程需要先经过 TCP 三次握手，因为 MySQL 是基于 TCP 协议进行传输的，如果 MySQL 服务 并没有启动
>
> - 如果一个用户已经建立了连接，即使管理员中途修改了该用户的权限，也不会影响已经存在连接的 权限。
> - MySQL 服务支持的最大连接数由 max_connections 参数控制，比如我的 MySQL 服务默认是 151 个, 超过这个值，系统就会拒绝接下来的连接请求

# B树和B+

## B树和B+树

> 在数据库系统中，记录的存储通常采用多种数据结构，以优化查询、插入、删除和更新操作的效率。以下是一些常见的数据结构及其在数据库中的应用：
>
> ### 1. 
>
> #### B树
>
> - **特点**：B树是一种自平衡的树数据结构，每个节点可以包含多个键和值，保证了数据的有序性和高效性。
> - **应用**：适用于存储索引数据，支持高效的查找、插入和删除操作。
> - **优势**：能够保持平衡，保证了操作的时间复杂度为 O(log⁡n)。
>
> 
>
> #### B+树
>
> - **特点**：B+树是B树的变种，所有实际数据存储在叶子节点中，内部节点只存储索引。
> - **应用**：广泛用于数据库索引结构，如MySQL的InnoDB存储引擎。
> - **优势**：叶子节点形成链表，有利于范围查询和顺序遍历。
>

## 其他数据结构

> ### 2. 哈希表
>
> #### 特点
>
> - **哈希表**通过将键值对映射到特定位置，实现快速的数据存取。
> - **应用**：适用于需要快速查找操作的场景，如数据库中的哈希索引。
> - **优势**：查找、插入和删除操作的平均时间复杂度为 O(1)O(1)O(1)。
>
> ### 3. 堆文件组织
>
> #### 特点
>
> - **堆文件**是一种简单的数据存储方式，记录无特定顺序地存储在文件中。
> - **应用**：适用于插入频繁但查询不频繁的场景。
> - **优势**：插入操作非常高效。
>
> ### 4. 聚簇索引和非聚簇索引
>
> #### 聚簇索引
>
> - **特点**：数据存储和索引相结合，数据按索引排序存储。
> - **应用**：适用于查询操作多且对数据排序有要求的场景，如主键索引。
> - **优势**：查询效率高，但插入、删除和更新操作可能较慢，因为需要维护数据的有序性。
>
> #### 非聚簇索引
>
> - **特点**：索引和数据分开存储，索引指向数据的位置。
> - **应用**：适用于多种查询条件的场景，如次要索引。
> - **优势**：灵活性高，但查询需要多次查找，效率较聚簇索引略低。
>
> ### 5. 树型结构（如Trie树）
>
> #### 特点
>
> - **Trie树**是一种特殊的树结构，通常用于存储字符串集合。
> - **应用**：适用于前缀匹配查询，如自动补全、词典树。
> - **优势**：高效的前缀查询和插入操作。
>
> ### 6. LSM 树（Log-Structured Merge-Tree）
>
> #### 特点
>
> - **LSM树**通过批量写入和顺序写入优化磁盘写入操作，特别适合于写入密集型工作负载。
> - **应用**：NoSQL数据库如Cassandra、LevelDB、HBase等。
> - **优势**：写入性能高，读取性能通过分层合并优化。
>
> ### 7. 图数据结构
>
> #### 特点
>
> - **图数据结构**用于存储节点和边的信息，适合表示和查询复杂关系的数据。
> - **应用**：图数据库如Neo4j、ArangoDB、JanusGraph等。
> - **优势**：高效处理关系查询，如社交网络、推荐系统。
>
> ### 总结
>
> 不同的数据库系统根据其特定的需求和应用场景，采用不同的数据结构来存储记录。常见的数据结构包括B树和B+树、哈希表、堆文件、聚簇和非聚簇索引、Trie树、LSM树以及图数据结构。选择适合的数据结构对于提升数据库的性能和效率至关重要。









# Leecode50

## 查询

### 如何输出所有被邀请人的姓名以及邀请人

> ```
> 输入
> Customer =
> | id | name | referee_id |
> | -- | ---- | ---------- |
> | 1  | Will | null       |
> | 2  | Jane | null       |
> | 3  | Alex | 2          |
> | 4  | Bill | null       |
> | 5  | Zack | 1          |
> | 6  | Mark | 2          |
> 输出
> | invited_person | inviter |
> | -------------- | ------- |
> | Zack           | Will    |
> | Mark           | Jane    |
> | Alex           | Jane    |
> ```

```sql
SELECT e1.name AS invited_person, e2.name AS inviter
FROM Customer  e1
JOIN Customer  e2 ON e1.referee_id = e2.id
WHERE e1.referee_id IS NOT NULL;
//join返回两个表都匹配的行，left join返回左侧有的行
```

### [文章浏览 I](https://leetcode.cn/problems/article-views-i/)

```
输入：
Views 表：
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+

输出：
+------+
| id   |
+------+
| 4    |
| 7    |
+------+
```

```sql

select DISTINCT author_id As id
from Views 
where author_id=viewer_id
ORDER BY author_id
```

## 连接

### [使用唯一标识码替换员工ID](https://leetcode.cn/problems/replace-employee-id-with-the-unique-identifier/)

**示例 1：**

```
输入：
Employees 表:
+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+
EmployeeUNI 表:
+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+
输出：
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+
解释：
Alice and Bob 没有唯一标识码, 因此我们使用 null 替代。
Meir 的唯一标识码是 2 。
Winston 的唯一标识码是 3 。
Jonathan 唯一标识码是 1 。
```

```sql
# Write your MySQL query statement below
select e1.name,e2.unique_id
from Employees e1
left JOIN EmployeeUNI e2 ON e1.id = e2.id 
```



## 聚合

> COUNT：计算指定列或表达式的行数，可以用于统计记录数量。
> 例如：SELECT COUNT(*) FROM table_name; 将返回表中的记录数。
>
> SUM：计算指定列或表达式的总和。
> 例如：SELECT SUM(salary) FROM employees; 将返回 employees 表中 salary 列的总和。
>
> AVG：计算指定列或表达式的平均值。
> 例如：SELECT AVG(age) FROM students; 将返回 students 表中 age 列的平均值。
>
> MAX：返回指定列或表达式的最大值。
> 例如：SELECT MAX(price) FROM products; 将返回 products 表中 price 列的最大值。
>
> MIN：返回指定列或表达式的最小值。
> 例如：SELECT MIN(quantity) FROM inventory; 将返回 inventory 表中 quantity 列的最小值

### [ 平均售价](https://leetcode.cn/problems/average-selling-price/)

```sql
SELECT
    product_id,
    IFNULL(Round(SUM(sales) / SUM(units), 2), 0) AS average_price
FROM (
    SELECT
        Prices.product_id AS product_id,
        Prices.price * UnitsSold.units AS sales,
        UnitsSold.units AS units
    FROM Prices 
    LEFT JOIN UnitsSold ON Prices.product_id = UnitsSold.product_id
    AND (UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date)
) T
GROUP BY product_id

```

SUM   .... GROUP BY  .....



### [每位教师所教授的科目种类的数量](https://leetcode.cn/problems/number-of-unique-subjects-taught-by-each-teacher/)

```
# Write your MySQL query statement below
select teacher_id,count(distinct subject_id) as cnt 
from Teacher  
group by teacher_id
```



## 子查询

> 查询的条件来自于同一张表—— 子查询
> MySQL的子查询是指在一个查询语句内部嵌套另一个完整的查询语句。子查询通常用作外部查询的条件、过滤器或计算字段的来源。它可以返回一个结果集，供外部查询使用。
> 子查询可以出现在SELECT、FROM、WHERE、HAVING和INSERT语句的各个部分。
>
> 还可以别名结合join使用：
> select * from 表名 as 别名1 join 表名 as 别名2 on 别名1.列名=别名2.列名；
>
> SELECT子查询：子查询可以作为SELECT语句的一部分，用于在查询结果中生成一个或多个列。例如：
>
> SELECT column1, column2, (SELECT COUNT(*) FROM table2) AS count FROM table1;
>

### [上级经理已离职的公司员工](https://leetcode.cn/problems/employees-whose-manager-left-the-company/)

```sql
# Write your MySQL query statement below


select employee_id  
from Employees 
where salary < 30000 and manager_id not in (SELECT employee_id FROM Employees)
ORDER BY
    employee_id
```



### [查询近30天活跃用户数](https://leetcode.cn/problems/user-activity-for-the-past-30-days-i/)

```sql
# Write your MySQL query statement below
select activity_date as day , count(distinct user_id) as active_users 
from Activity  where activity_date between date_sub('2019-07-27',interval 29 day) and '2019-07-27'
group by activity_date;
```



## 更新

> 下面是选自 "Websites" 表的数据：
>
> ```
> +----+--------------+---------------------------+-------+---------+
> | id | name         | url                       | alexa | country |
> +----+--------------+---------------------------+-------+---------+
> | 1  | Google       | https://www.google.cm/    | 1     | USA     |
> | 2  | 淘宝          | https://www.taobao.com/   | 13    | CN      |
> | 3  | 菜鸟教程      | http://www.runoob.com/    | 4689  | CN      |
> | 4  | 微博          | http://weibo.com/         | 20    | CN      |
> | 5  | Facebook     | https://www.facebook.com/ | 3     | USA     |
> +----+--------------+---------------------------+-------+---------+
> ```
>
> 
>
> 
>
> 假设我们要把 "菜鸟教程" 的 alexa 排名更新为 5000，country 改为 USA。
>
> 我们使用下面的 SQL 语句：
>
> 
>
> UPDATE Websites  SET alexa='5000', country='USA'  WHERE name='菜鸟教程';
>
> 执行以上 SQL，再读取 "Websites" 表，数据如下所示：
>
> ![img](https://www.runoob.com/wp-content/uploads/2013/09/update1.jpg)

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

