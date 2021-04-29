from django.db import connection

from .models import PerformanceMetrics


cursor = connection.cursor()


class Queries():
    """ Handles all interactions with the database """

    SELECT_STATEMENT = "SELECT {fields} FROM {table_name} WHERE {filters} GROUP BY {group_by} ORDER BY {order_by}"

    def add_data(self, date, channel, country, operating_system, impressions, clicks, installs, spend, revenue):
        """
        Adds the data into the database.
        """
        prototype = PerformanceMetrics()
        prototype.date = date
        prototype.channel = channel
        prototype.country = country
        prototype.operating_system = operating_system
        prototype.impressions = impressions
        prototype.clicks = clicks
        prototype.installs = installs
        prototype.spend = spend
        prototype.revenue = revenue
        prototype.save()

    def get_data(self, fields, filters, group_by, order_by):
        """
        Gets the data from the database.
        Corresponding data is mapped to the column names and saved in a list of dicts.

        :param fields: Column names for the select clause
        :param filters: Column names and values for the where clause
        :param group_by: Column names for the group by clause
        :param order_by: Column names for the order by clause
        :return json_data: List of returned results
        """

        table_name = PerformanceMetrics()._meta.db_table
        statement = Queries.SELECT_STATEMENT.format(fields=fields, table_name=table_name, filters=filters,
                                                    group_by=group_by, order_by=order_by)
        cursor.execute(statement)
        row_headers = [x[0] for x in cursor.description]
        results = cursor.fetchall()
        json_data = []
        for result in results:
                json_data.append(dict(zip(row_headers, result)))
        return json_data