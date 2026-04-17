import os
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Missing OPENAI_API_KEY in .env")

client = OpenAI(api_key=api_key)

SAMPLES_DIR = Path("samples")
OUTPUTS_DIR = Path("outputs")


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


def main():
    OUTPUTS_DIR.mkdir(exist_ok=True)

    sample_files = sorted(SAMPLES_DIR.glob("*.md"))[:3]

    for sample_file in sample_files:
        text = sample_file.read_text(encoding="utf-8")
        result = generate_concerns(text)

        output_path = OUTPUTS_DIR / f"{sample_file.stem}.txt"
        output_path.write_text(result, encoding="utf-8")

        print(f"done: {sample_file.name}")


if __name__ == "__main__":
    main()