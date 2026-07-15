# 项目名称
Langchain项目结合Rag,tools,logging制作的客服Agent

## 🚀 快速开始

请按照以下步骤在本地运行本项目：

### 1. 克隆项目

将仓库克隆到本地计算机：

```bash
git clone <你的仓库地址>
cd <项目文件夹名称>
```

### 2. 安装依赖

建议使用虚拟环境，然后安装所需的 Python 依赖包：

```bash
pip install -r requirements.txt
```

### 3. 启动应用

在项目根目录下打开终端，运行以下命令启动 Streamlit 应用：

```bash
streamlit run app.py
```

启动后，浏览器通常会自动打开 `http://localhost:8501`。如未自动打开，请手动访问该地址。


## ⚠️ 注意事项

- 确保已安装 Python 3.x 版本
- 如遇端口冲突，可使用 `streamlit run app.py --server.port 8502` 指定其他端口
- **DEEPSEEK_API_KEY**: 运行此项目前请先在环境变量中设置DEEPSEEK_API_KEY即deepseek-key
- **DASHSCOPE_API_KEY**：运行此像目前请先在环境变量中设置DASHSCOPE_API_KEY即阿里云key
