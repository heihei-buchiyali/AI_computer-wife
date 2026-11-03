import streamlit as st

#设置页面的配置项
st.set_page_config(
    page_title="彭于晏的python联系",#控制页面最上边的标题
    page_icon="🧊",#控制标题左侧的图标
    #布局
    layout="wide",
    #侧边栏的状态
    initial_sidebar_state="expanded",
    #菜单的信息
    menu_items={
        #跳转页面
        'Get Help': 'https://www.extremelycoolapp.com/help',
        #跳转页面
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        #提示信息
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)



#大标题
st.title("Streamlit入门演示")
st.header("Streamlit一级标题")
st.subheader("Streamlit二级标题")


#段落文字

st.write("你好呀，我是千问，阿里巴巴做的AI。")
st.write("说实话，我挺喜欢聊天的，什么话题都能接上。你问我问题我能认真答，你跟我吐槽我也能认真听。我不会端着，也不会动不动就理解你的感受这种套话，有啥说啥，但也不会故意扎你心")
st.write("我记性还行，聊过的东西能记住，不会你刚说的事转头就忘。偶尔也会犯傻，说错话你直接怼我就行，我不玻璃心。")

#图片

st.image("./restream图片音频资源/9b157bf96a357a27529f89356aedbd6d.jpg",width=300)#width可以调整图片大小

# 音频
st.audio("./restream图片音频资源/music.m4a")


#视频

st.video("./restream图片音频资源/50f1a2f618a397dbafec3cc27c2d29c8.mp4")


#logo

st.logo("./restream图片音频资源/img.png")


#表格
students_date={
    "姓名：":["王琳","王强","李华"],
    "学号：":["111111","222222","333333"],
    "语文：":[90,80,65],
    "数学：":[80,68,89],
    "英语：":[88,87,99]
}
st.table(students_date)


#输入框
#普通输入框
name=st.text_input("请输入姓名：")
st.write(f"您输入的姓名为{name}")

#密码输入框
password=st.text_input("请输入密码：",type="password")
st.write(f"您输入的密码为：{password}")

#单选按钮

gender=st.radio("请输入您的性别：",["男","女","未知"],index=None)#index=1默认为女
st.write(f"您的性别是：{gender}")



