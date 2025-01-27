class BaseConverter(object):
    IGNORE = "converter_ignore"

    def __init__(self):
        self.format_name = None
        self.output_dir = None
        self.run_name = None
        self.input_assembly = None

    def check_format(self, *args, **kwargs):
        err_msg = (
            "Converter for %s format has no method check_format" % self.format_name
        )
        raise NotImplementedError(err_msg)

    def setup(self, *args, **kwargs):
        err_msg = "Converter for %s format has no method setup" % self.format_name
        raise NotImplementedError(err_msg)

    def convert_line(self, *args, **kwargs):
        err_msg = (
            "Converter for %s format has no method convert_line" % self.format_name
        )
        raise NotImplementedError(err_msg)

    def addl_operation_for_unique_variant(self, wdict, wdict_no):
        pass
