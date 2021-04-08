from pwn import *
from tqdm.auto import tqdm

context.log_level = 'CRITICAL'

def solve_expr(expr):
    is_foo = expr.startswith('foo')

    if is_foo:
        parsed = list(re.findall('foo\((\S+), (\S+)\) = (\S+)', expr)[0])
        t = parsed.index('?')
        
        if t == 0:
            # foo(?, 1) = 1
            solver = process('./foobc')
        elif t == 1:
            # foo(1, ?) = 1
            solver = process('./fooac')
        else:
            # foo(1, 1) = ?
            solver = process('./fooab')
    else:
        parsed = list(re.findall('bar\((\S+), (\S+), (\S+)\) = (\S+)', expr)[0])
        t = parsed.index('?')
        
        if t == 0:
            # bar(?, 1, 1) = 1
            solver = process('./barbcd')
        elif t == 1:
            # bar(1, ?, 1) = 1
            solver = process('./baracd')
        elif t == 2:
            # bar(1, 1, ?) = 1
            solver = process('./barabd')
        else:
            # bar(1, 1, 1) = ?
            solver = process('./barabc')
    
    solver.readline()
    solver.sendline(expr)
    solution = re.findall('Result (\d+)', solver.readline().decode('utf-8'))[0]
    solver.kill()
    return str(solution)

#p = process('./infinity_gauntlet') # For testing!
p = remote('shell.actf.co', 21700)
f = open("out.txt", "w")


p.readline()
p.readline()

for i in range(250):
    r = re.findall('=== ROUND (\d+) ===', p.readline().decode('utf-8'))[0]
    print(f"Solving round {r}/250")
    expression = p.readline().decode('utf-8')
    solution = solve_expr(expression)
    p.sendline(solution)
    res = p.readline().decode('utf-8')
    if res.startswith('Wrong!'):
        print('DEBUG')
        print(expression)
        print(res)
        print('We failed :(')
        exit()
    else:
        #f.write(f'{r}   {solution}  \t{expression[:-1]}\n')
        if int(r) >= 50:
            f.write(f'{solution}\n')

f.close()

p = process('./solver')
print(p.readline().decode('utf-8'))