"""This module provides simple drawing utilities
"""
import re
import graphviz
from typing import Any
from pandas import DataFrame

from sklearn.tree import DecisionTreeClassifier, export_graphviz


def draw_tree(
    tree: DecisionTreeClassifier,
    df: DataFrame,
    size: int = 10,
    ratio: float = 0.6,
    precision: int = 2,
    **kwargs,
):
    """Draws a decision tree using graphviz

    Args:
        tree (DecisionTreeClassifier): The decision tree to draw
        df (DataFrame): The input dataframe
        size (int, int): The size of the image. Defaults to 10.
        ratio (float, float): _description_. Defaults to 0.6.
        precision (int, optional): _description_. Defaults to 2.

    Returns:
        Graphviz DOT Source: The GraphViz DOT Source Code
    """
    graphviz_source = export_graphviz(
        tree,
        out_file=None,
        feature_names=df.columns,
        filled=True,
        rounded=True,
        special_characters=True,
        rotate=False,
        precision=precision,
        **kwargs,
    )
    return graphviz.Source(
        re.sub("Tree {", f"Tree {{ size={size}; ratio={ratio}", graphviz_source)
    )
