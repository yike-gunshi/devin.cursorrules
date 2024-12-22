# Devin.cursorrules

Transform your $20 Cursor/Windsurf into a Devin-like experience in one minute! This repository contains configuration files and tools that enhance your Cursor or Windsurf IDE with advanced agentic AI capabilities similar to Devin, including:

- Process planning and self-evolution
- Extended tool usage (web browsing, search, LLM-powered analysis)
- Automated execution (for Windsurf in Docker containers)

## Usage

1. Copy all files from this repository to your project folder
2. For Cursor users: The `.cursorrules` file will be automatically loaded
3. For Windsurf users: Use both `.windsurfrules` and `scratchpad.md` for similar functionality

## Setup

1. Create Python virtual environment:
```bash
# Create a virtual environment in ./py310
python3 -m venv py310

# Activate the virtual environment
# On Unix/macOS:
source py310/bin/activate
# On Windows:
.\py310\Scripts\activate
```

2. Install dependencies:
```bash
# Install required packages
pip install -r requirements.txt

# Install Playwright's Chromium browser (required for web scraping)
python -m playwright install chromium
```

## 环境变量配置

为了保护敏感信息（如API密钥），我们使用环境变量来管理配置：

1. **创建环境配置文件**：
   ```bash
   # 复制环境变量示例文件
   cp .env.example .env
   ```

2. **配置API密钥**：
   - 编辑`.env`文件
   - 将`your-api-key-here`替换为你的实际OpenAI API密钥
   - 确保`.env`文件已添加到`.gitignore`中（避免意外提交）

3. **环境变量说明**：
   - `OPENAI_API_KEY`：OpenAI API密钥（必需）
   - `PYTHONPATH`：Python路径配置
   - `PYTHONUNBUFFERED`：Python输出缓冲设置

4. **使用Docker时的环境变量**：
   ```bash
   # 方法1：使用已配置的.env文件
   docker-compose up

   # 方法2：直接在命令行设置（不推荐用于生产环境）
   OPENAI_API_KEY=your-api-key-here docker-compose up

   # 方法3：在CI/CD环境中使用加密的环境变量
   ```

5. **安全注意事项**：
   - 永远不要将API密钥提交到版本控制系统
   - 在生产环境使用环境变量或密钥管理系统
   - 定期轮换API密钥
   - 使用最小权限原则配置API密钥

## Docker部署

1. 配置环境变量：
```bash
# 复制环境变量示例文件
cp .env.example .env

# 编辑.env文件，设置你的OpenAI API密钥
# OPENAI_API_KEY=your_api_key_here
```

2. 使用Docker Compose启动服务：
```bash
# 构建并启动服务
docker-compose up --build

# 在后台运行
docker-compose up -d --build
```

3. 停止服务：
```bash
docker-compose down
```

## 服务说明

- 默认使用gpt-4o模型
- 支持中英文输入
- 预留了8000端口用于未来HTTP服务扩展
- 代码更改会通过volume实时同步到容器中

## Tools Included

- Web scraping with JavaScript support (using Playwright)
- Search engine integration (DuckDuckGo)
- LLM-powered text analysis
- Process planning and self-reflection capabilities

## Testing

The project includes comprehensive unit tests for all tools. To run the tests:

```bash
# Make sure you're in the virtual environment
source py310/bin/activate  # On Windows: .\py310\Scripts\activate

# Run all tests
PYTHONPATH=. python -m unittest discover tests/
```

The test suite includes:
- Search engine tests (DuckDuckGo integration)
- Web scraper tests (Playwright-based scraping)
- LLM API tests (OpenAI integration)

## 故障排除

### 常见问题

1. **API密钥相关问题**
   - 错误：`OPENAI_API_KEY environment variable is not set`
     - 解决：确保已经正确设置了环境变量
     - 检查`.env`文件是否存在并包含有效的API密钥
     - 确保Docker运行时可以访问到环境变量

2. **Docker相关问题**
   - 错误：`Error response from daemon: driver failed programming external connectivity`
     - 解决：检查端口是否被占用
     - 尝试停止其他Docker容器或更改端口映射
   
   - 错误：`no space left on device`
     - 解决：清理未使用的Docker镜像和容器
     ```bash
     docker system prune -a
     ```

3. **Python依赖问题**
   - 错误：`ModuleNotFoundError`
     - 解决：确保所有依赖都已安装
     ```bash
     pip install -r requirements.txt
     ```
   
   - 错误：`playwright not found`
     - 解决：安装Playwright浏览器
     ```bash
     python -m playwright install chromium
     ```

4. **权限问题**
   - 错误：`Permission denied`
     - 解决：检查文件权限
     - 确保当前用户有足够的权限
     - Docker中使用正确的用户权限

### 调试技巧

1. **查看容器日志**
   ```bash
   # 查看特定服务的日志
   docker-compose logs base
   docker-compose logs scraper
   
   # 实时查看日志
   docker-compose logs -f
   ```

2. **检查环境变量**
   ```bash
   # 检查环境变量是否正确设置
   docker-compose exec base env | grep OPENAI
   ```

3. **进入容器调试**
   ```bash
   # 进入运行中的容器
   docker-compose exec base bash
   ```

4. **测试API连接**
   ```bash
   # 测试LLM API
   docker-compose run base python -m tools.llm_api --prompt "test"
   ```

### 性能优化

1. **Docker优化**
   - 使用多阶段构建减小镜像大小
   - 合理使用缓存层
   - 及时清理未使用的镜像和容器

2. **Python优化**
   - 使用异步操作处理并发请求
   - 合理设置超时时间
   - 实现请求重试机制

## Background

For detailed information about the motivation and technical details behind this project, check out the blog post: [Turning $20 into $500 - Transforming Cursor into Devin in One Hour](https://yage.ai/cursor-to-devin-en.html)

## License

MIT License
