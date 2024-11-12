"""nested class -> a class defined within another class.
class Outer:
    class Inner:
"""

class Work:

    class Billable:
        def __init__(self, task_title:str, is_billable:bool, time_spent:int, status:str ):
            self.task_title= task_title
            self.is_billable=is_billable
            self.time_spent=time_spent
            self.status=status

    def __init__(self, work_title:str):
        self.work_title=work_title
        self.billable_tasks=[]

    def add_billable_task(self, task_title:str, is_billable:bool, time_spent:int, status:str):
        new_task=self.Billable(task_title, is_billable, time_spent, status)
        self.billable_tasks.append(new_task)

    def list_billable_tasks(self):
        return self.billable_tasks

work1=Work('Testare automata')

work1.add_billable_task('Mentenanța testelor automate', True, 100, 'in progress...')
work1.add_billable_task ('Crearea și configurarea de teste automate', True, 200, 'in progress...')
work1.add_billable_task('Mentorat și coaching', False, 50, 'Completed')
work1.add_billable_task('Învățare și dezvoltare personală', False, 80, 'in progress...')
work1.add_billable_task('Documentarea testelor automate', True, 40, 'incomplete...')


for task in work1.list_billable_tasks():
    if task.is_billable:
        print(task.task_title)



