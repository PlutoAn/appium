## README

### iOS自动测试简要说明

### 依赖
- appium iOS 环境

### 结构说明
- iOS_suite.py是整个自动化测试入口，修改配置后直接运行python iOS_suite.py
- package为安装包目录
- 其他目录为各模块文件

### 文件命名规则
- 文件夹为模块名字，比如download
- 文件名为平台_模块_测试用例文件名字，比如i_download_autocases，
- 类命名要以平台_类名，比如i_DownloadAutocaseTests
- testcase命名需与测试用例序列号一一对应，比如下载-001，对应i_download_autocases中的test\_001