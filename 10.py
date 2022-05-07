from multiprocessing import Queue


def update(num_queue):
    vall=0
    size=num_queue.get_max_size()
    out_queue=Queue(size)
    while(not num_queue.is_empty()):
        num=num_queue.dequeue()
        if num%4==0:
            vall+=num
            out_queue.enqueue(vall)
    return out_queue
    #both