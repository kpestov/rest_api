from models import TreeNode


def get_all_elements():
    items = TreeNode.query.filter(TreeNode.parent_id == 2).all()
    names = [item.name for item in items]

    items_name = {}
    list_of_dicts = []

    for i in range(len(names)):
        items_name['name'] = names[i]
        print(items_name)
        list_of_dicts.append(items_name)

    return list_of_dicts