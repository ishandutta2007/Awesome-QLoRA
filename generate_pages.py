import os

os.makedirs('pages', exist_ok=True)
os.makedirs('assets', exist_ok=True)

# Generate SVG Banner
svg_content = """<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200" viewBox="0 0 800 200">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4e54c8" />
      <stop offset="100%" stop-color="#8f94fb" />
    </linearGradient>
  </defs>
  <rect width="800" height="200" fill="url(#grad)" rx="15" ry="15"/>
  <text x="50%" y="50%" font-family="Arial, sans-serif" font-size="48" font-weight="bold" fill="white" text-anchor="middle" dominant-baseline="middle">
    Awesome QLoRA
  </text>
  <text x="50%" y="75%" font-family="Arial, sans-serif" font-size="20" fill="#f0f0f0" text-anchor="middle">
    Quantized Low-Rank Adaptation: Evolution, Variants, & Applications
  </text>
</svg>"""

with open('assets/banner.svg', 'w') as f:
    f.write(svg_content)

pages = [
    ("nf4.md", "4-bit NormalFloat (NF4) Data Type", "NF4 is an information-theoretically optimal data type...", "graph LR\\n A[32-bit Weights] --> B[Quantize to NF4]\\n B --> C[4-bit Storage]"),
    ("dq.md", "Double Quantization (DQ)", "Double Quantization reduces the memory footprint...", "graph LR\\n A[First Quantization] --> B[Quantization Constants]\\n B --> C[Second Quantization]"),
    ("paged_optimizers.md", "Paged Optimizers", "Paged Optimizers manage memory spikes...", "graph TD\\n A[GPU OOM Risk] -->|Evict| B[CPU RAM]\\n B -->|Prefetch| A"),
    ("baseline.md", "The Baseline Framework", "The original QLoRA framework...", "graph LR\\n A[Frozen 4-bit Base] --> B[Add 16-bit LoRA Adapters]"),
    ("qa_lora.md", "Initialization & Quantization Alignment", "QA-LoRA and LoftQ align quantization...", "graph TD\\n A[Base Initialization] --> B[Alternating Optimization]\\n B --> C[Matching Adapter Weights]"),
    ("dora.md", "Weight Decomposition Adaptations (DoRA)", "DoRA separates magnitude and direction...", "graph LR\\n A[Weight] --> B[Magnitude]\\n A --> C[Direction]"),
    ("peft_bnb.md", "PEFT + BitsAndBytes", "The standard HuggingFace implementation...", "graph LR\\n A[HuggingFace Hub] --> B[bitsandbytes]\\n B --> C[PEFT Model]"),
    ("unsloth.md", "Unsloth Optimized QLoRA", "Unsloth uses custom Triton kernels...", "graph TD\\n A[PyTorch] --> B[Triton Kernels]\\n B --> C[Faster Training]"),
    ("axolotl.md", "Axolotl / DeepSpeed ZeRO-3 QLoRA", "Multi-GPU distributed training...", "graph LR\\n A[Dataset] --> B[Axolotl Configuration]\\n B --> C[Multi-GPU Training]"),
    ("local_hubs.md", "Consumer-Grade Local Finetuning Hubs", "Ollama, LM Studio, etc...", "graph TD\\n A[Local Hardware] --> B[LM Studio / Ollama]\\n B --> C[Custom LLM]"),
    ("enterprise.md", "Enterprise Domain Adaptation Sprints", "Using private data to adapt models...", "graph LR\\n A[Private Data] --> B[QLoRA Finetuning]\\n B --> C[Domain Model]"),
    ("edge.md", "On-Device Edge Robotic Alignment", "Running models on edge devices...", "graph TD\\n A[Sensors] --> B[Edge Device QLoRA]\\n B --> C[Updated Policy]"),
]

for filename, title, desc, mermaid in pages:
    content = f"# {title}\\n\\n## Overview\\n{desc}\\n\\n## Architecture\\n```mermaid\\n{mermaid}\\n```\\n\\n[< Back to README](../README.md)"
    with open(f"pages/{filename}", 'w') as f:
        f.write(content)
