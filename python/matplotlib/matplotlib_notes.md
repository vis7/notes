# bar plot
stay_count = df['Stay'].value_counts()
ax = sns.barplot(stay_count.index, stay_count.values)

ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.tight_layout()
plt.show()



