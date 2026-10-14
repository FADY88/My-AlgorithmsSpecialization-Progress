# Jobs scheduling algorithm is my first greedy algorithm
# jobs is a tuple of (weight, length)
def schedule(jobs):
  scheduledJobs = sorted(jobs, key=lambda x: x[0] / x[1], reverse=True)
  completionTime = 0
  time = 0
  for x in scheduledJobs:
    completionTime += (x[1] + time) * x[0]
    time += x[1]
  return (scheduledJobs, completionTime)

if __name__ == "__main__":
  jobs = [(1, 2), (2, 3), (3, 4), (4, 5)]
  assert schedule(jobs) == ([(4, 5), (3, 4), (2, 3), (1, 2)], 85), "Test case 1 failed"
  jobs = [(3, 5), (1, 2)]
  assert schedule(jobs) == ([(3, 5), (1, 2)], 22), "Test case 2 failed"
