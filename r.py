import math

def r(seed, a, c, m, N):
    y=[seed]
    u = [seed/m]
    g = []

    for i in range(1, N+1):
        
        y.append((a * y[i-1] + c)%m)
        u.append(y[i]/m)

        #g.append(-0.5 * (math.log(1-u[i])))

        if(u[i] <= 0.5):
            g.append("TESTA")
        else:
            g.append("CROCE")
            
            

    print(u[1:])
    print(g)
 
        
