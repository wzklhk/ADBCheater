# QutoutiaoCheater
Read Qutoutiao text automatically
# Just for fun

使用ADB辅助和python脚本程序自动阅读趣头条的新闻

## 原理
1. 将手机打开到趣头条界面
2. 用 ADB 工具点击屏幕和滑动屏幕
  $ adb shell input swipe x1 y1 x2 y2
  $ adb shell input tap x y

## 使用
1. 正确配置ADB到系统环境变量
2. 运行将程序SCREEN_WIDTH和SCREEN_LENGTH改为要使用手机的分辨率
3. 运行QutoutiaoCheat.py程序
