import os
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SAMPLES_DIR = Path("samples")
OUTPUTS_DIR = Path("outputs")


def generate_concerns(project_description):
    prompt = f"""
You are an assistant that analyzes CEQA project descriptions.

Given a 1–2 paragraph project description, generate a ranked list of likely public concerns.

For each concern, include:
- Appendix G category (use standard CEQA Appendix G names only, e.g., Biological Resources, Transportation, Air Quality, Noise, Hydrology and Water Quality, Land Use and Planning, Population and Housing, Utilities and Service Systems)
- A short, specific description of the concern grounded in the project details
- A brief rationale explaining why this concern would likely be raised

Ensure categories are precise and avoid generic or vague labels. Base each concern directly on signals in the project description.

Format the output cleanly with clear numbering, spacing, and consistent structure for readability.

Project Description:
{project_description}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content


def main():
    OUTPUTS_DIR.mkdir(exist_ok=True)

    sample_files = sorted([
    f for f in SAMPLES_DIR.glob("*.md")
    if f.name != "README.md"
])

    for sample_file in sample_files:
        text = sample_file.read_text(encoding="utf-8")
        result = generate_concerns(text)

        output_path = OUTPUTS_DIR / f"{sample_file.stem}.txt"
        output_path.write_text(result, encoding="utf-8")

        print(f"done: {sample_file.name}")


if __name__ == "__main__":
    main()