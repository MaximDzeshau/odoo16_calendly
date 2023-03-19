from odoo import models, fields, api, _
from odoo.addons.calendly.utils import functions
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class Calendly(models.Model):
    _description = 'Calendly settings'
    _inherit = "res.users"
    
    start_work_hour = fields.Float(string=_("Start"), default=8.0)
    end_work_hour = fields.Float(string=_("End"), default=17.0)
    # groups_id = fields.Many2many('res.users', 'calendly_calendly_user_rel', 'calendly_id', 'user_id', string='Users')
    # company_ids = fields.Many2many('res.company', 'calendly_calendly_company_rel', 'calendly_id', 'company_id', string='Users')
    
    @api.constrains('start_work_hour')
    def _work_hour_validation(self):
        for time in self:
            if functions.float_to_time(time.start_work_hour) < '00:00' or functions.float_to_time(time.start_work_hour) > '23:59':
                raise ValidationError(_('The time value must be between 0:00 and 23:59!'))
            
    @api.constrains('end_work_hour')
    def _work_hour_validation(self):
        for time in self:
            if functions.float_to_time(time.end_work_hour) < '00:00' or functions.float_to_time(time.end_work_hour) > '23:59':
                raise ValidationError(_('The time value must be between 0:00 and 23:59!'))