# [Silver II] Simple Game - 28053 

[문제 링크](https://www.acmicpc.net/problem/28053) 

### 성능 요약

메모리: 31256 KB, 시간: 180 ms

### 분류

해 구성하기, 유클리드 호제법, 수학, 정수론

### 문제 설명

<p>Let $s$ be an arithmetic sequence consisting of $2n$ integers, where the first term is denoted as $a$ and the common difference as $b$. In other words, $s = [a, a+b, a+2b, \ldots, a+(2n-1)b]$.</p>

<p>You should perform a sequence of $n$ operations, where each operation involves selecting two <strong>coprime</strong> integers from $s$ and erasing them. Once an integer is erased from $s$, it cannot be selected again for any subsequent operations.</p>

<p>Find any sequence of operations satisfying the above conditions, or report that such a sequence does not exist.</p>

### 입력 

 <p>The first line contains three integers $n, a, b$. ($1 \leq n \leq 10^5$, $1 \leq a, b \leq 10^9$)</p>

### 출력 

 <p>If no such sequence of operations exists, print <code>No</code>.</p>

<p>Otherwise, print <code>Yes</code>, followed by $n$ lines. On each line, print the two integers selected from $s$ for the corresponding operation.</p>

<p>If there are multiple possible answers, you may print any.</p>

