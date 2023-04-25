# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_plot.ipynb.

# %% auto 0
__all__ = ['reduce_dim', 'plot_cluster', 'plot_corr']

# %% ../nbs/01_plot.ipynb 3
from fastbook import *
import seaborn as sns

#for embeddings
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from umap.umap_ import UMAP

# %% ../nbs/01_plot.ipynb 5
from .feature import *
from .dataset import Data

# %% ../nbs/01_plot.ipynb 6
sns.set(rc={"figure.dpi":300, 'savefig.dpi':300})
sns.set_context('notebook')
sns.set_style("ticks")

# %% ../nbs/01_plot.ipynb 7
def reduce_dim(df, method='pca', n_components=2, seed=123):
    if method == 'pca':
        reducer = PCA(n_components=n_components, random_state=seed)
    elif method == 'tsne':
        reducer = TSNE(n_components=n_components, random_state=seed)
    elif method == 'umap':
        reducer = UMAP(n_components=n_components, random_state=seed)
    else:
        raise ValueError('Invalid method specified')
        
    proj = reducer.fit_transform(df.iloc[:, 1:])
    embedding_df = pd.DataFrame(proj, columns=[f"{method.upper()}{i}" for i in range(1, n_components + 1)])
    embedding_df = pd.concat([df[df.columns[0]], embedding_df], axis=1)
    return embedding_df

# %% ../nbs/01_plot.ipynb 8
def plot_cluster(df, method='pca', hue=None, palette='tab10', legend=False):
    embedding_df = reduce_dim(df, method=method)
    x_col, y_col = [col for col in embedding_df.columns if col.startswith(method.upper())]
    sns.relplot(data=embedding_df, x=x_col, y=y_col, hue=hue, palette=palette, s=50, alpha=0.8, legend=legend)
    plt.xticks([])
    plt.yticks([])

# %% ../nbs/01_plot.ipynb 15
def plot_corr(x,#a column of df
              y,#a column of df
              xlabel=None,# x axis label
              ylabel=None,# y axis label
              order=3, # polynomial level, if straight, order=1 
             ):
    correlation, pvalue = spearmanr(x, y)
    sns.regplot(x=x,
            y=y,
            order=order,
            line_kws={'color': 'gray'}
           )
    
    if xlabel is not None:
        plt.xlabel(xlabel)
        
    if ylabel is not None:
        plt.ylabel(ylabel)

    plt.text(x=0.8, y=0.1, s=f'Spearman: {correlation:.2f}', transform=plt.gca().transAxes, ha='center', va='center');
