"""
输入： 一个字符串S
任意一个字符串，修改字符，如何才能使得修改后的字符串不包含两个连续相同的字符？模拟即可
"""
def f1(s):
    n = len(s)
    res = 0
    s = list(s)
    for i in range(1, n):
        if s[i - 1] == s[i]:
            s[i] = "+"
            res += 1
    return res

'''
最优规划
第一行 n, m, k 分别代表行数、列数和颜色转换需要的金币数
输入 colors颜色二维数组
输入金币二维数组代表每点的金币个数
动态规划即可,dp[i][j]代表到达 (i,j) 最大的价值，转移方程也就不难推出了。
需要注意的是上一步(i-1,j) or (i, j-1)是否可以到达（如果为-1那么就是不可达
如果上一步到此步有颜色转换 那么上一步是否可以移动到此位置也就是dp[i-1][j] or dp[i][j-1] >= k
'''
def f2(n,m,k,colors,coins):
    dp = [[0]*200 for _ in range(200)]
    res = 0
    for i in range(n):
        for j in range(m):
            if i or j:
                dp[i][j] = -1
            else:
                continue
            if i > 0 and dp[i-1][j] >= 0:
                if colors[i-1][j] == colors[i][j]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j] + coins[i][j])
                elif dp[i-1][j] >= k:
                    dp[i][j] = max(dp[i][j], dp[i-1][j] + coins[i][j] - k)
            if j > 0 and dp[i][j-1] >= 0:
                if colors[i][j-1] == colors[i][j]:
                    dp[i][j] = max(dp[i][j], dp[i][j-1] + coins[i][j])
                elif dp[i][j-1] >= k:
                    dp[i][j] = max(dp[i][j], dp[i][j-1] + coins[i][j] - k)
            res = max(res,dp[i][j])
    return res 

'''
区间覆盖最大次数
第一行： n 代表区间个数
第二行， 输入所有区间的起始端点
第三行， 输入所有区间的末尾端点
使用差分数组, 插入[from, to]区间的时候 使得mp[from]++, mp[to+1]--, 然后再通过前缀求和，就可以得到每个点的覆盖次数。需要注意的是 1^9+10的数据情况下 我们不能模拟全部点，应该只保存端点，因此应该使用散列表。
'''
def f3(n,froms,tos):
    mp = dict()
    max_count = 0
    count = 0
    for i in range(n):
        mp[froms[i]] += 1
        mp[tos[i]+1] -= 1
    stack = []
    for k, v in mp.items():
        count += v
        max_count = max(max_count,count)
        stack.append([k,count])
    ans = 0
    for i in range(len(stack)):
        if stack[i][1] == max_count:
            ans += stack[i+1][0] - stack[i][0]
    return max_count, ans

'''
给出一个加号连接的操作序列，使用加减乘除随机替换其中一个加号，求修改之后的结果。
'''
def f():
    n = int(input())
    a = list(map(float, input().split(" ")))
    m = int(input())
    ops = input().split(" ")
    assert len(ops) == 2*m
    sum_a = sum(a)
    ans = []
    for i in range(m):
        idx, op = int(ops[2*i]), ops[2*i+1]
        tmp = float(eval(f"{a[idx-1]}{op}{a[idx]}") - a[idx-1] - a[idx])
        if op == "+":
            tmp = a[idx-1] + a[idx] - a[idx-1] - a[idx]
        if op == "-":
            tmp = a[idx-1] - a[idx] - a[idx-1] - a[idx]
        if op == "*":
            tmp = a[idx-1] * a[idx] - a[idx-1] - a[idx]
        if op == "/":
            tmp = a[idx-1] / a[idx] - a[idx-1] - a[idx]
        ans.append(f"{(sum_a + tmp):.1f}")
    print(" ".join(ans))
    '''
    public class T1 {
    static String[] ss;
    static double res = 0.0;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        in.nextLine();
        int[] nums = new int[n];

        for (int i = 0; i < n; i++) {
            nums[i] = in.nextInt();
            res += 1.0*nums[i];
        }

        in.nextLine();
        int m = in.nextInt();
        in.nextLine();

        ss = in.nextLine().split(" ");
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            double cur = res;
            int idx = Integer.parseInt(ss[2*i]);
            String op = ss[2*i+1];
            int a = nums[idx-1], b = nums[idx];
            cur -= (a+b);
            cur += gao(a, b, op);
            sb.append(Math.round(cur*100)*0.01d).append(" ");
        }
        System.out.println(sb);
    }
    static double gao(int a, int b, String op) {
        if ("+".equals(op)) return a+b;
        else if ("-".equals(op)) return a-b;
        else if ("*".equals(op)) return a*b;
        else if ("/".equals(op)) return 1.0*a/b;
        return 0;
    }
}
    '''

