import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)




left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ1')
expander.write('問い合わせ1の回答')
expander = st.expander('問い合わせ2')
expander.write('問い合わせ2の回答')
expander = st.expander('問い合わせ3')
expander.write('問い合わせ3の回答')



# if st.checkbox('ハリネズミが見たい'):
#    img = Image.open('10040304_615.jpg')
#    st.image(img, caption='hedgehog', use_column_width=True)

#syumi = st.text_input('あなたの趣味を教えてください')
#condition = st.slider('あなたの今の調子は？', 0, 100, 50)

#'あなたの趣味:', syumi, 'です'
#'コンディション:', condition



#if st.checkbox('ハリネズミ'):
#   img = Image.open('10040304_615.jpg')
#    st.image(img, caption='hedgehog', use_column_width=True)

# 'あなたの好きな数字は、', option,

#numberlist = list(range(0,100,20))
#st.write(numberlist)

#df = pd.DataFrame(
#    np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
#    columns=['lat','lon']
#)

#df_2 = pd.DataFrame(
#    np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
#    columns=['a','b']
#)



# st.table(df.style.highlight_max(axis=0))
# st.dataframe(df_2,  width=100, height=100)

#"""
# 章
## 節
### 項

#```python
#import streamlit as st
#import numpy as np
#import pandas as pd
#```
#これも表示されるのか

#"""

# st.map(df)


