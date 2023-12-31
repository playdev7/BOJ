n = int(input())
words = list(set([input() for _ in range(n)]))
[print(word) for word in sorted(words, key=lambda x:(len(x), x))]