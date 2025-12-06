# chart.py

# Import required libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style and context
sns.set_style("whitegrid")
sns.set_context("talk")  # Presentation-ready text sizes

# Generate synthetic data for customer support response times
np.random.seed(42)  # For reproducibility

data = {
    "Support Channel": np.repeat(["Email", "Chat", "Phone"], 100),
    "Response Time (minutes)": np.concatenate([
        np.random.normal(loc=60, scale=15, size=100),  # Email
        np.random.normal(loc=30, scale=10, size=100),  # Chat
        np.random.normal(loc=90, scale=20, size=100)   # Phone
    ])
}

# Convert to pandas DataFrame
df = pd.DataFrame(data)

# Create figure with exact 512x512 pixels
# 512 pixels / 100 dpi = 5.12 inches
plt.figure(figsize=(5.12, 5.12), dpi=100)

# Create violin plot
sns.violinplot(
    x="Support Channel",
    y="Response Time (minutes)",
    data=df,
    palette="Set2",
    inner="quartile"  # Shows median and quartiles
)

# Add titles and labels
plt.title("Customer Support Response Time Distribution by Channel")
plt.xlabel("Support Channel")
plt.ylabel("Response Time (minutes)")

# Save chart as PNG exactly 512x512 pixels
plt.savefig("chart.png", dpi=100)  # No bbox_inches='tight' to preserve size

# Optional: show plot
plt.show()
