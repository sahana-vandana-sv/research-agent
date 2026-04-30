# scratch/explore_beir.py
from datasets import load_dataset

print("Loading corpus...")
corpus_dataset = load_dataset("BeIR/scifact", "corpus", split="corpus")

print("Loading queries...")
queries_dataset = load_dataset("BeIR/scifact", "queries", split="queries")

# Look at the structure
print("\n--- Corpus columns ---")
print(corpus_dataset.column_names)

print("\n--- First 3 corpus entries ---")
for i, doc in enumerate(corpus_dataset):
    if i >= 3:
        break
    print(f"\nID: {doc['_id']}")
    print(f"Title: {doc['title']}")
    print(f"Text (first 200 chars): {doc['text'][:200]}")

print("\n--- Queries columns ---")
print(queries_dataset.column_names)

print("\n--- First 5 queries ---")
for i, q in enumerate(queries_dataset):
    if i >= 5:
        break
    print(f"ID: {q['_id']} | Text: {q['text']}")