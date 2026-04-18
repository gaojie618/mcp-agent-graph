import platform
import os
from pathlib import Path
from dotenv import load_dotenv

project_root = Path(__file__).parent.parent.parent.parent
agent_graph_services_env_path = project_root / "docker" / "agent_graph_services" / ".env"

if agent_graph_services_env_path.exists():
    load_dotenv(agent_graph_services_env_path)
else:
    # 如果找不到，尝试从当前工作目录加载
    cwd_env_path = Path.cwd() / "docker" / "agent_graph_services" / ".env"
    if cwd_env_path.exists():
        load_dotenv(cwd_env_path)

class Settings:
    """应用配置设置"""

    # 应用版本和名称
    APP_NAME: str = "Agent-Graph"
    APP_VERSION: str = "3.0.0"

    MONGODB_URL: str = os.getenv(
        "MONGODB_URL",
        f"mongodb://{os.getenv('MONGO_ROOT_USERNAME', 'admin')}:"
        f"{os.getenv('MONGO_ROOT_PASSWORD', 'securepassword123')}@"
        f"localhost:{os.getenv('MONGO_PORT', '27017')}/"
    )

    MONGODB_DB: str = os.getenv("MONGO_DATABASE", "agent-graph")

    # JWT 配置
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "your-secret-key-change-in-production")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", "15"))  # 15分钟
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRE_DAYS", "7"))  # 7天

    # 超级管理员配置
    ADMIN_USERNAME: str = os.getenv("ADMIN_USERNAME", "admin")
    ADMIN_PASSWORD: str = os.getenv("ADMIN_PASSWORD", "admin123")

    # MinIO 配置
    MINIO_ENDPOINT: str = os.getenv("MINIO_ENDPOINT", f"localhost:{os.getenv('MINIO_API_PORT', '9010')}")
    MINIO_ACCESS_KEY: str = os.getenv("MINIO_ROOT_USER", "minioadmin")
    MINIO_SECRET_KEY: str = os.getenv("MINIO_ROOT_PASSWORD", "minioadmin123")
    MINIO_SECURE: bool = os.getenv("MINIO_SECURE", "false").lower() == "true"
    MINIO_BUCKET_NAME: str = os.getenv("MINIO_BUCKET_NAME", "agent-graph")

    # 根据操作系统确定配置目录
    @property
    def AGENT_GRAPH_DIR(self) -> Path:
        """获取 Agent-Graph 配置目录"""

        # 默认行为
        system = platform.system()
        home = Path.home()

        if system == "Windows":
            return home / ".agent_graph"
        elif system == "Darwin":  # macOS
            return home / ".agent_graph"
        elif system == "Linux":
            return home / ".agent_graph"
        else:
            return home / ".agent_graph"

    @property
    def EXPORTS_DIR(self) -> Path:
        """获取导出文件存储目录"""
        return self.AGENT_GRAPH_DIR / "exports"

    @property
    def MCP_TOOLS_DIR(self) -> Path:
        """获取AI生成的MCP工具存储目录"""
        return self.AGENT_GRAPH_DIR / "mcp"

    def ensure_directories(self) -> None:
        """确保所有必要的目录存在"""
        self.AGENT_GRAPH_DIR.mkdir(exist_ok=True)
        self.EXPORTS_DIR.mkdir(exist_ok=True)
        self.MCP_TOOLS_DIR.mkdir(exist_ok=True)

    def get_mcp_tool_dir(self, tool_name: str) -> Path:
        """获取指定MCP工具的目录路径"""
        return self.MCP_TOOLS_DIR / tool_name

# 创建全局设置实例
settings = Settings()