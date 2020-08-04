import json, pprint

from json_processor.nested_json_processor import flatten_json

def run_json_processor(object, key):
    #Step 1: Convert object to JSON. json_dict will be of type dictionary
    json_dict = json.loads(object)

    #Step 2: Flatten out deeply nested JSON object
    flatten_json_dict = flatten_json(json_dict)

    pprint.pprint(flatten_json_dict)

    #Step 3: Search for input key in flattened JSON
    try:
        return flatten_json_dict[key]
    except Exception as e:
        return "Key Not Part of Input"

def main():

    object1 = '{"a":{"b":{"c":"d"}}}'
    key1 = 'a/b/c'
    print(run_json_processor(object1,key1))

    object2 = ' { "x": { "y": { "z": "a" } } }'
    key2 = 'x/y/z'
    print(run_json_processor(object2, key2))

    object3 = '{"row": {"elements": [{"distance": {"text": "94.6 mi","value": 152193},"duration": {"text": "1 hour 44 mins","value": 6227},"status": "OK"},{"distance": {"text": "200 mi","value": 177946},"duration": {"text": "5 hour 30 mins","value": 6228},"status": "OK"}]},"status": "OK"}'
    key3 = 'row/elements/1/duration/value'
    print(run_json_processor(object3, key3))

    object4 = '{"customer":{"name":"Harold","address":{"flat":"Apartment 68","street":"Canary Lane","city":"London","postcode":"WR1 2BZ"}}}'
    key4 = 'customer/address/city'
    print(run_json_processor(object4, key4))

    object5 = '{"cluster":{"info":"Cluster Name","health":"OK","pods":[{"info":"Pod1","health":"OK"}]}}'
    key5 = 'cluster/security'
    print(run_json_processor(object5, key5))

if __name__ == "__main__":
    main()