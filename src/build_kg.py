# src/build_kg.py
import os
import json
import re
import pandas as pd
from groq import Groq
from getpass import getpass

# ========================= CONFIG =========================
FILES = {
    "faculty": "data/raw/faculty_page.txt",
    "phd": "data/raw/phd_iiserb_page_clean.txt",
    "postdocs": "data/raw/postdocs_page_clean.txt",
    "research_groups": "data/raw/researchGroups_clean.txt",
    "bsms_3rd": "data/raw/bsms_3rd_year_page_clean.txt",
    "bsms_4th": "data/raw/bsms_4th_year_page_clean.txt",
    "bsms_5th": "data/raw/ms_5th_year_page_clean.txt"
}

MODEL = "llama-3.1-8b-instant"
CHUNK_SIZE = 2000
# =========================================================

def load_text_files():
    combined = ""
    for label, path in FILES.items():
        with open(path, "r", encoding="utf-8") as f:
            text = f.read().strip()
            combined += f"\n\n### PAGE: {label.upper()} ###\n{text}"
    return combined

def chunk_text(text, max_len=CHUNK_SIZE):
    return [text[i:i+max_len] for i in range(0, len(text), max_len)]

# Your schema_prompt here (same as in notebook)
schema_prompt = """..."""  # Paste the full schema_prompt here

def main():
    api_key = os.getenv("GROQ_API_KEY") or getpass("Enter GROQ_API_KEY: ")
    client = Groq(api_key=api_key)

    print("Loading text files...")
    text = load_text_files()
    chunks = chunk_text(text)
    print(f"Total chunks: {len(chunks)}")

    all_nodes = []
    all_edges = []

    for i, chunk in enumerate(chunks):
        print(f"\nProcessing chunk {i+1}/{len(chunks)}")
        prompt = schema_prompt + "\n\n### TEXT ###\n" + chunk

        try:
            resp = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                max_tokens=2400
            )
            out = resp.choices[0].message.content
            match = re.search(r"\[.*\]", out, re.DOTALL)
            if not match:
                print("No JSON found")
                continue
            data = json.loads(match.group(0))
        except Exception as e:
            print(f"Error: {e}")
            continue

        for item in data:
            if "node" in item:
                all_nodes.append(item["node"])
            for e in item.get("edges", []):
                all_edges.append(e)

    # Deduplicate
    unique_nodes = {n["id"]: n for n in all_nodes if "id" in n}
    nodes = list(unique_nodes.values())

    seen = set()
    edges = []
    for e in all_edges:
        if {"from", "relation", "to"} <= e.keys():
            key = (e["from"], e["relation"], e["to"])
            if key not in seen:
                seen.add(key)
                edges.append(e)

    print(f"Final Nodes: {len(nodes)} | Edges: {len(edges)}")

    # Save outputs
    os.makedirs("knowledge_graphs", exist_ok=True)
    with open("knowledge_graphs/dse_kg.json", "w") as f:
        json.dump({"nodes": nodes, "edges": edges}, f, indent=2)
    
    pd.DataFrame(nodes).to_csv("knowledge_graphs/nodes.csv", index=False)
    pd.DataFrame(edges).to_csv("knowledge_graphs/edges.csv", index=False)

    print("Knowledge Graph saved to knowledge_graphs/")

if __name__ == "__main__":
    main()
