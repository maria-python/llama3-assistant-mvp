from llm import chat_with_llm
from memory import Memory

SYSTEM_PROMPT = (
    "You are a personal AI assistant. "
    "You help the user learn and reflect. "
    "You remember the context of the conversation and respond clearly and thoughtfully."
)

def main():
    memory = Memory()
    memory.load()

    print("Personal Assistant")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ("exit", "quit"):
                print("Exiting the chat. Goodbye!")
                memory.save()
                break

            memory.add_message(role="user", content=user_input)

            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                *memory.get_recent_messages(limit=10)
            ]

            assistant_reply = chat_with_llm(messages)

            print(f"Assistant: {assistant_reply}\n")

            memory.add_message(role="assistant", content=assistant_reply)

        except KeyboardInterrupt:
            print("\nExiting the chat. Goodbye!")
            memory.save()
            break

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
