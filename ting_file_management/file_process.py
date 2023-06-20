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


process("statics/nome_pedro.txt", Queue())


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
