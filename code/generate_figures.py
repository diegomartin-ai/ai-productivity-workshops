import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

os.makedirs('../figures', exist_ok=True)

# Workflow comparison figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Traditional workflow
steps_trad = ['Literature\nReview', 'Data\nCleaning', 'Estimation', 'Interpretation', 'Writing']
times_trad = [5, 4, 3, 2, 4]
colors_trad = ['#c0c0c0'] * 5

ax1.barh(steps_trad, times_trad, color='#8c8c8c', edgecolor='#333333', height=0.6)
ax1.set_xlabel('Days (approximate)', fontsize=9)
ax1.set_title('Traditional Workflow', fontsize=11, fontweight='bold', color='#003f5f')
ax1.set_xlim(0, 6)
ax1.invert_yaxis()
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# AI-augmented workflow
steps_ai = ['Literature\nReview', 'Data\nCleaning', 'Estimation', 'Interpretation', 'Writing']
times_ai = [1, 1.5, 1.5, 1, 1]
colors_ai = ['#00a651'] * 5

ax2.barh(steps_ai, times_ai, color='#00a651', edgecolor='#003f5f', height=0.6)
ax2.set_xlabel('Days (approximate)', fontsize=9)
ax2.set_title('AI-Augmented Workflow', fontsize=11, fontweight='bold', color='#003f5f')
ax2.set_xlim(0, 6)
ax2.invert_yaxis()
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# Add tool labels on AI bars
tools = ['NotebookLM', 'Claude/Copilot', 'Claude/Copilot', 'ChatGPT', 'Claude']
for i, (t, tool) in enumerate(zip(times_ai, tools)):
    ax2.text(t + 0.15, i, tool, va='center', fontsize=7.5, color='#003f5f', style='italic')

plt.tight_layout()
plt.savefig('../figures/workflow_comparison.pdf', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: figures/workflow_comparison.pdf")
