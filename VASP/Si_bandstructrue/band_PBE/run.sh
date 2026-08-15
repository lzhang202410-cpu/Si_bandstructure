#!/bin/bash                         #声明语言
#SBATCH -J vasp_Si_band             #作业名字  -job-name
#SBATCH -p comput                   #节点名称  partition 
#sinfo -lN                          #查看节点个数
#SBATCH -N 1                        #节点数量
#SBATCH -n 2                        #总核数
#SBATCH -o out.%j                   #输出日志
#SBATCH -e err.%j                   #报错日志


#########    加载环境    ########
export PATH="/home/zl/.local/bin:$PATH"
export PATH="/home/zl/文档/vaspkit.1.3.5.linux.x64/vaspkit.1.3.5/bin:$PATH"

# 进入脚本所在目录（无论从哪里调用都能正确定位,$0 is current directory)
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
cd "$SCRIPT_DIR"

##### 运行指令 mpirun vasp_std #####
mpirun -np 4 /opt/bin/vasp_std > out.log 2> err.log

