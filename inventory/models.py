from django.db import models
from django.db.models import Avg, Sum

from purchasing.models import Vendor
from quality.models import Report

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
        ('C', 'Hundred'),
        ('M', 'Thousand'),
        ('CWT', 'Hundred Weight'),

    )
    
    PART_TYPES = (
        ('P', 'Purchased'),
        ('M', 'Manufactured'),
    )

    part_number = models.CharField(unique=True, max_length=64)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    part_type = models.CharField(max_length=1, choices=PART_TYPES, default='M')
    stocking_uom = models.CharField(max_length=4, choices=UOM_CHOICES, default='EA')
    purchasing_uom = models.CharField(max_length=4, choices=UOM_CHOICES, default='EA')
    part_weight = models.DecimalField(max_digits=10, decimal_places=10)

    def __unicode__(self):
        return self.part_number
    
class InventoryTag(models.Model):
    """
    A physical inventory item, which is identified by its tag number. Related
    to `InventoryItem` and `InventoryLocation`.
    """
    
    tag_number = models.IntegerField()
    item = models.ForeignKey(InventoryItem)
    location = models.ForeignKey(InventoryLocation)
    lot_number = models.ForeignKey(Report)
    vendor = models.ForeignKey(Vendor)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=10)
    receiving_date = models.DateTimeField(auto_now_add=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=10)
    
    def split_tag(self, quantity, location):
        """
        Splits a tag number into a new tag number. This is useful for situations
        in which a product with a single lot number will not phsycically fit in 
        a single location. This creates a new tag number and location, but
        retains all other information associated.
        """
        
        new_tag = InventoryTag(item=self.item, 
                                location=location, quantity=quantity)
        new_tag.save()
        self.quantity -= quantity
        self.save()
    
    def __unicode__(self):
        return self.tag_number   

class RoutingStep(models.Model):
    STEP_TYPES = (
        ('I', 'Internal'),
        ('E', 'External'),
    )
    
    TIME_INTERVALS = (
        ('S', 'Seconds'),
        ('M', 'Minutes'),
        ('H', 'Hours'),
    )
    
    part = models.ForeignKey(InventoryItem)
    step_number = models.IntegerField()
    setup_time = models.IntegerField()
    setup_interval = models.CharField(max_length=1, choices=TIME_INTERVALS)
    cycle_time = models.IntegerField()
    cycle_interval = models.CharField(max_length=1, choices=TIME_INTERVALS)
    
    class Meta:
        ordering = ['step_number']
        
    def __unicode__(self):
        return self.step_number

