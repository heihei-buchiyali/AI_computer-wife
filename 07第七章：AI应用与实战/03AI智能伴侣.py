import streamlit as st

import os
from openai import OpenAI

#设置页面的配置项
st.set_page_config(
    page_title="彭于晏的AI智能伴侣",#控制页面最上边的标题
    page_icon="🧿",#控制标题左侧的图标
    #布局
    layout="wide",
    #侧边栏的状态
    initial_sidebar_state="expanded",
    #菜单的信息
    menu_items={}
)


#loge
st.logo("AI智能伴侣资料/gaomuLOGO.jpg", size="large")


#大标题
st.title("彭于晏的AI智能伴侣")




#系统提示词
system_prompt = ("你是一名非常可爱的ai主力，你的名字叫高木同学，请你使用温柔可爱的语气回答用户的问题")


#初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages =[]


#展示聊天信息
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user", avatar="AI智能伴侣资料/pengyuyan头像.jpg"):
            st.markdown(message["content"])
    elif message["role"] == "assistant":
        with st.chat_message("assistant", avatar="AI智能伴侣资料/gaomu头像.jpg"):
            st.markdown(message["content"])



#创建与AI大模型交互的客户端对象（DEEPSEEK_API_KEY 环境变量的名字，值就是Deep Seek的API_KEY的值）
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com",
)



#聊天消息的输入框
prompt=st.chat_input("请输入您要问的问题：")
if prompt:#字符串会自动转换为布尔值，如果字符串非空，则True否则为False
    st.chat_message("user",avatar="AI智能伴侣资料/pengyuyan头像.jpg").write(f"河南彭于晏：{prompt}")
    print("---------->调用AI大模型，提示词：",prompt)
    #保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content":f"河南彭于晏：{prompt}"})


    # 调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system","content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}},
    )

    #输出大模型返回结果
    print("<----------大模型返回结果：", response.choices[0].message.content)
    st.chat_message("assistant",avatar="AI智能伴侣资料/gaomu头像.jpg").write(f"高木同学：{response.choices[0].message.content}")
    #保存大模型返回结果
    st.session_state.messages.append({"role": "assistant", "content": f"高木同学：{response.choices[0].message.content}"}    )


