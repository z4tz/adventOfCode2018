from inputreader import aocinput
import networkx as nx


class Worker:
    def __init__(self):
        self.currentJob = None
        self.completeAt = None

    def startWork(self, Job, currentTime):
        self.currentJob = Job
        self.completeAt = currentTime + 60 + ord(Job) - 64  # -64 as ord('A') = 65

    def comepleteWork(self):
        job = self.currentJob
        self.currentJob = None
        self.completeAt = None
        return job


def order(steps):
    edges = []
    for step in steps:
        split = step.split()
        edges.append((split[1], split[7]))
    graph = nx.DiGraph()
    graph.add_edges_from(edges)

    order = []
    queue = [node for node in graph.nodes() if len(list(graph.predecessors(node))) == 0]

    def available(node, completed):
        for prereq in graph.predecessors(node):
            if prereq not in completed:
                return False
        return True

    while queue:
        queue.sort()
        node = queue.pop(0)
        order.append(node)
        queue.extend([successor for successor in graph.successors(node) if available(successor, order)])

    # part 2
    queue = [node for node in graph.nodes() if len(list(graph.predecessors(node))) == 0]
    workers = [Worker() for _ in range(5)]

    completedWork = []
    time = 0
    while True:
        complete = [worker.comepleteWork() for worker in workers if time == worker.completeAt]
        completedWork.extend(complete)

        for work in complete:
            for successor in graph.successors(work):
                if available(successor, completedWork) and successor not in queue:
                    queue.append(successor)
        queue.sort()
        availableWorkers = [worker for worker in workers if worker.currentJob is None]
        for i in range(min([len(availableWorkers), len(queue)])):
            availableWorkers[i].startWork(queue.pop(0), time)

        try:  # if all workers are done list will be empty and we continue
            time = min([worker.completeAt for worker in workers if worker.completeAt is not None])
        except ValueError:
            break

    return ''.join(order), time


def main(day):
    data = aocinput(day)
    print(order(data))


if __name__ == '__main__':
    main(7)
