A,B,C = map (int , input().split())
if C==0:
    print("Takahashi" if A>B else "Aoki")
else:
    print("Aoki" if B >A else "Takahashi")