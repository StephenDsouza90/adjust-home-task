def process_parameters(request):
    """
    Processes the request from the api based on the query parameter.

    :param request: Request data from the api
    :return fields: Fields names from the query parameter
    :return filters: Filters names from the query parameter
    :return group_by: Group by names from the query parameter
    :return sort_by: Sort by names from the query parameter
    """

    fields = request.GET.get("fields")
    filters = request.GET.get("q")
    group_by = request.GET.get("group_by")
    sort_by = request.GET.get("sort_by")
    return fields, filters, group_by, sort_by

def get_column_names(fields, group_by):
    """
    Handles getting the correct column names for the select clause.
    If group by exists then the relevant columns in the cols_for_sum and cols_for_sum_and_round and aggregated.
    If the CPI excits, then the cpi is computed along with the relevant names.
    By default, if a column name is in the group by and not in fields then the name is added in the select clause.

    :param fields: Fields names from the query parameter
    :param group_by: Group by names from the query parameter
    :select_clause group_by: Structured column names for the select clause
    """

    if not fields:
        return " * "

    cols = []
    fields_list = fields.split(",")
    compute_cpi = "cpi" in fields_list
    fields_list = [f for f in fields_list if f != "cpi"]
    cols_for_sum = ["impressions", "clicks", "installs"]
    cols_for_sum_and_round = ["spend", "revenue"]
    if group_by:
        if compute_cpi:
            cols.append("ROUND((SUM(spend) / SUM(installs)), 2) as cpi")
        for f in fields_list:
            if f in cols_for_sum:
                cols.append("SUM({}) as {}".format(f, f))
            elif f in cols_for_sum_and_round:
                cols.append("ROUND(SUM({}), 2) as {}".format(f, f))
            else:
                cols.append(f)
        cols = cols + group_by.split(",")
    else:
        if compute_cpi:
            cols.append("ROUND((spend / installs), 2) as cpi")
        cols = cols + fields_list
    select_clause = ", ".join(cols)
    return select_clause

def get_filters(q):
    """
    Handles getting the correct column names and values for the where clause.
    - gte stands for greater then and equal to
    - gt stands for greater than
    - lte stands for less than and equals to
    - lt stands for less than

    :param q: Filters names from the query parameter
    :return where_clause: Structured where clause containing the column name and value
    """

    if not q:
        return ""

    filters = []
    for filter in q.split(","):
        col, val = filter.split(":")
        actual_col = col.split(".")[0]
        if "." in col:
            if ".gte" in col:
                filters.append("{} >= '{}'".format(actual_col, val))
            elif ".gt" in col:
                filters.append("{} > '{}'".format(actual_col, val))
            elif ".lte" in col:
                filters.append("{} <= '{}'".format(actual_col, val))
            elif ".lt" in col:
                filters.append("{} < '{}'".format(actual_col, val))
        else:
            filters.append("{}='{}'".format(actual_col, val))

    where_clause = " AND ".join(filters)
    where_clause = f" WHERE {where_clause} "
    return where_clause

def get_group_by(group_by):
    """
    Handles getting the correct column names for the group by clause.

    :param group_by: Group by names from the query parameter
    :return group_by: Group by column names for the group by clause
    """

    if group_by:
        return f" GROUP BY {group_by} "
    else:
        return ""

def get_order_by(sort_by):
    """
    Handles getting the correct column names and order type for the order by clause.
    By default, the order type is asc order if no instruction is in the parameter.

    :param sort_by: Sort by names from the query parameter
    :param sort_by: Sort by column names for order by clause
    """

    if not sort_by:
        return ""

    cols = []
    for col in sort_by.split(","):
        order_type = "asc"
        if ":" in col:
            actual_col, order_type = col.split(":")
        else:
            actual_col = col
        cols.append(f"{actual_col} {order_type}")

    order_by_clause = ", ".join(cols)
    return f"ORDER BY {order_by_clause}"
