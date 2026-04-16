import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_concerns(project_description):
    prompt = f"""
You are an assistant that analyzes CEQA project descriptions.

Project description:
{project_description}

Generate a ranked list of likely public concerns.

For each concern, include:
- Appendix G category
- Short description
- Brief rationale

Keep the output structured and concise.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    sample_description = """
    The applicant proposes constructing 615 residential units on 135 acres of active orchard land,
    including roads, stormwater infrastructure, and a public park.
    """

    result = generate_concerns(sample_description)

    print("\nPredicted Public Concerns:\n")
    print(result)