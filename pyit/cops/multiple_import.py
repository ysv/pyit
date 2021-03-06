from pyit.cop import IRawFileCop, Cop, IFormatCop
from pyit.utils import line_indent
from tokenize import tokenize, untokenize
from pyit.offence import Offence
from io import BytesIO


class MultipleImport(Cop):

    COP_CONFIG = {}
    __implements__ = [IFormatCop]

    offences = []

    def __init__(self, cop_conf=None):
        if cop_conf is None:
            self.cop_conf = {**self.DEFAULT_CONFIG, **self.COP_CONFIG}
        else:
            self.cop_conf = {**self.DEFAULT_CONFIG, **self.COP_CONFIG, **cop_conf}

    @classmethod
    def name(cls):
        return 'multiple_import_cop'

    def process_file(self, lines, filename):
        pass

    def fix_format(self, lines, filename):
        res = []

        # processed_lines = 0
        for line in lines:
            if not line.lstrip().startswith('import'):
                res.append(line)
                continue

            indent = line_indent(line)
            spl = line.split(',')
            first_import = spl.pop(0).split()[1]
            spl.insert(0, first_import)
            for import_name in spl:
                res.append(indent + 'import ' + import_name + '\n')
        # import code
        # code.interact(local=dict(globals(), **locals()))
        return res
