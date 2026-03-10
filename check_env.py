# check_env.py  环境验证脚本
import torch

if __name__ == "__main__":
    # 打印PyTorch版本
    print("PyTorch 版本:", torch.__version__)
    # 打印CUDA是否可用
    print("CUDA 可用:", torch.cuda.is_available())
    # 创建随机张量测试
    x = torch.rand(2, 3)
    print("随机张量:\n", x)