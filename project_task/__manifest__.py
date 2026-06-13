{
    'name': 'Project Task',
    'version': '14.0.2.1.0',
    'summary': 'Project Management',
    'sequence': 10,
    'description': """Project Management""",
    'category': 'Tutorials',


    'license': 'AGPL-3',
    'depends': [
        'project'
    ],
    'data':['security/ir.model.access.csv',
        'wizard/task_report_view.xml',
        'report/task_report_template.xml'],
    'demo': [],
    'qweb': [],

    'installable': True,
    'application': True,
    'auto_install': False,
}
