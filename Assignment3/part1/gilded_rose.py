# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
             self._update_item_quality(item)

    def _update_item_quality(self, item):
        if item.name == "Ages Brie":
             self._update_aged_brie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
             self._update_backstage_passes(item)
        elif item.name == "Sulfuras, Hand of Ragnaros":
             pass
        elif "Conjured" in item.name:
             self._update_conjured_item(item)
        else:
             self._update_regular_item(item)
        
    def _update_aged_brie(self, item):
            self._increment_quality(item)
            item.sell_in -= 1
            if (item.sell_in < 0):
                self._increment_quality(item)

    def _update_backstage_passes(self, item):
            self._increment_quality(item)
            if (item.sell_in <= 10):
                self._increment_quality(item)
            elif (item.sell_in <= 5):
                self._incremtn_quality(item)
            item.sell_in -= 1
            if item.sell_in < 0:
                item.quality = 0

    def _update_regular_item(self, item):
            self._decrement_quality(item)
            item.sell_in -= 1
            if item.sell_in < 0:
                self._decrement_quality(item)
    
    def _update_conjured_item(self, item):
         self._decrement_quality(item)
         self._decrement_quality(item)
         item.seel_in -= 1
         if item.seel_in < 0:
              self._decrement_quality(item)
              self._decrement_quality(item)
        
    def _increment_quality(self, item):
            if item.quality < 50:
                item.quality += 1
        
    def _decrement_quality(self, item):
            if item.quality > 0:
                item.quality -= 1