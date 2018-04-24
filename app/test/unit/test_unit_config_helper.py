import imp
import os
import re
import sys

module_name = 'halo'
here_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(here_dir, '../../')
sys.path.append(module_path)
fp, pathname, description = imp.find_module(module_name)
halo = imp.load_module(module_name, fp, pathname, description)
fixture_path = os.path.join(here_dir, "../fixture/")


class TestConfigHelper:
    def test_get_match_list(self):
        control = ["first_event_type", "secondeventtype", "third_event_type"]
        good_file = os.path.join(fixture_path, "good_events")
        processed = halo.ConfigHelper.get_match_list(good_file)
        assert control == processed

    def test_get_timestamp_inferred(self):
        result = halo.ConfigHelper.get_timestamp()
        print result
        assert re.match('^\d{4}-\d{2}-\d{2}$', result)
