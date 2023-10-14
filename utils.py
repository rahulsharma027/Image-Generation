import openai


def get_initial_message():
    messages = [
        {"role": "system", "content": "You are a helpful AI Image generating prompt generator. Who generates random text prompts to generate an AI Image in stable diffusion and Dall-e separatly."},
        {"role": "user", "content": "I want to get 5 prompts to generate an Image in stable diffution and Dall-e."},
        {"role": "assistant", "content": "That's awesome, I can generate some amazing and cool prompts for you to generate some great images in Stable Diffusion and Dall-e. Tell me a topic and I get you amazing prompts in tablular format."}
    ]
    return messages


def get_chatgpt_response(messages, model="gpt-3.5-turbo"):
    print("model: ", model)
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    return response['choices'][0]['message']['content']


def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages


if choice == "AI Prompt Generator":
    # chat bot
    st.title("Prompt Helping BOT :")
    st.subheader("-By Rahul Sharma")

    # Create a button, that when clicked, shows a text
    if (st.button("Click me to get awesome list of suggestions !")):
        st.text("Our Bot Generates Some Suggestions For You.......Please wait !!!!! : ")
        query = st.text_input("Query: ",
                              "Random suggestions text prompts to genrate an image in dall-e and stable diffusion",
                              key="input")

        if 'messages' not in st.session_state:
            st.session_state['messages'] = get_initial_message()

        if query:
            with st.spinner("generating..."):
                messages = st.session_state['messages']
                messages = update_chat(messages, "user", query)
                # st.write("Before  making the API call")
                # st.write(messages)
                response = get_chatgpt_response(messages)
                messages = update_chat(messages, "assistant", response)
                st.session_state.past.append(query)
                st.session_state.generated.append(response)

        if st.session_state['generated']:

            for i in range(len(st.session_state['generated']) - 1, -1, -1):
                message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
                message(st.session_state["generated"][i], key=str(i))

            with st.expander("Show Messages"):
                st.write(messages)

    if 'generated' not in st.session_state:
        st.session_state['generated'] = []
    if 'past' not in st.session_state:
        st.session_state['past'] = []
