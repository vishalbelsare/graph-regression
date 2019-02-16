import warnings

def _check_valid_graphs(graphs):
    """
    Checks if all graphs in list have same shapes.

    Raises an ValueError if there are more than one shape in the input list,
    or if the list is empty or has one element.

    Parameters
    ----------
    graphs : list
        List of array-like with shapes (n_vertices, n_vertices).

    Raises
    ------
    ValueError
        If all graphs do not have same shape, or input list is empty or has
        one element.
    """
    if len(graphs) <= 1:
        msg = "Regression methods requires more than one graph."
        raise ValueError(msg)

    shapes = set(map(np.shape, graphs))

    if len(shapes) > 1:
        msg = "There are {} different sizes of graphs.".format(len(shapes))
        raise ValueError(msg)