'''
第二题求一个数组任意排序之后 求最小的相邻两数的差的和，排序即可。AC
'''
def f():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    # print(a)
    ans = 0
    for i in range(n-1):
        ans += a[i+1]-a[i]
    print(ans)
    
    
'''
树状数字板子题，单点更新，区间求和
'''
class BinTree:
    def __init__(self, n):
        self.l = [0] * (n + 1)
        self.n = n

    def lowbit(self, x):
        return x & -x
    
    def add(self, x, y):
        while x <= self.n:
            self.l[x] += y
            x += self.lowbit(x)
            
    def cal(self, x):
        ans = 0
        while x > 0:
            ans += self.l[x]
            x -= self.lowbit(x)
        return ans
def f():
    n, m = list(map(int, input().split()))
    op = list(map(int, input().split()))
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    tree = BinTree(n)
    ans = []
    for i in range(m):
        # print(op[i], x[i], y[i])
        if op[i] == 1:
            ans.append(str(tree.cal(y[i]) - tree.cal(x[i]-1)))
        else:
            cur = tree.cal(x[i]) - tree.cal(x[i]-1)
            tree.add(x[i], y[i] - cur)
    print(" ".join(ans))
    
def f():
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    z = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n-1, -1, -1):
        cnt = 0
        tmp = 10**18
        for j in range(i, -1, -1):
            cnt += x[j] - y[j]
            tmp = min(tmp, z[j] * cnt)
        ans[i] = tmp
    m = int(input())
    q = list(map(int, input().split()))
    for i in range(m):
        print(ans[q[i]-1], sep=" ")
        
        
"""
小美不干外卖配送了，转行开了一家水果店。
一天她接到了一个大单，客户订购了 n 个水果，并且要求打包成多个果篮，一个果篮最多装 m 个水果。
为了包装方便，水果按从 1 到 n 编号，同一个果篮里装的水果编号必须是连续的。果篮的成本与容积成线性关系。为了估计容积，小美简单地用样本中点估计了一下。具体来说，假设一个果篮中装的最大的水果体积是 u，最小的是 v，那么这个果篮的成本就是 k × floor((u+v)/2) + s，其中 k 是果篮中装入水果的个数，s 是一个常数，floor(x) 是下取整函数，比如 floor(3.8)=3, floor(2)=2。
客户并没有规定果篮的数量，但是希望果篮的成本越小越好，毕竟买水果就很贵了。请求出小美打包这 n 个水果所用的最小花费。
输入描述
第一行三个正整数 n, m, s。意义如题面所示。
第二行 n 个正整数 a1, a2, ..., an，表示每个水果的体积。
对于全部数据，1 ≤ n ≤ 1e4,   1 ≤ m ≤ 1e3,   m ≤ n,   1 ≤ ai, s ≤ 1e4。
输出描述
输出一个整数，表示打包这 n 个水果果篮的最小成本。
"""
def f():
    n, m, s = list(map(int,input.split(" ")))
    a = list(map(int,input.split(" ")))
    dp = [float("inf")]*(n+1)
    dp[0] = 0
    for i in range(1,n+1):
        MAX, MIN = a[i-1], a[i-1]
        j = 1
        while j <= m and j <= i:
            MAX = max(MAX,a[i-j])
            MIN = min(MIN,a[i-j])
            temp = j*((MAX+MIN)/2)+s
            dp[i] = min(dp[i],dp[i-j]+temp)
            j += 1
    return dp[-1]