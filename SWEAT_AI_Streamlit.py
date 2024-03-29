import streamlit as st
import StreamlitController as sc

st.sidebar.title("Give us information!")
leader = st.sidebar.radio('Team leader?', ['Yes', "No"])
role = st.sidebar.selectbox("What did you work on?", ["Frontend", "Backend", "Infra", "ML"])
repositoryUrl = st.sidebar.text_input('Repository url', value="https://www.github.com/")
additional_desc = st.sidebar.text_input('Additional Information', value="Tell me more about your project!")

st.title('Welcome to SWEAT!')
st.subheader('Save your time with our auto-portfolio service!')
complete_btn = st.button("작성 완료하기")
if st.sidebar.button('Start Portfolio with Github'):
    st.empty()
    response = sc.getResponse(leader, role, repositoryUrl, additional_desc)
    print(response)

    input_project_info = st.text_area("프로젝트 소개", response['project_info'], height=200, )
    input_team_introduce = st.text_area("기간, 팀원 및 역할 소개", response['period'], height=200)
    input_team_function = st.text_area("핵심 기능 정리", response['core_function'], height=200)
    input_individual_work = st.text_area("개인 기여", " ", height=200)

    if complete_btn:
        st.empty()
        con = st.container()
        con.caption("프로젝트 소개")
        con.write(input_project_info)
        con.caption("기간, 팀원 및 역할 소개")
        con.write(input_team_introduce)
        con.caption("핵심 기능 정리")
        con.write(input_team_function)
        con.caption("개인 기여")
        con.write(input_individual_work)
