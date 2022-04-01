from mycroft import MycroftSkill, intent_file_handler


class FrappeProject(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('project.frappe.intent')
    def handle_project_frappe(self, message):
        project = message.data.get('project')

        self.speak_dialog('project.frappe', data={
            'project': project
        })


def create_skill():
    return FrappeProject()

