# Public Concern Predictor

Build a tool that predicts what concerns the public and reviewing agencies are likely to raise during CEQA public review, given a project description.

## Background

Before a CEQA project goes out for public review, the lead agency tries to anticipate what concerns will be raised. Doing this well requires knowing the project, knowing CEQA's standard impact categories (Appendix G of the CEQA Guidelines), and ideally knowing what's been raised on similar past projects.

Your tool should take a project description and produce a ranked list of likely public concerns, grouped by Appendix G category, with a rationale for each.

## The Work

Build a tool that takes a 1-2 paragraph project description as input and produces a structured, ranked list of likely public concerns.

Each predicted concern should include:
- The Appendix G category it falls under (e.g., Biological Resources, Transportation, Noise)
- A brief description of the concern
- A rationale for why this concern is likely to be raised
- Optionally, citations from similar past CEQA projects (see Pinecone below)

### Bonus: RAG with Past CEQA Projects

We maintain a Pinecone vector database containing chunked text from past CEQA documents. You can use this to find similar past projects and cite specific precedent for each predicted concern.

See `PINECONE.md` for connection details and usage instructions.

## Sample Data

The `samples/` directory contains example project descriptions you can use to test your tool. These are real CEQA projects at various stages.

## Done When

- Your tool produces useful predictions for at least three different project descriptions.
- Your README (update this one) explains how you grounded the output (basic version) or how you built the retrieval system (bonus version).
- You've evaluated the quality of predictions against what was actually raised in at least one real project's comment period.

## Getting Started

1. Use an AI API of your choice (OpenAI, Anthropic, Google, etc.) with your own API key. We'll refund you for API costs.
2. Review the sample project descriptions in `samples/`.
3. Read enough about CEQA Appendix G to understand the standard impact categories. The CEQA Guidelines are publicly available.
4. For the RAG bonus, see `PINECONE.md` for how to query the vector database of past CEQA documents.
5. Build your tool, test it against the samples, and iterate.

## What to Send Back

When you're done, please update this README with:

- How to run the tool
- Your approach to predicting concerns and ranking them
- How you handled the RAG component (if attempted)
- What surprised you
- What you'd do with more time
- How you'd evaluate whether this actually works in practice

Also include:

- A rough total of the hours you spent, so we can compensate you for your time.
- Any questions you'd want to ask us before shipping something like this for real.
