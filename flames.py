import streamlit as st
st.title("WELCOME TO FLAMES GAME")
s1=st.text_input("Enter the first name:").strip()
s2=st.text_input("Enter the second name:").strip()
s1=list(s1)
s2=list(s2)
s='flames'

c=0
for i in s1+s2:
    if i!=0:
        c+=1

res=["Friend","Lovers","Affection","Marriage","Enemies","Siblings"]
while len(res)>1:
    splitindex=(c%len(res)-1)
    if splitindex>=0:
        right=res[splitindex+1:]
        left=res[:splitindex]
        res=right+left
    else:
        res=res[:len(res)-1]
if st.button('submit'):
    st.success(res[0])
