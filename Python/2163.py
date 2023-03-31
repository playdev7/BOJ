# 1402번 틀리고 생각난 소인수분해 함수 선언
def prime(num):
    primes = []
    i, j = 2, 0
    while num > 1:
        if num % (i+j) == 0:
            primes.append(i+j)
            num = num / (i+j)
        else:
            j += 1
    return primes

# 최소공배수 구해줄 함수 선언
def min_mul(nums1, nums2):
    result = 0
    numbers = nums1 + nums2
    numbers.sort()

    for i in range(len(numbers)):
        try:
            if numbers[i] == numbers[i-1]:
                numbers.remove(i)
        except:
            pass

    for j in numbers:
        if result == 0:
            result += j
        else:
            result = result * j

    return result

def main():
    n, m = input().split()

    n_primes = prime(int(n))
    m_primes = prime(int(m))

    print(min_mul(n_primes, m_primes))


if __name__ == "__main__":
    main()