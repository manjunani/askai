import streamlit as st
import google.generativeai as palm

footer = """<style>
a:link , a:visited{
color: blue;
background-color: transparent;
}

a:hover,  a:active {
color: yellow;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
color: blue;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a href="https://manjunani.github.io/manjunathasaiuppu" target="_blank">Manjunatha Sai Uppu</a> Fund me at <a href="https://www.buymeacoffee.com/manjunathauppu" target="_blank">Buy me a Coffee</a></p>
</div>
"""

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if __name__ == "__main__":
    st.title("AskAI")
    palm.configure(api_key="APIKEY")
    models = [m for m in palm.list_models(
    ) if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    raw_prompt = st.text_input("Enter Your Prompt")
    status = st.button("Go....")
    prompt = '\"\"\"{0}\"\"\"'.format(raw_prompt)
    if status:
        completion = palm.generate_text(
            model=model,
            prompt=prompt,
            temperature=0,
            # The maximum length of the response
            max_output_tokens=800,
        )
        if completion.result is not None:
            st.write(completion.result)
        else:
            st.write("Please Provide a Good Prompt")
    st.markdown(footer, unsafe_allow_html=True)
