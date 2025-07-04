import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")  # set a nice theme

class EDAVisualizer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def plot_product_distribution(self):
        plt.figure(figsize=(17, 9))
        # Convert to DataFrame for Seaborn compatibility with hue
        
        counts = self.df["Product"].value_counts().reset_index()
        counts.columns = ["Product", "Count"]
        
        ax = sns.barplot(data=counts, x="Product", y="Count", hue="Product", 
                     palette="Blues_d", legend=False)

        plt.title("Distribution of Complaints Across Products", fontsize=16, weight='bold')
        plt.xlabel("Product", fontsize=14)
        plt.ylabel("Number of Complaints", fontsize=14)
        plt.xticks(rotation=45, ha="right", fontsize=12)
        
       # Annotate bars with values
        for p in ax.patches:
            height = p.get_height()
            ax.annotate(f'{int(height):,}', (p.get_x() + p.get_width() / 2, height),
                        ha='center', va='bottom', fontsize=11, color='black', weight='bold')
        
        plt.tight_layout()
        plt.show()

    def plot_text_length_histogram(self):
        lengths = self.df["Consumer complaint narrative"].dropna().apply(lambda x: len(x.split()))
        plt.figure(figsize=(12, 7))

        # Plot histogram with KDE
        sns.histplot(lengths, bins=50, color="coral", kde=True, edgecolor="black", alpha=0.7)
        
        plt.title("Narrative Word Count Distribution", fontsize=16, weight='bold')
        plt.xlabel("Word Count", fontsize=14)
        plt.ylabel("Number of Complaints", fontsize=14)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()

    def narrative_stats(self):
        narratives = self.df["Consumer complaint narrative"].dropna()
        num_with = narratives.shape[0]
        num_without = self.df.shape[0] - num_with
        print(f"Complaints with narrative: {num_with:,}")
        print(f"Complaints without narrative: {num_without:,}")
