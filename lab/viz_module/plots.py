"""Módulo 4 — Visualização de Dados.

Complete cada função com o apoio do GitHub Copilot. Cada função deve **gerar um
gráfico e salvá-lo** no caminho ``out_path`` (formato PNG). Use ``matplotlib`` e
``seaborn``. Em ambientes sem interface gráfica (CI), mantenha o backend "Agg".

Valide com:  ``python lab/check.py --module viz``
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # backend sem interface gráfica (funciona no CI)
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import seaborn as sns  # noqa: E402


def _save_figure(fig, out_path: str):
    """Salva a figura em PNG, cria a pasta de destino se necessário e a fecha."""
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, format="png", dpi=100, bbox_inches="tight")
    plt.close(fig)
    return fig


def plot_rating_distribution(df: pd.DataFrame, out_path: str):
    """Histograma da distribuição da coluna ``rating``. Inclua título e labels em
    português e salve a figura em ``out_path``."""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df["rating"].dropna(), bins=20, color="#722f37", edgecolor="white")
    ax.set_title("Distribuição das notas (rating)")
    ax.set_xlabel("Nota (rating)")
    ax.set_ylabel("Quantidade de vinhos")
    return _save_figure(fig, out_path)


def plot_top_varieties(df: pd.DataFrame, out_path: str):
    """Gráfico de barras horizontais com as 10 variedades (``variety``) com maior
    quantidade de vinhos. Salve a figura em ``out_path``."""
    top = df["variety"].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(top.index.astype(str), top.values, color="#722f37")
    # barh desenha a primeira categoria embaixo; inverte para a maior ficar no topo.
    ax.invert_yaxis()
    ax.set_title("Top 10 variedades por quantidade de vinhos")
    ax.set_xlabel("Quantidade de vinhos")
    ax.set_ylabel("Variedade (variety)")
    return _save_figure(fig, out_path)


def plot_boxplot_by_variety(df: pd.DataFrame, out_path: str):
    """Boxplot de ``rating`` para as 5 variedades mais frequentes. Salve a figura
    em ``out_path``."""
    top5 = df["variety"].value_counts().head(5).index
    subset = df[df["variety"].isin(top5)]
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.boxplot(data=subset, x="variety", y="rating", order=list(top5), ax=ax)
    ax.set_title("Distribuição de rating nas 5 variedades mais frequentes")
    ax.set_xlabel("Variedade (variety)")
    ax.set_ylabel("Nota (rating)")
    return _save_figure(fig, out_path)
