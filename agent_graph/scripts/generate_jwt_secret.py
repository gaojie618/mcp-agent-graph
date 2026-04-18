#!/usr/bin/env python3
"""
JWT密钥生成工具
用于生成安全的JWT密钥
"""
import secrets

def generate_jwt_secret(length: int = 64) -> str:
    """
    生成安全的JWT密钥
    
    Args:
        length: 密钥字节长度（默认64字节，生成约88字符的Base64字符串）
    
    Returns:
        安全的随机密钥字符串
    """
    return secrets.token_urlsafe(length)

if __name__ == "__main__":
    secret = generate_jwt_secret()
    print("=" * 60)
    print("🔑 JWT密钥生成成功！")
    print("=" * 60)
    print(f"\n{secret}\n")
    print("=" * 60)
    print("📝 使用方法:")
    print("1. 复制上面的密钥")
    print("2. 在 docker/agent_graph_services/.env 文件中设置:")
    print(f"   JWT_SECRET_KEY={secret}")
    print("3. 启动服务")
    print("=" * 60)