"""
Si 能带结构可视化
读取 VASPKIT 生成的 BAND.dat 和 KLABELS 文件
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'mathtext.fontset': 'stix',       # Times New Roman 风格数学字体
    'font.family':      'STIXGeneral', # 正文也用 STIX
})

# ── 读取数据 ──────────────────────────────────────────────────────────────────

data = np.loadtxt("REFORMATTED_BAND.dat", comments="#")
kpts = data[:, 0]#k点坐标
bands = [data[:, i] for i in range(1, data.shape[1])]#能带位置 data.shape[1]获取数组，data.shape[0]获取数组的行数
# ── 读取高对称点标签 ──────────────────────────────────────────────────────────

labels, positions = [], []
with open("KLABELS") as f:#读取LABELS文件
    for line in f:
        parts = line.split()#切分字符串的神器。它默认把一行文字按照“空格”切开，变成一个列表
        if len(parts) == 2:#只有当刚才切出来的列表长度恰好为 2 时才处理。
            try:
                label = parts[0].replace("GAMMA", r"$\Gamma$")
                positions.append(float(parts[1]))#
                labels.append(label)#
            except ValueError:
                pass

# ── 读取竖线位置（断点） ──────────────────────────────────────────────────────

vlines = np.unique(np.loadtxt("KLINES.dat")[:, 0])#KLINES.dat文件np.unique()函数，返回所有不重复元素的排序数组

# ── 绘图 ──────────────────────────────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(6, 5))

for band in bands:
    ax.plot(kpts, band, color="#2B6CB0", linewidth=1.2)

ax.axhline(0, color="gray", linewidth=0.8, linestyle="--", label="Fermi level")

for x in vlines:
    ax.axvline(x, color="black", linewidth=0.8)

ax.set_xticks(positions)
ax.set_xticklabels(labels, fontsize=12)
ax.set_xlim(kpts[0], kpts[-1])  # 恢复正向 X 轴 (Gamma -> X -> W -> L -> Gamma -> K -> X)
ax.set_ylim(-13, 10)
ax.set_ylabel("Energy (eV)", fontsize=12)
ax.set_title("Si Band Structure (PBE)", fontsize=13)

plt.tight_layout()
plt.savefig("band_structure.png", dpi=300)
plt.show()
print("图片已保存为 band_structure.png")
