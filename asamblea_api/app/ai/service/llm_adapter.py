from app.client.mistral_ai import create_client


# MistralAI response generator
async def ai_response_generator(prompt: str):
    mistral_client = create_client()

    system_message = "You are a helpful chatbot. You will help people with answers to their questions. In spanish"
    # Output variables
    output = f"**User:** {prompt}\n\n"
    # Prompt template for message history
    prompt_template = f"Human: {prompt}"
    output += f"**System:** {system_message}\n\n"

    # Mistral chat messages
    mistral_messages = [
        {
            "role": "system",
            "content": system_message,
        },
        {
            "role": "user",
            "content": prompt_template,
        },
    ]

    # Stream the chat
    output += f"**Chatbot:** "

    response_messages = mistral_client.chat.complete(model="mistral-small", messages=mistral_messages)
    output += f"**System:** {response_messages}\n\n"
    return response_messages.choices[0].message.content

