---
tags:
- espnet
- audio
- automatic-speech-recognition
language: zh
datasets:
- wenetspeech
license: cc-by-4.0
---

## ESPnet2 ASR model 

### `espnet/pengcheng_guo_wenetspeech_asr_train_asr_raw_zh_char`

This model was trained by Pengcheng Guo using wenetspeech recipe in [espnet](https://github.com/espnet/espnet/).

### Demo: How to use in ESPnet2

```bash
cd espnet
git checkout 5c21f63e45e0961a5d817017c282b0cafd68a3aa
pip install -e .
cd egs2/wenetspeech/asr1
./run.sh --skip_data_prep false --skip_train true --download_model espnet/pengcheng_guo_wenetspeech_asr_train_asr_raw_zh_char
```

<!-- Generated by scripts/utils/show_asr_result.sh -->
# RESULTS
## Environments
- date: `Wed Oct  6 15:11:20 CST 2021`
- python version: `3.8.11 (default, Aug  3 2021, 15:09:35)  [GCC 7.5.0]`
- espnet version: `espnet 0.10.2a1`
- pytorch version: `pytorch 1.9.0`
- Git hash: ``
  - Commit date: ``

## asr_train_asr_conformer_raw_zh_char
### WER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_asr_rnn_asr_model_valid.acc.ave_10best/aishell_test|7176|7176|67.1|32.9|0.0|0.1|33.0|32.9|
|decode_asr_rnn_asr_model_valid.acc.ave_10best/dev|13825|16684|32.1|54.1|13.8|0.1|68.0|64.2|
|decode_asr_rnn_asr_model_valid.acc.ave_10best/test_meeting|8370|8599|13.4|84.6|2.0|0.1|86.7|86.8|
|decode_asr_rnn_asr_model_valid.acc.ave_10best/test_net|24774|25995|46.2|50.4|3.4|1.1|54.9|52.5|

### CER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_asr_rnn_asr_model_valid.acc.ave_10best/aishell_test|7176|104765|96.3|3.6|0.1|0.2|3.9|32.9|
|decode_asr_rnn_asr_model_valid.acc.ave_10bestdev|13825|333357|90.7|3.4|5.9|0.4|9.7|64.2|
|decode_asr_rnn_asr_model_valid.acc.ave_10best/test_meeting|8370|220614|84.6|5.0|10.4|0.5|15.9|86.8|
|decode_asr_rnn_asr_model_valid.acc.ave_10best/test_net|24774|416968|91.8|5.3|2.9|0.6|8.8|52.5|

### TER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|

## ASR config

<details><summary>expand</summary>

```
config: conf/train_asr_conformer.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/asr_train_asr_conformer_raw_zh_char
ngpu: 1
seed: 0
num_workers: 1
num_att_plot: 3
dist_backend: nccl
dist_init_method: env://
dist_world_size: 8
dist_rank: 0
local_rank: 0
dist_master_addr: localhost
dist_master_port: 44205
dist_launcher: null
multiprocessing_distributed: true
unused_parameters: false
sharded_ddp: false
cudnn_enabled: true
cudnn_benchmark: false
cudnn_deterministic: true
collect_stats: false
write_collected_feats: false
max_epoch: 30
patience: null
val_scheduler_criterion:
- valid
- acc
early_stopping_criterion:
- valid
- loss
- min
best_model_criterion:
-   - valid
    - acc
    - max
keep_nbest_models: 10
grad_clip: 5
grad_clip_type: 2.0
grad_noise: false
accum_grad: 4
no_forward_run: false
resume: true
train_dtype: float32
use_amp: false
log_interval: null
use_tensorboard: true
use_wandb: false
wandb_project: null
wandb_id: null
wandb_entity: null
wandb_name: null
wandb_model_log_interval: -1
detect_anomaly: false
pretrain_path: null
init_param: []
ignore_init_mismatch: false
freeze_param: []
num_iters_per_epoch: null
batch_size: 20
valid_batch_size: null
batch_bins: 30000000
valid_batch_bins: null
train_shape_file:
- exp/asr_stats_raw_zh_char/train/speech_shape
- exp/asr_stats_raw_zh_char/train/text_shape.char
valid_shape_file:
- exp/asr_stats_raw_zh_char/valid/speech_shape
- exp/asr_stats_raw_zh_char/valid/text_shape.char
batch_type: numel
valid_batch_type: null
fold_length:
- 51200
- 150
sort_in_batch: descending
sort_batch: descending
multiple_iterator: false
chunk_length: 500
chunk_shift_ratio: 0.5
num_cache_chunks: 1024
train_data_path_and_name_and_type:
-   - dump/raw/train_l/wav.scp
    - speech
    - sound
-   - dump/raw/train_l/text
    - text
    - text
valid_data_path_and_name_and_type:
-   - dump/raw/dev/wav.scp
    - speech
    - sound
-   - dump/raw/dev/text
    - text
    - text
allow_variable_data_keys: false
max_cache_size: 0.0
max_cache_fd: 32
valid_max_cache_size: null
optim: adam
optim_conf:
    lr: 0.0015
scheduler: warmuplr
scheduler_conf:
    warmup_steps: 30000
token_list:
- <blank>
- <unk>
- 的
- 我
- 是
- 你
- 了
- 一
- 不
- 这
- 个
- 有
- 就
- 们
- 在
- 他
- 人
- 么
- 来
- 说
- 那
- 要
- 好
- 啊
- 大
- 到
- 上
- 也
- 没
- 都
- 去
- 能
- 子
- 会
- 为
- 得
- 时
- 还
- 可
- 以
- 什
- 家
- 后
- 看
- 呢
- 对
- 事
- 天
- 下
- 过
- 想
- 多
- 小
- 出
- 自
- 儿
- 生
- 给
- 里
- 现
- 着
- 然
- 吧
- 样
- 道
- 吗
- 心
- 跟
- 中
- 很
- 点
- 年
- 和
- 地
- 怎
- 知
- 十
- 老
- 当
- 把
- 话
- 别
- 所
- 之
- 情
- 实
- 开
- 面
- 回
- 行
- 国
- 做
- 己
- 经
- 如
- 真
- 起
- 候
- 些
- 让
- 发
- 她
- 觉
- 但
- 成
- 定
- 意
- 二
- 长
- 最
- 方
- 三
- 前
- 因
- 用
- 呀
- 种
- 只
- 走
- 其
- 问
- 再
- 果
- 而
- 分
- 两
- 打
- 学
- 间
- 您
- 本
- 于
- 明
- 手
- 公
- 听
- 比
- 作
- 女
- 太
- 今
- 从
- 关
- 妈
- 同
- 法
- 动
- 已
- 见
- 才
- 孩
- 感
- 吃
- 常
- 次
- 它
- 进
- 先
- 找
- 身
- 全
- 理
- 又
- 力
- 正
- 主
- 应
- 高
- 被
- 钱
- 快
- 等
- 头
- 重
- 车
- 谢
- 日
- 东
- 放
- 无
- 工
- 咱
- 哪
- 五
- 者
- 像
- 西
- 该
- 干
- 相
- 信
- 机
- 百
- 特
- 业
- 活
- 师
- 边
- 爱
- 友
- 新
- 外
- 位
- 更
- 直
- 几
- 第
- 非
- 四
- 题
- 接
- 少
- 哥
- 死
- 完
- 刚
- 电
- 气
- 安
- 爸
- 白
- 告
- 美
- 解
- 叫
- 月
- 带
- 欢
- 谁
- 体
- 喜
- 部
- 场
- 姐
- 军
- 万
- 结
- 合
- 难
- 八
- 每
- 目
- 亲
- 朋
- 认
- 总
- 加
- 通
- 办
- 马
- 件
- 受
- 任
- 请
- 住
- 王
- 思
- 门
- 名
- 平
- 系
- 文
- 帮
- 路
- 变
- 记
- 水
- 九
- 算
- 将
- 口
- 男
- 度
- 报
- 六
- 张
- 管
- 够
- 性
- 表
- 提
- 何
- 讲
- 期
- 拿
- 保
- 嘛
- 司
- 原
- 始
- 此
- 诉
- 处
- 清
- 内
- 产
- 金
- 晚
- 早
- 交
- 离
- 眼
- 队
- 七
- 入
- 山
- 代
- 市
- 海
- 物
- 零
- 望
- 世
- 婚
- 命
- 越
- 收
- 向
- 花
- 房
- 错
- 节
- 父
- 反
- 战
- 买
- 量
- 或
- 员
- 号
- 千
- 怕
- 底
- 且
- 品
- 民
- 化
- 爷
- 并
- 与
- 服
- 需
- 资
- 求
- 教
- 娘
- 医
- 数
- 院
- 书
- 利
- 往
- 确
- 各
- 单
- 风
- 送
- 必
- 条
- 包
- 准
- 光
- 整
- 病
- 弟
- 嗯
- 计
- 照
- 强
- 务
- 影
- 城
- 夫
- 俩
- 决
- 声
- 连
- 乐
- 息
- 远
- 北
- 至
- 饭
- 留
- 宝
- 神
- 近
- 考
- 备
- 案
- 界
- 容
- 况
- 母
- 较
- 持
- 证
- 选
- 制
- 程
- 喝
- 害
- 字
- 失
- 立
- 台
- 玩
- 查
- 块
- 便
- 挺
- 段
- 周
- 由
- 句
- 紧
- 李
- 据
- 杀
- 南
- 商
- 识
- 网
- 式
- 愿
- 传
- 流
- 消
- 伤
- 根
- 演
- 希
- 故
- 坐
- 建
- 注
- 许
- 调
- 共
- 空
- 半
- 却
- 酒
- 联
- 微
- 言
- 肯
- 赶
- 跑
- 笑
- 区
- 岁
- 红
- 达
- 官
- 轻
- 易
- 火
- 线
- 拉
- 首
- 导
- 团
- 慢
- 指
- 写
- 深
- 论
- 片
- 改
- 啥
- 满
- 步
- 音
- 功
- 聊
- 客
- 未
- 格
- 基
- 睡
- 观
- 份
- 视
- 色
- 价
- 政
- 转
- 终
- 复
- 啦
- 呃
- 阿
- 倒
- 义
- 警
- 林
- 使
- 科
- 运
- 苦
- 待
- 费
- 随
- 救
- 试
- 班
- 敢
- 精
- 及
- 术
- 造
- 续
- 养
- 展
- 答
- 绝
- 众
- 站
- 妹
- 差
- 谈
- 卖
- 播
- 创
- 领
- 象
- 志
- 投
- 习
- 兄
- 元
- 皇
- 专
- 态
- 急
- 局
- 兴
- 楚
- 飞
- 护
- 装
- 热
- 奶
- 取
- 设
- 游
- 读
- 福
- 药
- 担
- 历
- 忙
- 规
- 掉
- 刘
- 切
- 断
- 尽
- 社
- 久
- 支
- 板
- 星
- 姑
- 曾
- 突
- 除
- 华
- 责
- 排
- 京
- 值
- 士
- 统
- 换
- 德
- 衣
- 组
- 示
- 脸
- 刻
- 黑
- 遇
- 虽
- 顾
- 戏
- 怪
- 懂
- 叔
- 夜
- 陈
- 亮
- 江
- 兵
- 负
- 布
- 青
- 落
- 推
- 假
- 类
- 令
- 技
- 英
- 质
- 黄
- 治
- 形
- 助
- 球
- 歌
- 参
- 广
- 继
- 简
- 画
- 奇
- 陪
- 阳
- 险
- 须
- 念
- 迎
- 幸
- 抓
- 破
- 另
- 争
- 竟
- 户
- 律
- 择
- 究
- 龙
- 足
- 店
- 脑
- 斯
- 党
- 权
- 约
- 疑
- 议
- 严
- 密
- 克
- 存
- 穿
- 承
- 校
- 击
- 际
- 标
- 云
- 营
- 察
- 超
- 食
- 集
- 级
- 礼
- 静
- 背
- 武
- 初
- 拍
- 梦
- 验
- 响
- 角
- 石
- 股
- 追
- 怀
- 婆
- 适
- 独
- 忘
- 血
- 醒
- 具
- 罪
- 享
- 毛
- 香
- 状
- 配
- 靠
- 语
- 仅
- 低
- 细
- 米
- 既
- 钟
- 极
- 停
- 味
- 则
- 油
- 器
- 楼
- 菜
- 研
- 互
- 压
- 贵
- 村
- 属
- 派
- 乎
- 坏
- 控
- 显
- 图
- 双
- 职
- 永
- 哈
- 鬼
- 依
- 料
- 按
- 府
- 坚
- 某
- 甚
- 居
- 练
- 顺
- 模
- 即
- 州
- 引
- 乱
- 速
- 庭
- 朝
- 室
- 似
- 付
- 划
- 尔
- 境
- 犯
- 烦
- 环
- 伙
- 巴
- 春
- 古
- 妇
- 势
- 款
- 增
- 财
- 河
- 守
- 虑
- 汉
- 枪
- 妻
- 爹
- 弄
- 委
- 企
- 冲
- 置
- 麻
- 育
- 项
- 防
- 胡
- 杨
- 致
- 辈
- 括
- 毕
- 卫
- 修
- 史
- 型
- 牌
- 嘴
- 苏
- 群
- 举
- 痛
- 座
- 概
- 搞
- 围
- 土
- 毒
- 唱
- 冷
- 累
- 玉
- 获
- 误
- 跳
- 脚
- 雨
- 剧
- 休
- 皮
- 止
- 济
- 肉
- 丽
- 借
- 铁
- 牛
- 哭
- 招
- 闹
- 银
- 优
- 温
- 狗
- 退
- 洗
- 拜
- 否
- 票
- 偷
- 抱
- 博
- 般
- 效
- 套
- 维
- 普
- 康
- 富
- 宫
- 索
- 罗
- 堂
- 智
- 省
- 介
- 孙
- 灵
- 评
- 藏
- 称
- 课
- 货
- 姨
- 艺
- 骗
- 雪
- 赛
- 景
- 昨
- 健
- 鱼
- 激
- 危
- 熟
- 圈
- 闻
- 监
- 替
- 君
- 恋
- 良
- 掌
- 草
- 松
- 供
- 努
- 例
- 短
- 帝
- 姓
- 率
- 族
- 亿
- 赵
- 蛋
- 判
- 预
- 频
- 卡
- 架
- 纪
- 弃
- 秀
- 兰
- 层
- 检
- 伴
- 抗
- 讨
- 源
- 夏
- 咋
- 惊
- 录
- 善
- 补
- 刀
- 充
- 升
- 章
- 午
- 若
- 私
- 吴
- 素
- 旅
- 临
- 挑
- 唐
- 露
- 树
- 斗
- 舞
- 左
- 叶
- 副
- 晓
- 厂
- 弹
- 印
- 秘
- 屋
- 田
- 木
- 困
- 园
- 封
- 逃
- 批
- 馆
- 疼
- 败
- 陆
- 敌
- 散
- 采
- 翻
- 缺
- 胜
- 免
- 销
- 鸡
- 降
- 波
- 测
- 限
- 释
- 忍
- 归
- 床
- 餐
- 茶
- 码
- 宁
- 乡
- 辛
- 彩
- 亚
- 浪
- 漂
- 庆
- 训
- 范
- 烧
- 词
- 吵
- 媳
- 探
- 余
- 恐
- 积
- 农
- 遍
- 舒
- 顶
- 构
- 呼
- 丝
- 执
- 雅
- 惯
- 右
- 脱
- 恩
- 野
- 折
- 趣
- 笔
- 谓
- 盘
- 贝
- 宣
- 绍
- 嘉
- 宋
- 抢
- 嫌
- 尊
- 碰
- 绪
- 丢
- 厉
- 沙
- 轮
- 施
- 织
- 托
- 县
- 策
- 杯
- 逼
- 傻
- 束
- 街
- 疗
- 益
- 骨
- 迷
- 姻
- 恶
- 默
- 寻
- 搜
- 哦
- 材
- 吸
- 劳
- 勇
- 占
- 暴
- 船
- 徐
- 虎
- 融
- 异
- 审
- 攻
- 雷
- 稳
- 呗
- 输
- 睛
- 臣
- 端
- 威
- 秋
- 欧
- 冰
- 韩
- 减
- <space>
- 操
- 混
- 汽
- 暗
- 隐
- 嫂
- 沉
- 烟
- 顿
- 凭
- 洋
- 嫁
- 购
- 粉
- 遗
- 杂
- 协
- 尝
- 键
- 亡
- 秦
- 纸
- 拥
- 革
- 猫
- 伯
- 祝
- 签
- 傅
- 牙
- 湖
- 莫
- 杰
- 旁
- 港
- 劲
- 宗
- 偏
- 触
- 唯
- 吓
- 辆
- 沈
- 列
- 梅
- 祖
- 舍
- 尤
- 赚
- 疫
- 腾
- 拼
- 奖
- 刺
- 齐
- 诚
- 媒
- 戴
- 账
- 炸
- 骂
- 避
- 麦
- 爆
- 域
- 烈
- 暖
- 季
- 猜
- 佳
- 净
- 腿
- 磨
- 曲
- 虚
- 阵
- 荣
- 访
- 核
- 鲜
- 阶
- 镇
- 灯
- 估
- 剩
- 硬
- 租
- 敬
- 损
- 惜
- 挂
- 董
- 巨
- 忆
- 登
- 丈
- 帅
- 童
- 耳
- 央
- 软
- 移
- 略
- 额
- 厅
- 挥
- 透
- 络
- 弱
- 珍
- 恨
- 巧
- 丁
- 谋
- 孤
- 豆
- 诗
- 冒
- 狼
- 渐
- 峰
- 售
- 凡
- 聚
- 洞
- 抽
- 劝
- 闭
- 摆
- 冬
- 凶
- 魔
- 灭
- 雄
- 挣
- 搬
- 龄
- 朱
- 编
- 航
- 席
- 驾
- 授
- 鼓
- 握
- 隔
- 猪
- 仙
- 颜
- 镜
- 胖
- 赢
- 仇
- 晨
- 欺
- 刑
- 谷
- 旦
- 亏
- 盖
- 症
- 喊
- 蓝
- 讯
- 殿
- 梁
- 躲
- 旧
- 针
- 箱
- 丰
- 洲
- 鞋
- 征
- 蒙
- 伟
- 袋
- 庄
- 患
- 怨
- 佛
- 稍
- 朵
- 纳
- 吉
- 川
- 典
- 迹
- 瑞
- 废
- 搭
- 涨
- 汤
- 启
- 桌
- 摸
- 赔
- 宜
- 纯
- 贴
- 聪
- 熊
- 延
- 瓶
- 版
- 缘
- 距
- 甜
- 析
- 盛
- 孕
- 彻
- 桥
- 尚
- 染
- 撞
- 途
- 沟
- 疯
- 敏
- 瞧
- 漫
- 胆
- 诺
- 刷
- 饿
- 仍
- 喂
- 辞
- 迟
- 淡
- 郑
- 歉
- 扰
- 宾
- 圆
- 赞
- 肚
- 慧
- 泪
- 吹
- 拖
- 遭
- 穷
- 罚
- 悔
- 绿
- 忽
- 唉
- 毫
- 绩
- 暂
- 射
- 岛
- 拾
- 珠
- 欠
- 忠
- 陷
- 阴
- 尼
- 悲
- 糊
- 撤
- 徒
- 剑
- 币
- 娜
- 违
- 泡
- 仗
- 粮
- 培
- 趟
- 菲
- 拒
- 棒
- 脾
- 赏
- 窗
- 宇
- 闲
- 附
- 踏
- 彼
- 涉
- 锁
- 撒
- 魂
- 羊
- 述
- 屈
- 库
- 滚
- 凉
- 颗
- 寒
- 呐
- 墙
- 娃
- 序
- 迪
- 丹
- 扬
- 瞎
- 递
- 凤
- 碗
- 屁
- 锅
- 奔
- 幅
- 债
- 糖
- 奋
- 汇
- 圣
- 订
- 偶
- 残
- 宽
- 狂
- 鼠
- 狠
- 幕
- 固
- 竞
- 蜜
- 吐
- 摄
- 骑
- 篇
- 毁
- 尾
- 摇
- 奥
- 厚
- 妖
- 禁
- 逐
- 均
- 尸
- 冠
- 阅
- 辑
- 捕
- 载
- 郭
- 俺
- 诊
- 欲
- 扎
- 鸟
- 柔
- 迫
- 豪
- 踪
- 扔
- 碎
- 末
- 娶
- 扫
- 朕
- 励
- 乔
- 闺
- 档
- 厨
- 倍
- 湾
- 郎
- 幼
- 纷
- 奴
- 阻
- 饮
- 怒
- 妙
- 琴
- 曹
- 脏
- 牵
- 瓜
- 滴
- 炮
- 缓
- 含
- 献
- 柜
- 仔
- 艾
- 潜
- 赌
- 震
- 础
- 添
- 兔
- 焦
- 躺
- 森
- 肥
- 洪
- 孝
- 偿
- 悉
- 撑
- 甘
- 桃
- 苹
- 魏
- 鲁
- 池
- 狱
- 厌
- 纠
- 朗
- 贷
- 铺
- 殊
- 坦
- 爬
- 擦
- 酸
- 钢
- 咖
- 瞒
- 蛮
- 谅
- 耐
- 申
- 夸
- 欣
- 诶
- 驶
- 屏
- 烂
- 凌
- 甲
- 胎
- 仪
- 貌
- 番
- 涂
- 抬
- 舅
- 扯
- 鹿
- 摩
- 诸
- 秒
- 泽
- 埋
- 蒋
- 隆
- 赖
- 奸
- 咬
- 恢
- 宿
- 乖
- 邀
- 抵
- 臭
- 闪
- 莉
- 熬
- 链
- 盯
- 侦
- 灾
- 堆
- 灰
- 卷
- 盾
- 障
- 截
- 恰
- 佩
- 戒
- 莲
- 裁
- 芬
- 戚
- 匪
- 滑
- 趁
- 询
- 绑
- 辣
- 挖
- 俗
- 祸
- 符
- 扣
- 插
- 仁
- 壁
- 腰
- 斤
- 燕
- 筑
- 柱
- 夺
- 援
- 映
- 壮
- 杜
- 摔
- 润
- 恭
- 乌
- 慰
- 啡
- 著
- 井
- 跌
- 牢
- 荐
- 拔
- 惹
- 侯
- 玲
- 炎
- 胸
- 旗
- 牲
- 喽
- 涛
- 衡
- 矛
- 伍
- 贤
- 惨
- 糟
- 慌
- 伏
- 醉
- 仓
- 拆
- 乘
- 疾
- 鼻
- 潮
- 予
- 奉
- 伦
- 劫
- 伊
- 怜
- 孟
- 肺
- 忧
- 倾
- 矩
- 荒
- 奏
- 塔
- 塞
- 迅
- 轨
- 瞬
- 丫
- 狐
- 叛
- 繁
- 眠
- 孔
- 谱
- 悄
- 泰
- 姜
- 侵
- 妃
- 冯
- 柳
- 洛
- 岸
- 凯
- 陛
- 幺
- 仿
- 氏
- 窝
- 曼
- 挡
- 浩
- 盟
- 轩
- 牺
- 贫
- 绕
- 谎
- 措
- 扶
- 梯
- 炼
- 勤
- 霸
- 横
- 罢
- 呆
- 税
- 桂
- 哎
- 慕
- 植
- 允
- 荡
- 洁
- 肖
- 耗
- 贼
- 艰
- 贺
- 幻
- 饱
- 胃
- 袭
- 廷
- 泥
- 丧
- 缩
- 砸
- 姥
- 拦
- 扮
- 糕
- 肤
- 猴
- 脆
- 炒
- 耀
- 盗
- 邓
- 扩
- 纵
- 振
- 敲
- 鹏
- 姆
- 湿
- 丑
- 召
- 苗
- 伸
- 惑
- 碍
- 萨
- 瘦
- 闯
- 迁
- 坑
- 弯
- 卑
- 尖
- 遥
- 侠
- 犹
- 押
- 冤
- 钻
- 汗
- 闷
- 邻
- 淘
- 抛
- 妆
- 贾
- 侧
- 傲
- 描
- 耍
- 猛
- 薇
- 裤
- 憾
- 督
- 贸
- 墨
- 勒
- 薄
- 嘞
- 渡
- 紫
- 悟
- 锦
- 溜
- 逆
- 惠
- 辉
- 贪
- 圾
- 垃
- 券
- 燃
- 虫
- 悠
- 伪
- 尿
- 懒
- 俊
- 寄
- 歇
- 盒
- 潘
- 储
- 愈
- 脉
- 粗
- 返
- 昌
- 泉
- 蔡
- 愧
- 赤
- 岳
- 婷
- 猎
- 饼
- 肩
- 勾
- 巡
- 竹
- 催
- 陌
- 踩
- 促
- 扭
- 堵
- 酷
- 芳
- 逛
- 陵
- 耽
- 凑
- 寿
- 缝
- 剪
- 郁
- 宅
- 抚
- 筹
- 沿
- 烤
- 奈
- 挨
- 晋
- 崩
- 浮
- 阁
- 彭
- 裂
- 崇
- 眉
- 桑
- 辩
- 漏
- 稀
- 液
- 汪
- 袁
- 掩
- 浑
- 坡
- 晕
- 缠
- 仰
- 挤
- 睁
- 羽
- 岗
- 捡
- 墓
- 综
- 矿
- 妥
- 厕
- 辱
- 惧
- 逗
- 帽
- 寸
- 搁
- 跨
- 渴
- 饰
- 璃
- 琳
- 爽
- 愤
- 饶
- 卧
- 誓
- 滋
- 鉴
- 腐
- 鸭
- 蛇
- 妮
- 莱
- 哟
- 钥
- 甄
- 肠
- 畅
- 慎
- 悬
- 逻
- 胁
- 辰
- 呈
- 棋
- 寨
- 萌
- 覆
- 姚
- 津
- 笨
- 轰
- 乏
- 匙
- 摊
- 陶
- 恼
- 昏
- 抑
- 姿
- 愁
- 誉
- 椅
- 羞
- 澡
- 踢
- 晶
- 萧
- 箭
- 罩
- 宠
- 羡
- 亦
- 祥
- 串
- 昆
- 煮
- 疏
- 纹
- 泄
- 痕
- 喷
- 册
- 跃
- 卢
- 岩
- 跪
- 兽
- 桶
- 飘
- 漠
- 堪
- 哄
- 寂
- 崔
- 腹
- 癌
- 拳
- 驻
- 霍
- 拨
- 诞
- 捐
- 御
- 榜
- 唤
- 荷
- 径
- 署
- 锋
- 玛
- 匆
- 恒
- 吕
- 邮
- 圳
- 黎
- 掏
- 莎
- 寞
- 佐
- 诈
- 牧
- 盐
- 叹
- 尬
- 匹
- 狸
- 膀
- 谨
- 尘
- 驱
- 乳
- 晒
- 宴
- 辜
- 哲
- 铜
- 薪
- 盆
- 割
- 忌
- 旋
- 翼
- 哀
- 咨
- 遵
- 夹
- 侣
- 译
- 胞
- 浅
- 邦
- 俄
- 弗
- 豫
- 甭
- 乃
- 扛
- 杭
- 瓦
- 槽
- 污
- 尴
- 琢
- 枝
- 详
- 柴
- 佑
- 盼
- 抖
- 惩
- 捷
- 葬
- 贡
- 艳
- 塑
- 茫
- 叨
- 浓
- 拐
- 捉
- 憋
- 稿
- 苍
- 葛
- 扑
- 娱
- 赋
- 杆
- 绘
- 聆
- 肌
- 婴
- 摘
- 岂
- 呵
- 冻
- 泳
- 揭
- 坤
- 盈
- 毅
- 撕
- 娇
- 唠
- 宏
- 吊
- 籍
- 楠
- 肃
- 抹
- 玄
- 湘
- 迈
- 酱
- 骄
- 咐
- 扇
- 幽
- 疲
- 邪
- 吞
- 趋
- 尺
- 玻
- 溃
- 诱
- 翠
- 兼
- 辅
- 岭
- 栏
- 柏
- 址
- 寺
- 逢
- 琪
- 慈
- 愣
- 契
- 渠
- 齿
- 薛
- 拟
- 填
- 坛
- 抄
- 痴
- 绳
- 役
- 擅
- 晃
- 斌
- 愉
- 届
- 悦
- 旨
- 砍
- 弥
- 挽
- 肝
- 鸣
- 庙
- 烫
- 聘
- 皆
- 婶
- 舌
- 枉
- 赫
- 蓉
- 瞅
- 阔
- 俱
- 循
- 鸿
- 彪
- 伺
- 堡
- 谦
- 剂
- 洒
- 赴
- 妨
- 磊
- 嘱
- 蝶
- 兆
- 豹
- 绣
- 篮
- 锻
- 陕
- 霉
- 涵
- 疆
- 丸
- 蠢
- 铃
- 浙
- 庞
- 萝
- 泛
- 芝
- 煤
- 甩
- 氛
- 页
- 逸
- 袖
- 携
- 躁
- 夕
- 匠
- 蹈
- 坊
- 雾
- 蹲
- 颠
- 脂
- 塌
- 棵
- 鹰
- 澳
- 哇
- 筋
- 纽
- 脖
- 棉
- 渣
- 寡
- 践
- 侄
- 披
- 魅
- 虹
- 肿
- 胶
- 霞
- 罐
- 晴
- 拓
- 卿
- 耻
- 砖
- 宪
- 歪
- 兜
- 衰
- 捧
- 歹
- 雕
- 穆
- 栋
- 瑶
- 毙
- 衷
- 膜
- 囊
- 莹
- 垫
- 吻
- 嘟
- 舰
- 虾
- 壳
- 穴
- 勉
- 裙
- 旺
- 柯
- 磕
- 贩
- 腻
- 蹦
- 卜
- 茹
- 驴
- 臂
- 删
- 菌
- 妾
- 蜂
- 祭
- 菊
- 咸
- 淑
- 笼
- 涯
- 碧
- 宙
- 骚
- 皓
- 赐
- 晰
- 腔
- 龟
- 泼
- 鹅
- 啪
- 巾
- 炉
- 沾
- 醋
- 澜
- 朴
- 棍
- 伞
- 雀
- 赠
- 妞
- 淋
- 刮
- 汁
- 椒
- 埃
- 嚷
- 盲
- 窃
- 辽
- 贱
- 滩
- 昭
- 贯
- 珊
- 涌
- 辨
- 捞
- 仲
- 拘
- 碑
- 侍
- 剿
- 搅
- 狮
- 藤
- 旭
- 翅
- 滨
- 禀
- 遮
- 瑟
- 斩
- 攒
- 犬
- 挫
- 僧
- 吩
- 渊
- 蒂
- 萍
- 庸
- 蓄
- 鼎
- 咪
- 姬
- 溪
- 郡
- 镖
- 怡
- 杉
- 畏
- 瓷
- 枚
- 煎
- 劣
- 饺
- 妄
- 卓
- 蔽
- 蒸
- 垂
- 嘲
- 慨
- 谊
- 蹭
- 逮
- 锐
- 钉
- 舟
- 沃
- 凝
- 翔
- 颈
- 靖
- 灌
- 膊
- 崖
- 娟
- 胳
- 铭
- 灿
- 亭
- 粒
- 卸
- 咕
- 坎
- 攀
- 婿
- 奢
- 茂
- 趴
- 耿
- 捏
- 怖
- 浴
- 婉
- 煌
- 霖
- 揍
- 昂
- 驰
- 壶
- 械
- 卦
- 粥
- 尹
- 瘾
- 雇
- 翰
- 肆
- 寇
- 曦
- 厢
- 杠
- 屠
- 芒
- 谣
- 沫
- 掘
- 酬
- 讼
- 乾
- 玫
- 瑰
- 逊
- 惦
- 儒
- 肾
- 粹
- 愚
- 渔
- 暑
- 伐
- 潇
- 喘
- 敦
- 翁
- 斥
- 帖
- 纱
- 梳
- 缴
- 茅
- 谭
- 氧
- 遣
- 履
- 刹
- 枕
- 婢
- 徽
- 轿
- 寓
- 咽
- 叉
- 嗓
- 捣
- 裹
- 览
- 拯
- 疚
- 蜀
- 丛
- 框
- 斑
- 宵
- 郝
- 蛙
- 熙
- 祁
- 哑
- 葱
- 唇
- 韦
- 媛
- 魄
- 锤
- 绵
- 炫
- 吨
- 稻
- 碌
- 刊
- 漆
- 搏
- 讶
- 痒
- 枫
- 妒
- 冥
- 郊
- 爵
- 逝
- 栽
- 叠
- 蚁
- 裕
- 帕
- 剥
- 谐
- 巫
- 颇
- 娥
- 廊
- 蕾
- 丘
- 丞
- 葡
- 坠
- 鸦
- 糗
- 虐
- 唬
- 屎
- 顽
- 巷
- 硅
- 罕
- 殖
- 嘿
- 韵
- 歧
- 垮
- 淮
- 馈
- 昊
- 宰
- 钦
- 霜
- 兑
- 萄
- 塘
- 胀
- 樱
- 枯
- 咳
- 窑
- 募
- 缸
- 昧
- 仑
- 恕
- 氓
- 叮
- 吼
- 坟
- 轴
- 贞
- 赎
- 帆
- 嫩
- 蚂
- 僵
- 颖
- 噜
- 咒
- 琐
- 勃
- 芯
- 绸
- 哼
- 仨
- 挪
- 狡
- 禅
- 粘
- 雯
- 扒
- 恳
- 蔬
- 匈
- 钓
- 桐
- 菇
- 哒
- 稚
- 膏
- 纲
- 狄
- 硕
- 廉
- 衙
- 艘
- 廖
- 腊
- 蟹
- 邱
- 缉
- 曝
- 桩
- 啤
- 嫉
- 棚
- 矮
- 汰
- 衍
- 拽
- 削
- 彤
- 斜
- 揉
- 樊
- 馨
- 钩
- 浦
- 肢
- 敷
- 喻
- 鞭
- 瞪
- 耕
- 掐
- 屡
- 榴
- 勋
- 泊
- 竭
- 鹤
- 溢
- 淳
- 倩
- 驳
- 抠
- 捅
- 筒
- 窄
- 鄙
- 嗦
- 袍
- 劈
- 炖
- 裸
- 贬
- 敞
- 嘎
- 淹
- 耶
- 秩
- 舱
- 厦
- 叙
- 孽
- 筷
- 浇
- 饥
- 噩
- 蚊
- 兮
- 皱
- 侃
- 辟
- 弊
- 袜
- 吾
- 俘
- 芸
- 夷
- 芦
- 囚
- 倡
- 琦
- 哨
- 巢
- 烛
- 帐
- 燥
- 讽
- 俞
- 馅
- 柿
- 墅
- 妍
- 瘤
- 沦
- 衬
- 瑜
- 蒜
- 蛛
- 窟
- 勿
- 沛
- 磁
- 狭
- 栈
- 懵
- 酿
- 戈
- 邵
- 龚
- 衫
- 勺
- 哗
- 叽
- 畜
- 爪
- 惫
- 颁
- 浸
- 摧
- 勘
- 惕
- 蔓
- 馒
- 挠
- 陀
- 豁
- 帘
- 淀
- 藩
- 蜡
- 凳
- 蘑
- 琼
- 棺
- 蝴
- 骆
- 掰
- 枣
- 遂
- 飙
- 咧
- 掀
- 梨
- 杏
- 嗑
- 棠
- 绽
- 捆
- 舆
- 肇
- 葩
- 呦
- 膝
- 鹊
- 揣
- 瓣
- 靓
- 卵
- 鲍
- 炭
- 戳
- 颤
- 禄
- 菩
- 崛
- 驸
- 佣
- 眨
- 聂
- 乙
- 嘻
- 拧
- 喵
- 佟
- 靳
- 阎
- 拢
- 厘
- 凰
- 疤
- 螺
- 淇
- 涩
- 拎
- 嗨
- 魁
- 薯
- 歼
- 沪
- 筛
- 谍
- 揪
- 刁
- 秃
- 谜
- 撇
- 肪
- 绊
- 逞
- 滥
- 寝
- 麟
- 奕
- 侮
- 喉
- 柄
- 荆
- 撼
- 窦
- 姗
- 乞
- 艇
- 竖
- 剖
- 嗽
- 捂
- 腕
- 鸽
- 刃
- 弓
- 辙
- 粤
- 泣
- 梗
- 茄
- 茜
- 驼
- 冈
- 倔
- 啃
- 蹄
- 唧
- 祈
- 腺
- 焰
- 睿
- 崽
- A
- 苛
- 窍
- 凿
- 倭
- 骤
- 槛
- 碳
- 诏
- 芽
- 浆
- 隶
- 搂
- 睦
- 彬
- 岔
- 诀
- 嚼
- 掺
- 殷
- 吁
- 啰
- 侈
- 亩
- 纤
- 倦
- 揽
- 媚
- 潭
- 莽
- 赃
- 睹
- 脊
- 逍
- 淼
- 沸
- 峡
- 仆
- 眷
- 屯
- 璐
- 雁
- 澄
- 渗
- 咔
- 啸
- 怂
- 娄
- 惶
- 恍
- 锡
- 秉
- 猾
- 挟
- 舔
- 弦
- 阱
- 俭
- 嚣
- 搓
- 懈
- 诡
- 隙
- 苟
- 倘
- 瘫
- 扁
- 鑫
- 撩
- 蓬
- 铲
- 峥
- 巅
- 葫
- 膳
- 狙
- 晏
- 祠
- 峻
- 尉
- 毯
- 沧
- 熏
- 咯
- 株
- 沐
- 奎
- 锣
- 霄
- 彦
- 叭
- 臻
- 昔
- 灶
- 傍
- 腥
- 屑
- 禾
- 彰
- 冉
- 矫
- 滞
- 瘩
- 匀
- 椎
- 槐
- 岚
- 跷
- 剔
- 倪
- 盏
- 泌
- 灸
- 隧
- 函
- 壤
- 剃
- 蹊
- 葵
- 拌
- 琅
- 炳
- 跋
- 瑾
- 哩
- 蔷
- 鳌
- 莺
- 诵
- 疙
- 吱
- 蓓
- 绎
- 匿
- 铮
- 怼
- 踹
- 嗅
- 焚
- 躯
- 蝇
- 橘
- 祟
- 辖
- 砂
- 韧
- 粪
- 诬
- 擒
- 黏
- 衔
- 溺
- 蜘
- 篷
- 贿
- 闫
- 焕
- 邢
- 兹
- 窖
- 旬
- 铸
- 咚
- 惭
- 佬
- 裴
- 裳
- 犀
- 弘
- 莓
- 钏
- 鄂
- 陋
- 伽
- 鞠
- 氪
- 垒
- 窜
- 橙
- 讳
- 甥
- 淫
- 拱
- 袱
- 坨
- 暧
- 渺
- 蕉
- 晗
- 茬
- 盔
- 妓
- 蚕
- 僻
- 朽
- 呛
- 挚
- 擎
- 绅
- 喇
- 鳄
- 巩
- 蜗
- 遛
- 俯
- 汹
- 猩
- 奠
- 钙
- 悍
- 躬
- 菱
- 翘
- 琉
- 虏
- 凄
- 稼
- 炕
- 皂
- 漱
- 斋
- 撂
- 敛
- 阮
- 芭
- 阀
- 缚
- 懦
- 亨
- 螃
- 侥
- 膨
- 筝
- 惟
- 黛
- 眯
- 茨
- 怠
- 辐
- 捎
- 殴
- 桓
- 瞄
- 冀
- 雍
- 霾
- 酵
- 檬
- 哺
- 裔
- 兢
- 麒
- 烹
- 绒
- 丐
- 娅
- 钞
- 垄
- 笛
- 赣
- 蕊
- 暮
- 噪
- 沮
- 肋
- 庇
- 橡
- 摁
- 痘
- 棘
- 拂
- 绷
- 刨
- 晾
- 蹬
- 鸥
- 璇
- 掠
- 瘟
- 俐
- 糙
- 骏
- 牡
- 撵
- 嘘
- 沥
- 庶
- 赁
- 喧
- 涡
- 瞳
- 迭
- 肘
- 颂
- 珑
- 觅
- 埔
- G
- 跤
- 朔
- 詹
- 梭
- 暇
- 惺
- 甸
- 怯
- 聋
- 赦
- 屉
- 闸
- 坝
- 吟
- 凸
- 拴
- 堤
- 矣
- 斧
- 呸
- 啼
- 韬
- 钧
- 坞
- 纺
- 氢
- 嵩
- 镯
- 髓
- 檐
- 涕
- 剁
- 稽
- 烨
- 钮
- 闽
- 仕
- 驯
- 吭
- 漓
- 眸
- 鞅
- 枢
- 煞
- 昕
- 畔
- 疹
- 矶
- 呱
- 熄
- 吏
- 泻
- 拙
- 蛤
- 禽
- 甫
- 厮
- 乍
- 蝉
- 撬
- 嘀
- 衅
- 鲨
- 萱
- 霹
- 旷
- 辫
- 坷
- 眶
- 蟆
- 呜
- 猬
- 嬷
- 萎
- 靶
- 雳
- 煲
- 溯
- 蚀
- 狈
- 滤
- 恙
- 瑛
- 栓
- 嫣
- 碟
- 祷
- 驿
- 犊
- 灼
- 哆
- 宛
- 榨
- 寥
- 翟
- 栗
- 滔
- 馋
- 杖
- 茉
- 饲
- 庐
- 隋
- 旱
- 崎
- 颅
- 焉
- 墩
- 篱
- 晟
- 扳
- 咎
- 竿
- 僚
- 溶
- 俏
- 霆
- 堕
- 冕
- 叩
- 绰
- 洽
- 襄
- 蛊
- 缅
- 侨
- 伶
- 蕴
- 酥
- 坂
- 拇
- 庚
- 卒
- 诛
- 禧
- 瓢
- 锯
- 扉
- 饷
- 诅
- 烘
- 浏
- 痰
- 榆
- 窥
- 鲸
- 捋
- 戎
- 笋
- 璋
- 诫
- 珈
- 癫
- 囤
- 厥
- 癖
- 翩
- 芹
- 匣
- 噬
- 栖
- 蝎
- 锄
- 玺
- 疮
- 缕
- 猥
- 槿
- 蔑
- 汝
- 珂
- 撮
- 坪
- 蒲
- 倚
- 嗷
- 撰
- 荧
- 芙
- 豚
- 筱
- 敖
- 孵
- 猝
- D
- 弈
- 徊
- 辗
- 赘
- 徘
- 烙
- 娲
- 嚎
- 迢
- 绥
- 羁
- 屌
- 铅
- 澎
- S
- 嬛
- 晦
- 煽
- 逾
- 饵
- 虞
- 筐
- 哧
- 抒
- 醇
- 祀
- 瑕
- 岐
- 潼
- 惚
- C
- 苑
- 靡
- 菠
- 赡
- 惰
- 梓
- 铛
- 澈
- 莞
- 呕
- 驭
- 邝
- 砰
- 轼
- 窒
- 慷
- 绞
- 絮
- 虔
- 惮
- 柬
- 嗡
- 拣
- 羲
- 蹋
- 隘
- 帜
- 卤
- 雌
- 唾
- 邹
- 俑
- 碾
- 婪
- 咏
- 粟
- 崭
- 钝
- 彝
- 陡
- 谛
- 秤
- 磅
- 淌
- 炊
- 鲤
- 羹
- 殉
- 曰
- 萤
- 阐
- 鬟
- 拭
- T
- 沁
- 滇
- 梧
- 烁
- 瞻
- 淤
- 凹
- 撸
- 棕
- 腌
- 缪
- 祺
- 痊
- 忑
- 柠
- 矜
- 忐
- 讹
- 瀚
- 尧
- 昼
- 芊
- 憨
- 鳞
- 匮
- 鸳
- 鸯
- 湃
- 屿
- 馍
- 沽
- 栾
- 蝠
- 窘
- 绛
- 巍
- 悯
- 焊
- 谴
- 浊
- 娴
- 畴
- 湛
- 螂
- 韭
- 哮
- 拷
- 攥
- 凛
- 颓
- 恺
- 蝙
- 襟
- 粑
- 洼
- 笃
- 渝
- 骁
- 殃
- 酌
- 乒
- 臊
- 疵
- 诧
- 谬
- 锈
- 袄
- 膛
- 瘸
- 嫖
- 梢
- 沼
- 棱
- 嚓
- 耸
- 喳
- 舵
- 橱
- 涮
- 檀
- 瞩
- 腑
- 岑
- 痪
- 墟
- 蔚
- 捍
- 徙
- 棣
- 猖
- 掷
- 恬
- 嫦
- 噔
- 饪
- 掂
- 恤
- 叱
- 芷
- 弩
- 楷
- 镶
- 茧
- 诠
- 咙
- 匡
- 擂
- 亵
- 杞
- 乓
- 渤
- 藉
- 憔
- 渭
- 禹
- 睐
- 趾
- 抉
- 悴
- 忒
- 茸
- 纬
- 懊
- 浚
- 溅
- 遏
- 琛
- 靴
- 戮
- 翎
- 谕
- 濒
- 锵
- 嬉
- 籽
- 殆
- 叼
- 苔
- 灏
- 嗖
- 俪
- 亢
- 冶
- 嗜
- 磋
- 汀
- 讪
- 萃
- 菁
- 镑
- 紊
- 脯
- 缆
- 哉
- 赂
- 婊
- B
- 蕃
- 迄
- 蜓
- 舜
- 嚏
- 昱
- 黔
- 犟
- 汐
- 昵
- 嗣
- 唆
- 蛾
- 黯
- 绯
- 瀑
- 憬
- 狩
- 掖
- 崴
- 褪
- 髦
- 酝
- 弧
- 咄
- 吝
- 馄
- 娩
- 窿
- 蜻
- 袒
- 玮
- 阙
- 篡
- 邯
- 朦
- 邑
- 喃
- 粽
- 捶
- 嫔
- 钗
- 穗
- 骼
- 胭
- 寐
- 噎
- M
- 碱
- 荤
- 笙
- 矢
- 芥
- 廓
- 扼
- 厄
- 毋
- 糯
- 惋
- 纶
- 碜
- 胧
- 懿
- 偃
- 沏
- 痹
- 慑
- 鹦
- 娠
- 铐
- 绢
- 傀
- 孜
- 饨
- 儡
- 孰
- 焱
- 峭
- 伎
- 幌
- 椰
- 譬
- 藕
- 坍
- 铝
- 鞍
- 蘸
- 貂
- 猿
- 炙
- 琊
- 峙
- 硝
- 幂
- 钰
- 眩
- 亥
- 簇
- 鹉
- 睫
- 斟
- 簧
- 颐
- 薰
- 癞
- 祛
- 燎
- 缎
- 簸
- 咣
- 绚
- 簿
- 邋
- 嵌
- 肮
- 稷
- 辍
- 闵
- 枸
- 撅
- 曙
- 苇
- K
- 悼
- 汶
- 匕
- 皖
- 腮
- 琶
- 汲
- 鼹
- 礁
- 颊
- 怔
- 汕
- 喀
- 砌
- 釜
- 畸
- 鹃
- 峨
- 奄
- 骡
- 斐
- 芈
- 莘
- 蟑
- 荔
- 缇
- 犒
- 宓
- 汾
- 沌
- 宦
- 憧
- 咤
- 吆
- 攘
- 漩
- 梵
- 阂
- 吒
- 芜
- 缔
- 秧
- 翊
- 晌
- 剐
- 蜕
- 芋
- 彷
- 牟
- 诲
- 臀
- 徨
- Q
- 杵
- 荫
- 榄
- 蹿
- 豌
- 迂
- 琵
- 拗
- 帷
- 楞
- 嘶
- 橄
- 胺
- 圭
- 砚
- 藻
- 凋
- 啄
- 褒
- 嗝
- 殡
- 嫡
- 恃
- 濡
- 缜
- 孺
- 泸
- 妊
- 衩
- 驹
- 榻
- 腆
- 鹂
- 箍
- 璧
- 熔
- 悚
- 遢
- 弛
- 诋
- 羚
- 鹭
- 嘚
- 骸
- 瘪
- 铠
- 瞿
- 屹
- 邸
- 痨
- 辘
- 浒
- 忏
- 钊
- 潦
- 怅
- 肴
- 蚯
- 胚
- 茵
- 蚓
- 戬
- 瘀
- 翡
- 恪
- 卉
- 蝌
- 雏
- 祯
- 谏
- 蚪
- 钵
- 馊
- 嗒
- 犁
- 寅
- V
- 锥
- 娼
- 晖
- 啬
- 纣
- 淆
- 丙
- 夯
- 竣
- 褚
- 褥
- 轧
- 氨
- 褂
- 钳
- 轲
- 竺
- 疡
- 淞
- 胤
- 摹
- 鳅
- 珀
- 偕
- 匾
- 觑
- 扈
- 傣
- 绫
- 枷
- 阑
- 柚
- 烊
- 怦
- 腼
- 珺
- 缀
- 裘
- 碉
- 峪
- 俸
- 羯
- 姊
- 疟
- 砺
- 盎
- 嘣
- 釉
- 溥
- 熠
- 垢
- 摞
- 哽
- 槟
- 囧
- 胰
- 遁
- 痞
- 熹
- 忡
- 稠
- 顷
- 瑚
- 卯
- 渎
- 炅
- 褶
- 烽
- 瞑
- 嘈
- 硫
- 壹
- 悖
- 酪
- 跺
- 阜
- 帛
- 漪
- 蝗
- 迦
- 蟒
- 咀
- 谤
- 睬
- 辕
- 绮
- 搀
- 裆
- 鳖
- 囡
- 羔
- 痣
- 滕
- 佘
- 樟
- 韶
- 霓
- 劾
- 赈
- 唏
- 闰
- 脐
- 沓
- 瓮
- 篓
- 笠
- 暄
- 涅
- 诽
- 洱
- 栅
- 蚱
- 囔
- 攸
- 酣
- 阪
- 榕
- 骇
- 婧
- 陨
- 憎
- 沂
- 磷
- 壕
- 醺
- 惬
- 璀
- 璨
- 喋
- P
- 炽
- 瘁
- 羿
- 褐
- 簪
- 冽
- 驮
- 芮
- 辄
- 咆
- 渍
- 觐
- 炷
- 蛰
- 驷
- 帚
- 蜷
- O
- X
- 邂
- 逅
- 缭
- 秽
- 琰
- 龌
- 龊
- 俨
- 涟
- 噼
- 掇
- 哔
- 炬
- 佯
- 粱
- 霁
- 鱿
- 夭
- 擀
- 陇
- 瞥
- 壑
- 盹
- 馁
- 蚌
- 焖
- 蛟
- 囱
- 蚝
- 抿
- 脓
- 蒿
- 飓
- 渲
- 宸
- 酗
- 荻
- 缥
- 弑
- 偎
- 宕
- 耘
- 瞌
- 瘴
- 溉
- 涝
- 咿
- 垛
- 垦
- 缈
- 苞
- 惆
- 汛
- 鹑
- 町
- 抡
- 慵
- 浣
- 耙
- 砥
- 噱
- 孬
- 札
- 弼
- 酋
- 镳
- 萦
- 泾
- 挞
- 钾
- 讷
- 圃
- 舶
- 穹
- 戾
- 汴
- 锂
- 昀
- 镀
- 眺
- 捺
- 猕
- 阚
- 骋
- 悸
- 蜚
- 咩
- 讥
- 篆
- 鸠
- 哐
- 锚
- 幢
- 翱
- 螳
- 徇
- 踞
- 蔗
- 蔼
- 漉
- 衲
- N
- 漳
- 枭
- 漾
- 歆
- 烬
- 曳
- 岌
- 孚
- 戛
- 呲
- 箫
- 娓
- 桨
- 涓
- 獭
- 芃
- 摒
- 戍
- 踝
- 轱
- 沱
- 锢
- 堰
- 抨
- 昙
- 鹌
- 蔻
- 迸
- 泯
- 龈
- 痔
- 骛
- 淄
- 泵
- 烯
- 蔫
- F
- 胥
- 忱
- 纫
- 搪
- 茎
- 暨
- 泞
- 踵
- 璞
- 佗
- 荃
- 鬓
- 蚣
- 罔
- 臆
- 贻
- 橇
- 麓
- 槌
- 琥
- I
- 纥
- 薅
- 樵
- 苓
- 熨
- 钨
- 骞
- 诣
- 涤
- 踊
- 醛
- 碴
- 蹴
- 缤
- 赊
- 岖
- 戊
- 禺
- 坯
- 戟
- 楂
- 隅
- 酶
- 邃
- 蛀
- 皎
- 炯
- 垣
- 锹
- 镰
- 夙
- 甬
- 叵
- 茁
- 珞
- 妲
- 涸
- 兀
- 嘤
- 谙
- 噗
- 榔
- 稣
- 剽
- 奚
- 啕
- 袅
- 讧
- 钠
- 怄
- 晤
- 肛
- 氰
- 迥
- 唰
- 诩
- 籁
- 砒
- 谩
- 诟
- 斓
- 泷
- 幡
- 爻
- 痫
- 眈
- 漕
- 惘
- 挎
- 噶
- 喱
- 氯
- U
- 跆
- 嗤
- 锏
- 睽
- 缮
- 蟋
- 蠕
- 扪
- 狞
- 飒
- 吮
- 弋
- 奘
- 蟠
- 梆
- 拈
- 帧
- 蟀
- 胯
- 掳
- 蝈
- 帼
- 瞰
- 嵇
- 阉
- 篝
- 笆
- 亘
- L
- 喔
- 愕
- 谚
- 轶
- 岱
- 丕
- 婕
- 羌
- 毡
- 呻
- 鼾
- 蜥
- 偌
- 庵
- 敝
- 蛐
- 麝
- 鞘
- 拮
- 涣
- 葆
- 雹
- 踌
- 蜈
- 馥
- 跻
- 狰
- 桀
- 毗
- 皿
- 缨
- 磐
- 啾
- 牒
- 缰
- 躇
- 踮
- 糠
- 嗲
- 刽
- 咫
- 殇
- 瀛
- 胱
- 炀
- 虱
- 砾
- 獒
- 涎
- 袤
- 鄱
- 瓯
- 锭
- 塾
- 蹉
- 珏
- 豺
- 锌
- 蜿
- 牦
- 瓒
- 莆
- 蜴
- 氮
- 跎
- 咛
- 骜
- 郸
- 搐
- 堑
- 涞
- 寰
- 跛
- 鸵
- 毂
- 妩
- 铤
- 薏
- 烩
- 遐
- 煦
- 仃
- 髅
- 酮
- 榷
- 腋
- 珩
- 臃
- 愫
- 蜒
- 荼
- 侬
- 淬
- 婵
- 偻
- 焯
- 骊
- 恻
- 濮
- 泱
- 庖
- 惴
- 鲫
- 硌
- 肓
- 芪
- 礴
- 磺
- 腱
- 冢
- 谪
- 骷
- 哏
- 腩
- 蓦
- 焙
- 桢
- 阖
- 睾
- 疱
- 郴
- 铿
- 铡
- 祉
- 跄
- 桦
- 椭
- 拄
- 皙
- 膈
- 裱
- 髋
- 伢
- 罹
- 鳍
- 赝
- 嬴
- 痤
- 藿
- 镐
- 铎
- 瘠
- 簌
- 杳
- 铢
- 阡
- 忤
- 舀
- 悻
- 媲
- 茗
- 湍
- 舫
- 瘙
- 瞟
- 擞
- 荀
- 刍
- J
- 潍
- 莴
- 斛
- 郦
- 栩
- 绾
- 蕙
- 黜
- 湄
- 藓
- 躏
- 锱
- 捻
- 佼
- 砝
- E
- 罡
- 忻
- 鹜
- 滟
- 傥
- 蛳
- W
- 铀
- 魇
- 觎
- 蹂
- 佞
- 诃
- 灞
- 镣
- 痱
- 侏
- 峦
- 榛
- 饽
- 龋
- 嗔
- 芍
- 椿
- 璎
- 渥
- 蟾
- 骰
- 吠
- 挛
- 倜
- 鳝
- 糜
- 噢
- 黝
- 藐
- 绡
- 掣
- 鳗
- 璜
- 犷
- 痉
- 膺
- 罄
- 阄
- 纨
- 纭
- 彗
- 嵘
- 埠
- 潢
- 桔
- 耷
- 逵
- 诓
- 怵
- 蚤
- 苯
- 邈
- 谑
- 颌
- 珐
- 踱
- 髻
- 倏
- 啷
- 篑
- 冗
- 蹶
- 荥
- 涧
- 镂
- 踉
- 呷
- 衢
- 荟
- 箴
- 桧
- 恿
- 坳
- 瑙
- 珅
- 莅
- 膘
- 宥
- 氟
- 秆
- 诙
- 蹑
- 茴
- 翳
- 渚
- H
- 唁
- 诿
- 窈
- 窕
- 膻
- 荨
- 蛔
- 筵
- 钛
- 獾
- 琏
- 箩
- 栀
- 隼
- 煸
- 罂
- 蛎
- 咂
- 谗
- 颦
- 佝
- 苣
- 搡
- 仄
- 垠
- 濂
- 泗
- 亟
- 蔺
- 蛆
- 霏
- 榈
- 裟
- 瑁
- 酚
- 蝼
- 怆
- 犄
- 沣
- 揖
- 斡
- 刎
- 鲟
- 峒
- 瞭
- 晁
- 袈
- 蓟
- 镁
- 骥
- 掸
- 玳
- 娑
- 馀
- 跚
- 槃
- 缄
- 猢
- 粕
- 隍
- 佃
- 獗
- 唢
- 菏
- 酰
- 腚
- 笈
- 哙
- 孢
- 飕
- 嘹
- 茱
- 蹒
- 殓
- 柩
- 谀
- 姣
- 戌
- 柑
- 粼
- 淅
- 啧
- 盅
- 鼬
- 啜
- 绉
- 咻
- 锲
- 铆
- Y
- 螨
- 茯
- 憩
- 臼
- 谄
- 讴
- 濠
- 雎
- 噻
- 淦
- 懋
- 尕
- 氦
- 褛
- 颉
- 喆
- 铬
- 褴
- 燮
- 銮
- 侗
- 蹙
- 煜
- 邺
- 锃
- 麋
- 矗
- 娆
- 匐
- 噌
- 潸
- 碘
- 浔
- 檄
- 皈
- 铂
- 遨
- 炜
- 曜
- 饴
- 舷
- 胫
- 叟
- 祎
- 沅
- 潺
- 楣
- 埂
- 瞠
- 幔
- 稞
- 抻
- 匝
- 幄
- 殒
- 瑭
- 袂
- 囫
- 瓴
- 攫
- 鲈
- 箔
- 哝
- 馗
- 蜍
- 痧
- 脘
- 姘
- 苒
- 缢
- 觞
- 蛹
- 饬
- 胄
- 筏
- 鸾
- 儆
- 痿
- 矬
- 酊
- 纾
- 铖
- 荏
- 掬
- 膑
- 贮
- 觊
- 囵
- 泓
- 搔
- 汞
- 蚩
- 婀
- 谧
- 恣
- 霎
- 饕
- 赅
- 鲶
- 梏
- 獠
- 俶
- 龛
- 桅
- 鹄
- 旌
- 鲲
- 姒
- 蠡
- 繇
- 祜
- 诨
- 汩
- 觥
- 孀
- R
- 谥
- 蕨
- 祐
- 榭
- 皑
- 纂
- 獐
- 覃
- 痂
- 孑
- 砧
- 圩
- 桎
- 啵
- 葚
- 嗫
- 浃
- 荠
- 阈
- 遴
- 枇
- 狒
- 秸
- 筠
- 硒
- 卞
- 玷
- 杈
- 狲
- 忿
- 俎
- 拚
- 颍
- 睢
- 颧
- 滦
- 霭
- 雉
- 毽
- 蓑
- 歙
- 鳃
- 鹬
- 墉
- 楔
- 舐
- 绔
- 弭
- 馏
- 挝
- 奂
- 嘭
- 忪
- 箕
- 诌
- 谒
- 颚
- 滂
- 醍
- 洵
- 鹫
- 虢
- 苋
- 玥
- 臾
- 蹩
- Z
- 杷
- 痍
- 酉
- 疸
- 鄢
- 垩
- 烷
- 湮
- 钎
- 樽
- 旮
- 葭
- 邬
- 缱
- 糍
- 亳
- 咦
- 苷
- 伉
- 隽
- 伫
- 聒
- 匍
- 飚
- 桠
- 睑
- 脍
- 焘
- 谶
- 赳
- 萸
- 讣
- 疽
- 臧
- 巽
- 毓
- 鸢
- 纰
- 啐
- 噙
- 舛
- 敕
- 醐
- 痢
- 嚯
- 婺
- 勖
- 岷
- 溧
- 骅
- 犸
- 麾
- 嗟
- 诘
- 懑
- 貔
- 貅
- 啉
- 崂
- 鸩
- 镭
- 绻
- 逑
- 煨
- 褓
- 姝
- 藜
- 溟
- 儋
- 谡
- 欸
- 郢
- 荚
- 疝
- 遽
- 陂
- 饯
- 孪
- 巳
- 荞
- 泔
- 岿
- 谆
- 镍
- 洙
- 佻
- 盂
- 睨
- 铄
- 餮
- 酯
- 癣
- 浜
- 酩
- 焗
- 挲
- 鬃
- 鲠
- 仞
- 诰
- 谔
- 胛
- 萼
- 涿
- 莠
- 珲
- 旯
- 蜢
- 黍
- 肽
- 涪
- 髡
- 氙
- 陉
- 鬶
- 侩
- 糅
- 氤
- 芾
- 砷
- 鳕
- 钣
- 锒
- 闱
- 铵
- 镊
- 玑
- 砀
- 癜
- 颔
- 楹
- 螈
- 醚
- 琮
- 铩
- 笄
- 瓤
- 裨
- 潋
- 悌
- 聿
- 祢
- 郜
- 汨
- 棂
- 氲
- 嶙
- 聩
- 菅
- 腧
- 妯
- 龇
- 谲
- 耄
- 耋
- 囿
- 黢
- 揄
- 鲇
- 仝
- 個
- 忖
- 峋
- 揶
- 迩
- 诳
- 踽
- 骐
- 趸
- 颞
- 撺
- 辇
- 猷
- 铉
- 羸
- 徜
- 徉
- 襁
- 镌
- 孱
- 钒
- 铣
- 呤
- 遑
- 俾
- 皋
- 笕
- 笺
- 趔
- 趄
- 辋
- 鄞
- 殚
- 岫
- 跬
- 嘌
- 苻
- 绶
- 郅
- 瑄
- 萋
- 蘼
- 湎
- 砣
- 钜
- 捭
- 喹
- 恹
- 娌
- 螯
- 锰
- 祚
- 阆
- 矾
- 厩
- 龅
- 炝
- 黠
- 妁
- 濑
- 鞑
- 柒
- 滁
- 淖
- 鸬
- 鬣
- 晔
- 恸
- 赓
- 侉
- 溏
- 還
- 珮
- 鸨
- 嚅
- 笤
- 靥
- 啮
- 滓
- 俚
- 唳
- 苜
- 蓿
- 鹚
- 耦
- 莜
- 麸
- 粳
- 綦
- 盱
- 噤
- 遒
- 玟
- 魍
- 魉
- 旖
- 栉
- 锷
- 醴
- 泮
- 恁
- 甾
- 琬
- 丶
- 擤
- 桉
- 踟
- 誊
- 谟
- 澧
- 玖
- 畿
- 顼
- 兖
- 贰
- 茏
- 愎
- 豇
- 旎
- 蹰
- 蜃
- 屐
- 芡
- 鎏
- 癸
- 卅
- 枥
- 陟
- 琨
- 粝
- 掮
- 妪
- 姹
- 鏖
- 捯
- 钴
- 竽
- 恽
- 佰
- 胗
- 崧
- 磴
- 绺
- 鳏
- 槁
- 啖
- 矍
- 徕
- 忾
- 烃
- 喏
- 囹
- 圄
- 砭
- 邕
- 犍
- 鸮
- 剜
- 琚
- 瘢
- 魑
- 眦
- 锉
- 柘
- 痦
- 苕
- 牯
- 湟
- 厝
- 濛
- 赭
- 馐
- 蜇
- 嶂
- 贲
- 靼
- 臬
- 陲
- 潞
- 芩
- 腓
- 锨
- 寮
- 於
- 洇
- 愠
- 疖
- 鹧
- 鸪
- 茕
- 戕
- 壬
- 庾
- 莒
- 鹈
- 鹕
- 蠹
- 勐
- 疥
- 辎
- 耒
- 嗬
- 沔
- 睥
- 邙
- 篾
- 揩
- 肱
- 胍
- 磬
- 菟
- 豢
- 垓
- 唑
- 剌
- 阗
- 汜
- 佤
- 璟
- 麽
- 鬻
- 怏
- 蕤
- 茭
- 睚
- 淙
- 牍
- 榫
- 濯
- 稹
- 媾
- 悱
- 骶
- 蛭
- 鞣
- 椁
- 槊
- 擢
- 滢
- 佚
- 菡
- 沭
- 扦
- 镆
- 闾
- 缛
- 窠
- 疣
- 骠
- 俅
- 喙
- 蹼
- 硼
- 黩
- 腴
- 醮
- 邛
- 漯
- 豉
- 昶
- 刿
- 凇
- 鲅
- 舸
- 邳
- 俟
- 铰
- 翌
- 鳟
- 葳
- 寤
- 碣
- 秭
- 揠
- 熵
- 燧
- 靛
- 嵊
- 窨
- 鹗
- 芎
- 颢
- 佶
- 骢
- 圜
- 岘
- 燊
- 壅
- 畲
- 萘
- 煊
- 粲
- 倌
- 嗳
- 橹
- 椽
- 夔
- 鲑
- 赧
- 殄
- 沆
- 瀣
- 廪
- 舢
- 狍
- 挈
- 鹳
- 蚜
- 彧
- 羟
- 盥
- 镛
- 痈
- 蜊
- 皲
- 篦
- 喑
- 鲢
- 邡
- 蕲
- 僳
- 秣
- 蛉
- 讫
- 祗
- 鹩
- 撷
- 狎
- 郓
- 镕
- 榉
- 鲷
- 娣
- 淝
- 桷
- 镉
- 郫
- 髌
- 醪
- 僭
- 伧
- 嵬
- 苁
- 鹘
- 徭
- 歃
- 阕
- 鸱
- 貉
- 闳
- 坻
- 缙
- 媪
- 莨
- 菪
- 绦
- 恫
- 崆
- 喟
- 葺
- 逶
- 迤
- 骈
- 馔
- 苎
- 溘
- 垭
- 樯
- 诤
- 魃
- 搽
- 绀
- 蚴
- 澶
- 蒺
- 罘
- 眙
- 怍
- 來
- 荪
- 贶
- 亓
- 唻
- 畈
- 谌
- 芨
- 鲀
- 窸
- 窣
- 荜
- 楫
- 衮
- 趵
- 勰
- 髯
- 椴
- 缶
- 荸
- 秫
- 菖
- 甙
- 翦
- 椟
- 峤
- 掼
- 謇
- 洄
- 鄯
- 妗
- 浐
- 颀
- 箸
- 畦
- 痼
- 橛
- 鲛
- 蝾
- 愍
- 蒹
- 嘁
- 韪
- 劭
- 垅
- 暹
- 僮
- 稗
- 筚
- 煅
- 嬅
- 蜉
- 骝
- 碚
- 冼
- 吶
- 洹
- 郧
- 炴
- 绌
- 泠
- 呓
- 簋
- 溴
- 篁
- 仟
- 锟
- 羧
- 鹞
- 嘬
- 渌
- 笸
- 霰
- 稔
- 钡
- 齁
- 胪
- 衾
- 尻
- 洮
- 蘅
- 鲳
- 殂
- 腭
- 涔
- 蝣
- 孳
- 澍
- 钼
- 蒡
- 枳
- 渑
- 茼
- 馕
- 埙
- 珣
- 菘
- 邰
- 樾
- 铱
- 鳐
- 唔
- 篙
- 箜
- 篌
- 耆
- 啫
- 枞
- 杼
- 嵋
- 舂
- 娉
- 铨
- 崃
- 笳
- 邗
- 逡
- 僖
- 泫
- 疴
- 捱
- 醅
- 堇
- 肄
- 荇
- 虬
- 谯
- 酞
- 桡
- 艮
- 膦
- 艹
- 啻
- 滏
- 茆
- 圪
- 磡
- 麼
- 闼
- 郯
- 仡
- 氐
- 贽
- 俦
- 蓖
- 跹
- 帏
- 氅
- 趿
- 暝
- 缟
- 棹
- 滹
- 毖
- 蝰
- 虻
- 缫
- 诮
- 闩
- ○
- 潴
- 樨
- 瘘
- 襦
- 妤
- 郾
- 衿
- 鸷
- 旰
- 镢
- 傈
- 倨
- 笏
- 蒽
- 醌
- 驽
- 浠
- 涠
- 蓁
- 柞
- 钺
- 蜮
- 诂
- 徵
- 锆
- 椋
- 叻
- 廿
- 藁
- 乜
- 摈
- 這
- 茌
- 辊
- 岬
- 郇
- 杓
- 轳
- 酎
- 蟥
- 時
- 镒
- 蚬
- 澹
- 赟
- 後
- 怿
- 箐
- 囍
- 揆
- 蹁
- 鬄
- 苫
- 蕖
- 卺
- 辔
- 偈
- 俳
- 吲
- 哚
- 瘆
- 蕞
- 笞
- 氩
- 嫘
- 墁
- 帔
- 褡
- 裢
- 乩
- 褊
- 颏
- 喒
- 錾
- 皌
- 戗
- 唪
- 啭
- 伥
- 茔
- 斫
- 齉
- 仵
- 赉
- 吡
- 啶
- 蹇
- 螅
- 汊
- 湓
- 凫
- 珙
- 腈
- 洌
- Ω
- 憷
- 跶
- 抔
- 濞
- 崤
- 殍
- 浥
- 铳
- 酽
- 馑
- 髂
- 隗
- 韫
- 晷
- 诒
- 埭
- 鹪
- 蕻
- 昃
- 瓠
- 萁
- 癔
- 怩
- 疳
- 跖
- 疔
- 簟
- 汆
- 疠
- 卟
- 墒
- 穰
- 铍
- 珥
- 钤
- 隻
- 樓
- 墎
- 鳜
- 沒
- 岀
- 杪
- 単
- 鲧
- 呋
- 彀
- 祇
- 豸
- 胴
- 唷
- 丨
- 燚
- 麴
- 觇
- 缑
- 橐
- 蚡
- 朊
- 俣
- 垡
- <sos/eos>
init: null
input_size: null
ctc_conf:
    ignore_nan_grad: true
model_conf:
    ctc_weight: 0.3
    lsm_weight: 0.1
    length_normalized_loss: false
use_preprocessor: true
use_preprocessor_valid: false
token_type: char
bpemodel: null
non_linguistic_symbols: null
cleaner: null
g2p: null
speech_volume_normalize: null
rir_scp: null
rir_utt_prefix: null
rir_apply_prob: 1.0
noise_scp: null
noise_utt_prefix: null
noise_apply_prob: 1.0
noise_db_range: '13_15'
frontend: default
frontend_conf:
    fs: 16k
specaug: specaug
specaug_conf:
    apply_time_warp: true
    time_warp_window: 5
    time_warp_mode: bicubic
    apply_freq_mask: true
    freq_mask_width_range:
    - 0
    - 30
    num_freq_mask: 2
    apply_time_mask: true
    time_mask_width_range:
    - 0
    - 40
    num_time_mask: 2
normalize: global_mvn
normalize_conf:
    stats_file: exp/asr_stats_raw_zh_char/train/feats_stats.npz
preencoder: null
preencoder_conf: {}
encoder: conformer
encoder_conf:
    output_size: 512
    attention_heads: 8
    linear_units: 2048
    num_blocks: 12
    dropout_rate: 0.1
    positional_dropout_rate: 0.1
    attention_dropout_rate: 0.0
    input_layer: conv2d
    normalize_before: true
    rel_pos_type: latest
    pos_enc_layer_type: rel_pos
    selfattention_layer_type: rel_selfattn
    activation_type: swish
    macaron_style: true
    use_cnn_module: true
    cnn_module_kernel: 15
postencoder: null
postencoder_conf: {}
decoder: transformer
decoder_conf:
    attention_heads: 8
    linear_units: 2048
    num_blocks: 6
    dropout_rate: 0.1
    positional_dropout_rate: 0.1
    self_attention_dropout_rate: 0.0
    src_attention_dropout_rate: 0.0
required:
- output_dir
- token_list
version: 0.10.2a1
distributed: true
```

</details>

## LM config

<details><summary>expand</summary>

```
NONE
```

</details>
