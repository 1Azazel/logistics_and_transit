
best_route = ""


def get_route(route_list):
    if best_route in route_list:
        return best_route


def select_route(route_list):
    selected_route = get_route(route_list)
    return selected_route

