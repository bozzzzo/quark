from quark_runtime import *



def test_building():
    _println(((((_JSONObject()).setObjectItem(u"sub-object", (((((_JSONObject()).setObjectItem(u"astring", (_JSONObject()).setString(u"string value"))).setObjectItem(u"aint", (_JSONObject()).setNumber(9))).setObjectItem(u"atrue", (_JSONObject()).setBool(True))).setObjectItem(u"afalse", (_JSONObject()).setBool(False))).setObjectItem(u"anull", (_JSONObject()).setNull()))).setObjectItem(u"sub-list", (((_JSONObject()).setListItem(0, (_JSONObject()).setString(u"after this string expect 42 and null"))).setListItem(1, (_JSONObject()).setNumber(42))).setListItem(2, (_JSONObject()).setNull()))).setObjectItem(u"sub-string", (_JSONObject()).setString(u"a string"))).toString());

def call_main(): import sys; main(_List(sys.argv[1:]))
def main(args):
    test_building();
