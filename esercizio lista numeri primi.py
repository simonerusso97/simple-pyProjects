def isPrime(n):
        if n == 1:
                return True
        for j in range(2, n):
                if n % j == 0:
                        return False
        return True

def listOfPrimeNumber(n):
        l = [1]
        for i in range(2, n+1):
                if isPrime(i):
                        l.append(i)

        return l


def listOfPrimeNumber2(n):
        l = [1, 2]
        for i in range(2, n+1):
                prime = True
                for j in l[1:]:
                        if i % j == 0:
                                prime = False
                                break
                if prime:
                        l.append(i)
        return l
