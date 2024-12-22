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