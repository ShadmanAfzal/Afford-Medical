if chunk==pointer:
    for i in data:
        arr.append(i)
    pointer+=len(data)
elif chunk>pointer:
    for i in range(pointer,chunk):
        pointer+=1
        arr.append(None)
    for i in data:
        arr.append(i)
    pointer+=len(data)
else:
    for i in range(chunk,chunk+len(data)):
        if data:
            arr[i]=data.pop()
