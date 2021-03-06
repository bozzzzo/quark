from quark_runtime import *



def test_assembling():
    innerObject = _JSONObject();
    (innerObject).setObjectItem(u"astring", (_JSONObject()).setString(u"string value"));
    (innerObject).setObjectItem(u"aint", (_JSONObject()).setNumber(9));
    (innerObject).setObjectItem(u"atrue", (_JSONObject()).setBool(True));
    (innerObject).setObjectItem(u"afalse", (_JSONObject()).setBool(False));
    (innerObject).setObjectItem(u"anull", (_JSONObject()).setNull());
    innerList = _JSONObject();
    (innerList).setListItem(0, (_JSONObject()).setString(u"after this string expect 42 and null"));
    (innerList).setListItem(1, (_JSONObject()).setNumber(42));
    (innerList).setListItem(2, (_JSONObject()).setNull());
    outer = _JSONObject();
    (outer).setObjectItem(u"sub-object", innerObject);
    (outer).setObjectItem(u"sub-list", innerList);
    (outer).setObjectItem(u"sub-string", (_JSONObject()).setString(u"a string"));
    _println((outer).toString());

def call_main(): import sys; main(_List(sys.argv[1:]))
def main(args):
    test_assembling();
