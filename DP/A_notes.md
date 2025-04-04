# 动态规划特点
「分治」是算法中的一种基本思想，其通过将原问题分解为子问题，不断递归地将子问题分解为更小的子问题，并通过组合子问题的解来得到原问题的解。

类似于分治算法，「动态规划」也通过组合子问题的解得到原问题的解。不同的是，适合用动态规划解决的问题具有「重叠子问题」和「最优子结构」两大特性。

## 重叠子问题
动态规划的子问题是有重叠的，即各个子问题中包含重复的更小子问题。若使用暴力法穷举，求解这些相同子问题会产生大量的重复计算，效率低下。

动态规划在第一次求解某子问题时，会将子问题的解保存；后续遇到重叠子问题时，则直接通过查表获取解，保证每个独立子问题只被计算一次，从而降低算法的时间复杂度。

## 最优子结构
如果一个问题的最优解可以由其子问题的最优解组合构成，并且这些子问题可以独立求解，那么称此问题具有最优子结构。

动态规划从基础问题的解开始，不断迭代组合、选择子问题的最优解，最终得到原问题最优解

# 动态规划的解题步骤

1. 确定dp数组（dp table）以及下标的含义
2. 确定递推公式
3. dp数组如何初始化
4. 确定遍历顺序
5. 举例推导dp数组

**注意：** 做动规的题目，写代码之前一定要把状态转移在dp数组的上具体情况模拟一遍，心中有数，确定最后推出的是想要的结果。

