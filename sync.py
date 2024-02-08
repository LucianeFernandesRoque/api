import time

def sync_task(task_id):
    print(f'começando uma nova tarefa de sincronização: {task_id}')
    time.sleep(2)
    print(f' Terminando a tarefa de sincronização {task_id}')

start_time = time.time()

sync_task(1)
sync_task(2)
sync_task(3)

print(f'Tempo decorrido: {time.time() - start_time:.2f}s ')