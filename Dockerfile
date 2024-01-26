# 用于创建 Docker 容器的脚本，可以将你的应用及其依赖打包，以便在任何支持 Docker 的环境中运行。
# 使用官方 Python 运行时作为父镜像
FROM python:3.8

# 将工作目录设置为 /app
WORKDIR /app

# 将当前目录内容复制到位于 /app 的容器中
COPY . /app

# 安装 requirements.txt 中的所有依赖
RUN pip install --no-cache-dir -r requirements.txt

# 使端口 80 可供此容器外的环境使用
EXPOSE 80

# 定义环境变量
# ENV NAME World

# 在容器启动时运行 app.py
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
