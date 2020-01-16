## README
项目使用python语言，是基于unittest框架实现的，框架的文档：https://git2.qingtingfm.com/TEST/appium/wikis/python-unittest

依赖

- appium：（ 文档：https://git2.qingtingfm.com/TEST/appium/wikis/Appium-setup-environment ）
- jenkins：（ 文档：https://git2.qingtingfm.com/TEST/appium/wikis/CI-AutoTest ）

各平台自动化测试脚本

- android
- iOS

部署流程
- 1.启动Tomcat -- sudo Tomcat start
- 2.启动Jenkins -- 访问localhost:8080/jenkins
- 3.启动Appium -- appium
- 4.启动ssh远程端口转发 -- ssh -N -R 8124:localhost:8080 root@118.178.135.107