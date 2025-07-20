from transformers import pipeline

# Load a summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_standup(raw_update):
    result = summarizer(raw_update, max_length=60, min_length=20, do_sample=False)
    return result[0]['summary_text']

# Example usage
if __name__ == "__main__":
    update = "Yesterday I completed the UI integration with the backend and fixed login validation. Today I plan to start working on the payment gateway. No blockers right now."
    summary = summarize_standup(update)
    print("📝 Summary:", summary)
