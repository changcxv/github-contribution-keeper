import os
import random
import subprocess
from datetime import datetime

# 配置
REPO_PATH = "/home/ubuntu/github-contribution-keeper"
LOG_FILE = os.path.join(REPO_PATH, "contribution_log.txt")

def make_commit():
    os.chdir(REPO_PATH)
    
    # 随机生成一些内容并追加到日志文件
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_val = random.randint(1000, 9999)
    with open(LOG_FILE, "a") as f:
        f.write(f"Contribution update at {current_time} - ID: {random_val}\n")
    
    # Git 提交操作
    try:
        subprocess.run(["git", "add", "contribution_log.txt"], check=True)
        commit_message = f"chore: daily contribution update {current_time}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print(f"Successfully pushed commit at {current_time}")
    except subprocess.CalledProcessError as e:
        print(f"Error during git operation: {e}")

if __name__ == "__main__":
    make_commit()
