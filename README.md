# dive_into_DL

2023.10

### 1.softmax

$$
y_i= \frac{e^i}{\sum e^i}
$$

### 2.交叉熵损失函数

对单个样本，假设真实分布为y，网络输出分布为 $\widehat{y}_i$，总的类别数为n，则在这种情况下，交叉熵损失函数的计算方法为：

$$
Loss=−\sum^n_{i=1}y_ilog\widehat{y}_i
$$

```
用一个例子来说明，在手写数字识别任务中，如果样本是数字“5”，那么真实分布应该为：[ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ]，
如果网络输出的分布为：[ 0.1, 0.1, 0, 0, 0, 0.7, 0, 0.1, 0, 0 ]，则n应为10，那么计算损失函数得：Loss=−0×log0.1−0×log0.1−0×log0−0×log0−0×log0−1×log0.7−0×log0−0×log0.1−0×log0−0×log0≈0.3567
如果网络输出的分布为：[ 0.2, 0.3, 0.1, 0, 0, 0.3, 0.1, 0, 0, 0 ]，那么计算损失函数得：Loss=−0×log0.2−0×log0.3−0×log0.1−0×log0−0×log0−1×log0.3−0×log0.1−0×log0−0×log0−0×log0≈1.2040
上述两种情况对比，第一个分布的损失明显低于第二个分布的损失，说明第一个分布更接近于真实分布，事实也确实是这样。
```


### 3.Dropout

希望       X的期望      E[X'] = X

$$
x'_i = 
\begin{cases}
    0 & \text{ 概率为 } p \\
    \frac{h}{1-p} & \text{ 其他情况}
\end{cases}
$$

### 4.BN作用于卷积，dropout作用于全连接层

### 5.卷积层

​				无padding时，形状变为

​                                                     $$ (n_h - k_h + 1) \times (n_w - k_w + 1) $$

​				填充padding, 卷积完成后，矩阵变为 

​						                             $$ (n_h - k_h + p_h + 1) \times (n_w - k_w + p_w + 1) $$

​				通常$p_h = k_h - 1$, $p_w = k_w - 1 $ ,当$k_h$ 为奇数：在上下两侧填充$p_h / 2$

​																	当$k_h$为偶数：在上侧填充$\lceil k/2 \rceil$,下侧填充$\lfloor k/2 \rfloor$

​		**步幅**

​				给定高度$s_h$ 和宽度$s_w$步幅，输出形状为：
$$
\lfloor \frac{(n_h - k_h + p_h + s_h)}{s_h} \rfloor \times \lfloor\frac{(n_w - k_w + p_w + s_w)}{s_w} \rfloor
$$


如果$p_h = k_h - 1, p_W = k_w - 1$,则
$$
\lfloor \frac{(n_h + s_h - 1)}{s_h} \rfloor \times \lfloor\frac{(n_w + s_w - 1)}{s_w} \rfloor
$$
如果输入X的高度和宽度能被步幅整除，则
$$
(\frac{n_h}{s_h}) \times(\frac{n_w}{s_w})
$$
### 6.Batch Normalization

​	bn层用于卷积和激活函数之间，加速收敛



