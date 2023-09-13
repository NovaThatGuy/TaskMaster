from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class TaskMasterApp(App):
    tasks = {'Low': [], 'Medium': [], 'High': []}

    def build(self):
        return self.root

    def add_task(self):
        task_text = self.root.ids.task_input.text
        importance_level = self.root.ids.importance_spinner.text

        if task_text and importance_level != 'Select Importance':
            self.tasks[importance_level].append(task_text)
            self.update_priority_columns()
            self.update_task_list()

            # Clear input fields and dropdown selection
            self.root.ids.task_input.text = ''
            self.root.ids.importance_spinner.text = 'Select Importance'

    def update_task_list(self):
        task_list_grid = self.root.ids.task_list_grid
        task_list_grid.clear_widgets()

        for importance, task_item_list in self.tasks.items():
            for task in task_item_list:
                task_label = Label(text=f"Task: {task}\nImportance: {importance}")
                task_list_grid.add_widget(task_label)

    def update_priority_columns(self):
        low_priority_grid = self.root.ids.low_priority_tasks
        medium_priority_grid = self.root.ids.medium_priority_tasks
        high_priority_grid = self.root.ids.high_priority_tasks

        # Clear existing widgets in the priority columns
        low_priority_grid.clear_widgets()
        medium_priority_grid.clear_widgets()
        high_priority_grid.clear_widgets()

        # Populate the priority columns based on importance level
        for importance, task_item_list in self.tasks.items():
            for task in task_item_list:
                task_label = Label(text=f"Task: {task}\nImportance: {importance}")
                if importance == 'Low':
                    low_priority_grid.add_widget(task_label)
                elif importance == 'Medium':
                    medium_priority_grid.add_widget(task_label)
                elif importance == 'High':
                    high_priority_grid.add_widget(task_label)

if __name__ == '__main__':
    TaskMasterApp().run()
