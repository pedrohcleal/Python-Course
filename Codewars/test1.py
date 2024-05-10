alpha = ['a','e','i','o','u']

def encode(st):
    for i in range(5):
        st = st.replace(alpha[i],str(i+1))
    return st
def decode(st):
    ''.join(  )
    for i in range(5):
        st = st.replace(str(i+1),alpha[i])
    return st