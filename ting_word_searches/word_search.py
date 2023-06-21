from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
from ting_file_management.file_process import process


def exists_word(word: str, instance: Queue):
    queue = instance._queue
    occurrences = {}
    for file in queue:
        for i in range(len(file["linhas_do_arquivo"])):
            if word.lower() in file["linhas_do_arquivo"][i].lower():
                file_name = file["nome_do_arquivo"]
                occurrence = {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": [{"linha": i + 1}],
                }
                if file_name not in occurrences:
                    occurrences[file_name] = occurrence
                else:
                    occurrences[file_name]["ocorrencias"].append(
                        occurrence["ocorrencias"][0]
                    )
    return list(occurrences.values())


q = Queue()
process("statics/nome_pedro.txt", q)

print("aaaaaaaaaa", q._queue)

print("bbbbbbbbbb", exists_word("pedro", q))


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
