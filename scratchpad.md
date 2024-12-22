# Lessons

- For website image paths, always use the correct relative path (e.g., 'images/filename.png') and ensure the images directory exists
- For search results, ensure proper handling of different character encodings (UTF-8) for international queries
- Add debug information to stderr while keeping the main output clean in stdout for better pipeline integration
- When using seaborn styles in matplotlib, use 'seaborn-v0_8' instead of 'seaborn' as the style name due to recent seaborn version changes
- When using Jest, a test suite can fail even if all individual tests pass, typically due to issues in suite-level setup code or lifecycle hooks
- 默认LLM模型已更新为gpt-4o
- 添加了调试信息以显示正在使用的模型名称

# Scratchpad

# Current Task: 项目全面检查和更新

## 任务说明
检查整个项目的所有文件，确保配置正确，特别是关于API密钥和Docker配置的部分。

## 检查清单
1. Python文件
   [ ] 检查所有Python文件中的API密钥使用
   [ ] 确保所有文件使用环境变量
   [ ] 检查错误处理机制

2. 配置文件
   [ ] 检查 .env.example
   [ ] 验证 .gitignore
   [ ] 检查 docker-compose.yml
   [ ] 检查 Dockerfile 和 Dockerfile.scraper

3. 文档
   [ ] 更新 README.md
   [ ] 检查安装说明
   [ ] 确保配置说明完整
   [ ] 添加故障排除指南

4. 测试文件
   [ ] 检查测试用例
   [ ] 确保测试环境配置正确

## 进展
- Python文件检查完成：
  [X] 检查所有Python文件中的API密钥使用
  [X] 确保所有文件使用环境变量
  [X] 检查错误处理机制

- 配置文件更新完成：
  [X] 检查 .env.example
  [X] 验证 .gitignore
  [X] 检查 docker-compose.yml
  [X] 检查 Dockerfile 和 Dockerfile.scraper

- 文档更新完成：
  [X] 更新 README.md
  [X] 检查安装说明
  [X] 确保配置说明完整
  [X] 添加故障排除指南

- 测试文件检查完成：
  [X] 检查测试用例
  [X] 确保测试环境配置正确

## 完成的改进
1. 移除了web_scraper.py中的硬编码路径
2. 更新了docker-compose.yml，移除了废弃的version字段
3. 添加了详细的故障排除指南到README.md
4. 确保所有文件使用环境变量而不是硬编码值
5. 改进了错误处理和用户提示

## 下一步建议
1. 考虑添加自动化测试流程
2. 实现API密钥轮换机制
3. 添加监控和日志聚合
4. 考虑添加CI/CD配置

# Testing Plan (2024-12-22)

## Components to Test
- [ ] LLM API
- [ ] Web Scraper
- [ ] Search Engine
- [ ] Docker Environment

## Test Cases

### 1. LLM API Test
- [ ] Test basic prompt
- [ ] Test error handling

### 2. Web Scraper Test
- [ ] Test single URL scraping
- [ ] Test multiple URL scraping
- [ ] Test error handling for invalid URLs

### 3. Search Engine Test
- [ ] Test basic search
- [ ] Test search result parsing

### 4. Docker Environment Test
- [ ] Test container communication
- [ ] Test volume mounting
- [ ] Test network connectivity

## Progress Log

Starting tests at 2024-12-22 14:38...

### LLM API Test Results
- Basic prompt test successful
- Model: gpt-4o
- Response received correctly
- Error handling test pending

### Web Scraper Test Results
- Single URL scraping successful
- Processing time: ~1.5s
- Proper error logging
- Multiple URL test pending

### Search Engine Test Results
- Basic search successful
- Returns 10 results with URLs, titles, and snippets
- Warning: lxml not installed, using API backend
- Search result parsing working correctly

### Docker Environment Test Results
- Container communication successful
  - Containers can resolve each other by service name
  - Network latency < 1ms
- Volume mounting working correctly
  - Files created in one container visible in others
  - Proper file permissions maintained
- Network connectivity working
  - External URLs accessible
  - DNS resolution working

## Test Summary
All core functionality is working as expected. Some minor improvements could be made:
1. Install lxml in dev container for better search engine performance
2. Add error handling tests for LLM API
3. Test multiple URL scraping
4. Add monitoring and logging aggregation
5. Consider adding CI/CD configuration

# Dev Container 配置问题排查

## 当前问题
- VS Code Dev Container 无法连接，报错 "Failed to read devcontainer configuration"
- 容器列表中找不到开发容器

## 排查步骤
[X] 1. 检查容器运行状态 - 已确认容器未运行
[X] 2. 验证 docker-compose 配置 - 已添加专门的dev服务
[X] 3. 确认环境变量设置 - 配置正确
[X] 4. 测试容器构建和启动 - 容器已成功启动
[X] 5. 验证用户权限问题 - 发现需要调整容器用户配置

## 发现的问题
容器启动时使用了 appuser 用户，但可能没有正确设置权限。需要：
1. 确保 appuser 用户有正确的 UID/GID
2. 确保工作目录权限正确
3. 添加必要的系统工具

## 解决方案
修改 Dockerfile 添加更多必要的系统工具和正确的权限设置：

## Lessons Learned
- Dev Container 配置需要确保 service 名称与 docker-compose.yml 中的服务名称完全匹配
- 开发容器需要配置 tty: true 来保持容器运行
- 使用 docker-compose up -d dev 命令可以单独启动开发容器
- 容器启动后要使用 docker-compose ps 确认状态
- 开发容器需要安装必要的系统工具并正确设置用户权限