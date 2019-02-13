## Questions
1. What are the strengths and weaknesses of each implementation? When is each fast or slow?

  The Python list queue should perform better when there are more enqueues, because enqueues are O(1) and dequeues are O(N) (because the entire list needs to be shifted when the first item is removed). * Why does this not seem true in the results?

  The linked list queue performs much better when there are more dequeues, although both are O(N). This may be because enqueueing requires the creation of a new linked list node.

  The ring buffer queue performs worse when there are many more enqueues than dequeues, because it needs to take time to double in size every time it fills up its array.

2. Is there an obvious winner across all scenarios?

  Yes, the fastest in all scenarios was the circular buffer queue.

3. The simulations we’ve provided perform operations in random orders. Is there a non-random series of operations you’d expect to be fast or slow for any of these structures?

  Python List Queue: dequeues require moving over all the items in the list, so doing dequeues when the list is short should be faster (thus alternating enqueues and dequeues)

  Linked List Queue: Not sure.

  Ring Buffer Queue: I would expect a series of many enqueues, and then many dequeues to be slow because the internal array would have to grow to a maximum size to accomplish this. On the other hand, I would expect alternating enqueues and dequeues (which would limit the number of times the array has to expand) to be fast.



## Results (sorry for formatting)
Benchmarking for P(enqueue)=0.5, P(dequeue)=0.5

                     enqueues/sec	dequeues/sec	max queue size	totals/sec
                     ---		---		---		---
PythonListQueue      191205		191023		962		382227
LinkedListQueue      143787		143679		703		287466
RingBufferQueue      148878		148675		1056		297552

Benchmarking for P(enqueue)=0.6, P(dequeue)=0.4

                     enqueues/sec	dequeues/sec	max queue size	totals/sec
                     ---		---		---		---
PythonListQueue      56893		37866		91344		94759
LinkedListQueue      108521		72287		174819		180808
RingBufferQueue      127823		85180		204800		213003

Benchmarking for P(enqueue)=0.4, P(dequeue)=0.6

                     enqueues/sec	dequeues/sec	max queue size	totals/sec
                     ---		---		---		---
PythonListQueue      174319		174319		16		348637
LinkedListQueue      137050		137049		16		274099
RingBufferQueue      148393		148393		17		296785

Benchmarking for P(enqueue)=0.49, P(dequeue)=0.51

                     enqueues/sec	dequeues/sec	max queue size	totals/sec
                     ---		---		---		---
PythonListQueue      181823		181820		140		363644
LinkedListQueue      135108		135108		98		270215
RingBufferQueue      161109		161109		98		322218
