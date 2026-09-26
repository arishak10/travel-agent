import streamlit as st
from agent import build_agent


st.set_page_config(
    page_title="AI Travel Agent",
    page_icon="✈️",
    layout="centered"
)


st.title("✈️ AI Travel Agent")

st.write(
    "Ask about destinations, travel plans, safety, "
    "places to visit, and travel information."
)


@st.cache_resource
def get_agent():
    return build_agent()


agent = get_agent()


query = st.text_input(
    "What would you like to know?",
    placeholder="Example: Plan a 5-day trip to Dubai"
)


if st.button("Ask Travel Agent"):

    if query:

        with st.spinner("Researching travel information..."):

            response = agent.run(query)

        st.markdown("### 🌍 Travel Information")
        st.markdown(response.content)

    else:
        st.warning("Please enter a travel question.")