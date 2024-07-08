def format_data(data, format_type):
    """Format data to the expected format if valid.

    Args:
        data (pandas.DataFrame): The DataFrame containing data.
        format_type (string): Expected format type to convert the data.

    Returns:
        pandas.DataFrame: The formated dataframe if format_type is valid, else the original dataframe.
    """
    if format_type == "JSON":
        return data.toJSON()
    elif format_type == "CSV":
        return data.toCSV()
    else:
        print("Wrong format")
    return data