s = input().split()
ans = []
for item in s:
    st = item[::-1].upper()
    sample = st.replace('.', '').replace('!', '')
    spe = st.replace(sample, '')[::-1]
    ans.append(sample + spe)
print(" ".join(ans))