from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class TaskMasterRoot(BoxLayout):
    pass

class TaskMasterApp(App):
    tasks = {'Low': [], 'Medium': [], 'High': []}

    def build(self):
        return TaskMasterRoot()

    def add_task(self):
        task_text = self.root.ids.task_input.text.strip()
        importance_level = self.root.ids.importance_spinner.text

        if task_text and importance_level != 'Select Importance':
            self.tasks[importance_level].append(task_text)
            self.update_priority_columns()

            # Clear input fields and dropdown selection
            self.root.ids.task_input.text = ''
            self.root.ids.importance_spinner.text = 'Select Importance'

    def update_task_list(self):
        # Clear existing widgets in the task_list_grid
        task_list_grid = self.root.ids.task_list_grid
        task_list_grid.clear_widgets()

        # Populate the task_list_grid based on importance level
        for importance in ['High', 'Medium', 'Low']:
            task_item_list = self.tasks.get(importance, [])
            for task in task_item_list:
                task_label = Label(text=f"Task: {task}\nImportance: {importance}")
                task_list_grid.add_widget(task_label)

    def update_priority_columns(self):
        # Clear existing widgets in the priority boxes
        low_priority_tasks_grid = self.root.ids.low_priority_tasks_grid
        medium_priority_tasks_grid = self.root.ids.medium_priority_tasks_grid
        high_priority_tasks_grid = self.root.ids.high_priority_tasks_grid

        low_priority_tasks_grid.clear_widgets()
        medium_priority_tasks_grid.clear_widgets()
        high_priority_tasks_grid.clear_widgets()

        # Populate the priority boxes based on importance level
        for task_importance in ['High', 'Medium', 'Low']:
            task_item_list = self.tasks.get(task_importance, [])
            for task in task_item_list:
                task_label = Label(text=f"Task: {task}\nImportance: {task_importance}")
                if task_importance == 'Low':
                    low_priority_tasks_grid.add_widget(task_label)
                elif task_importance == 'Medium':
                    medium_priority_tasks_grid.add_widget(task_label)
                elif task_importance == 'High':
                    high_priority_tasks_grid.add_widget(task_label)



if __name__ == '__main__':
    TaskMasterApp().run()
