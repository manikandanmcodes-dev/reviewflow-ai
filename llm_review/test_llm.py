from llm_review.reviewer import generate_review

review = generate_review(
    {
        "title": "Add login API"
    },
    [
        {
            "file": "auth.py",
            "risk": "Debug print statement found"
        }
    ]
)

print(review)