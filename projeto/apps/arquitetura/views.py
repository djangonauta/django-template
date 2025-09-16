from django_filters.views import FilterView


class ElidedListView(FilterView):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        page = self.request.GET.get(self.page_kwarg, 1)
        ctx["page_obj"].adjusted_elided_pages = ctx["paginator"].get_elided_page_range(
            page,
            on_each_side=1,
            on_ends=1,
        )

        filter_params = self.request.GET.copy()
        if "page" in filter_params:
            filter_params.pop("page")

        ctx["query_params"] = filter_params.urlencode()
        return ctx
