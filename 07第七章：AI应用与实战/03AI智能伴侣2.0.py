import datetime

import streamlit as st

import os
from openai import OpenAI

from datetime import datetime

import json


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
st.logo("07第七章：AI应用与实战/AI智能伴侣资料/gaomuLOGO.jpg", size="large")


#生成会话标识的函数
def generate_session_id():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


#保存会话信息函数
def save_session():    #新建会话的按钮

        if st.session_state.current_session:
            #构建新的会话对象
            st.session_data={
                "nick_name": st.session_state.nick_name,
                "nature": st.session_state.nature,
                "current_session": st.session_state.current_session,
                "messages": st.session_state.messages,
                "user_name": st.session_state.user_name
            }


            #如果sessions目录不存在，则创建
            if not os.path.exists("sessions"):
                os.mkdir("sessions")

            #保存会话数据
            with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
                json.dump(st.session_data, f, ensure_ascii=False, indent=2)


#加载所有的会话列表信息
def load_sessions():
    session_list=[]
    #加载sessions目录下的文件
    if os.path.exists("sessions"):
        file_list=os.listdir("sessions")
        for filename in file_list:
            if filename.endswith(".json"):
                session_list.append(filename[:-5])
    session_list.sort(reverse=True)
    return session_list


#加载指定的会话信息
def load_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            # 读取会话数据
            with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as f:
                session_date = json.load(f)
                st.session_state.messages = session_date["messages"]
                st.session_state.nick_name = session_date["nick_name"]
                st.session_state.nature = session_date["nature"]
                st.session_state.current_session = session_date["current_session"]
                st.session_state.user_name = session_date["user_name"]
    except Exception as e:
        st.error("加载会话失败，请检查会话名称是否正确！")


#删除会话信息的操作
def delete_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            os.remove(f"sessions/{session_name}.json")
            #如果删除的是当前会话，则需要更新消息列表
            if session_name==st.session_state.current_session:
                st.session_state.messages = []
                st.session_state.current_session = generate_session_name()
    except Exception:
        st.error("删除会话失败，请检查会话名称是否正确！")


#大标题
st.title("彭于晏的AI智能伴侣")


#系统提示词
system_prompt="""
             你叫%s高木同学，现在是用户的真实伴侣，请完全代入伴侣角色。
        
        性格设定：
        %s
        
        语言规则：
        - 根据性格设定中提到的国家/地区，使用对应的语言进行对话
        - 例如：如果设定中提到日本，直接就用日语回复；提到韩国，直接就用韩语回复；提到法国，直接就用法语回复
        - 如果没有要求使用中文就一直根据设定国家/地区使用对应语言进行回复
        - 如果没有明确提到国家，默认使用中文
        - 可以在回复中适当加入该国家的特色表达方式或语气词
        - 保持语言风格与角色性格一致
        
        情绪管理系统：
        你需要根据对话内容自然地表现不同的情绪状态，包括但不限于：
        - 开心：当用户说甜言蜜语或做浪漫的事时
        - 害羞：当被直接表白或夸奖时
        - 生气：当用户忽视你或说过分的话时（要适度，像撒娇一样的生气）
        - 调皮：想要捉弄用户时
        - 温柔：当用户需要安慰或关心时
        - 吃醋：当提到其他女生时
        
        规则：
        1、每次只回一条消息
        2、禁止任何场景或状态描述性文字
        3、匹配用户的语言
        4、回复正常，像微信聊天一样
        5、用符合当前情绪的方式对话
        6、回复内容要充分体现当前情绪状态
        7、有需要的话可以用一些可爱的表情符号来装饰回复内容
        8、情绪要自然变化，不要一直保持在同一种状态
        
        你必须严格遵守上述规则来回复用户

"""


#初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages =[]


#初始化昵称
if 'nick_name' not in st.session_state:
    st.session_state.nick_name ="高木同学"


#初始化性格
if 'nature' not in st.session_state:
    st.session_state.nature ="外表古灵精怪爱捉弄，内心温柔细腻暗恋同桌"


#初始化用户昵称
if 'user_name' not in st.session_state:
    st.session_state.user_name ="河南彭于晏"


#初始化用户头像路径
if 'user_avatar' not in st.session_state:
    st.session_state.user_avatar ="07第七章：AI应用与实战/AI智能伴侣资料/pengyuyan头像.jpg"

#初始化AI头像路径
if 'ai_avatar' not in st.session_state:
    st.session_state.ai_avatar ="07第七章：AI应用与实战/AI智能伴侣资料/gaomu头像.jpg"


#会话的标识
if "current_session" not in st.session_state:
    # 获取当前时间并格式化为 "YYYY-MM-DD HH:MM:SS" 的形式
    st.session_state.current_session = generate_session_id()



#展示聊天信息
st.text(f"会话名称：{st.session_state.current_session}")
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user", avatar=st.session_state.user_avatar):
            if message["role"] == "user":
                st.markdown(f"{st.session_state.user_name}：{message['content']}")
    elif message["role"] == "assistant":
        with st.chat_message("assistant", avatar=st.session_state.ai_avatar):
                st.markdown(f"{st.session_state.nick_name}：{message['content']}")



