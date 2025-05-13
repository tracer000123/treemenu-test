from django import template
from django.urls import resolve
from menu.models import MenuItem, Menu

register = template.Library()

def build_tree(items):
    """Build a nested dict {item: children} structure"""
    item_dict = {item['id']: {**item, 'children': []} for item in items}
    root_items = []
    for item in item_dict.values():
        parent_id = item['parent_id']
        if parent_id:
            item_dict[parent_id]['children'].append(item)
        else:
            root_items.append(item)
    return root_items

def mark_active(tree, current_path):
    for node in tree:
        node['active'] = node['url'] == current_path
        if node['children']:
            child_active = mark_active(node['children'], current_path)
            node['active'] = node['active'] or child_active
    return any(n['active'] for n in tree)

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path

    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu_tree': []}

    items = list(MenuItem.objects.filter(menu=menu)
                 .values('id', 'title', 'url', 'parent_id')
                 .order_by('order', 'title'))
    tree = build_tree(items)
    mark_active(tree, current_path)
    return {'menu_tree': tree}
