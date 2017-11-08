from summarization import Summarizer

summarizer = Summarizer("samples")
sums = summarizer.summarize_all()
for sum in sums:
    print(sum)