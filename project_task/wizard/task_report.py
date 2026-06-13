from odoo import api, fields, models


class TaskReport(models.TransientModel):
    _name = "task.report"
    _description = "Task Report "

    from_time = fields.Date(string='From Date')
    to_time = fields.Date(string='To Date')

    project_task_ids = fields.Many2many('project.project', 'project_task_details_rel', 'project_id', 'task_id',
                                        'Project', )

    def action_search_print(self):
        vals = {}
        task_list = []
        data = {
            'model': 'project.task',
            'form': self.read()[0]
        }
        tasks = self.env['project.task'].search([])
        for task in tasks:
            for project in self.project_task_ids:
                if project.id == task.project_id.id:
                    if (task.date_deadline >= self.from_time) and (task.date_deadline <= self.to_time):
                        vals = {'task': task.name, 'date': task.date_deadline, 'description': task.description}
                        task_list.append(vals)

            data['tasks'] = task_list
        return self.env.ref('project_task.action_task_report').report_action(self, data=data)
