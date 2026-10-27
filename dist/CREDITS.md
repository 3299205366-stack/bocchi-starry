# STARRY · 素材与设计参考

本地个人同人游戏；原创故事、卡名和界面代码。没有使用 AI 生图。

## 官方图片
- 动画官网：https://bocchi.rocks/tv/
- 直接下载第 1、4、8、12 话公开故事页图片共 13 张。逐张来源见 assets/art/official/sources.json；第 12 话标题图未作为人物卡使用。
- 四位官方立绘、既有官方剧照与 PV 缩略图：来自 https://github.com/mintonight/girls-band-anime 的已标注官方来源资源。用于角色路线、首页、收藏卡。
- 动画原作与角色版权归原权利人；公开可访问不等于获得再分发许可。此目录供本机个人体验，未公开部署。

## 音频与视频
- 13 首本地 MP3、专辑封面来自用户指定 https://github.com/sudoriaa/BOCCHI-THE-ROCK 。不将仓库代码许可视为音乐授权。
- winter.mp4 来自同一仓库，实际是 30 秒和服同人插画动态视频，非动画演奏原片；在放映室明确标注。
- 官方动画演奏使用 YouTube 嵌入：p010N38zFrA、fJh5UeiULZs、f4i6Pi2KQh0、5tc14WHUoMw。平台网络、登录和嵌入限制仍可能影响播放。
- 尝试下载官方演奏时被平台要求登录验证，未取得原片本地文件。未读取浏览器登录凭据。
- 同步歌词支持 LRC 导入、逐句高亮、点击跳转与偏移校准；尚未内置完整歌词。已检查本地 MP3 无歌词标签；其他 FLAC 请求失败，未冒充已经检查其内容。

## 设计研究
- sudoriaa/BOCCHI-THE-ROCK：角色展示、歌曲/视频组织、B 站入口。
- jiang068/Nijika_Page：角色切换淡入与上移动效、灰度悬停和画廊组织。
- Bamzzo/Bamzzo.github.io：读取页面作参考，未直接使用其不明来源素材。
- ZHYxulei/Lonely-Rock：查看仓库文件树；完整克隆失败，未声称完整审阅其实现。
- mintonight/girls-band-anime：角色翻卡、舞台意象、滚动叙事和官方素材组织。

未复制参考站的完整产品；新增独立的 12 章选择剧情、音乐播放器、回忆系统、免费抽卡与手机布局。

## 高清主视觉与浅色主题更新
官网 CSS https://bocchi.rocks/tv/assets/css/page/top.css 引用的 ph_all_1.jpg、ph_hitori_1.jpg、ph_nijika_1.jpg、ph_ryo_1.jpg、ph_ikuyo_1.jpg 已下载到 assets/art/official/，原始分辨率均为 1220 × 1500。原始地址前缀：https://bocchi.rocks/tv/assets/img/page/top/mainvisual/slides/ 。未插值放大。
用户提供配色：#FCD4D4、#FCFCD4、#D4FCFC、#E8D4FC、#D4E8FC、#D4FCE8、#FCE8D4。

## 2026-10-26 当前媒体方案（替代上文早期方案）
- 已移除 YouTube 播放器。四段视频仅跳转 B 站，支持目标网站的弹幕：BV1j8411g7dt（吉他与孤独与蓝色星球）、BV1L24y1S7bH（若能化作星座）、BV13x4y1u7nG（不会忘记）、BV1F24y1y7By（那个乐队）。通过 B 站公开 view 接口逐条核对标题，均 code=0。实际站外播放仍取决于 B 站。
- 已内置 13 首同步歌词（约 49 KB），来源网易云音乐公开歌词接口。逐首按歌名、歌手、音频时长匹配；本地音频和源歌曲时长差均小于 0.1 秒。来源及歌曲 ID 见 assets/lyrics-sources.json。不是自动语音识别，未人工逐句校对全部时轴；播放器保留偏移校准。歌词和音乐著作权归原权利人，本地使用未对外发布。

## 2026-10-27 更新
- 新增 28 张官网剧照，逐张来源见 assets/art/official/sources-extra.json。听歌相册使用这些图片，卡池扩为 27 张。
- 卡背 Logo：https://bocchi.rocks/kessokuband/assets/img/common/header/logo_kessoku.svg 。
- 放映室共 13 部，分动画现场 4 部与完整 MV/OP/ED 9 部。选择参考仓库的链接并对照公开 API 播放量；数量为选取时快照，不保证始终为全站最高。B 站内嵌播放器可观看与显示弹幕，发送弹幕与更高清画质可前往原页。
- 和服视频已从产品及发布包移除。
- 声浪为音乐音量驱动的平滑装饰曲线，不是逐采样波形或心率测量。

## 网站字体
小赖字体 Xiaolai Regular v3.126，来源 https://github.com/lxgw/kose-font ，SIL Open Font License 1.1，原版字形转换为 WOFF2 后本地托管，授权文件见 assets/fonts/OFL.txt。
