def update_queue(in_queue1,in_queue2):
    out_queue=Queue(in_queue1.get_max_size()+in_queue2)