import os
import subprocess

DIR_PATH = r'C:\Users\ishan\Documents\Projects\Awesome-QLoRA'
README_PATH = os.path.join(DIR_PATH, 'README.md')

def run_cmd(cmd):
    subprocess.run(cmd, shell=True, cwd=DIR_PATH)

with open(README_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Step 1: Link bullets in tables
links_map = {
    '**4-bit NormalFloat (NF4) Data Type**': '[**4-bit NormalFloat (NF4) Data Type**](pages/nf4.md)',
    '**Double Quantization (DQ)**': '[**Double Quantization (DQ)**](pages/dq.md)',
    '**Paged Optimizers**': '[**Paged Optimizers**](pages/paged_optimizers.md)',
    '**The Baseline Framework (Dettmers et al., 2023)**': '[**The Baseline Framework (Dettmers et al., 2023)**](pages/baseline.md)',
    '**Initialization & Quantization Alignment (QA-LoRA / LoftQ, ~2023–2024)**': '[**Initialization & Quantization Alignment (QA-LoRA / LoftQ, ~2023–2024)**](pages/qa_lora.md)',
    '**Weight Decomposition Adaptations (DoRA + QLoRA, ~2024–Present)**': '[**Weight Decomposition Adaptations (DoRA + QLoRA, ~2024–Present)**](pages/dora.md)',
    '**PEFT + BitsAndBytes (The Reference Pipeline)**': '[**PEFT + BitsAndBytes (The Reference Pipeline)**](pages/peft_bnb.md)',
    '**Unsloth Optimized QLoRA**': '[**Unsloth Optimized QLoRA**](pages/unsloth.md)',
    '**Axolotl / DeepSpeed ZeRO-3 QLoRA**': '[**Axolotl / DeepSpeed ZeRO-3 QLoRA**](pages/axolotl.md)',
    '**Consumer-Grade Local Finetuning Hubs**': '[**Consumer-Grade Local Finetuning Hubs**](pages/local_hubs.md)',
    '**Enterprise Domain Adaptation Sprints**': '[**Enterprise Domain Adaptation Sprints**](pages/enterprise.md)',
    '**On-Device Edge Robotic Alignment**': '[**On-Device Edge Robotic Alignment**](pages/edge.md)'
}
for k, v in links_map.items():
    content = content.replace(k, v)
with open(README_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
run_cmd('git init && git add . && git commit -m "detailed pages created" && git push')

# Step 2: Decorate, SEO, emojis, badges, banner
badges = '<div align="center">\\n'
badges += '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a>\\n'
badges += '<a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>\\n'
badges += '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>\\n'
badges += '</div>\\n\\n'

banner = '<div align="center">\\n<img src="assets/banner.svg" alt="Awesome QLoRA Banner" />\\n</div>\\n\\n'

if '# Awesome-QLoRA' in content:
    content = content.replace('# Awesome-QLoRA', banner + badges + '# 🌟 Awesome-QLoRA 🌟\\n> **An exhaustive, SEO-friendly guide to Quantized Low-Rank Adaptation (QLoRA) for massive language models.**')
else:
    content = banner + badges + '# 🌟 Awesome-QLoRA 🌟\\n' + content

content = content.replace('## 1. The Core Architectural Innovations', '## 🏗️ 1. The Core Architectural Innovations')
content = content.replace('## 2. The Chronological Evolution & Variants', '## ⏳ 2. The Chronological Evolution & Variants')
content = content.replace('## 3. Structural Scaling & Implementation Types', '## 🚀 3. Structural Scaling & Implementation Types')
content = content.replace('## 4. Production & Downstream Applications', '## 🏭 4. Production & Downstream Applications')

with open(README_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
run_cmd('git add . && git commit -m "seo optimised and decorated" && git push')

# Step 3: Star History (with chartrepos initially so we can replace it later)
star_history = """
## ⭐️ Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007/Awesome-QLoRA&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chartrepos=ishandutta2007/Awesome-QLoRA&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chartrepos=ishandutta2007/Awesome-QLoRA&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chartrepos=ishandutta2007/Awesome-QLoRA&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
content += star_history
with open(README_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
run_cmd('git add . && git commit -m "star history added" && git push')

# Step 4: Fixed star plot (chartrepos -> chart?repos)
content = content.replace('chartrepos', 'chart?repos')
with open(README_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
run_cmd('git add . && git commit -m "fixed star plot" && git push')

# Step 5: Invalid awesome link fixed
if 'https://github.com/sindresorhus/awesome' not in content:
    content += '\\n\\n[Awesome Link](https://github.com/sindresorhus/awesome)'
content = content.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')
with open(README_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
run_cmd('git add . && git commit -m "invalid awesome link fixed" && git push')