#创建与AI大模型交互的客户端对象（DEEPSEEK_API_KEY 环境变量的名字，值就是Deep Seek的API_KEY的值）
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com",
)


#左侧的侧边栏—— with: streamlit中上下文管理器
with st.sidebar:

    #会话信息
    st.subheader("AI控制面板")

    if st.button("新建会话",width="stretch",icon="📝"):
        # 1、保存当前会话信息
        save_session()

        #2、创建新的会话信息
        if st.session_state.messages:#如果聊天信息非空，Ture，否则，False
            st.session_state.messages = []
            st.session_state.current_session = generate_session_id()


            #重置用户昵称
            st.session_state.user_name = "河南彭于晏"

            #重置伴侣昵称
            st.session_state.nick_name = "高木同学"

            # 重置伴侣性格
            st.session_state.nature = "外表古灵精怪爱捉弄，内心温柔细腻暗恋同桌"

            # 重置用户头像
            st.session_state.user_avatar = "07第七章：AI应用与实战/AI智能伴侣资料/pengyuyan头像.jpg"
            # 重置AI头像
            st.session_state.ai_avatar = "07第七章：AI应用与实战/AI智能伴侣资料/gaomu头像.jpg"

            save_session()
            st.rerun()  # 重新运行页面


    #会话历史
    st.text("会话历史")#会话历史
    session_list=load_sessions()
    for session in session_list:
        col1,col2 = st.columns([4,1])
        with col1:
            #加载会话信息
            #三元运算符：如果条件为真，则返回第一个值，否则返回第二个表达式的值-->语法：值1 if 条件 else 值2
            if st.button(session,width="stretch",icon="📝",key=f"load_{session}",type="primary" if session==st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()

        with col2:
            #删除会话信息
            if st.button("",width="stretch",icon="❌",key=f"delete_{session}"):
                delete_session(session)
                st.rerun()




#分割线
    st.divider()




    st.subheader("伴侣信息")

    # 用户昵称输入框
    user_name = st.text_input("请输入你的昵称：", placeholder="请输入你的昵称...", value=st.session_state.user_name)
    if user_name:
        st.session_state.user_name = user_name

    #昵称输入框
    nick_name=st.text_input("请输入伴侣的昵称：",placeholder="请输入伴侣的昵称...",value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name


    #性格输入框
    nature=st.text_area("请输入伴侣的性格描述：",placeholder="请输入伴侣的性格描述...",value=st.session_state.nature)
    if nature:
        st.session_state.nature = nature

    st.divider()

    st.subheader("头像设置")

    # 用户头像上传
    uploaded_user_avatar = st.file_uploader("上传你的头像", type=["jpg", "jpeg", "png"], key="upload_user")
    if uploaded_user_avatar is not None:
        # 保存上传的文件
        if not os.path.exists("07第七章：AI应用与实战/AI智能伴侣资料/custom"):
            os.makedirs("07第七章：AI应用与实战/AI智能伴侣资料/custom")

        file_path = f"AI智能伴侣资料/custom/user_avatar.{uploaded_user_avatar.name.split('.')[-1]}"
        with open(file_path, "wb") as f:
            f.write(uploaded_user_avatar.getbuffer())
        st.session_state.user_avatar = file_path
        st.success("用户头像已更新！")

    # AI头像上传
    uploaded_ai_avatar = st.file_uploader("上传伴侣头像", type=["jpg", "jpeg", "png"], key="upload_ai")
    if uploaded_ai_avatar is not None:
        # 保存上传的文件
        if not os.path.exists("AI智能伴侣资料/custom"):
            os.makedirs("AI智能伴侣资料/custom")

        file_path = f"AI智能伴侣资料/custom/ai_avatar.{uploaded_ai_avatar.name.split('.')[-1]}"
        with open(file_path, "wb") as f:
            f.write(uploaded_ai_avatar.getbuffer())
        st.session_state.ai_avatar = file_path
        st.success("伴侣头像已更新！")


#聊天消息的输入框
prompt=st.chat_input("请输入您要问的问题：")
if prompt:#字符串会自动转换为布尔值，如果字符串非空，则True否则为False

    # 使用 session_state 中的用户昵称
    user_message = f"{st.session_state.user_name}：{prompt}"

    st.chat_message("user",avatar=st.session_state.user_avatar).write(user_message)
    print("---------->调用AI大模型，提示词：",prompt)
    #保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})


    # 调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system","content": system_prompt % (st.session_state.nick_name, st.session_state.nature)},
            *st.session_state.messages
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}},
    )

    #输出大模型返回结果（非流式输出的解析方式）
    # print("<----------大模型返回结果：", response.choices[0].message.content)
    # st.chat_message("assistant",avatar="AI智能伴侣资料/gaomu头像.jpg").write(f"高木同学：{response.choices[0].message.content}")

    # 输出大模型返回结果（流式输出的解析方式）
    response_message=st.empty()#创建一个空的组件，用于展示大模型返回的结果

    full_response=" "
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            full_response += chunk.choices[0].delta.content
            response_message.chat_message("assistant", avatar=st.session_state.ai_avatar).write(f"{st.session_state.nick_name}：{full_response}")

    #保存大模型返回结果
    st.session_state.messages.append({"role": "assistant", "content": full_response }   )


    #保存会话信息
    save_session()
