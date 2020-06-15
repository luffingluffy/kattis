# ref to hanging out on terrace on kattis (https://open.kattis.com/problems/hangingout)
# tried to do a recursion method to solve it so as to challenge myself (am learning about it)

limit, n = map(int, input().split())
denied = 0

def no_of_events(n):
    if n == 0:
        return 0
    else:
        z = input().split()
        
        # here is where it goes wrong: im calling for the function in the if statement..
        # would there be a way to get the result without calling for the recusion/ express the if statement in another way?
        # tldr: i need the result of the recursion to get the answer of the recursion        
        
        if z[0] == "enter" and int(z[1]) + no_of_events(n - 1) <= limit:
            return int(z[1]) + no_of_events(n - 1)

        elif z[0] == "enter" and int(z[1]) + no_of_events(n - 1) > limit:
            denied += 1
            return 0 + no_of_events(n - 1)

        elif z[0] == "leave":
            return -int(z[1]) + no_of_events(n - 1)

no_of_events(n)
print(denied)
