

### CLASS DEFINITIONS ###

class Templ8r:

    ### CONSTRUCTOR ###

    def __init__(self):
        pass

    ### METHODS ###

    def new_class(self, cls_name: str) -> str:
        cls: str = ''

        cls +=  '### CLASS DEFINITIONS ###\n'
        cls +=  '\n'
        cls += f"class {cls_name}:\n"
        cls +=  '\n'
        cls +=  '\t### CONSTRUCTOR ###\n'
        cls +=  '\n'
        cls +=  '\tdef __init__(self):\n'
        cls +=  '\t\tpass\n'

        return cls