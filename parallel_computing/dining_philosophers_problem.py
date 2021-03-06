import threading
import time

class Philosopher(threading.Thread):
    running = True

    def __init__(self, xname, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.name = xname
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight

    def run(self):
        while (self.running):
            time.sleep(10)
            print('%s is hungry.' % self.name)
            self.dine()

    def dine(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight

        while self.running:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()
            print('%s is changing forks' % self.name)
            fork1, fork2 = fork2, fork1
        else:
            return

        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        print('%s is eating. ' % self.name)
        time.sleep(10)
        print('%s has stopped eating.' % self.name)


def DiningPhilosophers():
    forks = [threading.Lock() for n in range(5)]
    philosopherNames = ('First', 'Second', 'Third', 'Fourth', 'Fifth')

    philosophers = [Philosopher(philosopherNames[i], forks[i % 5], forks[(i + 1) % 5]) for i in range(5)]

    Philosopher.running = True
    for p in philosophers: p.start()
    time.sleep(100)
    Philosopher.running = False

if __name__ == '__main__':
    DiningPhilosophers()