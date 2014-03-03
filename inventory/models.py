from django.db import models
from parts.models import Part
from django.db.models import Avg, Sum
from django.contrib.auth.models import User

class InventoryLocation(models.Model):
    """
    A specific physical location in a warehouse.
    """
    location_code = models.CharField(max_length=32, unique=True)
    
    def __unicode__(self):
        return self.location_code
        
    @models.permalink
    def get_absolute_url(self):
        return ('inventory.views.location', [str(self.location_code)])
        
            
class InventoryItem(models.Model):
    """
    An inventory object
    """
    UOM_CHOICES = (
                    ('EA', 'Each'),
                    ('LB', 'Pound'),
                    ('FT', 'Foot'),
                    ('IN', 'Inch'),
                 )
                 
    part_number = models.ForeignKey(Part)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    stocking_uom = models.CharField(max_length=4, choices=UOM_CHOICES)
    
    def __unicode__(self):
        return self.part_number
    
class InventoryTag(models.Model)
    """
    A physical inventory item, which is identified by its tag number. Related
    to `InventoryItem` and `InventoryLocation`.
    """
    tag_number = models.IntegerField()
    item = models.ForeignKey(InventoryItem)
    location = models.ForeignKey(InventoryLocation)
    lot_number = models.CharField()
    vendor = models.ForeignKey(Vendor)
    unit_cost = models.DecimalField()
    receiving_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.tag_number
    
    


