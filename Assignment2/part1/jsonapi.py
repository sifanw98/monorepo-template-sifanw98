import json

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return{"__extended_json_type__": "complex", "values": [obj.real, obj.imag]}
        elif isinstance(obj, range):
            return{"__extended_json_type__": "range", "values": [obj.start, obj.stop, obj.step]}
        return json.JSONEncoder.default(self, obj)
    
class ComplexDecoder(json.JSONDecoder):
    def __init__(self, **kwargs):
        kwargs["object_hook"] = self.object_hook
        super().__init__(**kwargs)

    def object_hook(self, obj):
        try:
            name = obj["__extended_json_type__"]
            decoder = getattr(self, f"decode_{name}")
        except (KeyError, AttributeError):
            return obj
        else:
            return decoder(obj)
    
    def decode_range(self, obj):
         start, stop, step = obj["values"]
         return range(start, stop, step)
    
    def decode_complex(self, obj):
         real, imag = obj["values"]
         return complex(real, imag)
    
def dumps(obj, **kwargs):
        return json.dumps(obj, cls=ComplexEncoder, **kwargs)

def loads(s, **kwargs):
        return json.loads(s, cls=ComplexDecoder, **kwargs)