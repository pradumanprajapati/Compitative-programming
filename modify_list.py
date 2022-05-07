def modify_list(linked_list):
    head_node=linked_list.get_head()
    while head_node.get_next().get_next()!=None:
        temp=head_node.get_next().get_next()
        if temp.get_data()>head_node.get_data():
            data=head_node.get_data()
            head_node.set_data(head_node.get_next().get_data)
            head_node.get_next().set_data(data)
        else:
            head_node.set_data(temp.get_data()-1)
        head_node=head_node.get_next()
linked_list=list(input())
print(linked_list)