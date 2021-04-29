from pandas import read_csv
from django.http import HttpResponse, JsonResponse

from .queries import Queries
from .utils import process_parameters, get_column_names, get_filters, get_group_by, get_order_by


query = Queries()


class Views():
    """ Represents views which are mapped to a route """

    FILE_PATH = "adjust_app/adjust_home_task/raw_data/dataset.csv"

    def home(self, request):
        return HttpResponse("Hello, Welcome to the Adjust Home Task!")


    def add_performace_metrics_data(self, request):
        """
        Add the performace metrics data into the DB.
        Using itertuples() as it is more performant than iterrows().
        """

        data_frame = read_csv(self.FILE_PATH)
        for row in data_frame.itertuples():
            date = row[1]
            channel = row[2]
            country = row[3]
            operating_system = row[4]
            impressions = row[5]
            clicks = row[6]
            installs = row[7]
            spend = row[8]
            revenue = row[9]
            query.add_data(date, channel, country, operating_system, impressions,
                        clicks, installs, spend, revenue)

        return HttpResponse("Data added to the DB!")


    def get_performace_metrics_data(self, request):
        """
        Process the request from the api and delivers the response to the user.
        """

        if request.method == "GET":
            fields, filters_list, group_by_list, order_by_list = process_parameters(request)

            group_by = get_group_by(group_by_list)
            fields = get_column_names(fields, group_by)
            filters = get_filters(filters_list)
            order_by = get_order_by(order_by_list)

            results = query.get_data(fields, filters, group_by, order_by)
        return JsonResponse(results, safe=False)
