import streamlit as st

with st.sidebar:
    st.header('Load Data')
    st.radio('Env', ['getafe', 'global'], horizontal=True)
    tab1, tab2, tab3 = st.tabs(["Relative", "Absolute", "All"])
    with tab1:
        st.text('Last ')
        col1, col2 = st.columns(2)
        with col1:
            st.number_input('value', value=1)
        with col2:
            st.selectbox(
                'unit',
                ['minutes', 'hours', 'days'], index=1)

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.date_input('date start')
            st.time_input('time start')
        with col2:
            st.date_input('date end')
            st.time_input('time end')
    with tab3:
        st.text('All data')
    st.button('Load')

    st.markdown('__________________')

    st.header('Filters')
