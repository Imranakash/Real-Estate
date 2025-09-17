from odoo import models, fields


class PropertyType(models.Model):
    _name = "real.estate.property.type"
    _description = "Property Type"

    name = fields.Char(string="Property Type", required=True)
    description = fields.Char(string="Description")


class Property(models.Model):
    _name = "real.estate.property"
    _description = "Real Estate Property"

    name = fields.Char(string="Property Name", required=True)
    property_type_id = fields.Many2one("real.estate.property.type", string="Property Type")

    available_from = fields.Date(string="Available From")
    price = fields.Float(string="Price")
    size = fields.Float(string="Size (sq ft)")

    state = fields.Selection([
        ("draft", "Draft"),
        ("available", "Available"),
        ("sold", "Sold"),
        ("cancelled", "Cancelled")
    ], string="Status", default="draft")

    furnished = fields.Boolean(string="Is Furnished?")
    active = fields.Boolean(string="Active", default=True)
