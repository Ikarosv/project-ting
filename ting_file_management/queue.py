from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def enqueue(self, value):
        return self._queue.append(value)

    def dequeue(self):
        return self._queue.pop(0)

    def search(self, index):
        try:
            if index < 0:
                raise
            return self._queue[index]
        except:
            raise IndexError("Índice Inválido ou Inexistente")
