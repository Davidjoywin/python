def ips_between(start, end):
    start = [int(i) for i in start.split('.')]
    end = [int(i) for i in end.split('.')]
    difference = 0
    ips = []
    for i in range(len(start)):
        ips.append(end[i]-start[i])
        
    for i in range(len(ips)):
        difference += ips[i] * (256**(4-1-i))
        
    return difference



    ##############SHORT CODE######################

def ips_between(start, end):
    ip_difference = [[int(i) for i in end.split('.')][i] - [int(i) for i in start.split('.')][i] for i in range(len([int(i) for i in start.split('.')]))]
    
    return sum([ip_difference[i] * (256**(len(ip_difference)-1-i)) for i in range(len(ip_difference))])
    