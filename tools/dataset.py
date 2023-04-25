# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_dataset.ipynb.

# %% auto 0
__all__ = ['Data']

# %% ../nbs/03_dataset.ipynb 3
from fastbook import *

# %% ../nbs/03_dataset.ipynb 4
class Data:
    """
    A class for fetching various datasets.
    """

    ANTIBIOTICS_URL = "https://github.com/sky1ove/tools/raw/main/dataset/antibiotics_2335.csv"
    G12D_URL = "https://github.com/sky1ove/tools/raw/main/dataset/KRASi_g12d.csv"
    G12D_IC50_URL = "https://github.com/sky1ove/tools/raw/main/dataset/dedup_IC50.csv"
    KSEQ_URL = "https://github.com/sky1ove/tools/raw/main/dataset/kras_seq.csv"

    def __init__(self):
        pass
    
    @staticmethod
    def get_antibiotics():
        """
        Fetches the deduplicated dataset from the cell paper: 
        A Deep Learning Approach to Antibiotic Discovery.
        """
        df = pd.read_csv(Data.ANTIBIOTICS_URL)
        return df
    
    @staticmethod
    def get_g12d():
        """
        Fetches the G12D dataset from the paper and patents.
        """
        df = pd.read_csv(Data.G12D_URL)
        return df
    
    @staticmethod
    def get_g12d_IC50():
        """
        Fetches the deduplicated IC50 G12D dataset from the paper and patents.
        """
        df = pd.read_csv(Data.G12D_IC50_URL)
        return df
    
    @staticmethod
    def get_kseq():
        """
        Fetches the sequence of KRAS and its mutations G12D and G12C.
        """
        df = pd.read_csv(Data.KSEQ_URL)
        return df
