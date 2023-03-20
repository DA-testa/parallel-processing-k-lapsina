# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    threads = [0 for _ in range(n)]
    for job_index in range(m):
        next_thread_index = 0
        for thread_index in range(1, n):
            thread = threads[thread_index]
            next_thread = threads[next_thread_index]
            if thread < next_thread:
                next_thread_index = thread_index
        output.append((next_thread_index, threads[next_thread_index]))
        threads[next_thread_index] += data[job_index]

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    inp = input().split()
    n = int(inp[0])
    m = int(inp[1])

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread, time in result:
        print(f"{thread} {time}")


if __name__ == "__main__":
    main()