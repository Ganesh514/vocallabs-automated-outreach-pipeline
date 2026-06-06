def find_similar_companies(domain):

    demo_data = {
        "openai.com": [
            "anthropic.com",
            "cohere.com",
            "perplexity.ai"
        ]
    }

    return demo_data.get(
        domain.lower(),
        [
            "example-company1.com",
            "example-company2.com"
        ]
    )