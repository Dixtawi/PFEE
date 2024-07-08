def filter_cv(dataset):
    """Filter dataset to remove cv with 0 jobs.

    Args:
        dataset (pandas.DataFrame): Dataset to filter, needs to have a number_jobs column.

    Returns:
        pandas.DataFrame: The filtered dataset.
    """
    dataset = filter(lambda x: x['number_jobs'] == 0, dataset)
    return dataset