class HrEmployeeAdaptionProgram(models.Model):  # Corrected 'model.Models' to 'models.Model'
    _name = 'hr.employee.adaption.program'

    name = fields.Char('Register number')
    employee_id = fields.Many2one('hr.employee', string='Employee')
    department_id = fields.Many2one('hr.department', string='Department')  # Corrected 'hr.dempartment' to 'hr.department'
    job_id = fields.Many2one('hr.job', string='Job')
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('done', 'Done'),
                              ('cancelled', 'Cancelled')],
                              string="State", default='draft')
    line_ids = fields.One2many('hr.employee.adaption.program.line', 'adaption_id', string='Line id')  # Corrected 'fiels.One2many' to 'fields.One2many'

    @api.onchange('employee_id')
    def _onchange_employee_id(self):
        if self.employee_id:
            self.department_id = self.employee_id.department_id.id
            self.job_id = self.employee_id.job_id.id
     
    

class HrEmployeeAdaptionProgramLine(models.Model):  # Corrected 'model.Models' to 'models.Model'
    _name = 'hr.employee.adaption.program.line'

    adaption_id = fields.Many2one('hr.employee.adaption.program', string='line id')
    task_id = fields.Many2one('hr.employee.task', string='Task')
    gui_job = fields.Many2one('hr.job', string='Guidance staff')  # Corrected 'hr.joba' to 'hr.job'
    one_week = fields.Integer(string='One week')
    two_week = fields.Integer(string='Two week')
    three_week = fields.Integer(string='Three week')
    four_week = fields.Integer(string='Four week')
    five_week = fields.Integer(string='Five week')
    six_week = fields.Integer(string='Six week')