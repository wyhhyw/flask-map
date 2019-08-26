from flask import Flask
from config import Config

app = Flask(__name__)
# 通过配置文件读取并应用配置
app.config.from_object(Config)
