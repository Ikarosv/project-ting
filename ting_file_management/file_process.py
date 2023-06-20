from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file: str, instance: Queue):
    for path in instance._queue:
        if path["nome_do_arquivo"] == path_file:
            return print("Arquivo já importado", file=sys.stderr)
    content = txt_importer(path_file)
    print(content)
    queue_item = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "linhas_do_arquivo": content,
    }
    instance.enqueue(queue_item)
    print(queue_item, file=sys.stdout)


def remove(instance: Queue):
    if not len(instance._queue):
        return print("Não há elementos", file=sys.stdout)

    removed = instance.dequeue()
    if removed:
        print(
            f"Arquivo {removed['nome_do_arquivo']} removido com sucesso",
            file=sys.stdout,
        )


def file_metadata(instance, position):
    if position >= len(instance._queue):
        return print("Posição inválida", file=sys.stderr)

    print(instance.search(position), file=sys.stdout)
