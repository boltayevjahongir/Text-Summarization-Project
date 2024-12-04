
from transformers import pipeline

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

# Text summarization function
def summarize_text(input_text, max_length=130, min_length=30):
    """Summarize the input text using a pre-trained transformer model."""
    summary = summarizer(input_text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]["summary_text"]

# Main function to interact with the user
if __name__ == "__main__":
    print("Welcome to the Text Summarization Tool!")
    print("Enter your text below (type 'exit' to quit):")

    while True:
        user_input = input("Enter your text: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        try:
            summary = summarize_text(user_input)
            print("Summary:")
            print(summary)
        except Exception as e:
            print(f"An error occurred: {e}")
