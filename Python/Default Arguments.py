def print_from_stream(n, stream=EvenStream()):
    if isinstance(stream, OddStream) : 
        Stream = OddStream()
    else:
        Stream = EvenStream()    
    for _ in range(n): 
        print(Stream.get_next()) 
