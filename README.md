# 🎸 STARRY · 下北泽异常事件簿

一个《孤独摇滚！》主题的非官方互动音乐小站：听歌、看演出、翻日历相册、抽卡，以及与结束乐队的四位成员展开原创同人故事。

[在线体验](https://ai-joye.com/starry/) · [素材来源](dist/CREDITS.md) · [第三方权利说明](THIRD_PARTY_NOTICES.md)

## 功能

- 四位角色、12 章原创同人剧情，分支回应、自动存档和回忆回看。
- 13 首歌曲、同步歌词、收藏、随机/循环播放；支持导入本地音频和 LRC。
- 13 部哔哩哔哩视频，分为动画现场和 MV / OP / ED，支持站内播放及原站链接。
- 27 张收藏卡、单抽/十连、30 抽 SSR 保底；不涉及付费。
- 28 张官方剧照组成翻页日历相册，支持自动轮播、暂停及查看原图。
- 小赖手写字体、多色纸张风格、手机竖屏适配。
- 存档仅在当前浏览器，可在设置中导出和导入；导入的音视频刷新后需要重新选择。

## 本地运行

需要 Python 3，无需 npm 安装或前端构建工具。

```sh
git clone https://github.com/3299205366-stack/bocchi-starry.git
cd bocchi-starry
python3 serve.py
```

打开 http://localhost:5178/ 。macOS 也可运行 `开始游戏.command`。开发服务器只监听本机，支持音频 Range 请求，不用于公网生产服务。

## 目录与验证

- `dist/`：直接可运行的 HTML、CSS、JavaScript 与素材。
- `serve.py`：本地预览服务器。
- `deploy/build.py`：按白名单输出到 `build/`。
- `qa/`：抽卡和歌词解析检查。

```sh
node qa/gacha-test.cjs
node qa/lyrics-test.cjs
python3 deploy/build.py
```

把 `build/` 交给支持 HTTPS 的静态托管服务即可。路径均为相对路径，可部署到子目录。建议开启文件缓存、音频 Range 支持，并允许 `https://player.bilibili.com` iframe。不要把开发目录或私钥上传到站点；本仓库不包含生产服务器登录信息和运维脚本。

## 许可

原创代码与文档采用 [MIT](LICENSE)。第三方音乐、歌词、插图、角色及 Logo **不属于 MIT 授权范围**，字体另按 OFL 许可。素材的公开再分发授权尚未确认，详见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)；重新发布前请取得相应许可或替换素材。
