class Solution(object):
    def longestBalanced(self, s):
        # prefix counts
        a = b = c = 0
        res = 1   # at least 1 char always valid
        
        # hashmaps for balance cases
        ab_c = {(0, 0): -1}   # (a-b, c)
        ac_b = {(0, 0): -1}   # (a-c, b)
        bc_a = {(0, 0): -1}   # (b-c, a)
        abc  = {(0, 0): -1}   # (a-b, a-c)
        
        # track longest single-character run
        run = 1
        
        for i, ch in enumerate(s):
            # longest same char run (for "aaa" type)
            if i > 0 and s[i] == s[i-1]:
                run += 1
            else:
                run = 1
            res = max(res, run)
            
            # update counts
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1
            
            # case 1: a=b
            key = (a-b, c)
            if key in ab_c:
                res = max(res, i - ab_c[key])
            else:
                ab_c[key] = i
            
            # case 2: a=c
            key = (a-c, b)
            if key in ac_b:
                res = max(res, i - ac_b[key])
            else:
                ac_b[key] = i
            
            # case 3: b=c
            key = (b-c, a)
            if key in bc_a:
                res = max(res, i - bc_a[key])
            else:
                bc_a[key] = i
            
            # case 4: a=b=c
            key = (a-b, a-c)
            if key in abc:
                res = max(res, i - abc[key])
            else:
                abc[key] = i
        
        return res
