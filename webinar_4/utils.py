

def prefilter_items(data, take_n_popular=None, exclude_popular=None, filter_weeks_no_sold=None):
    # Уберем самые популярные товары (их и так купят)
    if exclude_popular is not None:
        popularity = data.groupby('item_id')['quantity'].sum().reset_index()
        popularity.rename(columns={'quantity': 'n_sold'}, inplace=True)
        top = popularity.sort_values('n_sold', ascending=False).head(exclude_popular).item_id.tolist()
        data.loc[data['item_id'].isin(top), 'item_id'] = 999999

    # Оставляем популярные товары
    if take_n_popular is not None:
        popularity = data.groupby('item_id')['quantity'].sum().reset_index()
        popularity.rename(columns={'quantity': 'n_sold'}, inplace=True)
        top = popularity.sort_values('n_sold', ascending=False).head(take_n_popular).item_id.tolist()
        data.loc[~data['item_id'].isin(top), 'item_id'] = 999999

    # Уберем товары, которые не продавались за последние n недель
    if filter_weeks_no_sold is not None:
        data.loc[data['week_no'] > filter_weeks_no_sold, 'item_id'] = 999999

    # Уберем не интересные для рекоммендаций категории (department)

    # Уберем слишком дешевые товары (на них не заработаем). 1 покупка из рассылок стоит 60 руб.

    # Уберем слишком дорогие товары

    return data


def postfilter_items(user_id, recommednations):
    pass
